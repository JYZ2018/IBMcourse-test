def menu():
    import requests
    from bs4 import BeautifulSoup

    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
    res=requests.get('http://www.xiachufang.com/explore/',headers=headers)
    #print(res.status_code)
    soup=BeautifulSoup(res.text,'html.parser')
    #print(soup)
    soup1=soup.find_all(class_="name")
    #print(soup1)
    #print(type(soup1))
    menus=''
    for s in soup1:
        menus=menus+s.text.strip()
    return menus

def sendmail(menus):
    import smtplib,ssl
    from email.mime.text import MIMEText
    from email.header import Header

    port = 587 # For starttls
    smtp_server = "smtp.mail.yahoo.com"
    sender_email = input("please enter your yahoo mail address:")
    receiver_email=input("please enter receiver_email address:")
    password = input("Type your password and press enter:")

    msg = MIMEText(menus)
    msg['From'] = Header(sender_email)
    msg['To'] = Header(receiver_email)
    msg['Subject'] = Header('python test for summer')

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()

def job():
    print('开始一次任务')
    menus = menu()
    sendemail(menus)
    print('任务完成')
import schedule
schedule.every().day.at("07:30").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
