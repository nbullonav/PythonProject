import pandas as pd
from datetime import datetime
from meteostat import Stations, Daily, Monthly
import matplotlib.pyplot as plt

stations = Stations()
stations = stations.region('PE').fetch() # weather stations in Peru

pd = stations
pd['ident'] = pd.index
conds = ~ (pd.monthly_start.isna() & pd.monthly_end.isna())
filteredpd = pd[conds]

stationlist = filteredpd['ident'].to_list()

start = datetime(1950,1,1)
end =   datetime(2025,2,28)
data = Monthly(stationlist ,start, end )
data = data.fetch()

pd = data
finaldata = pd.join(filteredpd, on ='station',how='left')

# Define needed fields
whichfields = ['tavg','prcp','wspd','pres','tsun','name','latitude','longitude']
# Define csv filename
csvfile = 'stations data.csv'

finaldata.to_csv(csvfile, columns=whichfields)