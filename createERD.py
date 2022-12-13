import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
from eralchemy2 import render_er

from sqlalchemy import (MetaData, Table, Column, Integer, String, Boolean, ForeignKey)    
metadata = MetaData()

# create your own model ....
UsersTable = Table(
            'Users', metadata, 
            Column('Username', String, primary_key=True), 
            Column('Password', String),
            Column('isAdmin', Boolean),
        )
AgahiTable = Table(
    'Agahis', metadata, 
    Column("Title", String, primary_key=True),
    Column("Message", String),
    Column("Writer", String),
    Column("CityPart", String),
    Column("Meter", String),
    Column("Room", String),
    Column("YearsOld", String),
    Column("Floor", String),
    Column("HasParking", String),
    Column("HasStoreroom", String),
)
# add your own table ....

# Show ER model from here
filename = 'mymodel.png'
render_er(metadata, filename)
imgplot = plt.imshow(mpimg.imread(filename))
plt.rcParams["figure.figsize"] = (15,10)
plt.show()