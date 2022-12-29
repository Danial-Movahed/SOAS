# SOAS
SOAS is not Ordinary Amlaki System
### This is the improved version of SOAS
# Implementation
## Inventory system
In this implementation, each user has an inverntory of houses. After adding a house, user can set the house for rent or sale *after* admin has verified that the house actually belongs to the user and is not fake.
## HoNic Engine
HoNic Engine is a house scoring system created in this version to help users choose a house, it uses the different characteristics of a house to calculate a "Nice Score". (To see the exact formula for calculating this value please see [wiki](https://github.com/Danial-Movahed/SOAS/wiki))

This score is used to sort the houses from best to worst.
## House selling
Let's assume that person A wants to sell their house and person B wants to buy from them.

First person B will send a request to buy from person A with suggested price and details.

If person A accepts the request, the transaction is going to happen and owner of that house will be changed.

In this version there is no need for admin to verify each request because each house and each user is verified.
## House renting
Let's assume that person A want to rent their house and person B wants to buy from them.

First person B will send a request to buy from person A with suggested mortgage and rent price and details.

If person A accepts the request, Person B is going to co-own the house with person A and no one can resell or rerent the house until either person B disables rent mode and gets out of the house or person A kicks (!) person B out of the house and disables the rent mode!
## Admin
For the first time opening the application, the "First time setup" windows is going to open and it will ask for the admin's credentials. After the first time setup is done, login window will open each time SOAS opens.

## Users
In login window, there is a signup button which will open the signup window and ask user for the details. Each user is not verified when first created and needs to be verified by an admin before user can login to SOAS.

## Saving data
This version uses sqlalchemy for saving data to a sqlite database from python. (See [wiki](https://github.com/Danial-Movahed/SOAS/wiki) for more information)

