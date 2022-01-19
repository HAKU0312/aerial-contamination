import requests,re
import pandas as pd
import numpy as np
import subprocess as sp
def main():

    sp.call("wget https://github.com/HAKU0312/aerial-contamination/blob/main/china-air-quality2.csv",shell=True)
    sp.call("wget https://github.com/HAKU0312/aerial-contamination/blob/main/taiwan-air-quality2.csv",shell=True)
    sp.call("wget https://github.com/HAKU0312/aerial-contamination/blob/main/japan-air-quality2.csv",shell=True)
    sp.call("wget https://github.com/HAKU0312/aerial-contamination/blob/main/india-air-quality2.csv",shell=True)
    sp.call("wget https://github.com/HAKU0312/aerial-contamination/blob/main/south_korea-air-quality2.csv",shell=True)
    df_china=pd.read_csv('china-air-quality2.csv')
    df_taiwan=pd.read_csv('taiwan-air-quality2.csv')
    df_japan=pd.read_csv('japan-air-quality2.csv')
    df_india=pd.read_csv('india-air-quality2.csv')
    df_korea=pd.read_csv('south_korea-air-quality2.csv')
    #print(df_korea)
    #df_score= pd.DataFrame(columns=['china_score', 'taiwan_score','japan_score','india_score','korea_score'])
    #print(df_score)
    #df_china['china_score']=(df_china['pm25']*0.125+df_china['pm10']*0.2)
    #df_china.insert(df_china.shape[1],'china_score')
    #print(df_china)
    #df_china['score'] =df_china[' pm25']*1+df_china[' pm10']*2+df_china[' o3']*3+df_china[' no2']*5+df_china[' so2']*10+df_china[' co']*10
    df_china.fillna(0)
    df_taiwan.fillna(0)
    df_japan.fillna(0)
    df_india.fillna(0)
    df_korea.fillna(0)
    #print(df_china.dtypes)
    df_china['china_score'] =df_china['pm25']*1+df_china['pm10']*2+df_china['o3']*3+df_china['no2']*5+df_china['so2']*10+df_china['co']*10
    df_taiwan['taiwan_score'] =df_taiwan['pm25']*1+df_taiwan['pm10']*2+df_taiwan['o3']*3+df_taiwan['no2']*5+df_taiwan['so2']*10+df_taiwan['co']*10
    df_japan['japan_score'] =df_japan['pm25']*1+df_japan['pm10']*2+df_japan['o3']*3+df_japan['no2']*5+df_japan['so2']*10+df_japan['co']*10
    df_india['india_score'] =df_india['pm25']*1+df_india['pm10']*2+df_india['o3']*3+df_india['no2']*5+df_india['so2']*10+df_india['co']*10
    df_korea['south_korea_score'] =df_korea['pm25']*1+df_korea['pm10']*2+df_korea['o3']*3+df_korea['no2']*5+df_korea['so2']*10+df_korea['co']*10

    print(df_korea)



if __name__ == "__main__":
 main()