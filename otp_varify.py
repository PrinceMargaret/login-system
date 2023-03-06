#!C:\Users\PrinceMargaret\anaconda3\python.exe
print("content-type:text/html\n\n")
__author__="Prince Jyoti"

import cgi,mysql.connector as mysql

#===========================================================================================================

form=cgi.FieldStorage()

email=form.getvalue("remail")
                                                                                               #variables

OTP=form.getvalue("OTP")


email="princeagrahari2000@gmail.com"

#============================================================================================================

#===========================================================================================================================
db = mysql.connect(
    host = "localhost",
    user = "root",
    database="mysql"
    
)
                                                                                                     #database
cursor = db.cursor()


cursor.execute("update user_data set user_otp=%s where email=%s",(OTP,email))
db.commit()
db.close()
cursor.close()

#=================================================================================================================
  
