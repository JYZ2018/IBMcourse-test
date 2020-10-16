def menu():
    from selenium import  webdriver
    import time
    from selenium.webdriver.chrome.options import Options # 从options模块中调用Options类
    from bs4 import BeautifulSoup

    options_1 = webdriver.ChromeOptions()
    options_1.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    chrome_driver_path = r"C:\Users\jingya zhang\AppData\Local\Programs\Python\Python37-32\chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver_path, chrome_options=options_1)

    driver.get('http://www.xiachufang.com/explore/')
    time.sleep(2)
    menudetails=driver.find_element_by_class_name('normal-recipe-list').find_elements_by_tag_name('li')
    urls=[]
    for menu in menudetails:
        link=menu.find_element_by_class_name('name').find_element_by_tag_name('a').get_attribute('href')
        urls.append(link)

    for url in urls:
        driver.get(url)
        time.sleep(3)
        source=driver.page_source
        soup=BeautifulSoup(source,'html.parser')

        with open(r'C:\Users\jingya zhang\Desktop\menu.txt','a',encoding='utf-8') as file:

            title=soup.find('h1').text
            file.write(title)
            file.write('\n')
            materials=soup.find(class_='ings').find_all('tr')
            for material in materials:
                liao=material.find(class_='name').text
                file.write(liao.strip())
                file.write(' ')
                unit=material.find(class_='unit').text
                file.write(unit.strip())
                file.write('\n')

            file.write('\n')

            steps=soup.find_all('li',class_='container')
            for step in steps:
                file.write(step.text.strip())
                file.write('\n')
                file.write('\n')
            file.write('\n')

    driver.close()

def email():
    import smtplib,ssl
    from email.mime.text import MIMEText
    from email.header import Header

    port = 587 # For starttls
    smtp_server = "smtp.mail.yahoo.com"
    sender_email = input("please enter your yahoo mail address:")
    receiver_email='27866537@qq.com'


    password = input("Type your password and press enter:")

    with open(r'C:\Users\jingya zhang\Desktop\menu.txt','r',encoding='utf-8') as file:
        menu=file.read()

    msg = MIMEText(menu)
    msg['From'] = Header(sender_email)
    msg['To'] = Header(receiver_email)
    msg['Subject'] = Header('daily menu from xiachufang')

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

menu()
email()
