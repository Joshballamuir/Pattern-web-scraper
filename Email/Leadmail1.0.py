#Leadsourcing email script by Josh Balla-Muir

import smtplib 
sv3 = 587
print("Welcome to leadsource email automator.")
sv = input("Please enter your email provider (gmail, outlook, aol or yahoo)")
if sv == 'gmail':
    sv2 = 'smtp.gmail.com'
if sv == 'outlook':
    sv2 = 'smtp.outlook.office365.com'
if sv == 'aol':
    sv2 = 'smtp.aol.com'
if sv == 'yahoo':
    sv2 = 'smtp.mail.yahoo.com'
    sv3 = '465'

print("Please login (remember to allow access for less secure apps)")

un = input("Username:")
pw = input("Password:")
sn = input("Sender name:")

loop = 1
while loop == 1:
    print("Enter the following in lower case:")
    a = input("Recipient's first name")
    b = input("Recipient's second name")
    c = input("Recipient's mail provider")
        
    aa = (a+b+'@'+c+'.com')
    bb = (a+b+'@'+c+'.co.uk')
    cc = (a+'.'+b+'@'+c+'.com')
    d = (a+'.'+b+'@'+c+'.co.uk')
    e = (a+'@'+c+'.com')
    f = (a+'@'+c+'.co.uk')
    g = (a[0]+b+'@'+c+'.com')
    h = (a[0]+b+'@'+c+'.co.uk')
    i = (a[0]+'.'+b+'@'+c+'.com')
    j = (a[0]+'.'+b+'@'+c+'.co.uk')
    k = (a[0]+'@'+c+'.com')
    l = (a[0]+'@'+c+'.co.uk')
    m = (a+b+'@'+c+'.net')
    n = (a+'.'+b+'@'+c+'.net')
    o = (a+'@'+c+'.net')
    p = (a[0]+'.'+b+'@'+c+'.net')
    q = (a[0]+'@'+c+'.net')
    r = (a[0]+b+'@'+c+'.net')
    
  
    company = input("Enter name of company")

    mail = smtplib.SMTP(host=sv2,port=sv3)
    mail.ehlo()
    mail.starttls()

    mail.login(un,pw)
    
    msg = 'Subject: %s\n\n%s' % ('Complaint', "{},""\n""\n""I would like to bring to your attention that I am not satisfied with recent financial dealings I have had with {}.""\n""\n""I wish to make a complaint in regards to a payment. Who is the best person to contact?""\n""\n""Regards,""\n""{}".format(a.title(),company,sn.title()))

    print('Sending email to the following:')
    print(aa,bb,cc,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r)

    confirm = input('Type y to confirm, n to abort or + to add additional addresses')
    if confirm == 'y':
    
        mail.sendmail(un, [aa,bb,cc,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r], msg) 
        mail.close()
        print("Email sent! Next:")

    if confirm == '+':
        print("Enter up to 5 additional addresses")
        r1 = input("Email 1") 
        r2 = input("Email 2")
        r3 = input("Email 3")
        r4 = input("Email 4")
        r5 = input("Email 5")

        choice = input("Enter a to send to all emails or c to send to custom list only")
        if choice == 'a':
            mail.sendmail(un, [aa,bb,cc,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,r1,r2,r3,r4,r5], msg) 
            mail.close()
            print("Email sent! Next:")
            

        if choice == 'c':
            mail.sendmail(un, [r1, r2, r3, r4, r5,], msg) 
            mail.close()
            print("Email sent! Next:")

        

    if confirm == 'n':
        print("Aborted")
        

    
    



###To do:
#replace variable input with excel variables
#print email before send - allow edit. No need for txt
