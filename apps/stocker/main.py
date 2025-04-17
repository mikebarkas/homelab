import requests
import pg8000.native
from os import environ
import datetime

# Define variables from outside the container.
username = environ.get('PGUSER')
password = environ.get('PGPASSWORD')
host = environ.get('PGHOST', 'localhost')
port = environ.get('PGPORT', '5432')
database = environ.get('PGDATABASE')
api_key = environ.get('API_KEY')
symbol = environ.get('STOCK_SYMBOL')

url = "https://finnhub.io/api/v1/quote?symbol=" + symbol
headers = {
    "X-Finnhub-Token": api_key
}
try:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        r = response.json()
        # c=current, d=change, dp=percent change, h=high, l=low, t=timestamp
        current = r["c"]
        change = r["d"]
        dtime = datetime.datetime.fromtimestamp(r["t"])
        time = dtime.strftime("%Y-%m-%d %H:%M:%S")
        
        connection = pg8000.native.Connection(
            username, password=password, host=host, port=port, database=database, ssl_context=False)
        sql_insert = "insert into stock (symbol, current, change, timestamp) values (:s, :c, :d, :t)"
        connection.run(sql_insert, s=symbol, c=current, d=change, t=time)
        connection.close()
    else:
        print(f"Error in api: {response.status_code}")

except Exception as e:
    print(f"Error in Stocker api: {e}")
