# imports
import nltk
nltk.download(['stopwords', 'rslp'])
stopwords = nltk.corpus.stopwords.words('portuguese')

from nltk import word_tokenize, sent_tokenize

import spacy
import string
import re

# remoção de caracteres especiais
def tratamento_dados(texto):
    '''
    Remove caracteres especiais e links
    '''
    camada_01 = re.sub('(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)', '', str(texto))
    camada_02 = re.sub('["("")"?@|$|.|!,:%;"]', '', camada_01)
    camada_03 = camada_02.lower()
    camada_04 = re.sub('[0-9]', '', camada_03)
    return camada_04

# remoção de stopwords
def remov_stopwords(texto):
    '''
    Remove stopwords em portugues
    '''
    lista_palavras = texto.split()
    frase_ajustada = ''
    for palavra in lista_palavras:
        if palavra not in stopwords:
            frase_ajustada = frase_ajustada + ' ' + palavra
    return frase_ajustada

# stemming
stemmer = nltk.stem.RSLPStemmer()

def stemmer(texto):
    lista_palavras = texto.split()
    frase_ajustada = ''
    for palavra in lista_palavras:
        extracao = stemmer.stem(palavra)
        frase_ajustada = frase_ajustada + ' ' + extracao
    return frase_ajustada

# lemmatizer
spacy_lemma = spacy.load('pt_core_news_sm')
spacy_lemma.max_length = 4178373

def lemmatizer(texto):
    doc = spacy_lemma(texto)
    doc_lematizado = [token.lemma_ for token in doc]
    return ' '.join(doc_lematizado)

# remocao de tags html
def remov_tags(texto):
    '''
    Remove tags HTML
    '''
    camada_01 = re.sub(r"<[^<]+?>", "", str(texto))
    camada_01 = re.sub(r"/", "", str(camada_01)) 
    camada_01 = re.sub(r"“", "", str(camada_01))
    camada_01 = re.sub(r"''", "", str(camada_01))    
    camada_01 = camada_01.strip()
    return camada_01
    
    
def tokenize_rows(text):
    '''
    Tokeniza as palavras da frase ou texto no datapoint
    '''
    tokenized_text = word_tokenize(text)
    return tokenized_text

