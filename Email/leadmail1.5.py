#Leadsource email script by Josh Balla-Muir

import smtplib 
sv3 = 587
print("Welcome to Leadmail.")
p1 = input("Please enter your email provider (gmail, outlook, aol or yahoo)")
sv = p1.lower()
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
    print("Enter the following:")
    first = input("Recipient's first name")
    second = input("Recipient's second name")
    p2 = input("Recipient's mail provider")

    a = first.lower()
    b = second.lower()
    c = p2.lower()

    company = p2.title()+' Ltd'
    
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
    s = (a+b[0]+'@'+c+'.com')
    t = (a+b[0]+'@'+c+'.co.uk')
    u = (a+b[0]+'@'+c+'.net')

    mail = smtplib.SMTP(host=sv2,port=sv3)
    mail.ehlo()
    mail.starttls()

    mail.login(un,pw)
    
    msg = 'Subject: %s\n\n%s' % ('Complaint', "{},""\n""\n""I would like to bring to your attention that I am not satisfied with recent financial dealings I have had with {}.""\n""\n""I wish to make a complaint in regards to a payment. Who is the best person to contact?""\n""\n""Regards,""\n""{}".format(a.title(),company,sn.title()))

    print('Sending email to the following:')
    print(aa,bb,cc,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r)

    loop = 2
    while loop == 2:

        print('Company = '+company)
        confirm = input('Type Y to confirm, N to abort, + to add additional addresses or d to change company name')
        confirm2 = confirm.lower()
        if confirm2 == 'y':
        
            mail.sendmail(un, [aa,bb,cc,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u], msg) 
            mail.close()
            print("Email sent! Next:")
            loop = 1

        if confirm == '+':
            print("Enter up to 5 additional addresses")
            r1 = input("Email 1") 
            r2 = input("Email 2")
            r3 = input("Email 3")
            r4 = input("Email 4")
            r5 = input("Email 5")

            if confirm2 == 'd':
                company = input("Enter new company name")
                #fix
                      
            choice = input("Enter A to send to all emails or C to send to custom list only")
            choice2 = choice.lower()
            if choice2 == 'a':
                mail.sendmail(un, [aa,bb,cc,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,r1,r2,r3,r4,r5], msg) 
                mail.close()
                print("Email sent! Next:")
                loop = 1
                #add new perms
                
            if choice2 == 'c':
                mail.sendmail(un, [r1, r2, r3, r4, r5,], msg) 
                mail.close()
                print("Email sent! Next:")
                loop = 1

            if confirm2 == 'n':
                print("Aborted")
                loop = 1
                #fix
                #ie perm?
