#Email script by Josh Balla-Muir

import smtplib #uses built in email functions
sv3 = 587 #sv (server variable) 3. Declares port
print("Welcome to business email automator.")#welcomes user
#asks user to chose email provider. Program chooses apropriate smtp address and port
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
#helpful reminder for succes
print("Please login (remember to allow access for less secure apps)")
#username and password inputs to later be plugged in to the login and message itself
un = input("Username:")
pw = input("Password:")
sn = input("Sender name:")

loop = 1 #begins loop after user details have been saved in so mass emailing is faster
while loop == 1:
    #asks for 3 variables: recipient's first name, last name, mail provider and company name
    print("Enter the following in lower case:")
    a = input("Recipient's first name")
    b = input("Recipient's second name")
    c = input("Recipient's mail provider")
    company = input("Enter name of company")
    #variables a, b and c can be used to generate unlimited recipient combinations to increase delivery success rate. I have made 18 permutations so far    
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
    
    mail = smtplib.SMTP(host=sv2,port=sv3) #sends smtp host and port values for login
    mail.ehlo() #ehlo command identifies server
    mail.starttls() #starts encryption

    mail.login(un,pw) #plugs in login details
    #message content. Includes formatting for subject, breaks and variables
    msg = 'Subject: %s\n\n%s' % ('Business opportunity', "{},""\n""\n""I am interested in making a deal with your company {}.""\n""\n""If you are interested then please get back to me.""\n""\n""Regards,""\n""{}".format(a.title(),company,sn.title()))
    #outputs generated email permutations
    print('Sending email to the following:')
    print(aa,bb,cc,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r)
    #asks user to confirm
    confirm = input('Type y to confirm, n to abort or + to add additional addresses')
    #'y' confirmation sends mail to addresses listed
    if confirm == 'y':
        
        mail.sendmail(un, [aa,bb,cc,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r], msg) 
        mail.close()
        print("Email sent! Next:")
        #email is sent and program loops
        
    #'+' input adds custom addresses
    if confirm == '+':
        print("Enter up to 5 additional addresses")
        r1 = input("Email 1") 
        r2 = input("Email 2")
        r3 = input("Email 3")
        r4 = input("Email 4")
        r5 = input("Email 5")
        #'a' sends to original list and custom addresses 
        choice = input("Enter a to send to all emails or c to send to custom list only")
        if choice == 'a':
            mail.sendmail(un, [aa,bb,cc,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,r1,r2,r3,r4,r5], msg) 
            mail.close()
            print("Email sent! Next:")
            #email is sent and program loops
            
        #'c' sends to custom addresses only
        if choice == 'c':
            mail.sendmail(un, [r1, r2, r3, r4, r5,], msg) 
            mail.close()
            print("Email sent! Next:")
            #email is sent and program loops
        
    #'n' aborts program
    if confirm == 'n':
        print("Aborted")
        
