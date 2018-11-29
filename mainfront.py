# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Sun Nov 18 23:10:15 2018

# @author: xaviervanegdom
# """

# python tkinter
from tkinter import Tk, Button, Label, Entry, Radiobutton, IntVar
from datetime import datetime

from get import *

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

from procesActivities import add_activity_by_id
from add_category import add_new_category
from times import start_end_this_week, start_end_last_week, start_end_next_week, start_end_this_month, start_end_next_month, start_end_last_month
from pointCalculcation import calculate_points_by_range_date

class Main_Window(): 
    
    ### function part of the main window function
    def add_activity(self): 
        if self.selected.get() == 0:
            self.lblWarning.configure(text='Geen categorie geselecteerd')
        else :
            print(self.categories[self.selected.get() - 1][4])
            if self.entryMoney.get() == '' and self.categories[self.selected.get() - 1][5] == 0:
                message = add_activity_by_id(self.selected.get())
                self.set_warning_add(message)
            else :
                try :
                    if int(self.entryMoney.get()) > 0:
                        message = add_activity_by_id(self.selected.get(), self.entryMoney.get())
                        self.entryMoney.configure(text = '')
                        self.set_warning_add(message)
                    elif int(self.entryMoney.get()) <= 0:
                        self.lblWarning.configure(text = f"Geen getal onder de 1!")
                except ValueError :
                    self.lblWarning.configure(text = f"Er moet een getal worden ingevoerd!")
            
    def set_warning_add(self, message):
        if message == 'start': 
            self.lblWarning.configure(text = f"Start")
        elif message == 'end':
            self.lblWarning.configure(text = f"Einde")
        elif message == 'succes_money':
            self.lblWarning.configure(text=f'€{self.entryMoney.get()},- toegevoegd bij {self.names[self.selected.get() - 1]}!!')
        elif message == 'succes_once':
            self.lblWarning.configure(text=f'once opgeslagen!!')
        elif message == 'already_saved':
            self.lblWarning.configure(text='Is al opgeslagen') 

    # new windows
    def new_category(self):
        #winfo_children()
        self.forget_all_main()
        New_Category_Window(self.window)

    def make_plot(self):
        self.forget_all_main()
        Plot_Canvas(self.window)

    def forget_all_main(self):
        # buttons
        self.btnSSM.place_forget()
        self.btnCategory.place_forget()
        self.btnPlot.place_forget()
        
        # radio boxes
        for i in self.rads:
            i.place_forget()

        # entries
        self.entryMoney.place_forget()

        # labels
        self.lblWarning.place_forget()
        self.lblMoney.place_forget()
    
    def __init__(self, window):
        ### window settings ###
        self.window = window
        self.window.title("Tracker - Main (dev)")
        # width x height + x_offset + y_offset:
        self.window.geometry('500x400+30+30')

        self.nav_size = 150

        ### instantiate widgets ###
        # buttons
        self.btnSSM = Button(self.window, text="Start/Stop/Amount", command=self.add_activity, fg="green") 
        self.btnCategory = Button(self.window, text="nieuwe categorie", command=self.new_category, width = 14, height = 1) 
        self.btnPlot = Button(self.window, text="plot", command=self.make_plot, width = 14, height = 1) 

        # radio boxes
        self.selected = IntVar()
        self.categories = select_all_from_category()
        self.names = [name[1].replace('_', ' ') for name in self.categories]
        self.indexes = [i[0] for i in self.categories]
        self.values = [i for i in range(1, len(self.names) + 1)]
        self.rads = []
        for i in range(len(self.names)):
            self.rads.append(Radiobutton(self.window, text=self.names[i], value=self.values[i], variable=self.selected))

        # entry
        self.entryMoney = Entry(self.window)

        # labels
        self.lblMoney = Label(self.window, text='Geld:', fg='blue')
        self.lblWarning = Label(self.window, fg='red')

        ### set geo ###
        # buttons
        self.btnSSM.place(x = 10, y = 40 ,width = 250, height = 150)
        
        # nav buttons
        self.btnCategory.place(x = 10, y = 10, width = self.nav_size)
        self.btnPlot.place(x = (self.nav_size + 20) * 1, y = 10, width = self.nav_size)

        # radio buttons
        for i in range(len(self.rads)):
            self.rads[i].place(x = 40, y = 240 + 25 * i)

        # entry
        self.entryMoney.place(x = 60, y = 260 + len(self.rads) * 25)

        # labels
        self.lblMoney.place(x = 10, y = 260 + len(self.rads) * 25)
        self.lblWarning.place(x = 40, y = 210)

