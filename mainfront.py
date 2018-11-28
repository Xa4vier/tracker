# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Sun Nov 18 23:10:15 2018

# @author: xaviervanegdom
# """

# python tkinter
from tkinter import *
from datetime import *
import csv

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

from domein.procesActivities import add_activity_by_id
from domein.pointCalculcation import calculate_points_by_range_date
from domein.categoryActions import get_all_categories, add_new_category

from times import start_end_this_week, start_end_last_week, start_end_next_week, start_end_this_month, start_end_next_month, start_end_last_month
from account import save_account


def main_window(window): 
    
    ### function part of the main window function
    def add_activity(): 
        if selected.get() == 0:
            lblWarning.configure(text='Geen categorie geselecteerd')
        else :
            print(categories[selected.get() - 1][3])
            if entryMoney.get() == '' and categories[selected.get() - 1][3] == 0:
                message = add_activity_by_id(selected.get())
                set_warning_add(message)
            else :
                try :
                    if int(entryMoney.get()) > 0:
                        message = add_activity_by_id(selected.get(), entryMoney.get())
                        entryMoney.configure(text = '')
                        set_warning_add(message)
                    elif int(entryMoney.get()) <= 0:
                        lblWarning.configure(text = f"Geen getal onder de 1!")
                except ValueError :
                    lblWarning.configure(text = f"Er moet een getal worden ingevoerd!")
            
    def set_warning_add(message):
        if message == 'start': 
            lblWarning.configure(text = f"Start")
        elif message == 'end':
            lblWarning.configure(text = f"Einde")
        elif message == 'succes_money':
            lblWarning.configure(text=f'€{entryMoney.get()},- toegevoegd bij {names[selected.get() - 1]}!!')
        elif message == 'succes_once':
            lblWarning.configure(text=f'once opgeslagen!!')
        elif message == 'already_saved':
            lblWarning.configure(text='Is al opgeslagen') 

    # new windows
    def new_category():
        forget_all_main()
        new_category_window(window)

    def make_plot():
        forget_all_main()
        plot_canvas(window)

    def forget_all_main():
        # buttons
        btnSSM.place_forget()
        btnCategory.place_forget()
        btnPlot.place_forget()
        
        # radio boxes
        for i in rads:
            i.place_forget()

        # entries
        entryMoney.place_forget()

        # labels
        lblWarning.place_forget()
        lblMoney.place_forget()

    ### window settings ###
    window.title("Tracker - Main (dev)")
    # width x height + x_offset + y_offset:
    window.geometry('500x400+30+30')

    nav_size = 150

    ### instantiate widgets ###
    # buttons
    btnSSM = Button(window, text="Start/Stop/Amount", command=add_activity, fg="green") 
    btnCategory = Button(window, text="nieuwe categorie", command=new_category, width = 14, height = 1) 
    btnPlot = Button(window, text="plot", command=make_plot, width = 14, height = 1) 

    # radio boxes
    selected = IntVar()
    categories = get_all_category()
    names = [name[1].replace('_', ' ') for name in categories]
    indexes = [i[0] for i in categories]
    values = [i for i in range(1, len(names) + 1)]
    rads = []
    for i in range(len(names)):
        rads.append(Radiobutton(window, text=names[i], value=values[i], variable=selected))

    # entry
    entryMoney = Entry(window)

    # labels
    lblMoney = Label(window, text='Geld:', fg='blue')
    lblWarning = Label(window, fg='red')

    ### set geo ###
    # buttons
    btnSSM.place(x = 10, y = 40 ,width = 250, height = 150)
    
    # nav buttons
    btnCategory.place(x = 10, y = 10, width = nav_size)
    btnPlot.place(x = (nav_size + 20) * 1, y = 10, width = nav_size)

    # radio buttons
    for i in range(len(rads)):
         rads[i].place(x = 40, y = 240 + 25 * i)

    # entry
    entryMoney.place(x = 60, y = 260 + len(rads) * 25)

    # labels
    lblMoney.place(x = 10, y = 260 + len(rads) * 25)
    lblWarning.place(x = 40, y = 210)

