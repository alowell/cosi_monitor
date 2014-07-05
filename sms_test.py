import smtplib

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login('cosi.monitor@gmail.com','nuclearcomptontelescope')
server.sendmail('ALEXXX','4155924332@vtext.com','SUP')
server.close()

