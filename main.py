# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Sun Nov 18 23:10:15 2018

# @author: xaviervanegdom
# """

# python packages
from tkinter import Tk, Button, Label, Entry, Radiobutton, IntVar
from datetime import datetime
import csv


from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT

# interface packages


# domein packages
from domein.procesActivities import add_activity_by_id
from domein.pointCalculcation import calculate_points_by_range_date
from domein.categoryActions import get_all_categories_user, add_new_category
from domein.userManagement import create_user, get_user, get_user_by_id
from domein.groupManagement import create_group, get_all_groups_with_admin_id, get_all_groups_admin_with_group_id, add_user_to_group

from account import Account, load_account_file, save_account_to_file
from times import start_end_this_week, start_end_last_week, start_end_next_week, start_end_this_month, start_end_last_month, start_end_next_month


class Main_Window(): 
    
    ### function part of the main window function
    def add_activity(self): 
        if self.selected.get() == 0:
            self.lblWarning.configure(text='Geen categorie geselecteerd')
        else :
           
            # hour/once 
            if self.categories[self.selected.get() - 1][4] == 1 or self.categories[self.selected.get() - 1][6] == 1:
                message = add_activity_by_id(self.account.id, self.selected.get())
                self.set_warning_add(message)
            
            else :
                
                try : # money and pot
                    
                    def save_money():
                        message = add_activity_by_id(self.account.id, self.selected.get(), self.entryMoney.get())
                        self.entryMoney.configure(text = '')
                        self.set_warning_add(message)  

                    if int(self.entryMoney.get()) > 0 and self.categories[self.selected.get() - 1][5] == 1: # money
                        save_money()      
                                  
                    elif int(self.entryMoney.get()) < 1 and self.categories[self.selected.get() - 1][5] == 1:
                        self.lblWarning.configure(text = f"Geen getal onder de 1!")

                    elif self.categories[self.selected.get() - 1][7] == 1:
                        save_money()

                except ValueError :
                    self.lblWarning.configure(text = f"Er moet een getal worden ingevoerd!")
            
    def set_warning_add(self, message):
        if message == 'start': 
            self.lblWarning.configure(text = f"Start {self.names[self.selected.get() - 1]}")
        elif message == 'end':
            self.lblWarning.configure(text = f"Einde {self.names[self.selected.get() - 1]}")
        elif message == 'succes_money':
            self.lblWarning.configure(text=f'€{self.entryMoney.get()},- toegevoegd bij {self.names[self.selected.get() - 1]}!!')
        elif message == 'succes_once':
            self.lblWarning.configure(text=f'{self.names[self.selected.get() - 1]} opgeslagen!!')
        elif message == 'already_saved': 
            self.lblWarning.configure(text=f'{self.names[self.selected.get() - 1]} is al opgeslagen') 
        elif message == 'succes_pot':
            self.lblWarning.configure(text=f'€{self.entryMoney.get()} toegevoegd aan: {self.names[self.selected.get() - 1]}!')

    # new windows
    def new_category(self):
        #winfo_children()
        self.forget_all_main()
        New_Category_Window(self.window, self.account)

    def group_management(self):
        self.forget_all_main()
        Group_Management_Window(self. window, self.account)

    def make_plot(self):
        self.forget_all_main()
        Plot_Window(self.window, self.account)

    def forget_all_main(self):
        children = self.window.winfo_children()
        
        for child in children:
            child.place_forget()

    def __init__(self, window, account):
        self.window = window
        self.account = account
        
        ### window settings ###
        self.window.title("Tracker - Main (dev)")
        # width x height + x_offset + y_offset:
        self.window.geometry('500x500+30+30')

        ### instantiate widgets ###
        # buttons
        self.btnSSM = Button(self.window, text="Start/Stop/Amount", command=self.add_activity, fg="green") 
        
        self.btnCategory = Button(self.window, text="nieuwe categorie", command=self.new_category, width = 14, height = 1) 
        self.btnPlot = Button(self.window, text="plot", command=self.make_plot, width = 14, height = 1) 
        self.btnGroup = Button(self.window, text='Beheer groep', command=self.group_management, width = 14, height = 1)

        # radio boxes
        self.selected = IntVar()
        self.categories = get_all_categories_user(account.id)
        self.names = [name[2].replace('_', ' ') for name in self.categories]
        self.indexes = [i[0] for i in self.categories]
        self.values = [i for i in range(1, len(self.names) + 1)]
        self.rads = []
        for i in range(len(self.names)):
            self.rads.append(Radiobutton(self.window, text=self.names[i], value=self.values[i], variable=self.selected))

        # entry
        self.entryMoney = Entry(self.window)

        # labels
        self.lblInfo = Label(self.window, text=f'Welkom {self.account.name}! ID : {self.account.id}', fg='orange')
        self.lblMoney = Label(self.window, text='Geld:', fg='blue')
        self.lblWarning = Label(self.window, fg='red')

        ### set geo ###
        xC = 10
        nav_size = 150
        # buttons
        self.btnSSM.place(x = xC, y = 70 ,width = 250, height = 150)
        
        # nav buttons
        self.btnCategory.place(x = xC, y = 40, width = nav_size)
        self.btnPlot.place(x = (nav_size + 20) * 1, y = 40, width = nav_size)
        self.btnGroup.place(x = (nav_size + 20) * 2 - 10, y = 40, width = nav_size)

        # radio buttons
        for i in range(len(self.rads)):
            self.rads[i].place(x = xC + 30, y = 270 + 25 * i)

        # entry
        self.entryMoney.place(x = xC + 50, y = 290 + len(self.rads) * 25)

        # labels
        self.lblInfo.place(x = xC, y = 10)
        self.lblMoney.place(x = xC, y = 290 + len(self.rads) * 25)
        self.lblWarning.place(x = xC + 30, y = 250)

