# Customer-Feedback

This a web-based tool using Django Web Framework for collecting customer feedback.

The project has been deployed to the cloud and hosted at PythonAnywhere. 

http://customerfeedback.pythonanywhere.com

Credentials for admin

Username: admin

Password: mji4kef2

There are 3 user roles for this app: Admin, Employee, and Customer. Admins manage the
system and view feedback. Employees use the app to solicit feedback from customers. 

Customers use the app to give feedback on various companies.

# Emails
Once a customer adds a review, the employee assigned to that company will receive an email that someone has added a review.

The app also sends out weekly reminder emails to all staff (admin and employees) on activity carried out in the app in the previous week (i.e reviews/companies/employess added,companies reassigned etc)

I've used the django.core.mail module from django

# Graphs

Using the FusionCharts Django Wrapper, I've been able to embed javascript charts in my django application.

These graphing facilities are used provide important statistics and data (on companies, employees and reviews) to admin on the home page.


