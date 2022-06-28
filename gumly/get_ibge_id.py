import pandas as pd
import numpy as np
import unidecode
import Levenshtein as lvs
import requests

'''
    Esse script tenta ajudar no tratamento de tabelas que contém municipios e estados, mas que por algum motivo não contém a coluna codigo_ibge

    To-do:
        - A função get_city_id() poderia ter apenas retirado do df original a lista de municipios e ufs unicos, e em cima disso buscar os dados do ibge, deixando para o usuário realizar o join.
        - Resolver memory leak.
'''


def get_city_id(df, mun_col='municipio', uf_col ='uf', debug=False, fuzzy_join = True, distance_letters=4):
    """
    Função que insere o código ibge (esses dados são carregados apartir da função mun_ibge que interage com a api do ibge) em um dataframe que contenha nomes de municipios e UF do respectivo estado.

    Exemplo:
        df_mun = get_city_id(df, mun_col = 'coluna com nome do municipio', uf_col = 'coluna com uf do municipio', distance_letters=3)

    Args:
        df (DataFrame): O DataFrame que vai receber as colunas com os dados de municipio do ibge.
        mun_col (str): Nome da coluna que contém os nomes dos municipios
        uf_col (str): Nome da coluna que contém as UFs
        debug (bool): True, mantém colunas de distancia minima, nome encontrado nos dados do ibge e nomes de municipios tratados.
        fuzzy_join (bool): True, realiza uma busca de nomes fuzzy encontrando o municipio que minimiza distancia de Levenshtein.
        distance_letters (int): distância máxima permitida na busca fuzzy. Aberto, se <4 então: 1, 2, 3

    Returns:
        DataFrame: Retorna o dataframe com colunas adicionais, sendo elas: codigo_regiao, codigo_uf, nome_regiao, nome_uf, sigla_regiao, sigla_uf, codigo_ibge. Caso debug = True, colunas adicionais são retornadas: score, muname, nome_ibge.
    """
    munest = mun_ibge()
    munest['muname'] = std_names(munest['nome_mun'])
    df['muname'] = std_names(df[mun_col])
    df[uf_col] = df[uf_col].str.upper()
    df_ided = pd.merge(df, munest, how='left', left_on=[uf_col, 'muname'], right_on = ['sigla_uf', 'muname'])
    # Avaliando qualidade do fit
    df_notfound = pd.DataFrame(df_ided[df_ided['codigo_ibge'].isna()][[mun_col, uf_col, 'muname']].drop_duplicates())
    porc_nf = len(df_ided[df_ided['codigo_ibge'].isna()][['municipio', 'uf']].drop_duplicates()) / len(df_ided[['municipio', 'uf']].drop_duplicates())
    eval_return(df_ided)
    # Buscando últimas rows sem match:
    if (len(df_notfound) > 0) & fuzzy_join:
        df_id = levs_app(df_ided, df_notfound, munest, uf_col, distance_letters)
    else:
        df_id = df_ided   
    eval_return(df_id)                       
    # Deve retornar o nome da cidade conforme base do ibge?
    if debug:
        df_id.drop(['muname','score', 'nome_ibge'], axis=1, inplace=True)
    return df_id

def mun_ibge(url='https://servicodados.ibge.gov.br/api/v1/localidades/municipios?orderBy=nome'):
    '''
    Função que se conecta à api do ibge para pegar os dados dos municipios
    
    Exemplo:
        mun_df = mun_ibge()

    Args:
        url (str): url da api localidades do ibge

    Returns:
        DataFrame: Retorna um dataframe com os seguintes dados para todos municipios:
            codigo_ibge
            nome do municipio: Porto Alegre
            codigo_uf: codigo do estado: 13
            sigla_uf: sigla do estado: RS
            nome_uf: nome do estado: Rio Grande do Sul
            codigo_regiao: codigo da região: 5
            sigla_região: sigla da região: CO
            nome_região: nome da região ex: Centro-Oeste
    '''
    # baixando dados do ibge
    url = url
    resp = requests.get(url)
    data = resp.json()
    mun_df = pd.DataFrame()
    for i in range(len(data)):
        row = {}
        munip = data[i]
        row['codigo_ibge'] = str(munip['id'])
        row['nome_mun'] = str(munip['nome'])
        row['codigo_uf'] = str(munip['microrregiao']['mesorregiao']['UF']['id'])
        row['sigla_uf'] = str(munip['microrregiao']['mesorregiao']['UF']['sigla'])
        row['nome_uf'] = str(munip['microrregiao']['mesorregiao']['UF']['nome'])
        row['codigo_regiao'] = str(munip['microrregiao']['mesorregiao']['UF']['regiao']['id'])
        row['sigla_regiao'] = str(munip['microrregiao']['mesorregiao']['UF']['regiao']['sigla'])
        row['nome_regiao'] = str(munip['microrregiao']['mesorregiao']['UF']['regiao']['nome'])
        mun_df = mun_df.append(row, ignore_index=True)
    return mun_df