class New_Category_Window():
    
    ### function part of the new category window function
    def add_category(self):
        
        try :
            if self.selected.get() == 4 and self.entryPotAmount.get() != '': # if the pot amount is selected
                
                start = self.string_time_to_database_time(self.entryPotStart.get())
                end = self.string_time_to_database_time(self.entryPotEnd.get())
                
                if self.groupId == 0: # if a group is selected 
                    message = add_new_category(self.selected.get(), self.entryName.get(), 
                    self.entryPoints.get(), self.account.id, self.entryPotAmount.get(), datetime.today(), start, end)
                
                else :
                    message = add_new_category(self.selected.get(), self.entryName.get(), 
                    self.entryPoints.get(), self.account.id, self.groupId, self.entryPotAmount.get(), datetime.today(), start, end)

                self.lblWarning.configure(text='Gelukt!')
            else :

                if self.groupId == 0: # if a group is seleted
                    message = add_new_category(self.selected.get(), self.entryName.get(), self.entryPoints.get(), self.account.id)
                
                else :
                    message = add_new_category(self.selected.get(), self.entryName.get(), self.entryPoints.get(), self.account.id, self.groupId)

                self.entryName.configure(text='')
                self.entryPoints.configure(text='')
                
                self.lblWarning.configure(text='Gelukt!')
        
        except ValueError:
            self.lblWarning.configure(text = 'Alleen getallen!')
    
    def string_time_to_database_time(self, date):
        date = datetime.strptime(date, '%d/%m/%Y')
        return date.strftime('%Y-%m-%d')

    def load_main_window(self):
        self.forget_all_new()
        Main_Window(self.window, self.account)

    def forget_all_new(self):
        children = self.window.winfo_children()
        
        for child in children:
            child.place_forget()

    def __init__(self, window, account, groupId = 0):
        self.window = window 
        self.account = account
        self.groupId = groupId
        
        ### window settings ###
        self.window.title("Tracker - Nieuwe categorie")
        self.window.geometry('300x420')

        ### instantiate widgets ###
        # buttons
        self.btnMain = Button(self.window, text="main", command=self.load_main_window, width = 20, height = 2)
        self.btnAdd = Button(self.window, text='Toevoegen', command=self.add_category, width = 20, height = 2)
        
        # entries
        self.entryName = Entry(self.window, width = 20, text='post-test')
        self.entryPoints = Entry(self.window, width = 20, text='1')
        self.entryPotAmount = Entry(self.window, width = 20, text='0') 
        self.entryPotStart = Entry(self.window, width = 20, text='19/11/2018')
        self.entryPotEnd = Entry(self.window, width = 20, text='16/12/2018')

        # radio buttons
        self.selected = IntVar()
        self.rbTime = Radiobutton(self.window,text='Tijd', value=1, variable=self.selected)
        self.rbMoney = Radiobutton(self.window,text='Geld', value=2, variable=self.selected)  
        self.rbOnce = Radiobutton(self.window,text='Eenmalig', value=3, variable=self.selected) 
        self.rbPot = Radiobutton(self.window,text='Pot', value=4, variable=self.selected) 

        # labels
        self.lblName = Label(self.window, text='Naam:', fg='blue')
        self.lblPoints = Label(self.window, text='Punten:', fg='blue')
        self.lblPot = Label(self.window, text='Pot:', fg='blue')
        self.lblPotStart = Label(self.window, text='Pot Start:', fg='blue')
        self.lblPotEnd = Label(self.window, text='Pot Einde:', fg='blue')
        self.lblDateExample = Label(self.window, text='Voorbeeld: 31/05/2018', fg='orange')
        self.lblWarning = Label(self.window, text='test', fg='red')

        ### set Geo ###
        xC = 80
        yC = 45
        btn_size = 190
        # buttons
        self.btnAdd.place(x = xC + 1, y = 300, width = btn_size)
        self.btnMain.place(x = xC + 1, y = 340, width = btn_size)

        # entry fields
        self.entryName.place(x = xC, y = 5)
        self.entryPoints.place(x = xC, y = yC + 25 * 4)
        self.entryPotAmount.place(x = xC, y = yC + 25 * 5 + 7)
        self.entryPotStart.place(x = xC, y = yC + 25 * 7 + 7 * 2)
        self.entryPotEnd.place(x = xC, y = yC + 25 * 8 + 7 * 3) 

        # radio buttons
        self.rbTime.place(x = xC, y = yC)
        self.rbMoney.place(x = xC, y = yC + 25)
        self.rbOnce.place(x = xC, y = yC + 25 * 2)
        self.rbPot.place(x = xC, y = yC + 25 * 3)

        # labels
        self.lblName.place(x = 5, y = 5)
        self.lblPoints.place(x = 5, y = yC + 25 * 4)
        self.lblPot.place(x = 5, y = yC + 25 * 5 + 10)
        self.lblPotStart.place(x = 5, y = yC + 25 * 7 + 7 * 2)
        self.lblPotEnd.place(x = 5, y = yC + 25 * 8 + 7 * 3)

        self.lblDateExample.place(x = xC, y = yC + 25 * 6 + 7 * 2)
        self.lblWarning.place(x = xC + 75, y = 380)

