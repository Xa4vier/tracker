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
        date =  datetime.datetime.today().strftime('%Y-%m-%d')
        time = datetime.datetime.today().strftime('%H:%M:%S')
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

    ### set grid ###
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
        hide_all_canvas()
        main_window(window)

    def hide_all_canvas():
        canvas.get_tk_widget().destroy()
        btnMain.pack_forget()

    def set_canvas_this_week():
        dt = datetime.today()
        start = dt - timedelta(days=dt.weekday())
        end = start + timedelta(days=6)
        categories = select_all_from_category()
        pass
        #for category in categories:
        
            #if category[]


    def calculate_points():
        pass

    ### title ###
    window.title('Tracker - Plot')
    window.geometry('700x600')

    ### instantiate widgets ###
    # figure
    figure = Figure(figsize=(5,5), dpi=100)
    subplot = figure.add_subplot(111)
    subplot.plot(range(100), range(100))

    # canvas
    canvas = FigureCanvasTkAgg(figure, window)
    canvas.show()
    canvas.get_tk_widget().pack(side = BOTTOM, fill = X, expand = TRUE)

    btnMain = Button(window, text="main", command=go_main_window, width = 14, height = 1) 
    btnThisWeek = Button(window, text="this week", command=set_canvas_this_week, width = 14, height = 1) 
    btnThisMonth = Button(window, text="this Month", command=go_main_window, width = 14, height = 1) 
    btnThisYear = Button(window, text="this Year", command=go_main_window, width = 14, height = 1) 
    btnLastWeek = Button(window, text="<< week", command=go_main_window, width = 14, height = 1) 
    btnNextWeek = Button(window, text=" week >>", command=go_main_window, width = 14, height = 1) 
    btnLastMonth = Button(window, text="<< month", command=go_main_window, width = 14, height = 1) 
    btnNextMonth = Button(window, text="monthh >>", command=go_main_window, width = 14, height = 1) 

    ### set pack ###
    
    # buttons
    btnMain.pack()
    btnThisWeek.pack()
    btnThisMonth.pack()
    btnThisYear.pack()
    btnLastWeek.pack(side=LEFT)
    btnNextWeek.pack(side=RIGHT)
    btnLastMonth.pack(side=LEFT)
    btnNextMonth.pack(side=RIGHT)

# set window
window = Tk()

# load main window layout
#plot_canvas(window)
main_window(window)

# window main loop
window.mainloop()