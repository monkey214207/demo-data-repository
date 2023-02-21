import pandas as pd
from sqlalchemy import create_engine

if __name__ == '__main__':
    # INPUT YOUR OWN CONNECTION STRING HERE
    # conn_string = 'postgres://user:password@host/database'
    conn_string = 'postgresql://postgres:postgres@localhost:5432/postgres'

    # perform to_sql test and print result
    db = create_engine(conn_string)
    conn = db.connect()

    table_name = "yellow_tripdata_sample_01"

    table_df = pd.read_csv('yellow_tripdata_sample_2019-01.csv')
    table_df.to_sql(table_name, con=conn, if_exists='append', index=False)

    # don't forget to close connection
    conn.close()