class Plot_Window():
    ### function part of the new category window function
    def go_main_window(self):
        self.forget_all_canvas()
        Main_Window(self.window, self.account)

    def forget_all_canvas(self):
        children = self.window.winfo_children()
        
        for child in children:
            child.place_forget()

    def hide_warnings(self):
        self.lblWarnig.configure(text = '')

    def set_this_week(self):
        self.start, self.end = start_end_this_week()
        self.set_canvas(self.start, self.end, calculate_points_by_range_date(self.start, self.end, self.account.id), 
        'This Week', range(1, 8), 'Days', 'Points', [self.min, 30])
    
    def last_week(self):     
        self.start, self.end = start_end_last_week(self.start)
        self.set_canvas(self.start, self.end, calculate_points_by_range_date(self.start, self.end, self.account.id), 
        'last Week', range(1, 8), 'Days', 'Points', [self.min, 30])

    def next_week(self):      
        self.start, self.end = start_end_next_week(self.end)
        self.set_canvas(self.start, self.end, calculate_points_by_range_date(self.start, self.end, self.account.id), 
        'Next Week', range(1, 8), 'Days', 'Points', [self.min, 30])

    def set_this_month(self):
        self.start, self.end = start_end_this_month()
        self.set_canvas(self.start, self.end, calculate_points_by_range_date(self.start, self.end, self.account.id), 
        'This Month', range(1, self.end.day + 1), 'Days', 'Points', [self.min, 30])

    def next_month(self):      
        self.start, self.end = start_end_next_month(self.end)
        self.set_canvas(self.start, self.end, calculate_points_by_range_date(self.start, self.end, self.account.id), 
        'Next Month', range(1, self.end.day + 1), 'Days', 'Points', [self.min, 30])

    def last_month(self):     
        self.start, self.end = start_end_last_month(self.start)
        self.set_canvas(self.start, self.end, calculate_points_by_range_date(self.start, self.end, self.account.id), 
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
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x = 150, y = 200, width = 1000, height = 450)

    def __init__(self, window, account):  
        self.window = window 
        self.account = account
        
        ### window ###
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
        
        self.btnLastWeek.place(x = 50, y = 375, width = btn_size_move)
        self.btnNextWeek.place(x = 1150, y = 375, width = btn_size_move)
        self.btnLastMonth.place(x = 50, y = 395, width = btn_size_move)
        self.btnNextMonth.place(x = 1150, y = 395, width = btn_size_move)

        # labels
        # lblWarnig.pack(side=BOTTOM)

        self.set_this_week()

