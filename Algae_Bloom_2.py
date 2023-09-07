import tkinter as tk

dark = True

decimal = False

temp_entered = False

ph_entered = False

Ph_to_overall = 0

temp = 0

overall = 0

ph_level = 0

root = tk.Tk()
root.geometry("300x400")
sum = 0

root.config(bg='#004D40')

root.title("Algae Blooms")

yes = tk.Label(root, text=' ', font=('Modern', 100))

buttonframe = tk.Frame(root)
buttonframe.configure(bg='#004D40')
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)

temperature = tk.Frame(root)
temperature.columnconfigure(0, weight=1)

def decimal():
    global decimal
    decimal = True

def change_color():
    global dark
    if dark == True:
        info.configure(foreground='black', background='white')
        label.configure(foreground='black', background='white')
        yes.configure(foreground='black', background='white')
        dark = False
        root.config(bg='#26A69A')
        buttonframe.config(bg='#26A69A')
    else:
        info.configure(foreground='white', background='black')
        label.configure(foreground='white', background='black')
        yes.configure(foreground='white', background='black')
        dark = True
        root.config(bg='#004D40')
        buttonframe.config(bg='#004D40')


def add_one():
    global ph_level
    global decimal
    if decimal == True:
        ph_level += 0.1
        label.config(text=ph_level)
        decimal = False
    else:
        ph_level += 1
        label.config(text=ph_level)


def add_two():
    global ph_level
    global decimal
    if decimal == True:
        ph_level += 0.2
        label.config(text=ph_level)
        decimal = False
    else:
        ph_level += 2
        label.config(text=ph_level)


def add_three():
    global ph_level
    global decimal
    if decimal == True:
        ph_level += 0.3
        label.config(text=ph_level)
        decimal = False
    else:
        ph_level += 3
        label.config(text=ph_level)

def add_four():
    global ph_level
    global decimal
    if decimal == True:
        ph_level += 0.4
        label.config(text=ph_level)
        decimal = False
    else:
        ph_level += 4
        label.config(text=ph_level)

def add_five():
    global ph_level
    global decimal
    if decimal == True:
        ph_level += 0.5
        label.config(text=ph_level)
        decimal = False
    else:
        ph_level += 5
        label.config(text=ph_level)

def add_six():
    global ph_level
    global decimal
    if decimal == True:
        ph_level += 0.6
        label.config(text=ph_level)
        decimal = False
    else:
        ph_level += 6
        label.config(text=ph_level)

def add_seven():
    global ph_level
    global decimal
    if decimal == True:
        ph_level += 0.7
        label.config(text=ph_level)
        decimal = False
    else:
        ph_level += 7
        label.config(text=ph_level)

def add_eight():
    global ph_level
    global decimal
    if decimal == True:
        ph_level += 0.8
        label.config(text=ph_level)
        decimal = False
    else:
        ph_level += 8
        label.config(text=ph_level)

def add_nine():
    global ph_level
    global decimal
    if decimal == True:
        ph_level += 0.9
        label.config(text=ph_level)
        decimal = False
    else:
        ph_level += 9
        label.config(text=ph_level)

def under_18():
    global temp
    temp += 0
    global temp_entered
    temp_entered = True

def eighteen_twentyone():
    global temp
    temp += 1
    global temp_entered
    temp_entered = True

def over_twentyone():
    global temp
    temp += 0
    global temp_entered
    temp_entered = True

def reset_temp():
    global temp_entered
    temp_entered = False


def clear():
    global ph_level
    global Ph_to_overall
    global ph_entered
    ph_entered = False
    Ph_to_overall == 0
    ph_level = 0
    label.config(text=ph_level)
    yes.config(text=' ')

def enter():
    global Ph_to_overall
    global ph_entered

    ph_entered = True

    if ph_level <= 9:
        Ph_to_overall += 0
    elif ph_level == 31:
        label.config(text='i will consume the flesh of your family', font=("Modern", 25))
    elif ph_level >= 12:
        Ph_to_overall += 0
    elif ph_level >= 9 and ph_level <= 12:
        Ph_to_overall += 1





def submit():
    global overall
    global temp
    global Ph_to_overall
    overall = temp + Ph_to_overall
    if temp_entered == False:
        yes.config(text="Please select a temperature", font=25)
        overall == 0
    if ph_entered == False:
        yes.config(text="Please enter your PH level", font=25)
        overall == 0
    if temp_entered == True and ph_entered == True:
        if overall == 2:
            yes.config(text="90% Chance For Algae Bloom", font=25)
        elif overall == 1:
            yes.config(text='45% Chance For Algae Bloom', font=25)
        else:
            yes.config(text='10% Chance For Algae Bloom', font=25)
