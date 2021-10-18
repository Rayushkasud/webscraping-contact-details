import bs4
import requests
import lxml
import re


# def get_url():
#     with open('URLs.txt','r') as f:
#         url = f.readline().strip()
#         if url == 'http://www.msrit.edu/contact-us.html':
#             get_details(url)
#         else:
#             print('not equal')
def get_details1(url):
    #URL = get_url()
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text,'lxml')
    getmail = soup.find('h6', class_='contact-mail')
    getnum = soup.find('h6', class_='contact-phone')
  
    email_id = (getmail.a.text)
    phone_num = (getnum.a.text)
    


    # href = so.find('li', class_='menu-379 menu-path-node-39 odd')
    # go_to = URL+href.a['href']
    # print(go_to)

    # response = requests.get(go_to)
    # soup2 = bs4.BeautifulSoup(response.text,'lxml')
    # phone = soup2.find('div' , class_='field__item even')
    #print(email_id)
    return email_id,phone_num

def get_details2(url):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text,'lxml')
    phoneTag = soup.find('p', class_='text-6 text-color-light font-weight-bold')
    phone_num = phoneTag.text
    emailTag = soup.find('a', href='mailto:mail@example.com')
    email_id = emailTag.text
    return email_id,phone_num

def get_details3(url):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text,'lxml')
    phoneTag = soup.find_all('p',class_='widget-contact__text')
    for index,phonetags in enumerate(phoneTag):
        if index == 2:
            phone_num = phonetags.text
            #print(phonetags.text)

    return 'N/a',phone_num

def get_details4(url):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text,'lxml')
    phoneTag1 = soup.find('a' ,href="tel:+91-80-26711781")
    #phoneTag2 = soup.find('a' ,href="tel:+91-80-26711782")

    emailTag = soup.find('a' , href='mailto:principal@bnmit.in, bnmitprincipal@gmail.com')
   
    phone_num=phoneTag1.text
 
    # print(phone_num)
    email_id = emailTag.text
    # print(email_id)
    return email_id , phone_num

def get_details5(url):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text,'lxml')
    phoneTag = soup.find_all('div', class_='media-body')
    for index,tags in enumerate(phoneTag):
        if index == 1:
            phone_num = tags.p.text
        if index == 2:
            email_id = tags.p.text

    # print(phone_num)
    # print(email_id)
    # phone_num = phoneTag.text
    # emailTag = soup.find('a', href='mailto:mail@example.com')
    # email_id = emailTag.text
    return email_id,phone_num

# def get_details6(url):
response = requests.get('https://www.reliancedigital.in/content/contactus')
resp = response.text
phone_results=[]
email_results=[]
soup = bs4.BeautifulSoup(response.text,'lxml')
emailTag = soup.find_all('a')
phone = re.compile('^tel:([^\?]*)')
mail = re.compile('^mailto:([^\?]*)')
for anchors in emailTag:
    phones = phone.search(str(anchors.get('href')))
    mails = mail.search(str(anchors.get('href')))
    if phones:
        # results = anchors.text
        phone_results.append(anchors.text)
    #print(email)
    if mails:
        email_results.append(anchors.text)

print(phone_results)
print(email_results)


    


#res = temp.search(resp)
# strings = str(res)
# res = strings[48:][:-2]

# phoneTag = soup.find('a', href=temp)
# phone_num = phoneTag.text
# print(temp)
    # emailTag = soup.find('a',href="mailto:info@cmrit.ac.in")
    # email_id = emailTag.text
    # return results,'n'
def get_details7(url):

    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text,'lxml')
    phoneTag = soup.find('a', href="tel:+918046199000")
    phone_num = phoneTag.text
    emailTag = soup.find('a',href="mailto:enquiry@alliance.edu.in")
    email_id = emailTag.text

    # phone_num = phoneTag.text
    # emailTag = soup.find('i',href="mailto:info@cmrit.ac.in")
    # email_id = emailTag.text
    return email_id,phone_num

   
def get_details8(url):

    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text,'lxml')
  
    emailTag = soup.find('a',href="mailto:admissions@pes.edu")
    email_id = emailTag.text

    return email_id,'na'

def get_details9(url):

    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text,'lxml')
  
    phoneTag = soup.find('table',id='tablepress-65')
    phone = phoneTag.tbody.tr
    phone = phone.find('td',class_='column-3')

    return 'na',phone.text