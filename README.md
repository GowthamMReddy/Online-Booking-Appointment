Online-Booking-Appointment in Python

------Project Group Details----------
B9IS123_2223_Group_C

Student Name              - Student ID

Rashmee Saxena            - 10632656

Gowtham Munivenkata Reddy - 10624812

Venkatrao Seelam          - 10625132

Likhith Pindi             - 10614739

-------Overview of Project----------
Now a day's people arround the world are facing some issue for which they need to coonsult the lawyers.
In their busy life people look for the easy way of consulting and getting their best lawyers. As technology is growing fast
people are tending to moving to smart applications to get their work done. this project is designed as to meet the current
trend and allow individuals to book their appointment online with lawyers to get their work done. this project primary focus is to 
provide user with Registration form and then login to website and enter the user details and book as appointment via payment.

------Design the project framework-------- 
Flask Framework Implemented with the below list of Softwares:
1. Python Flask Framework-- Used for Backend business login and integrating the front end and Database
2. HTML-- Used for front end design creating web page
3. CSS -- Used for styling the webpage
4. Oracle -- Used for storing the data
5. Stripe payment gateway API-- used to integrate with payment gateway to complete transaction

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

Gowtham (10624812) :
Designed the UserDashboard page using HTML and CSS and added the fields 'User Name', 'Age', 'Appointment_for', 'Lawyer_Name', 'Lawyer_Address', 'lawyer_contact'.
Using CSS3 provided styling to the webpage and made fields visible with proper visibility. linked above field to python using the python flask framework.
Used Render-template to render the template and run on the server. Added images to the webpage, connected to the oracle DB and storing the data into Oracle DB.
Tested application end to end and verified data in database also helped other group members to complete the task and resolve the 

Rashmee (10632656) :

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



Venkat(10625132) :
 Understood application and created business requirements. Updated the user dashboard page with the user profile button. made changes in HTML page and CSS page. helped group members with DB configuration and designing the webpage, fixed defects while debugging the application. Performed testing on application to make sure everything is working as expected.
I used Hypertext Markup Language (HTML5) to create a spinning wheel page and using CSS3, like as colour, font size, and more, I'm adding styling for creating that html page and also write a code for java script for spinning the wheel and also I'm integrating with pyhton flask. It is standard alone application. In that HTML page was integrating flask. After that I’m creating alert message using HTML page for that styling purpose, I’m using CSS and then I"m integrate with pyhton flak with this code. I’m helping with groups members for checking the code and test the code entire code. Working together for login and signup pages by using html pages and css.