def reset():
    global ph_level
    global overall
    global sum
    global ph_entered
    global temp
    global Ph_to_overall
    temp *= 0
    ph_entered = False
    ph_level *= 0
    label.config(text=' ')
    yes.config(text=' ')
    overall *= 0
    sum *= 0
    Ph_to_overall *= 0
    global temp_entered
    temp_entered = False




btn1 = tk.Button(buttonframe, text='1', font=('CenturyGothic', 25), command=add_one)
btn1.configure(bg='#495adf')
btn1.grid(row=0, column=0, sticky=tk.W + tk.E)

btn2 = tk.Button(buttonframe, text='2', font=('CenturyGothic', 25), command=add_two)
btn2.grid(row=0, column=1, sticky=tk.W + tk.E)

btn3 = tk.Button(buttonframe, text='3', font=('CenturyGothic', 25), command=add_three)
btn3.grid(row=0, column=2, sticky=tk.W + tk.E)

btn4 = tk.Button(buttonframe, text='4', font=('CenturyGothic', 25), command=add_four)
btn4.grid(row=1, column=0, sticky=tk.W + tk.E)

btn5 = tk.Button(buttonframe, text='5', font=('CenturyGothic', 25), command=add_five)
btn5.grid(row=1, column=1, sticky=tk.W + tk.E)

btn6 = tk.Button(buttonframe, text='6', font=('CenturyGothic', 25), command=add_six)
btn6.grid(row=1, column=2, sticky=tk.W + tk.E)

btn7 = tk.Button(buttonframe, text='7', font=('CenturyGothic', 25), command=add_seven)
btn7.grid(row=2, column=0, sticky=tk.W + tk.E)

btn8 = tk.Button(buttonframe, text='8', font=('CenturyGothic', 25), command=add_eight)
btn8.grid(row=2, column=1, sticky=tk.W + tk.E)

clear = tk.Button(root, text='CLEAR THE PH LEVEL', font=('CenturyGothic', 25), command=clear)

btn9 = tk.Button(buttonframe, text=9, font=('CenturyGothic', 25), command=add_nine)
btn9.grid(row=2, column=2, sticky=tk.W + tk.E)

btnperiod = tk.Button(buttonframe, text='.', font=('CenturyGothic', 25), command=decimal)
btnperiod.grid(row=3, column=0, sticky=tk.W + tk.E)

under18 = tk.Button(temperature, text="UNDER 18C", font=('CenturyGothic', 25), command=under_18)
under18.grid(row=0, column=0, sticky=tk.W + tk.E)

eightto21 = tk.Button(temperature, text='BETWEEN 19 AND 21', font=('CenturyGothic', 25), command=eighteen_twentyone)
eightto21.grid(row=0, column=1, sticky=tk.W + tk.E)

over21 = tk.Button(temperature, text='ABOVE 21', font=('CenturyGothic', 25), command=over_twentyone)
over21.grid(row=0, column=3, sticky=tk.W + tk.E)

reset_temp = tk.Button(root, text='RESET THE SELECTED TEMPERATURE', font=('Modern', 10), command=reset_temp)

information = "Algae blooms can be absolutely terrible for the environment, disrupting the ecosystem and causing permanent disrutions. Because of this, it is important to get rid of them as soon as they appear. To assist with the detection of these algae blooms, I have created a program that uses the temperature and PH level of water to predict whether or not algae blooms are present. Before doing this, however, I ran experiments which determined that the ideal temperature for algae growth is roughly 20 degrees celcius. Please use the buttons to enter your PH level and the temperature of your water. When you are satisfied, press 'submit' to find out whether algae blooms are likely to be in your water or not."
info = tk.Label(root, text=information, justify='left', wraplength=450, font=('BookAntiqua', 15))
info.pack()

reset = tk.Button(root, text='RESET EVERYTHING', font=('CenturyGothic', 25), command=reset)

submit = tk.Button(root, text="SUBMIT", font=('CenturyGothic', 25), command=submit)

enter = tk.Button(root, text='ENTER PH LEVEL', font=('CenturyGothic', 25), command=enter)

theme = tk.Button(root, text='CHANGE THEME', font=('CenturyGothic', 25), command=change_color)

label = tk.Label(root, text=('PH level =', ph_level), font=('CenturyGothic', 25))
label.pack(padx=50, pady=20)

buttonframe.pack()

clear.pack()

enter.pack(padx=0, pady=0)

temperature.pack(padx=0, pady=0)

reset_temp.pack()

submit.pack(padx=200, pady=0)

yes.pack()

reset.pack()

theme.pack()

root.mainloop()
