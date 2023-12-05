import pandas as pd

wholeDf = pd.read_csv("zip_code_database.csv")
ncZip = wholeDf[wholeDf.state == 'NC']
ncZip.to_csv('nc_zipcodes.csv')

print(ncZip.head)