def new_category_window(window):
    
    ### function part of the new category window function
    def add_category():
        message = add_new_category(selected.get(), entryName.get(), entryPoints.get())
        entryName.configure(text='')
        entryPoints.configure(text='')
       
    def load_main_window():
        forget_all_new()
        main_window(window)

    def forget_all_new():
        # buttons
        btnMain.place_forget()
        btnAdd.place_forget()
        # radio buttons
        rbMoney.place_forget()
        rbTime.place_forget()
        rbOnce.place_forget()
        # entries
        entryName.place_forget()
        entryPoints.place_forget()
        # labels
        lblName.place_forget()
        lblPoints.place_forget()


    ### window settings ###
    window.title("Tracker - Nieuwe categorie")
    window.geometry('300x250')

    ### instantiate widgets ###
    # buttons
    btnMain = Button(window, text="main", command=load_main_window, width = 20, height = 2)
    btnAdd = Button(window, text='Toevoegen', command=add_category, width = 20, height = 2)
    
    # entries
    entryName = Entry(window, width=20)
    entryPoints = Entry(window, width=20)  

    # radio buttons
    selected = IntVar()
    rbTime = Radiobutton(window,text='Tijd', value=1, variable=selected)
    rbMoney = Radiobutton(window,text='Geld', value=2, variable=selected)  
    rbOnce = Radiobutton(window,text='Eenmalig', value=3, variable=selected) 

    # labels
    lblName = Label(window, text='Naam', fg='blue')
    lblPoints = Label(window, text='Punten', fg='blue')

    ### set grid ###
    xC = 60
    btn_size = 190
    # buttons
    btnAdd.place(x = xC + 1, y = 155, width = btn_size)
    btnMain.place(x = xC + 1, y = 195, width = btn_size)

    # text fields
    entryName.place(x = xC, y = 5)
    entryPoints.place(x = xC, y = 120)

    # radio buttons
    rbTime.place(x = xC, y = 45)
    rbMoney.place(x = xC, y = 70)
    rbOnce.place(x = xC, y = 95)

    # labels
    lblName.place(x = 5, y = 5)
    lblPoints.place(x = 5, y = 120)

