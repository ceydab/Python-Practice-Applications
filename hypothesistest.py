'''this is a simple project to get data from a csv file and convert it into a table in postgresql 
and then use the table for upper tail hypothesis test. the data is extracted from 
https://www.kaggle.com/datasets/justinas/nba-players-data?select=all_seasons.csv'''

import psycopg2
import pandas as pd
import scipy.stats as stats
import math 

con = psycopg2.connect(
    host = "localhost",
    database = "postgres",
    port = "5432",
    user = "postgres",
    password = "1536"
)
con.autocommit = True
cur = con.cursor()

data =  pd.read_csv("playerstats.csv")
df = pd.DataFrame(data)
cur.execute("CREATE TABLE players (id serial PRIMARY KEY, name varchar, games integer)")
# cur.execute("DROP TABLE players")
# cur.execute("DELETE FROM players ")
for row in df.itertuples():
    cur.execute("INSERT INTO players (name, games)  VALUES (%s,%s)", (row.plname, row.gp))
# '''Table created, database transferred'''

#Check the null hypothesis that H: u<=45 against H: u>45 with alpha level 0.05
# meanvalue = df.mean()
testmean = 45

def meanofgames():
    cur.execute("SELECT AVG(GAMES) FROM PLAYERS;")
    for mean in cur.fetchone():
        return mean
def stddev():
    cur.execute("SELECT STDDEV(GAMES) FROM PLAYERS")
    for stddev in cur.fetchone():
        return stddev
zvalue = stats.norm.ppf(0.95)

def samplesize():
    cur.execute(" SELECT COUNT(GAMES) FROM PLAYERS")
    for size in cur.fetchone():
        return size
x_crit = zvalue*int(stddev())/math.sqrt(samplesize()) +45

if meanofgames() > x_crit:
    print("Reject the null hypothesis")
else:
    print("There isnt sufficient evidence to reject the null hypothesis")



con.close()