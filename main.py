from ast import Lambda
from itertools import count
from tkinter import ttk
from tkinter import *
from typing import Counter

from tradingEconomics import *
from reuters import *
import webbrowser

# make the action to the url
def weblink(*args):
    index = mylist.curselection()[0]
    item = mylist.get(index)
    if 'https://' in item:
        webbrowser.open_new(item)

def displayTradingEconomics():
    # Message in the title area
    global w
    w["text"] = "display Treading Economics website"

    # display space settings
    global scroll_bar 
    global mylist
    mylist.delete(0, END)

    countryName = variable1.get()
    siteURL = {
        "Japan" : 'https://tradingeconomics.com/japan/news'
        , "United States" : 'https://tradingeconomics.com/united-states/news'
    }
    newsTitle = newsTradingEconomics(siteURL[variable1.get()])[0]
    newsURL = newsTradingEconomics(siteURL[variable1.get()])[1]
    tmpNewList = []
    count = 0
    for item in range(len(newsTitle)):
        tmpNewList.append(newsTitle[count])
        tmpNewList.append(newsURL[count])
        tmpNewList.append("")
        count += 1

    mylist.bind('<<ListboxSelect>>', weblink)

    for item in tmpNewList:
        mylist.insert(END, item)
    

    # display result
    mylist.pack( expand=True, fill = BOTH )
    scroll_bar.config( command = mylist.yview ) # link scrol bar and mylist contents




def displayReuters():
    # message in the title area
    global w
    w["text"] = "display Reuter news website"

    # display space settings
    global scroll_bar 
    global mylist
    mylist.delete(0, END)

    countryName = variable1.get()
    siteURL = {
        "Japan" : 'https://www.reuters.com/site-search/?query=japan'
        , "United States" : 'https://www.reuters.com/site-search/?query=us'
    }
    newsTitle = newsReuters(siteURL[variable1.get()])[0]
    newsURL = newsReuters(siteURL[variable1.get()])[1]

    tmpNewList = []
    count = 0
    for item in range(len(newsTitle)):
        tmpNewList.append(newsTitle[count])
        tmpNewList.append(newsURL[count])
        tmpNewList.append("")
        count += 1

    mylist.bind('<<ListboxSelect>>', weblink)

    for item in tmpNewList:
        mylist.insert(END, item)

    # display result
    mylist.pack( expand=True, fill = BOTH )
    scroll_bar.config( command = mylist.yview ) # link scrol bar and mylist contents




root = Tk()
root.geometry("640x600")
root.title("Forex project")
w = Label(root, text="\nWELCOME TO MY PROJECT", font="Helvtica 15 bold")
w.pack()


fm = Frame(root, width=300, height=200, bg="blue")
fm.pack(side=TOP, expand=NO, fill=NONE)

# button for displayTradingEconomics, Reuter, quit
myTradingEconomics = Button(fm, text='TradingEconomics', command=displayTradingEconomics, width=20).pack(side=LEFT)
myReuter = Button(fm, text='Reuter', command=displayReuters, width=20).pack(side=LEFT)
myExit = Button(fm, text='Stop', command=root.destroy, width=20).pack(side=LEFT)

# dropdown menu to select country
variable1 = StringVar(root)
variable1.set("Japan") # default value
country1 = OptionMenu(root, variable1, "Japan", "United States").pack()

# display title message
titleMessage = Label(root, text="Select option to display", font="Helvtica 15 bold")
titleMessage.pack()

# blank display space
scroll_bar = Scrollbar(root)
scroll_bar.pack( side = RIGHT, fill = Y )
mylist = Listbox(root, yscrollcommand = scroll_bar.set )
mylist.pack( expand=True, fill = BOTH )
scroll_bar.config( command = mylist.yview ) # link scrol bar and mylist contents


root.mainloop()