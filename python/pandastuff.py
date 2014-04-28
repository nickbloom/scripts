# Import pandas
import pandas as pd

# Load a .csv as a pandas data.frame
invbanks = pd.read_csv('Users/nbloom/Desktop/invbanks.csv')

# grab a particular item (or index) from the data frame
# Format: df.loc[row.index, column.index (which will be a name, unless your column names are integers)]
invbanks.loc[1:20,"name"]