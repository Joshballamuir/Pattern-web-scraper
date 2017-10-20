#Leadsourcing email script by Josh Balla-Muir

import smtplib
print("Welcome to leadsource email automator.")
sv = input("Please enter your email provider (gmail and outlook are currently supported)")
if sv == 'gmail':
    sv2 = 'smtp.gmail.com'
if sv == 'outlook':
    sv2 = 'smtp.outlook.office365.com'

print("Please login (if using gmail remember to allow less secure app usage)")

un = input("Username:")
pw = input("Password:")

loop = 1
while loop == 1:
    
    r1 = input("Enter recipient's email") 
    r2 = input("Enter 2nd permutation")
    r3 = input("Enter 3rd permutation")
    r4 = input("Enter 4th permutation")
    r5 = input("Enter 5th permutation")
    r6 = input("Enter 6th permutation")
    name = input("Enter name of recipient") 
    company = input("Enter name of company")

    mail = smtplib.SMTP(host=sv2,port=587)
    mail.ehlo()
    mail.starttls()

    mail.login(un,pw)
    
    msg = 'Subject: %s\n\n%s' % ('Complaint', "{},""\n""\n""I would like to bring to your attention that I am not satisfied with recent financial dealings I have had with {}.""\n""\n""I wish to make a complaint in regards to a payment. Who is the best person to contact?""\n""\n""Regards,""\n""Stuart".format(name,company))

    mail.sendmail(un, [r1, r2, r3, r4, r5, r6,], msg) 
    mail.close()

    print("Email sent! Next:")
    



###To do:

#replace variable input with excel variables
#automate permutation
#print email before send - allow edit. No need for txt
