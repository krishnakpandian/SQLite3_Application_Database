# -*- coding: utf-8 -*-
"""
Spyder Editor

Krishna Pandian
SQLite Application Database Management Project
"""

import sqlite3
import validators
from validate_email import validate_email  
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException


account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)
key = client.keys('').fetch()
credential = client.chat.credentials.create(type='gcm')
client = Client()

pathway = 'data.db'


def credentials():
    print(credential.sid)

    
def retrieve_first():
    valid = True
    while(valid):
        first_name = input('What is your First Name?\n')
        for char in first_name:
            if char.isdigit():
                print('Invalid String\n')
                break
        valid = False
    return first_name
    
    
def retrieve_last():
    valid = True
    while(valid):
        last_name = input('What is your Last Name?\n')
        for char in last_name:
            if char.isdigit():
                print('Invalid String\n')
                break
        valid = False
    return last_name
            
    
def retrieve_email():
    email_good = False
    while not email_good:
        email = input('What is your Email?\n')
        valid_email = validate_email(email)
        if valid_email == False:
            print('Invalid Input\n')
        else:
            database = sqlite3.connect(pathway)    
            command = database.cursor()
            command.execute('SELECT 1 FROM APPLICANT WHERE email = :email',{'email':email})
            duplicate = command.fetchall()
            if len(duplicate) != 0:
                print('No Duplicate Applications\n')
            else:
                email_good = True
    return email

def valid_number(number):
    try:
        response = client.lookups.phone_numbers(number).fetch(type="carrier")
        print(response)
        return True
    except TwilioRestException as e:
        if e.code == 20404:
            return False
        else:
            raise e
            return False

    
def retrieve_number():
    valid = True
    while(valid):
        phone_number = input('What is your Phone Number? (No Dashes)\n')
        
        valid = not valid_number(phone_number)
        if valid == True:
            print('Invalid Number\n')
        
        valid = False
    return phone_number

def retrieve_grade():
    valid = True
    while(valid):
        grade = input("What is your current G.P.A\n")
        try:
            if float(grade) > 4.0 or float(grade) < 0:
                print('Invalid Input\n')
            else:
                valid = False
        except:
            print('Invalid Input\n')
    return float(grade)
    
    
def retrive_linkedin():
    valid = True
    while(valid):
        linkedin = input('What is thie link to your LinkedIn?\n')
        if 'linkedin.com/in/' not in linkedin:
            continue
        test = validators.url(linkedin)
        if test:
            valid = False
    return linkedin            

    
def database_create():
    database = sqlite3.connect(pathway)
    command = database.cursor()
    try:
        command.execute("""Create TABLE APPLICANT (first text, last text, email text, phone text, linkedin text, grade float)""")
        database.commit()
    except:
        print('failed')
        database.close()

    
def database_add(first,last, email, number, linkedin, grade):
    database = sqlite3.connect(pathway)
    command = database.cursor()
    
    try:
        command.execute("INSERT INTO APPLICANT VALUES(?,?,?,?,?,?)",(first.lower(), last.lower(), email, number, linkedin, grade))
        database.commit()
        database.close()
        return True
    except Exception as e:
        print(e)
        return False
    
def database_del_by_gpa():
    database = sqlite3.connect(pathway)
    command = database.cursor()

    command.execute("SELECT * FROM APPLICANT WHERE grade < 3.0")  
    delete = command.fetchall()
    print(delete)
    
    for arg in range(len(delete)):
        command.execute("DELETE FROM APPLICANT WHERE first = :first AND last = :last AND email = :email",{'first': delete[arg][0].lower(), 'last': delete[arg][1].lower(), 'email': delete[arg][2]})
    
    database.commit()
    database.close()

def database_del(first, last, email):
    database = sqlite3.connect(pathway)
    command = database.cursor()

    try:
        command.execute("DELETE FROM APPLICANT WHERE first = :first AND last = :last AND email = :email",{'first': first.lower(), 'last': last.lower(), 'email': email})
    except:
        print('Data Not Available')
        
    database.commit()
    database.close()    
    
    
def database_print():
    database = sqlite3.connect(pathway)
    command = database.cursor()
    
    command.execute("SELECT * FROM APPLICANT WHERE grade != 5.0")
    current = command.fetchall()
    
    database.commit()
    database.close()
    
    print(current)
    return current    
    
    
