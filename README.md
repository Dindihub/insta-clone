# insta-clone

## Description

This Application is an instagram application clone. It allows allows users to register,login,views posts,post photos and create a profile.Users can aslo comment on photos,like and follow other accounts. Users can search profiles by username. 


## Author

Sandra Dindi

You can view the site at:[insta-clone]()




## User Stories
As a user I would like to:
* Sign up
* Login
* Create a profile 
* Post images
* Comment on posts
* Like posts
* Follow accounts
* Search for profiles



## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Login | **On page load** | A login form for resgistered users, redirect to register page if not|
| Create an profile| **On login and create profile page** | create your profile|
| on home page | **On home page view** | see photos from other users|
| On home page| **upload image button** | upload your images|
| on home page| **On search bar** |  search for profiles|
|on home page | **on photos** | like and comment on other photos


## SetUp / Installation Requirements
### Prerequisites
* python3.8
* pipenv


### Cloning
* In your terminal:

        $ git clone git@github.com:Dindihub/insta-clone.git
        $ cd insta-clone

## Running the Application
* Creating the virtual environment

        $ pip3 install pipenv 
        $ pipenv shell
        
       


* To run the application, in your terminal:

        $ python3.8 manage.py runserver
        

## Testing the Application
* To run the tests for the class files:

        $ python3.8  manage.py tests 

## Technologies Used
* Python3.8
* Django 4.0.4
* Heroku

## Known Bugs
Follow and likes buttons do not work

### License
MIT (c) 2022 **[Sandra Dindi](https://github.com/Dindihub/insta-clone.git)**

