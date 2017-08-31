# HackFest BIT
## Team : Fault in Our Code
### Team Name(for Hackfest): Azor Ahai
#### Contest Description
* HackFest was a 8 Hour Code-athon conducted by Depratment of Computer Science and Engineering, Bannari Amman Institute of Technology on August 30,2017.
* 60+ Participants participated in the event.
* A set of 12 Problem statements were given and the participants were asked to solve any one among the twelve problem statements.

#### Selected Problem Statement
We **Team Azor Ahai** wanted to stand out from the crowd, so we chose to solve 3 problems out of the 12.
1. Create a Web App using Python and implement CRUD Operations
2. Create a GST Billing Application
3. Create a WebApp to show live weather updates of a particular city.

##### Python Web App
* We created the web application using Django, and we leveraged the inbuilt Django Administration for CRUD operations.
* A python was scriot was created to create database records.
* A Superuser was created to manage the database operations.
* All Create, Read, Update and Delete operations can be done using the Dashboard

##### GST Billing Application
* GST Tax rates for Goods and Services were scraped from internet using *BeautifulSoup* and *urllib*.
* GST Tax data was fed into DataBase using Python Scripts.
* Webpage which allows users to enter the item, quantity and price is connected with a Python Backend which fetches the tax rate from the database and computes the Tax amount and the total amount payable.
* A Bill is displayed as a webpage which can be printed.

##### Weather Updates
* A Python based web app which gets City name from user and displays weather statistics of the city.
* We used OpenWeather API to get live weather updates.
* Materialize CSS is used here.

#### How to Run
1. Install Django
```
pip install django
```
2. Clone the repository
```
git clone https://github.com/laxmena/Hackfest-BIT.git
```
3. Navigate to the Django Project and make migrations
```
cd Hackfest-BIT/HackfestBIT
python manage.py migrate
```
4. Create a Superuser
```
python manage.py createsuperuser
```
5. Run server
```
python manage.py runserver 8000
```
6. Open this link in browser
```
http://localhost:8000/home
```

###### Customize GST Billing App

7. Open admin dashboard
```
http://localhost:8000/admin
```

8. After logging in, open GST Services under GST Billing section

9. Click the add button to the top right corner. Enter details and save.

10. Open *http://localhost:8000/GSTBilling/home/* to see changes.
