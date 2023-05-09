#ct-price-formatted

import requests
import re
import os
from bs4 import BeautifulSoup
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

from func import processar_preco, clean
from media import getMedia
from daily import recordDaily
from graph import graphDaily

os.system('cls')

URL_continente = "https://www.continente.pt/produto/banana-continente-2597619.html"
URL_auchan = "https://www.auchan.pt/pt/produtos-frescos/fruta/banana-e-frutos-tropicais/banana-importada-kg/234229.html"
URL_minipreco = "https://www.minipreco.pt/produtos/frutas-e-vegetais/frutas/uva-banana-e-kiwi/p/98"
URL_aperinha = "https://www.aperinha.pt/banana-importada-kg"

#current_txt = "current.txt"

continente_txt = "site/precos/continente.txt"
auchan_txt = "site/precos/auchan.txt"
aperinha_txt = "site/precos/aperinha.txt"
minipreco_txt = "site/precos/minipreco.txt"

last_update_txt = "site/precos/last_update.txt"
media_txt = "site/precos/media.txt"


#CONTINENTE
def getContinente():
    page = requests.get(URL_continente)
    soup = BeautifulSoup(page.content, "html.parser")

    result_continente = soup.find("span", class_="ct-price-formatted").get_text()
    result_continente = processar_preco(result_continente)

    print("Continente: ", result_continente)

    file_object = open(continente_txt, 'a')
    file_object.write(result_continente)
    file_object.close()


# AUCHAN
def getAuchan():
    page = requests.get(URL_auchan)
    soup = BeautifulSoup(page.content, "html.parser")

    result_auchan = soup.find("span", class_="value").get_text()
    result_auchan = processar_preco(result_auchan)

    print("Auchan: ", result_auchan)

    file_object = open(auchan_txt, 'a')
    file_object.write(result_auchan)
    file_object.close()


# MINIPRECO
def getMinipreco():
    page = requests.get(URL_minipreco)
    soup = BeautifulSoup(page.content, "html.parser")

    result_minipreco = soup.find("span", class_="average-price").get_text()
    result_minipreco = processar_preco(result_minipreco)

    print("Minipreco: ", result_minipreco)

    file_object = open(minipreco_txt, 'a')
    file_object.write(result_minipreco)
    file_object.close()


# APERINHA
def getAperinha():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    page = requests.get(URL_aperinha, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    result_aperinha = soup.select('#price-value')[0].get_text()

    result_aperinha = processar_preco(result_aperinha)

    print("APerinha: ", result_aperinha)

    file_object = open(aperinha_txt, 'a')
    file_object.write(result_aperinha)
    file_object.close()

# LAST UPDATE
def getLastUpdate():
    last_update = now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    print("\nLast update: ", last_update)

    file_object = open(last_update_txt, 'a')
    file_object.write(last_update)
    file_object.close()

#MAIN
def main():
    #clean(current_txt)
    clean(continente_txt)
    clean(auchan_txt)
    clean(aperinha_txt)
    clean(minipreco_txt)

    clean(last_update_txt)

    print("Preço das bananas:")

    getContinente()
    getAuchan()
    getMinipreco()
    getAperinha()
    getLastUpdate()

    clean(media_txt)
    getMedia()
	
    recordDaily()
    graphDaily()

if __name__ == "__main__":
    main()
    