class New_Category_Window():
    
    ### function part of the new category window function
    def add_category(self):
        message = add_new_category(self.selected.get(), self.entryName.get(), self.entryPoints.get())
        self.entryName.configure(text='')
        self.entryPoints.configure(text='')
       
    def load_main_window(self):
        self.forget_all_new()
        Main_Window(self.window)

    def forget_all_new(self):
        # buttons
        self.btnMain.place_forget()
        self.btnAdd.place_forget()
        # radio buttons
        self.rbMoney.place_forget()
        self.rbTime.place_forget()
        self.rbOnce.place_forget()
        # entries
        self.entryName.place_forget()
        self.entryPoints.place_forget()
        # labels
        self.lblName.place_forget()
        self.lblPoints.place_forget()

    def __init__(self, window):
        ### window settings ###
        self.window = window
        self.window.title("Tracker - Nieuwe categorie")
        self.window.geometry('300x250')

        ### instantiate widgets ###
        # buttons
        self.btnMain = Button(self.window, text="main", command=self.load_main_window, width = 20, height = 2)
        self.btnAdd = Button(self.window, text='Toevoegen', command=self.add_category, width = 20, height = 2)
        
        # entries
        self.entryName = Entry(self.window, width=20)
        self.entryPoints = Entry(self.window, width=20)  

        # radio buttons
        self.selected = IntVar()
        self.rbTime = Radiobutton(self.window,text='Tijd', value=1, variable=self.selected)
        self.rbMoney = Radiobutton(self.window,text='Geld', value=2, variable=self.selected)  
        self.rbOnce = Radiobutton(self.window,text='Eenmalig', value=3, variable=self.selected) 

        # labels
        self.lblName = Label(self.window, text='Naam', fg='blue')
        self.lblPoints = Label(self.window, text='Punten', fg='blue')

        ### set grid ###
        self.xC = 60
        self.btn_size = 190
        # buttons
        self.btnAdd.place(x = self.xC + 1, y = 155, width = self.btn_size)
        self.btnMain.place(x = self.xC + 1, y = 195, width = self.btn_size)

        # text fields
        self.entryName.place(x = self.xC, y = 5)
        self.entryPoints.place(x = self.xC, y = 120)

        # radio buttons
        self.rbTime.place(x = self.xC, y = 45)
        self.rbMoney.place(x = self.xC, y = 70)
        self.rbOnce.place(x = self.xC, y = 95)

        # labels
        self.lblName.place(x = 5, y = 5)
        self.lblPoints.place(x = 5, y = 120)

