import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
from eralchemy2 import render_er

from sqlalchemy import (MetaData, Table, Column, Integer, String, ForeignKey)    
metadata = MetaData()

# create your own model ....
users = Table('users', metadata,
    Column('user_id', Integer(), primary_key=True),
    Column('username', String(15), nullable=False, unique=True),
)    
orders = Table('orders', metadata,
    Column('order_id', Integer()),
    Column('user_id', ForeignKey('users.user_id')),
)
# add your own table ....

# Show ER model from here
filename = 'mymodel.png'
render_er(metadata, filename)
imgplot = plt.imshow(mpimg.imread(filename))
plt.rcParams["figure.figsize"] = (15,10)
plt.show()