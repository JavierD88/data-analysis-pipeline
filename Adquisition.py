import pandas as pd
import matplotlib.pyplot as plt
import requests as req
from bs4 import BeautifulSoup
import re


def websquirting ():
    url = "http://chartsbin.com/view/32595"
    res = req.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    BEER = soup.select('tbody tr')
    listarep = []

    for e in BEER:
        for i in e:
            listarep.append(i.text.strip())

    countries = [e.split('\d+') for e in listarep]
    return countries


def cleancountries (c):
    c = c[::2]
    b = []

    for i in c:
        if i not in c:
            b.append(i)
    return c, b

def cleancolums (c, b):
   
    C = [e for i in c for e in i]
    B = [e for i in b for e in i]
    datafram = pd.DataFrame()
    datafram['Country'] = C
    datafram['l. Beer'] = B
    datafram = datafram.at[19, 'Country'] = 'USA'
    return datafram

def adquisition(): 
    countries = websquirting()
    c, b = cleancountries (countries)
    df = cleancolums(c, b)
    datafram = renameUSA (df)

    return datafram