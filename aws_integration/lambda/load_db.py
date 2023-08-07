"""This script is used to load data into a mysql database"""

from os import getenv
from os.path import realpath, dirname, join
import pandas as pd
import csv
from sqlalchemy import create_engine
from dotenv import load_dotenv
from time import ctime, sleep

def read_data(file_locator: str) -> None:
    '''Load data into the transactions table of a postgres datbase
       Input: File Directory''' 

    load_dotenv()

    host = getenv('db_HOST')
    port = 3306
    user = getenv('db_USER')
    password = getenv('PASSWORD')
    database = getenv('DATABASE')

    engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{database}")
    print("Created Connection")
    df = pd.read_csv(file_locator)
    df.to_sql('transactions', engine, if_exists='replace', index=False)
    print('Loaded Data into DB!')



def stream_data(file_locator: str) -> None:
    '''Load data into the transactions table of a postgres datbase
       Input: File Directory''' 

    load_dotenv()

    host = getenv('db_HOST')
    port = 3306
    user = getenv('db_USER')
    password = getenv('PASSWORD')
    database = getenv('DATABASE')

    engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{database}")
    print("Created Connection")
    with open(file_locator) as file_object:
        data = csv.reader(file_object)
        header = next(data)
        for row in data:
            df_row = pd.DataFrame([row], columns = header)
            print(df_row)
            df_row.to_sql('transactions', engine, if_exists='append', index=False)
            print(f"commited to db at : {ctime()}")
            sleep(5)
    


if __name__ == '__main__':
    locator = realpath(dirname('__file__'))
    file_location = join(locator, 'records.csv')
    stream_data(file_location)


        