def std_names(pdseries):
    '''
    Função que normaliza nome de municípios, ela pretende padronizar os nomes de municípios removendo acentuação e outros caracteres especiais.

    Args: 
        pdseries (pd.Series): Pandas Series of String Type

    Returns: 
        pd.Series: Normalized Pandas Series of String Type
    '''
    pdseries = pdseries.apply(lambda x: unidecode.unidecode(x.lower()))
    return pdseries.str.replace(' ', '').str.replace('-','').str.replace('0', 'o').str.replace('\'', '').str.replace('y','')

def levs_app(df_ided, df_notfound, munest, uf_col, distance_letters):
    '''
    Args:
        df_ided (DataFrame): Esse é o dataframe resultante do primeiro join com a tabela de municipios
        df_notfound (DataFrame): Esse aqui é o dataframe das que faltaram
        munest (DataFrame): Essa é a tabela do ibge
        uf_col (str): Esse é o nome da coluna que tem uf
        distance_letters (int): o número de letras que tu permite de distância entre duas palavras
    Returns:
        df_id (DataFrame): retorna df_notfound com o que deu pra salvar ou o que deu match dentro da distância especificada
    '''
    print('Iniciando aproximação com Levenshtein.')
    df_notfound['codigo_ibge'] = ''
    df_notfound['score'] = np.nan
    df_notfound['nome_mun'] = ''
    for rowdf in df_notfound.iterrows():
        score = distance_letters
        for rowmun in munest.iterrows():
            distance_lvs = lvs.distance(rowdf[1]['muname'], rowmun[1]['muname'])
            if rowdf[1]['uf'] == rowmun[1]['sigla_uf']:
                if score > distance_lvs:
                    score = distance_lvs
                    prob_city = rowmun[1]['muname']
                    df_notfound.at[rowdf[0], 'codigo_ibge'] = rowmun[1]['codigo_ibge']
                    df_notfound.at[rowdf[0], 'score'] = score
                    df_notfound.at[rowdf[0], 'nome_mun'] = rowmun[1]['nome_mun']
    # merging columns
    if 'municipio' in df_notfound.columns:
        df_notfound.drop('municipio', axis=1,inplace=True)
    df_id = pd.merge(df_ided, df_notfound, how='left', on=[uf_col, 'muname'])
    for col in df_id.columns:
        if '_x' in col:
            cola = col
            colb = col[:-1] + 'y'
            col_final = col[:-2]
            df_id[cola] = df_id[cola].replace(np.nan, '')
            df_id[colb] = df_id[colb].replace(np.nan, '')
            df_id[col_final] = df_id[cola] + df_id[colb]
            df_id.drop([cola, colb], axis=1,inplace=True)
            df_id[col_final].replace('', np.nan, inplace=True)
    return df_id  

def eval_return(df_id):
    '''
    Função que determina qualidade do match de municípios
    Args:
        df_id (DataFrame): output da get_city_id # não é bem o output esse print ainda ta ali dentro
    Returns:
        {}: não retorna nada só printa o resultado

    '''
    err_codibge = len(df_id[df_id['codigo_ibge'].str.len() != 7]['municipio'].drop_duplicates()) 
    porc_nfl = len(df_id[df_id['codigo_ibge'].isna()][['municipio', 'uf']].drop_duplicates()) / len(df_id[['municipio', 'uf']].drop_duplicates())               
    print('Match de: ' + str(round((1 - porc_nfl)*100,2)) + '%.' + ' Número de cidades não encontradas: ' + str(err_codibge) + ' linhas.')

def est_ibge():
    a = mun_ibge()
    df = a[['nome_uf', 'sigla_uf', 'codigo_uf']].drop_duplicates().reset_index(drop=True)
    return df

def get_estado_id(df, col):
    '''
    adiciona coluna com dados de uf em uma data frame que contenha uma coluna com nome do estado.
    Args:
        df (DataFrame): dataframe que tu quer adicionar as ufs
        col (str): coluna com o nome do estados
    Returns:
        df_ufed (DataFrame): dataframe original com duas colunas adicionais:
            nome_uf: nome do estado
            sigla_uf: sigla do estado
            codigo_uf: código do estado
    '''
    estname = est_ibge()
    estname['estname'] = std_names(estname['nome_uf'])
    df['estname'] = std_names(df[col])
    df_ufed = pd.merge(df, estname, how='left', on='estname')
    df_ufed.drop('estname', axis=1, inplace=True)
    print('Número de linhas sem uf: ' + str(len(df_ufed[df_ufed['nome_uf'].isna()])))
    return df_ufed