class Plot_Canvas():
    ### function part of the new category window function
    def go_main_window(self):
        self.forget_all_canvas()
        Main_Window(self.window)

    def forget_all_canvas(self):
        # canvas
        self.canvas.get_tk_widget().destroy()
        # buttons
        self.btnMain.place_forget()
        self.btnThisWeek.place_forget() 
        self.btnThisMonth.place_forget() 
        #btnThisYear.pack_forget() 
        self.btnLastWeek.place_forget()
        self.btnNextWeek.place_forget()
        self.btnLastMonth.place_forget()
        self.btnNextMonth.place_forget() 
        self.lblWarnig.place_forget()

    def hide_warnings(self):
        self.lblWarnig.configure(text = '')

    def set_this_week(self):
        self.start, self.end = start_end_this_week()
        self.set_canvas(self.start, self.end, calculate_points_by_range_date(self.start, self.end), 
        'This Week', range(1, 8), 'Days', 'Points', [self.min, 30])
    
    def last_week(self):     
        self.start, self.end = start_end_last_week(self.start)
        self.set_canvas(self.start, self.end, calculate_points_by_range_date(self.start, self.end), 
        'last Week', range(1, 8), 'Days', 'Points', [self.min, 30])

    def next_week(self):      
        self.start, self.end = start_end_next_week(self.end)
        self.set_canvas(self.start, self.end, calculate_points_by_range_date(self.start, self.end), 
        'Next Week', range(1, 8), 'Days', 'Points', [self.min, 30])

    def set_this_month(self):
        self.start, self.end = start_end_this_month()
        self.set_canvas(self.start, self.end, calculate_points_by_range_date(self.start, self.end), 
        'This Month', range(1, self.end.day + 1), 'Days', 'Points', [self.min, 30])

    def next_month(self):      
        self.start, self.end = start_end_next_month(self.end)
        self.set_canvas(self.start, self.end, calculate_points_by_range_date(self.start, self.end), 
        'Next Month', range(1, self.end.day + 1), 'Days', 'Points', [self.min, 30])

    def last_month(self):     
        self.start, self.end = start_end_last_month(self.start)
        self.set_canvas(self.start, self.end, calculate_points_by_range_date(self.start, self.end), 
        'Last Month', range(1, self.end.day + 1), 'Days', 'Points', [self.min, 30])

    def set_canvas(self, start, end, points, title, xAxes, xLabel, yLabel, axHline):
        try :
            self.canvas.get_tk_widget().destroy()
        except AttributeError:
            pass
        start = start.strftime('%d-%m-%Y')
        end = end.strftime('%d-%m-%Y')
        self.show_canvas(range(1, len(points) + 1), points, f'{title} - {start} - {end}', xAxes, xLabel, yLabel, axHline)

    # canvas object is returned so that other child functions can access it
    def show_canvas(self, x, y, title, xAxes = False, xLabel = False, yLabel = False, axHline = False):
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
        self.canvas = FigureCanvasTkAgg(figure, self.window)
        self.canvas.show()
        self.canvas.get_tk_widget().place(x = 125, y = 200, width = 1150, height = 550)

    def __init__(self, window):   
        ### window ###
        self.window = window
        self.window.title('Tracker - Plot')
        self.window.geometry('1400x740')

        # variables 
        self.min = 20
        self.end = datetime
        self.start = datetime.today()
        
        ### instantiate widgets ###
        self.canvas = True # will become a Figure

        # buttons
        self.btnMain = Button(self.window, text="main", fg='blue', command=self.go_main_window, width = 14, height = 1) 
        self.btnThisWeek = Button(self.window, text="this week", fg='orange', command=self.set_this_week, width = 14, height = 1) 
        self.btnThisMonth = Button(self.window, text="this Month", fg='orange', command=self.set_this_month, width = 14, height = 1) 
        #self.btnThisYear = Button(self.window, text="this Year", command=set_this_year, width = 14, height = 1) 
        self.btnLastWeek = Button(self.window, text="<< week", fg='red', command=self.last_week, width = 14, height = 1) 
        self.btnNextWeek = Button(self.window, text=" week >>", fg='red', command=self.next_week, width = 14, height = 1) 
        self.btnLastMonth = Button(self.window, text="<< month", fg='red', command=self.last_month, width = 14, height = 1) 
        self.btnNextMonth = Button(self.window, text="month >>", fg='red', command=self.next_month, width = 14, height = 1) 

        # labels
        self.lblWarnig = Label(self.window, fg='red')

        ### set pack ###
        
        # buttons
        btn_size = 150
        btn_size_move = 100    
        self.btnMain.place(x = 600, y = 12, width = btn_size)
        self.btnThisWeek.place(x = 600, y = 150, width = btn_size)
        self.btnThisMonth.place(x = 600, y = 170, width = btn_size)
        #btnThisYear.place()
        
        self.btnLastWeek.place(x = 10, y = 375, width = btn_size_move)
        self.btnNextWeek.place(x = 1290, y = 375, width = btn_size_move)
        self.btnLastMonth.place(x = 10, y = 395, width = btn_size_move)
        self.btnNextMonth.place(x = 1290, y = 395, width = btn_size_move)

        # labels
        # lblWarnig.pack(side=BOTTOM)

        self.set_this_week()

def main(): 
    # set window
    window = Tk()

    # load main window layout
    Main_Window(window)
    #plot_canvas(window)

    # window main loop
    window.mainloop()

if __name__ == '__main__':
    main()