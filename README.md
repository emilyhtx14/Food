# FoodSavers
FoodSavers is a web application that incentivizes users to donate to local supermarkets. FoodSavers primarily focuses on reducing supermarket food waste. Users on this web app are able to donate money for daily deliveries of soon-to-expired food (but still good to eat) to local homeless shelters. 


### Prerequest for Demo
* The project source code, **python3** and an **virtual env** with **Django** installed are required in order to run the project demo.


### Install virtualenv
    cd Food
    brew install python3
    sudo pip3 install virtualenv
    source venv/bin/active
    pip install Django==3.0

### Demo
    cd Food/src/djangoProject1
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

### Create a Donation
First a user enters the web application and logs into the server. Then a user is provided with ideal supermarket locations based on their own locatino (via Google Maps Javascript API). Finally a user is able to select any supermarket they want and submit a donation to the appropriate supermarket delivery date.  

This donation registers in a backend Django Database that contains all user submissions for the surrounding area. 

### Show User Profile Progress

After logging in a user can see their personal progress. They can track donation milestones, environmental impact, etc. In addition, the more a user donates, the more coupons they get from the supermarket as a token of thanks.

### Show Delivery Data 
One of the most special features of this project is the fact that the database renders dynamically to all users across the database. Additionally a % representing how close the community is to reaching a supermarket's delivery date goal is also shown.

### Contact
* Email : emilyhtx14@gmail.com
