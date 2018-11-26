# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Sun Nov 18 23:10:15 2018

# @author: xaviervanegdom
# """

# python tkinter
from tkinter import *
from datetime import *

from get import *
from insert import *
from update import *

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

def days_hours_minutes(td):
    return td.seconds//3600, (td.seconds//60)%60 # hours, minutes

def main_window(window): 
    
    ### function part of the main window function
    def add_activity(): 
        if selected.get() == 0:
            lblWarning.configure(text='Geen categorie geselecteerd')
        else :
            lblWarning.configure(text='')
            category = select_category_by_id(selected.get())
            if category[2] == 1: # time
                proces_time(category)
            elif category[3] == 1: # money
                proces_money(category)
            elif category[4] == 1: # once
                proces_once(category)

    def proces_time(category):
        date =  datetime.today().strftime('%Y-%m-%d')
        time = datetime.today().strftime('%H:%M:%S')
        if len(select_time_by_date_endtime_cid(category[0], date)) == 0:
            insert_time_start(category[0], date, time)
        else :
            update_time_end(category[0], date, time)

    def proces_money(category):
        try :
            if int(entryMoney.get()) >= 0 : 
                insert_money(category[0], int(entryMoney.get()))
                name = category[1].replace('_', ' ')
                lblWarning.configure(text=f'€{entryMoney.get()},- toegevoegd aan {name}!')
            else :
                lblWarning.configure(text='kan niet onder de 1')
        except ValueError:
            lblWarning.configure(text='alleen getallen')

    def proces_once(category):
        date =  datetime.today().strftime('%Y-%m-%d')
        if len(select_once_by_cid_and_date(category[0], date)) == 0:
            insert_once(category[0], date)
            lblWarning.configure(text='Gelukt!')
        else :
            lblWarning.configure(text='Is al opgeslagen')   

    # new windows
    def new_category():
        hide_all_main()
        new_category_window(window)

    def make_plot():
        hide_all_main()
        plot_canvas(window)

    def hide_all_main():
        # buttons
        btnSSM.grid_remove()
        btnCategory.grid_remove()
        btnPlot.grid_remove()
        
        # radio boxes
        for i in rads:
            i.grid_remove()

        # entries
        entryMoney.grid_remove()

        # labels
        lblWarning.grid_remove()
        lblMoney.grid_remove()

    ### window settings ###
    window.title("Tracker - Main")
    window.geometry('500x400')

    ### instantiate widgets ###
    # buttons
    btnSSM = Button(window, text="Start/Stop/Amount", command=add_activity, width = 30, height = 10, fg="green") 
    btnCategory = Button(window, text="nieuwe categorie", command=new_category, width = 14, height = 1) 
    btnPlot = Button(window, text="plot", command=make_plot, width = 14, height = 1) 

    # radio boxes
    selected = IntVar()
    texts = select_all_category_names()
    texts = [text[0].replace('_', ' ') for text in texts]
    values = range(1, len(texts) + 1) 
    rads = []
    for i in range(len(texts)):
        rads.append(Radiobutton(window, text=texts[i], value=values[i], variable=selected))

    # entry
    entryMoney = Entry(window)

    # labels
    lblMoney = Label(window, text='Geld:', fg='blue')
    lblWarning = Label(window, fg='red')

    ### set geo ###
    # buttons
    btnSSM.grid()
    btnCategory.grid(column=1, row=2)
    btnPlot.grid(column=1, row=3)

    # radio buttons
    for i in range(len(rads)):
        rads[i].grid(row=i+3)

    # entry
    entryMoney.grid(row=len(rads) + 4)

    # labels
    lblMoney.grid(row=len(rads) + 3)
    lblWarning.grid(row=2)

def new_category_window(window):
    
    ### function part of the new category window function
    def add_category():
        if selected.get() == 1:
            insert_category(entryName.get(), True, False, False, entryPoints.get())
        elif selected.get() == 2 :
            insert_category(entryName.get(), False, True, False, entryPoints.get())
        else :
            insert_category(entryName.get(), False, False, True, entryPoints.get())
        entryName.configure(text='')
        entryPoints.configure(text='')
        
    def load_main_window():
        hide_all_new()
        main_window(window)

    def hide_all_new():
        # buttons
        btnMain.grid_remove()
        btnAdd.grid_remove()
        # radio buttons
        rbMoney.grid_remove()
        rbTime.grid_remove()
        rbOnce.grid_remove()
        # entries
        entryName.grid_remove()
        entryPoints.grid_remove()
        # labels
        lblName.grid_remove()
        lblPoints.grid_remove()


    ### window settings ###
    window.title("Tracker - Nieuwe categorie")
    window.geometry('300x200')

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
    lblName = Label(window, text='Naam')
    lblPoints = Label(window, text='Punten')

    ### set grid ###
    # buttons
    btnAdd.grid(row=6)
    btnMain.grid(row=7)

    # text fields
    entryName.grid(row=1)
    entryPoints.grid(row=5)

    # radio buttons
    rbTime.grid(row=2)
    rbMoney.grid(row=3)
    rbOnce.grid(row=4)

    # labels
    lblName.grid(row=1, column=2)
    lblPoints.grid(row=5, column=2)

