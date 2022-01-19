import requests,re
import pandas as pd
import numpy as np
import subprocess as sp
def main():

    sp.call("wget https://github.com/HAKU0312/aerial-contamination/blob/main/china-air-quality2.csv",shell=True)
    sp.call("wget https://github.com/HAKU0312/aerial-contamination/blob/main/taiwan-air-quality2.csv",shell=True)
    sp.call("wget https://github.com/HAKU0312/aerial-contamination/blob/main/japan-air-quality2.csv",shell=True)
    #sp.call("wget https://github.com/HAKU0312/aerial-contamination/blob/main/india-air-quality.csv",shell=True)
    #sp.call("wget https://github.com/HAKU0312/aerial-contamination/blob/main/india-air-quality.csv",shell=True)
    #sp.call("wget https://github.com/HAKU0312/aerial-contamination/blob/main/south_korea-air-quality.csv",shell=True)
    #sp.call("wget https://github.com/HAKU0312/aerial-contamination/blob/main/china-air-quality_score.csv",shell=True)
    df_china=pd.read_csv('china-air-quality2.csv')
    df_taiwan=pd.read_csv('taiwan-air-quality2.csv')
    df_japan=pd.read_csv('japan-air-quality2.csv')
    #df_india=pd.read_csv('india-air-quality.csv')
    #df_korea=pd.read_csv('south_korea-air-quality.csv')
    #print(df_korea)
    #df_score= pd.DataFrame(columns=['china_score', 'taiwan_score','japan_score','india_score','korea_score'])
    #print(df_score)
    #df_china['china_score']=(df_china['pm25']*0.125+df_china['pm10']*0.2)
    #df_china.insert(df_china.shape[1],'china_score')
    #print(df_china)
    #df_china['score'] =df_china[' pm25']*1+df_china[' pm10']*2+df_china[' o3']*3+df_china[' no2']*5+df_china[' so2']*10+df_china[' co']*10
    df_china.fillna(0)
    df_taiwan.fillna(0)
    #print(df_china.dtypes)
    df_china['china_score'] =df_china['pm25']*1+df_china['pm10']*2+df_china['o3']*3+df_china['no2']*5+df_china['so2']*10+df_china['co']*10
    df_taiwan['taiwan_score'] =df_taiwan['pm25']*1+df_taiwan['pm10']*2+df_taiwan['o3']*3+df_taiwan['no2']*5+df_taiwan['so2']*10+df_taiwan['co']*10
    print(df_taiwan)



if __name__ == "__main__":
 main()