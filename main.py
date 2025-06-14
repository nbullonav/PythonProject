import pandas as pd
import os
from datetime import datetime
from meteostat import Stations, Daily, Monthly
import matplotlib.pyplot as plt

#fechainic = input("Ingrese la fecha de inicio: ")
#fechafin = input("Ingrese la fecha de fin: ")

def getWeatherData():
  stations = Stations()
  stations = stations.region('PE').fetch()
  pd = stations
  pd['ident'] = pd.index
  conds = ~ (pd.monthly_start.isna() & pd.monthly_end.isna())
  filteredpd = pd[conds]
  stationlist = filteredpd['ident'].to_list()
  start = datetime(1950,1,1)
  end =   datetime(2025,2,28)
  data = Monthly(stationlist ,start, end )
  data = data.fetch()
  dfdata = data 
  finaldata = dfdata.join(filteredpd, on ='station',how='left')
  whichfields = ['tavg','prcp','wspd','pres','tsun','name','latitude','longitude']
  csvfile = 'stationsdata.csv'
  finaldata.to_csv(csvfile, columns=whichfields)

if __name__ == '__getWeatherData__':
    getWeatherData()
