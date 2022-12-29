import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
from eralchemy2 import render_er

from sqlalchemy import (MetaData, Table, Column, Integer, String, Boolean, ForeignKey)    

meta = MetaData()
UsersTable = Table(
    'Users', meta, 
    Column('Username', String, primary_key=True), 
    Column('Password', String),
    Column('isAdmin', Boolean),
    Column('isVerified', Boolean),
)
AdTable = Table(
    'Ads', meta, 
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
    Column("isSold", Boolean)
)
RequestTable = Table(
    'Reqs', meta, 
    Column("Title", String),
    Column("Details", String),
    Column("Price", String),
    Column("Username", String),
    Column("To", String),
    Column("Status", String),
    Column("Id", String, primary_key=True)
)
# Show ER model from here
filename = 'ERD.png'
render_er(meta, filename)
imgplot = plt.imshow(mpimg.imread(filename))
plt.rcParams["figure.figsize"] = (15,10)
plt.show()
