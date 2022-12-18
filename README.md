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
Tested application end to end and verified data in database also helped other group members to complete the task and resolve the issues.