### Group actions ###

# the view with all the buttons to go to group actions
class Group_Management_Window():

    def load_main_window(self):
        self.forget_all()
        Main_Window(self.window, self.account)

    def load_create_group(self):
        self.forget_all()
        Make_Group_Window(self.window, self.account)

    def load_add_user(self):
        self.forget_all()
        Add_User_Group_Window(self.window, self.account)

    def load_add_category(self):
        self.forget_all()
        Select_Group_For_Category(self.window, self.account)

    def forget_all(self):
        for child in self.window.winfo_children() :
            child.place_forget()

    def __init__(self, window, account):
        self.window = window
        self.account = account
        
        ### window settings ###
        self.window.title('Tracker - Groepen beheer')
        # width x height + x_offset + y_offset:
        self.window.geometry('226x200')

        ### widgets ###
        # buttons
        self.btnMain = Button(self.window, text='Main', command=self.load_main_window, width = 20, height = 2)
        self.btnCreate = Button(self.window, text='Nieuwe groep', command=self.load_create_group, width = 20, height = 2)
        self.btnAddUser = Button(self.window, text='Gebruiker toevoegen', command=self.load_add_user, width = 20, height = 2)
        self.btnAddCategory = Button(self.window, text='Categorie Toevoegen', command=self.load_add_category, width = 20, height = 2)

        ### geo ###
        # buttons

        xC = 20
        yC = 20
        self.btnMain.place(x = xC, y = yC)
        self.btnCreate.place(x = xC, y = yC + 40 * 1)
        self.btnAddUser.place(x = xC, y = yC + 40 * 2)
        self.btnAddCategory.place(x = xC, y = yC + 40 * 3)

