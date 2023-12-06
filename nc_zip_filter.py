# This file is only here to create the nc_zip_codes csv. 
# If that file is in the repo, please don't run this file.

import pandas as pd
import numpy as np

wholeDf = pd.read_csv("zip_code_database.csv")
ncZip = wholeDf[np.logical_and(wholeDf.state == 'NC', wholeDf.type == 'STANDARD')]
ncZip.to_csv('nc_zip_codes.csv')