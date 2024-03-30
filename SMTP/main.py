import smtplib as smt
Connection = smt.SMTP("smtp.gmail.com",587)


myEmail = "basselawni1@gmail.com"
passWord="adohrhuvzpzovbsh"
Connection.starttls()
Connection.login(user=myEmail,password=passWord)
Connection.sendmail(from_addr=myEmail,to_addrs="Basselshow1@gmail.com",msg="Subject:Hello\n\nThis is not the body")
Connection.close()
