from tkinter import *
from scrapeDetails import *
from tkinter import scrolledtext


def focus_field(event):
    input_field.focus_set()

def get(url):

    result = get_details(url)
        

    
    results_area.insert('end','Website: '+url+'\n')
    results_area.insert('end','mail: '+str(result[0])+'\n')
    results_area.insert('end','Phone Number :'+str(result[1])+'\n')
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



   



