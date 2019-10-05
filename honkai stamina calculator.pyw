from tkinter import *
import subprocess
import datetime

win = Tk()

win.title("Honkai Stamina Calculator™")
# win.geometry("400x160")

def calculate1():
    currentStamina = CurrentStaminaBox.get()
    totalStamina = TotalStaminaBox.get()
    print(int(totalStamina)-int(currentStamina))
    hoursNeeded = (int(totalStamina)-int(currentStamina))
    print(datetime.datetime.now())
    time_when_full = datetime.datetime.now() + datetime.timedelta(hours=hoursNeeded/10)
    result1 = Label(win, text=(str(hoursNeeded/10) + " hours left until full stamina which will be on " + str(time_when_full.strftime("%a %B %d, %Y %I:%M %p"))), bg="black", fg="white")
    result1.grid(row=5, column=0, sticky=W)

def calculate2():
    currentStamina = CurrentStaminaBox.get()
    totalStamina = TotalStaminaBox.get()
    FMT = '%m/%d/%Y %I:%M %p'
    date = DateBox.get()
    time = DateBox2.get()
    timenow = datetime.datetime.now()
    fulltime = date + " " + time
    print(fulltime)
    timenow2 = timenow.strftime(FMT)
    answer = datetime.datetime.strptime(str(fulltime), FMT) - timenow.strptime(str(timenow2), FMT)
    print(answer)
    (h, m, s) = str(answer).split(':')
    result = int(h) + (int(m) / 60)
    result2 = result * 10
    result3 = int(totalStamina) - result2

    print(result3)
    # print(int(totalStamina)-int(currentStamina))
    # hoursNeeded = (int(totalStamina)-int(currentStamina))
    # print(datetime.datetime.now())
    # time_when_full = datetime.datetime.now() + datetime.timedelta(hours=hoursNeeded/10)
    result2 = Label(win, text=("You will need " + str(result3) + " stamina now so you'll have full stamina on " + fulltime), bg="black", fg="white")
    result2.grid(row=12, column=0, sticky=W)
    
def closeapp():
    sys.exit()


oneLabel = Label(win, text="Current Stamina:")
oneLabel.grid(row=0, column=0, sticky=W)
CurrentStaminaBox = Entry(win, width=50)
CurrentStaminaBox.grid(row=1, column=0, sticky=W)

twoLabel = Label(win, text="Total Stamina")
twoLabel.grid(row=2, column=0, sticky=W)
TotalStaminaBox = Entry(win, width=10)
TotalStaminaBox.grid(row=3, column=0, sticky=W)
oneButton = Button(win, text="CALCULATE!", command=calculate1)
oneButton.grid(row=4, column=0, sticky=W)
# twoButton = Button(win, text="OKAY!!", command=number)
# twoButton.grid(row=5, column=0, sticky=W)

threeLabel = Label(win, text="How much stamina should I have now so I get full stamina on a certain time?")
threeLabel.grid(row=6, column=0, sticky=W, pady=(15, 0))
dboxtxt = Label(win, text="MM/DD/YY")
dboxtxt.grid(row=7, column=0, sticky=W)
DateBox = Entry(win, width=10)
DateBox.grid(row=8, column=0, sticky=W,)
dboxtxt2 = Label(win, text="HH:MM am/pm ")
dboxtxt2.grid(row=9, column=0, sticky=W)
DateBox2 = Entry(win, width=10)
DateBox2.grid(row=10, column=0, sticky=W,)
oneButton = Button(win, text="CALCULATE!!", command=calculate2)
oneButton.grid(row=11, column=0, sticky=W)

finalLabel = Label(win, text="Ich liebe dich...")
finalLabel.grid(row=13, column=0, sticky=W, pady=(15, 0))
exitButton = Button(win, text="EXIT", command=closeapp)
exitButton.grid(row=14, column=1, sticky=W)


win.mainloop()
