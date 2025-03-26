import pandas as pd
import os
from datetime import datetime
from meteostat import Stations, Daily, Monthly
import matplotlib.pyplot as plt

#Retrieving Weather stations located in Peru
stations = Stations()
stations = stations.region('PE').fetch() # weather stations in Peru

# station IDs capture into a dataframe
pd = stations
pd['ident'] = pd.index
conds = ~ (pd.monthly_start.isna() & pd.monthly_end.isna())
filteredpd = pd[conds]

# sending station IDs to a list
stationlist = filteredpd['ident'].to_list()

# Defining a start and end date for our dataset
start = datetime(1950,1,1)
end =   datetime(2025,2,28)
data = Monthly(stationlist ,start, end )
# Command to fetch Monthly Station data
data = data.fetch()

# retrieved data into a dataframe
dfdata = data 
# We want to make a left join of the Station list w/ the data 
finaldata = dfdata.join(filteredpd, on ='station',how='left')

# Define needed fields
whichfields = ['tavg','prcp','wspd','pres','tsun','name','latitude','longitude']
# Define .csv filename
csvfile = 'stations data.csv'
output_path = os.path.join(os.environ['GITHUB_WORKSPACE'], csvfile)
finaldata.to_csv(csvfile, columns=whichfields)
print(f"CSV file written to: {output_path}")