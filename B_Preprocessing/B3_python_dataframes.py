########################################################################################################################
#
#   Brief demo of some cool things you can do with Pandas
#
#
########################################################################################################################
import pandas
import collections

data = pandas.read_csv('./publications.csv') # read data from a file


#***********************************************************************************************
# DISPLAY FIRST FEW ROWS
#***********************************************************************************************
print(data.head(5))


print('\n' + '*'*80 + '\n') # skip lines
#***********************************************************************************************
# PRINT SHAPE / SIZE OF THE DATAFRAME
#***********************************************************************************************
print(data.shape)


print('\n' + '*'*80 + '\n') # skip lines
#***********************************************************************************************
# PRINT FREQUENCY COUNTS SORTED BY VALUE
#***********************************************************************************************
print(data['journal'].value_counts())


print('\n' + '*'*80 + '\n') # skip lines
# ***********************************************************************************************
#  PRINT FREQUENCY COUNTS SORTED BY KEY
# ***********************************************************************************************

yrs = data['pubyear'].value_counts()
yrdict = yrs.to_dict()
od = collections.OrderedDict(sorted(yrdict.items()))
for key, value in od.items():
  print("{} : {}".format(key, value))


print('\n' + '*'*80 + '\n') # skip lines
#***********************************************************************************************
#  DROP ROWS CONTAINING A CERTAIN VALUE IN A SPECIFIC COLUMN
# ***********************************************************************************************
print(data.columns.values)
print(data.shape)


indexNames = data[ data['pubyear'] == 2011 ].index # get names of indexes for rows that match this condition
data.drop(indexNames , inplace=True) # delete those rows from the dataframe
print('new shape')
print(data.shape)
