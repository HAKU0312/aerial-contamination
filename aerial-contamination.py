import requests,re
import pandas as pd
import numpy as np
import subprocess as sp
def main():

    sp.call("wget https://github.com/HAKU0312/aerial-contamination/blob/main/china-air-quality.csv",shell=True)
    sp.call("wget https://github.com/HAKU0312/aerial-contamination/blob/main/taiwan-air-quality.csv",shell=True)
    df_china=pd.read_csv('china-air-quality.csv')
    df_taiwan=pd.read_csv('taiwan-air-quality.csv')
    print(df_germany)

if __name__ == "__main__":
 main()