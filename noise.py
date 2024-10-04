import pandas as pandas
import dask.dataframe as dd
#df= pandas.read_csv('filteredfile2.csv')

#Only keep columns relevant to our research: Create date, closed date, comlaint type, descriptor
def noise_complaints(input_file, start_date, end_date, output_file=None):
    usecols = [0, 1, 2, 5, 6]  # Only load necessary columns
    column_names = ['unique_key', 'created_date', 'closed_date', 'complaint_type', 'descriptor']
    dtypes = {
        'unique_key': 'object',
        'created_date': 'object',
        'closed_date': 'object',
        'complaint_type': 'object',
        'descriptor': 'object'
    }

df = dd.read_csv(input_file, header=None, names=column_names, dtype=dtypes, usecols=usecols)