# the view to make a group
class Make_Group_Window():

    def add_group(self):
        if self.entryName.get() != '':
            message = create_group(self.account.id, self.entryName.get())
            self.lblWarning.configure(text=f'{message}')
        else :
            self.lblWarning.configure(text='Geen naam ingevuld!')

    def load_management_window(self):
        for child in self.window.winfo_children():
            child.place_forget()
        Group_Management_Window(self.window, self.account)


    def __init__(self, window, account):
        self.window = window
        self.account = account
        
        ### window settings ###
        self.window.title("Tracker - Groep Maken")
        # width x height + x_offset + y_offset:
        self.window.geometry('300x200')

        ### widgets ###

        # buttons
        self.btnAdd = Button(self.window, text='Toevoegen', command=self.add_group, width = 20, height = 2)
        self.btnMain = Button(self.window, text="Groep beheer", command=self.load_management_window, width = 20, height = 2)

        # entry fields
        self.entryName = Entry(self.window, width = 20, text='post-test')

        # labels
        self.lblName = Label(self.window, text='Naam:', fg='blue')
        self.lblWarning = Label(self.window, fg='red')

        ### set Geo ###
        xC = 80
        btn_size = 190
        # buttons
        self.btnAdd.place(x = xC + 1, y = 50, width = btn_size)
        self.btnMain.place(x = xC + 1, y = 90, width = btn_size)
        
        # entry fields
        self.entryName.place(x = xC, y = 20)

        # labels
        self.lblName.place(x = 5, y = 20)

        self.lblWarning.place(x = 110, y = 130)

# the view to add users to a group that a user is admin of
class Add_User_Group_Window():

    def load_management_window(self):
        for child in self.window.winfo_children():
            child.place_forget()
        Group_Management_Window(self.window, self.account)

    # def search_group(self):
    #     if self.entryGroupId.get() != '':
    #         self.lblWarning1.configure(text = '')
    #         group = get_all_groups_admin_by_group_id(self.account.id, int(self.entryGroupId.get())
    #     else : 
    #         self.lblWarning1.configure(text = 'Je moet iets invullen!')

    # radio buttons - first view
    def set_rb_groups(self):
        self.groups = get_all_groups_with_admin_id(self.account.id)
        self.radGroups = []
        self.valuesGroups = [group[0] for group in self.groups]
        self.namesGroups = [group[1] for group in self.groups]
        for i in range(len(self.groups)):
            self.radGroups.append(Radiobutton(self.window, text=f'Id: {self.valuesGroups[i]} - {self.namesGroups[i]}', value=self.valuesGroups[i], variable=self.selectedGroups))

    def set_rb_groups_place(self): # and the button connected to the radio buttons
        for i in range(len(self.radGroups)):
            self.radGroups[i].place(x = self.xC, y = self.yC + 30 * i)
        self.btnSelectGroup.place(x = self.xC + 1, y = self.yC + 30 * len(self.groups))
        self.yC += (30 * len(self.groups) + 1)

    # find a user to add to group - second view
    def select_group(self):
        self.show_group_label()
        self.show_entry_group()

    def show_group_label(self):
        index = self.valuesGroups.index(self.selectedGroups.get())
        self.lblGroup.configure(text = f'ID: {self.selectedGroups.get()} - {self.namesGroups[index]}')
        self.lblGroup.place(x = self.xC, y = self.yC + 30 )

    def show_entry_group(self):
        self.entryPersonId.place(x = self.xC, y = self.yC + 55)
        self.btnSearchPerson.place(x = self.xC + 1, y = self.yC + 90)
        self.lblPId.place(x = 5, y = self.yC + 59)

    # button to add user to group - thirt view
    def search_person(self):
        def show_warning1(text):
            self.lblWarning1.configure(text = text) # person information afther selected
            self.lblWarning1.place(x = self.xC , y = self.yC + 120)
        self.lblWarning2.configure(text = '')
        try : 
            if self.entryPersonId.get() != '':
                self.tempAdd = get_user_by_id(int(self.entryPersonId.get())) # gives back a person row
                if self.tempAdd != None:
                    show_warning1(f'Name: {self.tempAdd[1]}')
                    self.btnAddPerson.place(x = self.xC, y = self.yC + 150)
                else :
                    show_warning1('Geen persoon gevonden!')
            else :
                show_warning1('Je moet iets invullen!')
        except ValueError :
            show_warning1('Je moet een getal invullen!')

    # add user to the database
    def add_person(self):
        message = add_user_to_group(self.account.id, self.tempAdd[0], self.selectedGroups.get())
        if message == 'succes':
            self.lblWarning2.configure(text = f'{self.tempAdd[1]} Toegevoegd!')
        else :
            self.lblWarning2.configure(text = message)
        self.lblWarning2.place(x = self.xC, y = self.yC + 180)

    def load_main(self):
        self.forget_all()
        Main_Window(self.window, self.account)

    def load_group_menu(self):
        self.forget_all()
        Group_Management_Window(self.window, self.account)

    def forget_all(self):
        for child in self.window.winfo_children() :
            child.place_forget()

    def __init__(self, window, account):
        self.window = window
        self.account = account
        
        # radio buttons to select group
        self.groups = []
        self.radGroups = []
        self.selectedGroups = IntVar()
        self.valuesGroups = []
        self.namesGroups = []

        # temp person to add
        self.tempAdd = ''

        ### window settings ###
        self.window.title("Tracker - Groep Maken")
        # width x height + x_offset + y_offset:
        self.window.geometry('400x400')

        ### start coord
        self.xC = 90
        self.yC = 10
        ### widgets ###

        # Buttons 
        # navigations
        self.btnMain = Button(self.window, text='Main', command=self.load_main, width = 14, height = 1)
        self.btnGroupNav = Button(self.window, text='Group Menu', command=self.load_management_window, width = 14, height = 1)

        #self.btnSearch = Button(self.window, text="Zoek groepen", command=self.search_group, width = 14, height = 1) 
        self.btnSelectGroup = Button(self.window, text='Selecteer Groep', command=self.select_group, width = 14, height = 1)
        self.btnSearchPerson = Button(self.window, text='Zoek Persoon', command=self.search_person, width = 14, height = 1)
        self.btnAddPerson = Button(self.window, text='Voeg Persoon Toe', command=self.add_person, width = 14, height = 1)

        # Entry fields
        #self.entryGroupId = Entry(self.window)
        self.entryPersonId = Entry(self.window)

        # Radio Buttons
        self.set_rb_groups()

        # labels
        #self.lblId = Label(self.window, text="Groep ID :")
        self.lblPId = Label(self.window, text = 'Person ID:', fg='blue')
        self.lblGroup = Label(self.window, fg='orange')
        
        self.lblWarning1 = Label(self.window, fg='red')
        self.lblWarning2 = Label(self.window, text='Toegevoegd', fg='red')

        
        ### geo ###
        # buttons
        #self.btnSearch.place(x = xC + 1, y = 50)
        self.btnMain.place(x = self.xC - 50, y = self.yC)
        self.btnGroupNav.place(x = self.xC + 100, y = self.yC)

        self.yC += 40 

        # entry fields
        #self.entryGroupId.place(x = xC, y = 10)

        # radio buttons
        self.set_rb_groups_place()

        # labels
        #self.lblId.place(x = 10, y = 10)

