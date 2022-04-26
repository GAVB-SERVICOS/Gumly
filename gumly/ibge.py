import pandas as pd
from ibge.localidades import Estados, Municipios
import unidecode
import re

def fetch():
    estado = []
    _regiao = []
    sigla_regiao = []
    uf_estado = []

    for dictionary in Estados().json():
        estado.append(dictionary["nome"])
        uf_estado.append(dictionary["sigla"])
        _regiao.append(dictionary["regiao"]["nome"])
        sigla_regiao.append(dictionary["regiao"]["sigla"])

    municipios = []
    municipios_uf = []
    municipios_estado = []
    municipios_regiao = []

    for dictionary in Municipios().json():
        municipios.append(dictionary["nome"])
        municipios_estado.append(dictionary["microrregiao"]["mesorregiao"]["UF"]["nome"])
        municipios_uf.append(dictionary["microrregiao"]["mesorregiao"]["UF"]["sigla"])
        municipios_regiao.append(dictionary["microrregiao"]["mesorregiao"]["UF"]["regiao"]["nome"])

    municipios_tratado = [re.sub('\W+','', unidecode.unidecode(x.lower())) for x in municipios]
    estado_tratado = [re.sub('\W+','', unidecode.unidecode(x.lower())) for x in estado]

    municipio_regiao_tratado = dict(zip(municipios_tratado,municipios_regiao))
    municipio_estado_tratado = dict(zip(municipios_tratado,municipios_estado))
    estado_regiao_tratado = dict(zip(estado_tratado,_regiao))

    dict_cep_estado = {pd.Interval(69900, 69999, closed = 'both') : 'Acre',
                       pd.Interval(57000, 57999, closed = 'both') : 'Alagoas',
                       pd.Interval(68900, 68999, closed = 'both') : 'Amapá',
                       pd.Interval(69000, 69299, closed = 'both') : 'Amazonas',
                       pd.Interval(69400, 69899, closed = 'both') : 'Amazonas',
                       pd.Interval(40000, 48999, closed = 'both') : 'Bahia',
                       pd.Interval(60000, 63999, closed = 'both') : 'Ceará',
                       pd.Interval(70000, 72799, closed = 'both') : 'Distrito Federal',
                       pd.Interval(73000, 73699, closed = 'both') : 'Distrito Federal',
                       pd.Interval(29000, 29999, closed = 'both') : 'Espírito Santo',
                       pd.Interval(72800, 72999, closed = 'both') : 'Goiás',
                       pd.Interval(73700, 76799, closed = 'both') : 'Goiás',
                       pd.Interval(65000, 65999, closed = 'both') : 'Maranhão',
                       pd.Interval(78000, 78899, closed = 'both') : 'Mato Grosso',
                       pd.Interval(79000, 79999, closed = 'both') : 'Mato Grosso do Sul',
                       pd.Interval(30000, 39999, closed = 'both') : 'Minas Gerais',
                       pd.Interval(66000, 68899, closed = 'both') : 'Pará',
                       pd.Interval(58000, 58999, closed = 'both') : 'Paraíba',
                       pd.Interval(80000, 87999, closed = 'both') : 'Paraná',
                       pd.Interval(50000, 56999, closed = 'both') : 'Pernambuco',
                       pd.Interval(64000, 64999, closed = 'both') : 'Piauí',
                       pd.Interval(20000, 28999, closed = 'both') : 'Rio de Janeiro',
                       pd.Interval(59000, 59999, closed = 'both') : 'Rio Grande do Norte',
                       pd.Interval(90000, 99999, closed = 'both') : 'Rio Grande do Sul',
                       pd.Interval(76800, 76999, closed = 'both') : 'Rondônia',
                       pd.Interval(69300, 69399, closed = 'both') : 'Roraima',
                       pd.Interval(88000, 89999, closed = 'both') : 'Santa Catarina',
                       pd.Interval(49000, 49999, closed = 'both') : 'Sergipe',
                       pd.Interval(1000, 19999, closed = 'both') : 'São Paulo',
                       pd.Interval(77000, 77999, closed = 'both') : 'Tocantins',
                       pd.Interval(69900000, 69999999, closed = 'both') : 'Acre',
                       pd.Interval(57000000, 57999999, closed = 'both') : 'Alagoas',
                       pd.Interval(68900000, 68999999, closed = 'both') : 'Amapá',
                       pd.Interval(69000000, 69299999, closed = 'both') : 'Amazonas',
                       pd.Interval(69400000, 69899999, closed = 'both') : 'Amazonas',
                       pd.Interval(40000000, 48999999, closed = 'both') : 'Bahia',
                       pd.Interval(60000000, 63999999, closed = 'both') : 'Ceará',
                       pd.Interval(70000000, 72799999, closed = 'both') : 'Distrito Federal',
                       pd.Interval(73000000, 73699999, closed = 'both') : 'Distrito Federal',
                       pd.Interval(29000000, 29999999, closed = 'both') : 'Espírito Santo',
                       pd.Interval(72800000, 72999999, closed = 'both') : 'Goiás',
                       pd.Interval(73700000, 76799999, closed = 'both') : 'Goiás',
                       pd.Interval(65000000, 65999999, closed = 'both') : 'Maranhão',
                       pd.Interval(78000000, 78899999, closed = 'both') : 'Mato Grosso',
                       pd.Interval(79000000, 79999999, closed = 'both') : 'Mato Grosso do Sul',
                       pd.Interval(30000000, 39999999, closed = 'both') : 'Minas Gerais',
                       pd.Interval(66000000, 68899999, closed = 'both') : 'Pará',
                       pd.Interval(58000000, 58999999, closed = 'both') : 'Paraíba',
                       pd.Interval(80000000, 87999999, closed = 'both') : 'Paraná',
                       pd.Interval(50000000, 56999999, closed = 'both') : 'Pernambuco',
                       pd.Interval(64000000, 64999999, closed = 'both') : 'Piauí',
                       pd.Interval(20000000, 28999999, closed = 'both') : 'Rio de Janeiro',
                       pd.Interval(59000000, 59999999, closed = 'both') : 'Rio Grande do Norte',
                       pd.Interval(90000000, 99999999, closed = 'both') : 'Rio Grande do Sul',
                       pd.Interval(76800000, 76999999, closed = 'both') : 'Rondônia',
                       pd.Interval(69300000, 69399999, closed = 'both') : 'Roraima',
                       pd.Interval(88000000, 89999999, closed = 'both') : 'Santa Catarina',
                       pd.Interval(49000000, 49999999, closed = 'both') : 'Sergipe',
                       pd.Interval(1000000, 19999999, closed = 'both') : 'São Paulo',
                       pd.Interval(77000000, 77999999, closed = 'both') : 'Tocantins'}
    
    result = dict(municipios_regiao = municipio_regiao_tratado,
                  municipios_estado = municipio_estado_tratado,
                  regiao = estado_regiao_tratado,
                  cep_estado = dict_cep_estado)
    
    return result

