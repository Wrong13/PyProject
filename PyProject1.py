import pandas as pd
import sqlalchemy
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

entity1 = pd.read_excel("razb_uch.xlsx",usecols="A:M")
entity2 = pd.read_excel("razb_uch.xlsx",usecols="N:V")

print(entity1)
print(entity2)

#connection = psycopg2.connect(user="postgres",password="password")
#connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

#cursor = connection.cursor()
#sql_createDb = cursor.execute('create database testdb;')

#cursor.close()
#connection.close()

engine = sqlalchemy.create_engine("postgresql+psycopg2://postgres:password@localhost/testdb")
engine.connect()

print(engine)

metaData = sqlalchemy.MetaData()
table1 = sqlalchemy.Table(
    "table1",
    metaData,
    sqlalchemy.Column("id_uch_vost_pol",sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("NAME_BEGIN_VOST_UCH",sqlalchemy.String(100)),
    sqlalchemy.Column("ESR_BEGIN_VOST_UCH",sqlalchemy.Integer),
    sqlalchemy.Column("DOR_BEGIN_VOST_UCH",sqlalchemy.Integer),
    sqlalchemy.Column("OKATO_BEGIN_VOST_UCH_NAME",sqlalchemy.String(100)),
    sqlalchemy.Column("X_BEG_VOST_UCH",sqlalchemy.Float),
    sqlalchemy.Column("Y_BEG_VOST_UCH",sqlalchemy.Float), 
    sqlalchemy.Column("NAME_END_VOST_UCH",sqlalchemy.String(100)),
    sqlalchemy.Column("ESR_END_VOST_UCH",sqlalchemy.Integer),
    sqlalchemy.Column("DOR_END_VOST_UCH",sqlalchemy.Integer),
    sqlalchemy.Column("OKATO_END_VOST_UCH_NAME",sqlalchemy.String(100)),
    sqlalchemy.Column("X_END_VOST_UCH",sqlalchemy.Float),
    sqlalchemy.Column("Y_END_VOST_UCH",sqlalchemy.Float)
)
table2 = sqlalchemy.Table(
    "table2",
    metaData,
    sqlalchemy.Column("NUM_CNSI_MELK_SET",sqlalchemy.Integer),
    sqlalchemy.Column("NAME_BEGIN_MELK_SET",sqlalchemy.String(100)),
    sqlalchemy.Column("ESR_BEGIN_MELK_SET",sqlalchemy.Integer),
    sqlalchemy.Column("DOR_BEGIN_MELK_SET",sqlalchemy.Integer),
    sqlalchemy.Column("OKATO_BEGIN_MELK_SET_NAME",sqlalchemy.String(100)),
    sqlalchemy.Column("NAME_END_MELK_SET",sqlalchemy.String(100)),
    sqlalchemy.Column("ESR_END_MELK_SET",sqlalchemy.Integer),
    sqlalchemy.Column("DOR_END_MELK_SET",sqlalchemy.Integer),
    sqlalchemy.Column("OKATO_END_MELK_SET_NAME",sqlalchemy.Integer),
)

metaData.create_all(engine)

print(metaData)


entity1.to_sql(name="table1",con=engine, if_exists="replace",index=False)
entity2.to_sql(name="table2",con=engine,if_exists="replace",index=False)
