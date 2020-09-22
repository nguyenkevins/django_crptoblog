[![Build Status](https://travis-ci.com/nguyenkevins/nitrogen.svg?branch=master)](https://travis-ci.com/nguyenkevins/nitrogen)
# Django Database

![Demo1](https://github.com/nguyenkevins/nitrogen/blob/master/misc/wallpaper.png)

### To-Do List: 
* Need better GUI

## Summary
Django Database uses Django and MySQL to open a site and put information about students into the database.
With the help of Bootstrap for the ease and simplicity of user-interface, it is able to do the following:
* Add new student
* Edit student
* Delete a student
* Store information into MySQL
* Export student information to CSV
* Clear every student information


## Prerequisite
* MySQL v8.x
* Python 3.8.x
* Django 3.x
* Bootstrap 4

## MySQL Setup
This bot currently has a table for holding student information.
* Grade
* Student First Name
* Student Last Name
* Parent/Guardian First Name
* Parent/Guardian Last Name
* Student Email
* Student Contact

To create the djangodb database, do this:
```
* Delete every _pycache_ folder
* Delete migrations folder inside the student folder
* Open your MySQL terminal and type:
CREATE DATABASE djangodb;
```
Next, create the student table by doing this:
```
* Open your terminal or command that is in the root of the project:
python manage.py makemigrations student
python manage.py migrate
```

After setting up the student database, it should be described looking like this:
```
student
+----------+--------------+------+-----+---------+----------------+
| Field    | Type         | Null | Key | Default | Extra          |
+----------+--------------+------+-----+---------+----------------+
| id       | int          | NO   | PRI | NULL    | auto_increment |
| sid      | varchar(2)   | NO   |     | NULL    |                |
| sfname   | varchar(15)  | NO   |     | NULL    |                |
| slname   | varchar(15)  | NO   |     | NULL    |                |
| gfname   | varchar(15)  | NO   |     | NULL    |                |
| glname   | varchar(15)  | NO   |     | NULL    |                |
| semail   | varchar(254) | NO   |     | NULL    |                |
| scontact | varchar(15)  | NO   |     | NULL    |                |
+----------+--------------+------+-----+---------+----------------+
```
