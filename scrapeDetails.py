import bs4
import requests
import lxml


def get_url():
    with open('URLs.txt','r') as f:
        url = f.readline().strip()
        return url
def get_details():
    URL = get_url()
    res = requests.get(URL)
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
