import pandas as pd
import sqlite3 as sql

dbgen = sql.connect("VocabDB/vocabs.db")
dbcs = dbgen.cursor()

for date in range(1, 31):
    sel_date = pd.read_csv(f"QWQ vocab data/Day {date}.csv")
    dbcs.execute(f"CREATE TABLE IF NOT EXISTS day{date}(Column1 Text, Column2 Text);")
    for i in range(len(sel_date)):
        dbcs.execute(f"INSERT INTO day{date}(column1, Column2)values(?,?);",(sel_date["단어"][i],sel_date["뜻"][i]))
        print(i)
    print(f"entered {date} successfully")
    print(sel_date)

dbgen.commit()