def city_to_region(df, colOrigem, ibge_data):
    
    #Trata a coluna do dataset
    df['temp'] = [re.sub('\W+','', unidecode.unidecode(x.lower())) for x in df[colOrigem].astype('str')]
        
    colNova = df['temp'].map(ibge_data['municipios_regiao'])
       
    df.drop(['temp'], axis = 1,inplace = True)
    
    return colNova

def city_to_state(df, colOrigem, ibge_data):
    #Trata a coluna do dataset
    df['temp'] = [re.sub('\W+','', unidecode.unidecode(x.lower())) for x in df[colOrigem].astype('str')]
        
    colNova = df['temp'].map(ibge_data['municipios_estado'])
       
    df.drop(['temp'], axis = 1,inplace = True)
    
    return colNova

def state_to_region(df, colOrigem, ibge_data):
    #Trata a coluna do dataset
    df['temp'] = [re.sub('\W+','', unidecode.unidecode(x.lower())) for x in df[colOrigem].astype('str')]
        
    colNova = df['temp'].map(ibge_data['regiao'])
       
    df.drop(['temp'], axis = 1,inplace = True)
    
    return colNova

def cep_to_state(df, colOrigem, ibge_data):
    #Trata a coluna do dataset
    df['temp'] = df[colOrigem].astype('str')
    df['temp'] = [re.sub('\W+','', x) for x in df.temp]
    df['temp'] = df.temp.astype('int')
        
    colNova = df['temp'].map(ibge_data['cep_estado'])
       
    df.drop(['temp'], axis = 1,inplace = True)
    
    return colNova

def cep_to_region(df, colOrigem, ibge_data):
    #Trata a coluna do dataset
    df['temp'] = df[colOrigem].astype('str')
    df['temp'] = [re.sub('\W+','', x) for x in df.temp]
    df['temp'] = df.temp.astype('int')
        
    df['temp'] = df['temp'].map(ibge_data['cep_estado'])
    
    df['temp'] = [re.sub('\W+','', unidecode.unidecode(x.lower())) for x in df['temp']]
        
    colNova = df['temp'].map(ibge_data['regiao'])
       
    df.drop(['temp'], axis = 1,inplace = True)
        
    return colNova
    