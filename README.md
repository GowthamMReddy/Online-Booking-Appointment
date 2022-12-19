Online-Booking-Appointment in Python

------Project Group Details----------
B9IS123_2223_Group_C

Student Name              - Student ID

Rashmee Saxena            - 10632656

Gowtham Munivenkata Reddy - 10624812

Venkatrao Seelam          - 10625132

Likhith Pindi             - 10614739

-------Overview of Project----------
Nowadays people arround the world are facing legal issues for which they need to consult a lawyer. 
In their busy life people look for an easy way of consulting and getting themselves a best lawyer. As technology is growing faster,
people are tending to moving to smart applications to get their work done. This project is designed to meet the current
trend and allow individuals to book their appointment online with lawyers to get their work done. This project's primary focus is to 
provide user with a registration form and then login to the website and enter the user details and book an appointment by making a small reserve payment.

------Design the project framework-------- 
Flask Framework Implemented with the below list of Softwares:
1. Python Flask Framework-- Used for Backend business login and integrating the front end and Database
2. HTML-- Used for front end design creating web page
3. CSS -- Used for styling the webpage
4. Oracle -- Used for storing the data
5. Stripe payment gateway API-- Used to integrate with payment gateway to complete transaction

---------------------------Online Appointment Booking is a front-end---------------

Implementation of online appoinment booking for lawyer consultation via payment checkout and book an appointment.

Once user has booked appoinment he can see the boking details and have an option to view and delete his booking. 

User is displayed with the booking details on user dashboard screen.

-------------------------Functionality of the Application----------

Implement online appointment booking platform

1. Integration with Stripe API for the payment gateway checkout
2. Integration with Oracle database to keep the track of the user details : 
3. User details are inserted at the time of registration
4. User details are fetched at the time of login
5. User details are updated when user updates from front-end application
6. User details are deleted when user cancel the booked appointment from application

----------------Attributes---------------------------
1. Install Python
2. Import Python predefined libraries such as Flask, render-template, url_for
3. Install Oracle DB
4. Download InstantClient_21_7 and place in the Oracle folder path ('C:\oraclexe\app\oracle').
5. Import cx_Oracle
6. Stripe API

-------------Individual Contribution------------------------

Gowtham (10624812):

Took initiative and led the team, gathered all the requirements and explained it to the team and contributed the major part of the project. Researched about Python flask framework and how it integrates with templates and db. Installed pre-defined libraries used for developing the application. Organised the folder structure as per the standards. Designed the UserDashboard page using HTML and CSS and added the fields 'User Name', 'Age', 'Appointment_for', 'Lawyer_Name', 'Lawyer_Address', 'lawyer_contact'. Using CSS3 provided styling to the webpage and made fields visible with proper visibility. linked above field to python using the python flask framework. Used Render-template to render the template and run on the server. Designed payments page and booking confirmation page using HTML and CSS. Corrected all CSS changes for the login and register pages. Created bookings table and stored user booking details using Oracle db configuration, on click of booking confirmation and made changes to redirect control from userdashboard page to payments page and then to booking confirmation page. Added background images to all the pages throughtout the application. Drafted sql query to fetch the data from the Oracle db and display on the booking page UI. Tested application end to end and verified data in database. Also helped other group members to complete the taskS and resolve the bugs. Handled all the git conflicts and managed the merges. Resoled major issue while connecting to the Oracle db by setting the flag and maintaining the code. Maintained and performed the code review throughout the project. Implemented cancel booking button on bookings page and on-click of cancel booking, the record will be deleted from the db. 


Likhith (10614739): 

Created user register page and user login page using the HTML and provided styling using the CSS3 technology. Established the connection between oracle db and python and created the register table  and storing the user data in database. Created login table and integrated with login page to store the user login data in db. Made use of python flask frame work to integrate the register page and login page with DB . Wrote python code for business logic to verify user registration/ login details.Written code to capture the  user data from register page and login page using request form methods. Implemented sql fetch query for pulling the data from db and display on booking UI. Helped other team members resolve the bugs and performed unit testing while developing. 


Rashmee (10632656):

Initiated with the project requirements and segregated the 
Implementation of the Flask framework with installation of pre-requisites for Python, PIP, Flask, Flask-login
Taken the ownership to handle all the commits and merges for the entire group and have stable code in main branch.
Tested the code and added exception handling for Database connectivity for oracle
worked on CSS file for index page
Learned and Implemented the API Integration for Payment checkout using Stripe with pubic keys
Designed the layout of the payment gateway modal on user dashboard page
Contributed in CSS changes for user dashboard css page.
Added JavaScript code in userdashboard html page.
Contributed and learned the API’s and it’s integration for payment gateway.
Stripe API’s configuration and setup was done which is added in user dashboard html file. 
Checkout process of a payment for booking is added. 
Contributed in web page development.
Updated the userdashboard page with the payment button and integrated with stripe API and made configuration in the Stripe API to get the Payment gateway . authenticated the payment gateway and added the validations to the fields in the Payment gateway. Fixed issues while developing the application.
Worked with html, css, javascript, python
Created requirements file to create the scenarios for testing and development of the web application.
Managed and contributed in devOps tool git for this project with separate branches for all and merge the code into main as to track down the latest code changes.
Helped team members  to clone the project in different machines while working on a group project and helped in using git commands. 


Venkat (10625132):

Understood application and created business requirements. Updated the user dashboard page with the user profile button. made changes in HTML page and CSS page. helped group members with DB configuration and designing the webpage, fixed defects while debugging the application. Performed testing on application to make sure everything is working as expected. I used Hypertext Markup Language (HTML5) to create a spinning wheel page and using CSS3, like as colour, font size, and more, I'm adding styling for creating that html page and also write a code for java script for spinning the wheel and also I'm integrating with pyhton flask. It is standard alone application. In that HTML page was integrating flask. After that I’m creating alert message using HTML page for that styling purpose, I’m using CSS and then I"m integrate with pyhton flak with this code. I’m helping with groups members for checking the code and test the code entire code. Working together for login and signup pages by using html pages and css.