def plot_canvas(window):
    ### function part of the new category window function
    def go_main_window():
        forget_all_canvas()
        main_window(window)

    def forget_all_canvas():
        # canvas
        canvas.get_tk_widget().destroy()
        # buttons
        btnMain.place_forget()
        btnThisWeek.place_forget() 
        btnThisMonth.place_forget() 
        #btnThisYear.pack_forget() 
        btnLastWeek.place_forget()
        btnNextWeek.place_forget()
        btnLastMonth.place_forget()
        btnNextMonth.place_forget() 
        lblWarnig.place_forget()

    def hide_warnings():
        lblWarnig.configure(text = '')

    def set_this_week():
        global start, end
        start, end = start_end_this_week()
        set_canvas(start, end, calculate_points_by_range_date(start, end), 'This Week', range(1, 8), 'Days', 'Points', [min, 30])
    
    def last_week():
        global start, end       
        start, end = start_end_last_week(start)
        set_canvas(start, end, calculate_points_by_range_date(start, end), 'last Week', range(1, 8), 'Days', 'Points', [min, 30])

    def next_week():
        global start, end       
        start, end = start_end_next_week(end)
        set_canvas(start, end, calculate_points_by_range_date(start, end), 'Next Week', range(1, 8), 'Days', 'Points', [min, 30])

    def set_this_month():
        global start, end
        start, end = start_end_this_month()
        set_canvas(start, end, calculate_points_by_range_date(start, end), 'This Month', range(1, end.day + 1), 'Days', 'Points', [min, 30])

    def next_month():
        global start, end       
        start, end = start_end_next_month(end)
        set_canvas(start, end, calculate_points_by_range_date(start, end), 'Next Month', range(1, end.day + 1), 'Days', 'Points', [min, 30])

    def last_month():
        global start, end       
        start, end = start_end_last_month(start)
        set_canvas(start, end, calculate_points_by_range_date(start, end), 'Last Month', range(1, end.day + 1), 'Days', 'Points', [min, 30])

    def set_canvas(start, end, points, title, xAxes, xLabel, yLabel, axHline):
        global canvas
        canvas.get_tk_widget().destroy()
        start = start.strftime('%d-%m-%Y')
        end = end.strftime('%d-%m-%Y')
        canvas = show_canvas(range(1, len(points) + 1), points, f'{title} - {start} - {end}', xAxes, xLabel, yLabel, axHline)

    # canvas object is returned so that other child functions can access it
    def show_canvas(x, y, title, xAxes = False, xLabel = False, yLabel = False, axHline = False):
        # figure
        figure = Figure(figsize=(5,5), dpi=100)
        subplot = figure.add_subplot(111)
        
        # set subplot
        subplot.set_title(title)
        #subplot.plot(x, y, color='orange')
        subplot.bar(x, y,)
        subplot.axhline(0 ,c="black",linewidth=1)

        if xAxes : subplot.set_xticks(xAxes)
        if xLabel : subplot.set_xlabel(xLabel)
        if yLabel : subplot.set_ylabel(yLabel)
        if axHline : 
            subplot.axhline(axHline[0] ,c="red",linewidth=1)
            subplot.axhline(axHline[1] ,c="blue",linewidth=1)

        subplot.set_yticks(range(-100, 101, 25))

        # canvas
        canvas = FigureCanvasTkAgg(figure, window)
        canvas.show()
        canvas.get_tk_widget().place(x = 125, y = 200, width = 1150, height = 550)
        return canvas
       
    ### title ###
    window.title('Tracker - Plot')
    window.geometry('1400x740')

    # variables 
    min = 20
    global start, end
    start = datetime.today()
    
    ### instantiate widgets ###
    global canvas
    canvas = show_canvas(range(7), range(7), 'dummie')

    # buttons
    btnMain = Button(window, text="main", fg='blue', command=go_main_window, width = 14, height = 1) 
    btnThisWeek = Button(window, text="this week", fg='orange', command=set_this_week, width = 14, height = 1) 
    btnThisMonth = Button(window, text="this Month", fg='orange', command=set_this_month, width = 14, height = 1) 
    #btnThisYear = Button(window, text="this Year", command=set_this_year, width = 14, height = 1) 
    btnLastWeek = Button(window, text="<< week", fg='red', command=last_week, width = 14, height = 1) 
    btnNextWeek = Button(window, text=" week >>", fg='red', command=next_week, width = 14, height = 1) 
    btnLastMonth = Button(window, text="<< month", fg='red', command=last_month, width = 14, height = 1) 
    btnNextMonth = Button(window, text="month >>", fg='red', command=next_month, width = 14, height = 1) 

    # labels
    lblWarnig = Label(window, fg='red')

    ### set pack ###
    
    # buttons
    btn_size = 150
    btn_size_move = 100    
    btnMain.place(x = 600, y = 12, width = btn_size)
    btnThisWeek.place(x = 600, y = 150, width = btn_size)
    btnThisMonth.place(x = 600, y = 170, width = btn_size)
    #btnThisYear.place()
    
    btnLastWeek.place(x = 10, y = 375, width = btn_size_move)
    btnNextWeek.place(x = 1290, y = 375, width = btn_size_move)
    btnLastMonth.place(x = 10, y = 395, width = btn_size_move)
    btnNextMonth.place(x = 1290, y = 395, width = btn_size_move)

    # labels
    # lblWarnig.pack(side=BOTTOM)

    set_this_week()

def make_account_window(window):

    def create_account():
        pass

    def login():
        pass

    ### window settings ###
    window.title("Tracker - Account aanmaken (dev)")
    # width x height + x_offset + y_offset:
    window.geometry('400x170+30+30')

    ### widgets ###

    # buttons 

    buttonAdd = Button(window, text="Maak aan", command=create_account, fg="green") 
    buttonLogin = Button(window, text="Log in", command=login, fg="green") 

    # entry
    entryName = Entry(window)
    entryPassword = Entry(window, show="*")
    entryPasswordCheck = Entry(window, show="*")
    
    # labels
    lblName = Label(window, text='Name:')
    lblPassword = Label(window, text='Password:')
    lblPasswordChek = Label(window, text='Password Check:')

    lblWarning = Label(window, fg='red', text='warning')

    ### set geo ###

    buttonAdd.place(x = 140, y = 110, width = 100)
    buttonLogin.place(x = 240, y = 110, width = 100)

    # entry
    x = 140
    w = 200
    entryName.place(x = x, y = 20, width = w)
    entryPassword.place(x = x, y = 50, width = w)
    entryPasswordCheck.place(x = x, y = 80, width = w)
    
    # labels
    lblName.place(x = 20, y = 24)
    lblPassword.place(x = 20, y = 54)
    lblPasswordChek.place(x = 20, y = 84)

    lblWarning.place(x = 140, y = 140)


# set window
window = Tk()


try :
    with open('data/account.csv', 'r') as f:
        reader = csv.reader(f)
        your_list = list(reader)
    account = [i for i in your_list[0]]
    main_window(window)

except FileNotFoundError:
    make_account_window(window)


# load main window layout

#plot_canvas(window)

# window main loop
window.mainloop()