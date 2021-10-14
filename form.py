from tkinter import *
from scrapeDetails import *
from tkinter import scrolledtext


def focus_field(event):
    input_field.focus_set()

def get(url):
    if url.strip() == "https://bmsce.ac.in/home/Contact-us":
         result = get_details2(url)
    elif url.strip() == "http://www.msrit.edu/contact-us.html":
        result = get_details(url)
    elif url.strip() == "https://www.iiitb.ac.in/":
        result = get_details3(url)
    elif url.strip() == 'https://www.bnmit.org/contact/':
        result = get_details4(url)
    elif url.strip() == 'https://drait.edu.in/home/contact_us':
        result = get_details5(url)
    elif url.strip() == 'https://www.cmrit.ac.in/':
        result = get_details6(url)
    elif url.strip() == 'https://drait.edu.in/home/contact_us':
        result = get_details7(url)
    elif url.strip() == 'https://drait.edu.in/home/contact_us':
        result = get_details8(url)
    elif url.strip() == 'https://drait.edu.in/home/contact_us':
        result = get_details9(url)
    elif url.strip() == 'https://drait.edu.in/home/contact_us':
        result = get_details10(url)

    else:
        result = ('no','data')
        


    # with open('results.txt','w') as f:

    #     f.writelines('mail: '+result[0]+'\n')
    #     f.writelines('Phone Number :'+result[1]+'\n')

    results_area.insert('end','mail: '+result[0]+'\n')
    results_area.insert('end','Phone Number :'+result[1]+'\n')
    results_area.update()
def writeURL():
    url = input_field.get()
    print(url)
    with open('URLs.txt','w') as f:
        f.writelines(url)
    get(url)
    


window = Tk()
window.configure(background='light blue')
window.title('Enter URL of website whose Data is to be fetched')
window.geometry('500x300')
heading = Label(window , text='Enter URL of website whose Data is to be fetched',bg='light blue',height='3')
input = Label(window,text='input',bg='light blue')
results = Label(window,text='Results',bg='light pink')

 
input.place(x=60,y=150)
results.place(x=40,y=210)
inputVal = StringVar()
resultsVal= StringVar()

heading.grid(row=0,column=1)
input.place(x=50,y=150)

input_field = Entry(textvariable = inputVal,width = 30)
input_field.bind('<Return>',focus_field)
results_area = scrolledtext.ScrolledText(window,wrap = WORD, width=50)


		
input_field.place(x=100, y=100)
results_area.place(x= 100,y= 200)

submit = Button(window, text="Submit", fg="Black",
                    bg="light blue",command= writeURL)

submit.place(x=100, y=150)
window.mainloop()



   