class Select_Group_For_Category():
    def load_new_category(self):
        if self.selected.get() > 0:
            for child in self.window.winfo_children() :
                child.place_forget()          
            New_Category_Window(self.window, self.account, self.selected.get())
        else :
            self.lblWarning.configure(text = "Je moet iets selecteren")

    def __init__(self, window, account):
        self.window = window
        self.account = account
        
        ### window settings ###
        self.window.title('Tracker - Groepen Selecteren')
        # width x height + x_offset + y_offset:
        #self.window.geometry('226x150')

        ### widgets ###
        # button
        self.btnSelectGroup = Button(self.window, text='Selecteer groep', command = self.load_new_category)
        
        #radio buttons
        self.selected = IntVar()
        groups = get_all_groups_with_admin_id(self.account.id)
        self.values = [group[0] for group in groups]
        names = [group[1] for group in groups]
        rads = []
        for i in range(len(groups)):
            rads.append(Radiobutton(self.window, text=f'{names[i]}', value=self.values[i], variable=self.selected))
        
        # labels
        self.lblWarning = Label(fg='red')

        ### geo ###
        # first radio button
        xC = 10
        yC = 10
        for i in range(len(rads)):
            rads[i].place(x = xC, y = yC + 30 * i)

        # second button
        self.btnSelectGroup.place(x = xC, y = yC + 30 * len(rads))

        # label
        self.lblWarning.place(x = xC, y = yC + 30 * len(rads) + 30)

        # set window 
        self.window.geometry(f'200x{(len(rads) * 35 + 50)}')