def plot_canvas(window):
    ### function part of the new category window function
    def go_main_window():
        forget_all_canvas()
        main_window(window)

    def forget_all_canvas():
        # canvas
        canvas.get_tk_widget().destroy()
        # buttons
        btnMain.pack_forget()
        btnThisWeek.pack_forget() 
        btnThisMonth.pack_forget() 
        #btnThisYear.pack_forget() 
        btnLastWeek.pack_forget()
        btnNextWeek.pack_forget()
        btnLastMonth.pack_forget()
        btnNextMonth.pack_forget() 
        lblWarnig.pack_forget()

    def hide_warnings():
        lblWarnig.configure(text = '')

    def set_this_week():
        global start, end
        dt = datetime.today()
        start = dt - timedelta(days=dt.weekday())
        end = start + timedelta(days=6)
        set_canvas(start, end, calculate_points_by_range_date(start, end), 'This Week', range(1, 8), 'Days', 'Points', [min, 30])
    
    def last_week():
        global start, end       
        start -= timedelta(days=2)
        start -= timedelta(days=start.weekday())
        end = start + timedelta(days=6)
        set_canvas(start, end, calculate_points_by_range_date(start, end), 'last Week', range(1, 8), 'Days', 'Points', [min, 30])

    def next_week():
        global start, end       
        end += timedelta(days=2)
        start = end - timedelta(days=end.weekday())
        end = start + timedelta(days=6)
        set_canvas(start, end, calculate_points_by_range_date(start, end), 'Next Week', range(1, 8), 'Days', 'Points', [min, 30])

    def set_this_month():
        global start, end
        dt = datetime.today()        
        start = dt - timedelta(days=dt.day - 1)
        next_month = start.replace(day=28) + timedelta(days=4)  # this will never fail
        end = next_month - timedelta(days=next_month.day)
        set_canvas(start, end, calculate_points_by_range_date(start, end), 'This Month', range(1, end.day + 1), 'Days', 'Points', [min, 30])

    def next_month():
        global start, end       
        end += timedelta(days=2)
        start = end - timedelta(days=end.day - 1)
        next_month = end.replace(day=28) + timedelta(days=4)
        end = next_month - timedelta(days=next_month.day)
        set_canvas(start, end, calculate_points_by_range_date(start, end), 'Next Month', range(1, end.day + 1), 'Days', 'Points', [min, 30])

    def last_month():
        global start, end       
        end = start.replace(day=1) - timedelta(days=1)
        start = end - timedelta(days=end.day - 1)
        set_canvas(start, end, calculate_points_by_range_date(start, end), 'Last Month', range(1, end.day + 1), 'Days', 'Points', [min, 30])

    def set_canvas(start, end, points, title, xAxes, xLabel, yLabel, axHline):
        global canvas
        canvas.get_tk_widget().destroy()
        start = start.strftime('%d-%m-%Y')
        end = end.strftime('%d-%m-%Y')
        canvas = show_canvas(range(1, len(points) + 1), points, f'{title} - {start} - {end}', xAxes, xLabel, yLabel, axHline)

    def calculate_points_by_range_date(start, end):
        categories = select_all_from_category()
        points = []
        for category in categories:
            if category[2] == 1: # time
                allTime = select_time_by_start_end(category[0], start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d'))
                points.append(calculate_points_category(category, start, end, allTime, calculate_points_time))
            elif category[3] == 1: # money
                allMoneys = select_money_by_start_end(category[0], start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d'))
                points.append(calculate_points_category(category, start, end, allMoneys, calculate_points_money))
            elif category[4] == 1: # once
                allOnces = select_once_by_start_end(category[0], start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d'))
                points.append(calculate_points_category(category, start, end, allOnces, calculate_points_once))
        return combine_points_on_day(points)

    def combine_points_on_day(points):
        pointsToReturn = [0] * len(points[0])
        for i in range(len(points[0])):
            for row in points:
                pointsToReturn[i] += row[i]
        return pointsToReturn

    # gets a function to calculate the categories 
    # i is used as the index for the points, and days is used to check the day in the date. 
    def calculate_points_category(category, start, end, dataset, func):
        if end.day > start.day : # like start = 23/5 end = 30/5
            points = [0] * (end.day - start.day + 1)
            i = 0
            for day in range(start.day, end.day + 1):
                func(category, points, day, dataset, i)
                i += 1

        else : # like start = 30/5 end = 6/6 
            next_month = start.replace(day=28) + timedelta(days=4)  # this will never fail
            endMonth = next_month - timedelta(days=next_month.day)
            points = [0] * (end.day + endMonth.day - start.day + 1)           
            day = start.day 
            for i in range(len(points)):
                func(category, points, day, dataset, i)
                if day == endMonth.day:
                    day = 0
                day += 1

        return [int(p) for p in points]

    def calculate_points_time(category, points, day, allTimes, i):
        for time in allTimes:
            if time[2].day == day:
                if time[4] != None:
                    hours, minutes = days_hours_minutes(time[4] - time[3])
                    points[i] += category[5] * hours + (minutes/60) * category[5]
                else :
                    points[i] += 0

    def calculate_points_money(category, points, day, allMoneys, i):
            for money in allMoneys:
                if money[3].day == day:
                    points[i] += category[5] * money[2]

    # calculate all the point for a category where there is a once
    def calculate_points_once(category, points, day, allOnces, i):
            for once in allOnces:
                if once[2].day == day:
                    points[i] += category[5]

    # canvas object is returned so that other child functions can access it
    def show_canvas(x, y, title, xAxes = False, xLabel = False, yLabel = False, axHline = False):
        # figure
        figure = Figure(figsize=(5,5), dpi=100)
        subplot = figure.add_subplot(111)
        
        # set subplot
        subplot.set_title(title)
        subplot.plot(x, y, color='orange')
        subplot.bar(x, y,)
        subplot.axhline(0 ,c="black",linewidth=1)

        if xAxes : subplot.set_xticks(xAxes)
        if xLabel : subplot.set_xlabel(xLabel)
        if yLabel : subplot.set_ylabel(yLabel)
        if axHline : 
            subplot.axhline(axHline[0] ,c="red",linewidth=1)
            subplot.axhline(axHline[1] ,c="blue",linewidth=1)

        subplot.set_yticks(range(-30, 31, 5))

        # canvas
        canvas = FigureCanvasTkAgg(figure, window)
        canvas.show()
        canvas.get_tk_widget().pack(side = BOTTOM, fill = X, expand = TRUE)
        return canvas
       
    ### title ###
    window.title('Tracker - Plot')
    window.geometry('1400x600')

    # variables 
    min = 20
    global start, end
    start = datetime.today()
    
    ### instantiate widgets ###
    global canvas
    canvas = show_canvas(range(7), range(7), 'dummie')

    # buttons
    btnMain = Button(window, text="main", command=go_main_window, width = 14, height = 1) 
    btnThisWeek = Button(window, text="this week", command=set_this_week, width = 14, height = 1) 
    btnThisMonth = Button(window, text="this Month", command=set_this_month, width = 14, height = 1) 
    #btnThisYear = Button(window, text="this Year", command=set_this_year, width = 14, height = 1) 
    btnLastWeek = Button(window, text="<< week", command=last_week, width = 14, height = 1) 
    btnNextWeek = Button(window, text=" week >>", command=next_week, width = 14, height = 1) 
    btnLastMonth = Button(window, text="<< month", command=last_month, width = 14, height = 1) 
    btnNextMonth = Button(window, text="month >>", command=next_month, width = 14, height = 1) 

    # labels
    lblWarnig = Label(window, fg='red')

    ### set pack ###
    
    # buttons
    btnMain.pack()
    btnThisWeek.pack()
    btnThisMonth.pack()
    #btnThisYear.pack()
    btnLastWeek.pack(side=LEFT)
    btnNextWeek.pack(side=RIGHT)
    btnLastMonth.pack(side=LEFT)
    btnNextMonth.pack(side=RIGHT)

    # labels
    lblWarnig.pack(side=BOTTOM)

    set_this_week()

# set window
window = Tk()

# load main window layout
main_window(window)

# window main loop
window.mainloop()