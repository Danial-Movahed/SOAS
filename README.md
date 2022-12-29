# SOAS
SOAS is not Ordinary Amlaki System

## This is the old implementation of the Amlaki System, for a newer implementation please see NewGeneration branch!

# Implementation
## Requests and Ads
This implementation is more like Divar system. Each user can create an ad and request to buy an ad. For example lets assume that person A has created an ad on SOAS and person B wants to buy from person A.

Person B will request to buy from person A.

Person A can see this request in my requests menu and accept or decline it.

If person A declines this request, the request will get deleted but if person A accepts the request, the request will appear in admin's requests menu and admin should also accept it before anything happens.

## Ad ordering 
In this implementation there is no scoring system for houses and the sorting is just newest to oldests ad (for scoring system see branch [NewGeneration](https://github.com/Danial-Movahed/SOAS/tree/NewGeneration))

## Saving data
This version uses sqlalchemy for saving data to a sqlite database from python. (See [wiki](https://github.com/Danial-Movahed/SOAS/wiki) for more information)

## Why admin should accept the request?
Because there is no way to find if the ad actually belongs to the user and is not fake, so admin is going to verify the integrity of the request and the ad and if everything is ok, admin will accept the request and the ad owner will be changed.

## Admin
For the first time opening the application, the "First time setup" windows is going to open and it will ask for the admin's credentials. After the first time setup is done, login window will open each time SOAS opens.

## Users
In login window, there is a signup button which will open the signup window and ask user for the details. Each user is not verified when first created and needs to be verified by an admin before user can login to SOAS.
