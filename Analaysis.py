import pandas as pd
import numpy as np

def Analysis ():
    MetalBeers = pd.read_csv("DataframeFinal.csv")
    MetalBeers.drop(['Unnamed: 0'] , axis=1, inplace=True)
    MetalBeers.corr(method ='pearson') 
    MetalB = MetalBeers.set_index('Country')
    LogMetalBeers = np.log(MetalB)

