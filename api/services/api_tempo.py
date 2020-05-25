#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 14:17:52 2020

@author: henrique
"""

import requests
import bs4

class apiTempo(object):

    def __init__(self):
        pass

    def search_element(self, elem, seletor_css, page):
        '''
        método que retorna um json com os dados
        procurados em uma página web, no elemento div
        :elem: string, elemento a ser procurado. ex. div,
        :lista:  list, lista de seletores CSS, para serem
        procurados dentro do elem. ex.lista = ['id','#author','.notice']
        :path_html: path com o link da página web
        '''
        try:
            res = requests.get(page)
            res.status_code
        except Exception as exc:
            erro = {}
            erro['Erro'] = 'Path ' + page + ' nao existe ou nao encontrado'
            erro['Status'] = 0
            return (erro)
        soup = bs4.BeautifulSoup(res.text, "lxml")
        elems = soup.select(elem)
        resultado = []
        dicionario = {}
        if elems:
            for i in range(len(elems)):
                temp = elems[i].get(seletor_css)
                if temp:
                    resultado.append(temp)
                dicionario[seletor_css] = resultado
            if dicionario[seletor_css] == []:
                erro = {}
                erro['Erro'] = 'Seletor_css ' + seletor_css + ' nao existe ou nao encontrado'
                erro['Status'] = 0
                return (erro)
            else:
                dicionario['Status'] = 1
                return (dicionario)
        else:
            erro = {}
            erro['Erro'] = 'Elemento ' + elem + ' nao existe ou nao encontrado'
            erro['Status'] = 0
            return (erro)
