import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
from eralchemy2 import render_er

from sqlalchemy import (MetaData, Table, Column, Integer, String, Boolean, ForeignKey, FLOAT)

meta = MetaData()
UsersTable = Table(
    'Users', meta, 
    Column('Username', String, primary_key=True), 
    Column('Password', String),
    Column('isAdmin', Boolean),
    Column('isVerified', Boolean),
)
HouseTable = Table(
    'Houses', meta, 
    Column("Title", String, primary_key=True),
    Column("Message", String),
    Column("Owner", String),
    Column("CityPart", String),
    Column("Meter", String),
    Column("Room", String),
    Column("YearsOld", String),
    Column("Floor", String),
    Column("HasParking", String),
    Column("HasStoreroom", String),
    Column("isVerified", Boolean),
    Column("isSale", Boolean),
    Column("Mode", Boolean),
    Column("SellPrice", FLOAT),
    Column("MortPrice", FLOAT),
    Column("RentPrice", FLOAT),
    Column("CanSell", Boolean),
    Column("LOwn", String),
    Column("Nice", FLOAT)
)
RequestTable = Table(
    'Reqs', meta, 
    Column("Title", String),
    Column("Details", String),
    Column("Price", FLOAT),
    Column("MortPrice", FLOAT),
    Column("RentPrice", FLOAT),
    Column("Username", String),
    Column("To", String),
    Column("Id", String, primary_key=True)
)

# Show ER model from here
filename = 'ERD.png'
render_er(meta, filename)
imgplot = plt.imshow(mpimg.imread(filename))
plt.rcParams["figure.figsize"] = (15,10)
plt.show()
