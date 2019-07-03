import pandas as pd
import matplotlib.pyplot as plt
import Adquisition
import Clean
import Analaysis
import requests as req
from bs4 import BeautifulSoup
import re

def main():
    datafram = Adquisition.adquisition()
    Analysis = Analaysis.Analysis()
    #Clean = Clean.Clean()

if __name__=="__main__":
    main() 
