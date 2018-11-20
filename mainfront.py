# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Sun Nov 18 23:10:15 2018

# @author: xaviervanegdom
# """

# python tkinter
from tkinter import *
import datetime

from get import *
from insert import *
from update import *

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
        date =  datetime.datetime.today().strftime('%Y-%m-%d')
        if len(select_once_by_cid_and_date(category[0], date)) == 0:
            insert_once(category[0], date)
            lblWarning.configure(text='Gelukt!')
        else :
            lblWarning.configure(text='Is al opgeslagen')   

    def new_category():
        hide_all_main()
        new_category_window(window)

    def hide_all_main():
        # buttons
        btnSSM.grid_remove()
        btnNew.grid_remove()
        
        # radio boxes
        for i in rads:
            i.grid_remove()

        # labels
        lblWarning.grid_remove()

    ### window settings ###
    window.title("Tracker - Main")
    window.geometry('400x400')

    ### instantiate widgets ###
    # buttons
    btnSSM = Button(window, text="Start/Stop/Amount", command=add_activity, width = 30, height = 10, fg="green") 
    btnNew = Button(window, text="nieuwe categorie", command=new_category) 

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
    btnSSM.grid(row=0)
    btnNew.grid(column=1, row=0)

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

def plot_window(window):
    ### title ###
    window.title("Tracker - Plot")
    ### function part of the new category window function

    ### instantiate widgets ###
    # buttons

    ### set grid ###

# set window
window = Tk()

# load main window layout
main_window(window)

# window main loop
window.mainloop()