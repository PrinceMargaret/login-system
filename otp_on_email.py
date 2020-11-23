#!C:\Users\PrinceMargaret\anaconda3\python.exe
print("content-type:text/html\n\n")

__author__="Prince"

import smtplib ,math, random ,cgi,mysql.connector as mysql

#===========================================================================================================

form=cgi.FieldStorage()
username=form.getvalue("usrnm")
email=form.getvalue("email")
                                                                                               #variables

password=form.getvalue("password")
cpassword=form.getvalue("cpassword")

db = mysql.connect(
    host = "localhost",
    user = "root",
    database="mysql"
    
)
                                                                                                     
cursor1 = db.cursor()    
cursor2 = db.cursor()
#============================================================================================================
def generateOTP() : 
   
    string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    OTP = "" 
    length = len(string)                                                                     
    for _ in range(6) : 
        OTP += string[math.floor(random.random() * length)]                                        #OTP
  
    return OTP 
OTP=generateOTP()
#=============================================================================================================
#editable part
cursor1.execute("SELECT * from admin")

 
records = cursor1.fetchall()      # list like [("owner email","app password")]

From, App_password= records[0][0],records[0][1]   # this detail used for login in smtp.gmail.com server
To=email         #give email where message you want send reciever email
Subject="PrinceMargaret"           #write your own subject PrinceMargaret only for example
Compose_email=f"your password is {OTP}"   #write what you want message 


with smtplib.SMTP("smtp.gmail.com",587) as smtp:
    smtp.ehlo()
    smtp.starttls()                                                                                #email
    smtp.ehlo()
    smtp.login(From,App_password)
    smtp.sendmail(From,To,f"Subject:{Subject} \n\n {Compose_email}")



#===========================================================================================================================



cursor2.execute("insert into user_data(username,email,passkey,otp) values(%s,%s,%s,%s)",(username,email,cpassword,OTP))
db.commit()
db.close()
cursor1.close()
cursor2.close()

#=================================================================================================================
  
print (''' <head><meta http-equiv="refresh" content="0;URL='otp.html'" /></head> ''')