### account options ###
class Make_Account_Window():

    def go_main_window(self):
        self.forget_all_make_account()
        Main_Window(self.window, self.account)

    def forget_all_make_account(self):
        children = self.window.winfo_children()
        
        for child in children:
            child.place_forget()

    def create_account_event(self):
        if self.check_form_create() :
            if save_account_to_file([self.entryName.get(), self.entryPassword.get()]) == 'succes':
                id = create_user(self.entryName.get(), self.entryPassword.get())
                self.account = Account(self.entryName.get(), id)
                self.go_main_window()
            else :
                self.lblWarning.configure(text = 'Er is iets mis gegaan')
            
    def check_form_create(self):
        message = ''
        check = True
        if self.entryName.get() == '':
            message = 'Vul een naam in\n'
        if self.entryPassword.get() == '' or self.entryPasswordCheck.get() == '':
            message += 'Vul een wachtwoord in\n'
        if self.entryPassword.get() != self.entryPasswordCheck.get():
            message += 'Wachtwoorden zijn niet het zelfde'
        if message != '':
            check = False
            self.lblWarning.configure(text = message)
        return check   

    def check_form_login(self): 
        message = ''
        check = True
        if self.entryName.get() == '':
            message = 'Vul een naam in\n'
        if self.entryPassword.get() == '' :
            message += 'Vul een wachtwoord in\n'
        if message != '':
            check = False
            self.lblWarning.configure(text = message)
        return check   

    def login(self):
        if self.check_form_login() :
            user = get_user(self.entryName.get(), self.entryPassword.get())
            if len(user) != 0 :
                if save_account_to_file([user[1], self.entryPassword.get()]) == 'succes':
                    self.account = Account(user[0], user[1])
                    self.go_main_window()

    def __init__(self, window):
        self.window = window

        ### window settings ###
        self.window.title("Tracker - Account aanmaken (dev)")
        # width x height + x_offset + y_offset:
        self.window.geometry('400x195+30+30')

        ### widgets ###

        # buttons 

        self.buttonAdd = Button(self.window, text="Maak aan", command=self.create_account_event, fg="green") 
        self.buttonLogin = Button(self.window, text="Log in", command=self.login, fg="green") 

        # entry
        self.entryName = Entry(self.window)
        self.entryPassword = Entry(self.window, show="*")
        self.entryPasswordCheck = Entry(self.window, show="*")
        
        # labels
        self.lblName = Label(self.window, text='Name:')
        self.lblPassword = Label(self.window, text='Password:')
        self.lblPasswordChek = Label(self.window, text='Password Check:')

        self.lblWarning = Label(self.window, fg='red')

        ### set geo ###

        self.buttonAdd.place(x = 140, y = 110, width = 100)
        self.buttonLogin.place(x = 240, y = 110, width = 100)

        # entry
        x = 140
        w = 200
        self.entryName.place(x = x, y = 20, width = w)
        self.entryPassword.place(x = x, y = 50, width = w)
        self.entryPasswordCheck.place(x = x, y = 80, width = w)
        
        # labels
        self.lblName.place(x = 20, y = 24)
        self.lblPassword.place(x = 20, y = 54)
        self.lblPasswordChek.place(x = 20, y = 84)

        self.lblWarning.place(x = 140, y = 140)

def main(): 
    # set window
    window = Tk()
    
    try :

        account = load_account_file() # check if credentials a saved local

        try : 

            user = get_user(account[0], account[1]) # check if user excist in the database
            account = Account(user[0], user[1]) # login
            Main_Window(window, account) 
            #Group_Management_Window(window, account)

        except ValueError:  # change this to something better
            pass

    except FileNotFoundError:
        Make_Account_Window(window)

    window.mainloop()

if __name__ == '__main__':
    main()