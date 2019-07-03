import pandas as pd
from IPython.display import display
from IPython.display import Image

def cleaning ():
    musicbase = pd.read_csv('metal_bands_2017.csv', engine= "python")
    pupulationbase = pd.read_csv('world_population_1960_2015.csv', engine= "python")
    musicbase = musicbase.drop(['Unnamed: 0', 'split', 'fans'] , axis=1, inplace=True)
    musicbase = musicbase=musicbase[musicbase['formed']!='-']
    pupulationbase = pupulationbase.rename(columns={'Country Name':'Country'}, inplace=True)
    musicbase = musicbase.rename(columns={'origin':'Country'}, inplace=True)
    a = pd.DataFrame(pupulationbase[['Country' ,'2015']])
    MetalBase1 = musicbase.merge(a, on='Country', how='left')
    MetalBase1 = MetalBase1[['band_name', 'formed', 'Country', 'style', '2015']].fillna('-')
    MetalBase1 = MetalBase1[MetalBase1['2015']!='-']

def findstyle ():
    lst=s.split(',')
    return lst[-1]

def applyfind ():
    MetalBase1['style']= MetalBase1['style'].apply(findstyle)
def cleaning2 ():
    a = MetalBase1.drop_duplicates()
    datafram = pd.read_csv('./Webscraping.csv')
    datafram2 = datafram.drop_duplicates()
    MetalBase2 = datafram.merge(a, on='Country', how='inner')
    MetalBase2.drop(['Unnamed: 0'] , axis=1, inplace=True)
    Nmetal= MetalBase2[['Country', 'band_name']]
    NBandas = Nmetal.groupby(Nmetal['Country']).count()
    MetalBase2 = MetalBase2.merge(NBandas, on='Country', how='left')
    MetalBase2.rename(columns={'band_name_y':'Metal_Bands'}, inplace=True)
    MetalBase2.drop(['band_name_x', 'style', 'formed'] , axis=1, inplace=True)
    MetalData = MetalBase2.drop_duplicates()
    MetalData.rename(columns={'2015':'Population'}, inplace=True)
    MetalData.to_csv('./DataframeFinal.csv')

def Clean(): 
    clean1 = cleaning()
    style = findstyle (clean1)
    app = applyfind(style)
    dfclean = cleaning2 (app)

    return dfclean