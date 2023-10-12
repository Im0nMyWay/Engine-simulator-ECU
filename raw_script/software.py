from tkinter import *
from tkinter import ttk,filedialog
from PIL import ImageTk, Image
import os,re,time

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------- FETCHING SETTINGS ------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def applied_theme():
    theme_pop_up = Toplevel(root)
    theme_pop_up.geometry('320x30')
    theme_pop_up.resizable(False,False)
    theme_pop_up.iconbitmap("ressources\Icon.ico")
    theme_pop_up.title('Refresh')
    text = ttk.Label(master=theme_pop_up,text='Theme changes will be applied next time you open the ECU',background=maincolor,foreground=textcolor)
    text.pack(anchor=N,expand=1,fill=BOTH)
    theme_pop_up.update_idletasks()
    time.sleep(2)
    theme_pop_up.destroy()
    root.destroy()
    

def applied_changes():
    changes_pop_up = Toplevel(root,background=maincolor)
    changes_pop_up.geometry('300x30')
    changes_pop_up.resizable(False,False)
    changes_pop_up.iconbitmap("ressources\Icon.ico")
    changes_pop_up.title('Refresh')
    text = ttk.Label(master=changes_pop_up,text='Changes have been applied !',background=maincolor,foreground=textcolor)
    text.pack(anchor=N,expand=1,fill=BOTH)
    changes_pop_up.update_idletasks()
    time.sleep(1)
    changes_pop_up.destroy()



def get_settings():
    global current_theme,settings_script

    settings_content = open('ressources\settings.txt','r')
    settings_script = settings_content.read()
    for item in settings_script.split("\n"):
        if 'theme' in item:
            current_theme = (re.findall('(?<=theme=)(\w+)',item.strip())[0])
    settings_content.close()

def update_theme(event):
    global credits_background,maincolor,logo_theme,textcolor,settings_script
    if current_theme == 'Clear':
        maincolor = '#e5e4e2'
        logo_theme = 'clear_logo.png'
        credits_background = '#e5e4e2'
        textcolor = 'black'

    if current_theme == 'Dark':
        maincolor = '#181825'
        logo_theme = 'dark_logo.png'
        credits_background = '#181825'
        textcolor = 'white'

    if current_theme == 'Default':
        maincolor = 'lightgray'
        credits_background = '#ffbe2e'
        logo_theme = 'default_logo.png'
        textcolor = 'black'
    

    for item in settings_script.split("\n"):
        if 'theme' in item:
            settings_script = (settings_script.replace(item,(item.replace((re.findall('(?<=theme=)(\w+)',item.strip())[0]),(theme_combobox.get())))))

    with open('ressources\settings.txt','w') as settings_to_write:
        settings_to_write.write(settings_script)
    settings_to_write.close()
    applied_theme()




def initial_theme():
    global credits_background,maincolor,logo_theme,textcolor,settings_script
    if current_theme == 'Clear':
        maincolor = '#e5e4e2'
        logo_theme = 'clear_logo.png'
        credits_background = '#e5e4e2'
        textcolor = 'black'

    if current_theme == 'Dark':
        maincolor = '#181825'
        logo_theme = 'dark_logo.png'
        credits_background = '#181825'
        textcolor = 'white'

    if current_theme == 'Default':
        maincolor = 'lightgray'
        credits_background = '#ffbe2e'
        logo_theme = 'default_logo.png'
        textcolor = 'black'

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------- PYTHON FUNCTIONS -------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#file selection
def openfile():
    global file_path,file_content,file_name,engine_script

    file_path = filedialog.askopenfilename(title ='Open Engine',filetypes=(('Engine Files','*.mr'),('All files','*.*')))
    file_content = open(file_path,'r')
    file_name = ((os.path.basename(file_path)).split('.')[0])
    opened_engine.config(text=file_name)
    engine_script = file_content.read()

    apply_button.grid(row=0,column=3,sticky=W)
    main_notebook.add(tab_2,text='Rev Limiter')
    main_notebook.add(tab_4,text='Ignition Advance')
    main_notebook.add(tab_3,text='Intake')
    main_notebook.add(tab_6,text='Starter')
    main_notebook.add(tab_5,text='Others')


    rev_limiter_duration.set('Missing')
    for item in engine_script.split("\n"):
        if "limiter_duration" in item:
            rev_limiter_duration.set(re.findall('(?<=limiter_duration:\s)\d+\.\d+|(?<=limiter_duration:\s)\d+|(?<=limiter_duration\s:)\d+\.\d+|(?<=v\s:)\d+|(?<=limiter_duration\s:\s)\d+\.\d+|(?<=limiter_duration\s:\s)\d+|(?<=limiter_duration:)\d+\.\d+|(?<=limiter_duration:)\d+',item.strip())[0])
    
    rev_limiter_rpm.set('Missing')
    for item in engine_script.split("\n"):
        if "rev_limit" in item:
            rev_limiter_rpm.set(re.findall('(?<=rev_limit:\s)\d+\.\d+|(?<=rev_limit:\s)\d+|(?<=rev_limit\s:)\d+\.\d+|(?<=v\s:)\d+|(?<=rev_limit\s:\s)\d+\.\d+|(?<=rev_limit\s:\s)\d+|(?<=rev_limit:)\d+\.\d+|(?<=rev_limit:)\d+',item.strip())[0])

    starter_torque.set('Missing')
    for item in engine_script.split("\n"):
        if "starter_torque" in item:
            starter_torque.set(re.findall('(?<=starter_torque:\s)\d+\.\d+|(?<=starter_torque:\s)\d+|(?<=starter_torque\s:)\d+\.\d+|(?<=v\s:)\d+|(?<=starter_torque\s:\s)\d+\.\d+|(?<=starter_torque\s:\s)\d+|(?<=starter_torque:)\d+\.\d+|(?<=starter_torque:)\d+',item.strip())[0])
    
    starter_speed.set('Missing')
    for item in engine_script.split("\n"):
        if "starter_speed" in item:
            starter_speed.set(re.findall('(?<=starter_speed:\s)\d+\.\d+|(?<=starter_speed:\s)\d+|(?<=starter_speed\s:)\d+\.\d+|(?<=starter_speed\s:)\d+|(?<=starter_speed\s:\s)\d+\.\d+|(?<=starter_speed\s:\s)\d+|(?<=starter_speed:)\d+\.\d+|(?<=starter_speed:)\d+|(?<=starter_speed:\s-)\d+\.\d+|(?<=starter_speed:\s-)\d+|(?<=starter_speed\s-:)\d+\.\d+|(?<=starter_speed\s-:)\d+|(?<=starter_speed\s:\s-)\d+\.\d+|(?<=starter_speed\s-:\s)\d+|(?<=starter_speed:-)\d+\.\d+|(?<=starter_speed:-)\d+',item.strip())[0])

    plenum_volume.set('Missing')
    for item in engine_script.split("\n"):
        if "plenum_volume" in item:
            plenum_volume.set(re.findall('(?<=plenum_volume:\s)\d+\.\d+|(?<=plenum_volume:\s)\d+|(?<=plenum_volume\s:)\d+\.\d+|(?<=v\s:)\d+|(?<=plenum_volume\s:\s)\d+\.\d+|(?<=plenum_volume\s:\s)\d+|(?<=plenum_volume:)\d+\.\d+|(?<=plenum_volume:)\d+',item.strip())[0])    
    
    idle_throttle_plate_position.set('Missing')
    for item in engine_script.split("\n"):
        if "idle_throttle_plate_position" in item:
            idle_throttle_plate_position.set(re.findall('(?<=idle_throttle_plate_position:\s)\d+\.\d+|(?<=idle_throttle_plate_position:\s)\d+|(?<=idle_throttle_plate_position\s:)\d+\.\d+|(?<=idle_throttle_plate_position\s:)\d+|(?<=idle_throttle_plate_position\s:\s)\d+\.\d+|(?<=idle_throttle_plate_position\s:\s)\d+|(?<=idle_throttle_plate_position:)\d+\.\d+|(?<=idle_throttle_plate_position:)\d+',item.strip())[0])
    
    number_of_intakes.set('None')
    for item in engine_script.split("\n"):
        if "intake" in item:
            number_of_intakes.set(len(re.findall('intake\s',engine_script.strip())))

    simulation_frequency.set('Missing')
    for item in engine_script.split("\n"):
        if "simulation_frequency" in item:
            simulation_frequency.set(re.findall('(?<=simulation_frequency:\s)\d+\.\d+|(?<=simulation_frequency:\s)\d+|(?<=simulation_frequency\s:)\d+\.\d+|(?<=v\s:)\d+|(?<=simulation_frequency\s:\s)\d+\.\d+|(?<=simulation_frequency\s:\s)\d+|(?<=simulation_frequency:)\d+\.\d+|(?<=simulation_frequency:)\d+',item.strip())[0])

    file_content.close()
    
    
def apply_changes():
    global engine_script
    for item in engine_script.split("\n"):
        if "limiter_duration" in item:
            engine_script = (engine_script.replace(item,(item.replace((re.findall('(?<=limiter_duration:\s)\d+\.\d+|(?<=limiter_duration:\s)\d+|(?<=limiter_duration\s:)\d+\.\d+|(?<=v\s:)\d+|(?<=limiter_duration\s:\s)\d+\.\d+|(?<=limiter_duration\s:\s)\d+|(?<=limiter_duration:)\d+\.\d+|(?<=limiter_duration:)\d+',item.strip())[0]),(rev_limiter_duration_entry.get())))))
    
    for item in engine_script.split("\n"):
        if "redline" in item:
            engine_script = (engine_script.replace(item,(item.replace((re.findall('(?<=redline:\s)\d+\.\d+|(?<=redline:\s)\d+|(?<=redline\s:)\d+\.\d+|(?<=v\s:)\d+|(?<=redline\s:\s)\d+\.\d+|(?<=redline\s:\s)\d+|(?<=redline:)\d+\.\d+|(?<=redline:)\d+',item.strip())[0]),str(int(rev_limiter_rpm_entry.get())-redline_delta)))))

    for item in engine_script.split("\n"):
        if "rev_limit" in item:
            engine_script = (engine_script.replace(item,(item.replace((re.findall('(?<=rev_limit:\s)\d+\.\d+|(?<=rev_limit:\s)\d+|(?<=rev_limit\s:)\d+\.\d+|(?<=v\s:)\d+|(?<=rev_limit\s:\s)\d+\.\d+|(?<=rev_limit\s:\s)\d+|(?<=rev_limit:)\d+\.\d+|(?<=rev_limit:)\d+',item.strip())[0]),(rev_limiter_rpm_entry.get())))))

    for item in engine_script.split("\n"):
        if "simulation_frequency" in item:
            engine_script = (engine_script.replace(item,(item.replace((re.findall('(?<=simulation_frequency:\s)\d+\.\d+|(?<=simulation_frequency:\s)\d+|(?<=simulation_frequency\s:)\d+\.\d+|(?<=v\s:)\d+|(?<=simulation_frequency\s:\s)\d+\.\d+|(?<=simulation_frequency\s:\s)\d+|(?<=simulation_frequency:)\d+\.\d+|(?<=simulation_frequency:)\d+',item.strip())[0]),(simulation_frequency_entry.get())))))

    for item in engine_script.split("\n"):
        if "idle_throttle_plate_position" in item:
            engine_script = (engine_script.replace(item,(item.replace((re.findall('(?<=idle_throttle_plate_position:\s)\d+\.\d+|(?<=idle_throttle_plate_position:\s)\d+|(?<=idle_throttle_plate_position\s:)\d+\.\d+|(?<=idle_throttle_plate_position\s:)\d+|(?<=idle_throttle_plate_position\s:\s)\d+\.\d+|(?<=idle_throttle_plate_position\s:\s)\d+|(?<=idle_throttle_plate_position:)\d+\.\d+|(?<=idle_throttle_plate_position:)\d+',item.strip())[0]),(idle_throttle_plate_position_entry.get())))))

    for item in engine_script.split("\n"):
        if "starter_torque" in item:
            engine_script = (engine_script.replace(item,(item.replace((re.findall('(?<=starter_torque:\s)\d+\.\d+|(?<=starter_torque:\s)\d+|(?<=starter_torque\s:)\d+\.\d+|(?<=v\s:)\d+|(?<=starter_torque\s:\s)\d+\.\d+|(?<=starter_torque\s:\s)\d+|(?<=starter_torque:)\d+\.\d+|(?<=starter_torque:)\d+',item.strip())[0]),(starter_torque_entry.get())))))

    for item in engine_script.split("\n"):
        if "starter_speed" in item:
            engine_script = (engine_script.replace(item,(item.replace((re.findall('(?<=starter_speed:\s)\d+\.\d+|(?<=starter_speed:\s)\d+|(?<=starter_speed\s:)\d+\.\d+|(?<=starter_speed\s:)\d+|(?<=starter_speed\s:\s)\d+\.\d+|(?<=starter_speed\s:\s)\d+|(?<=starter_speed:)\d+\.\d+|(?<=starter_speed:)\d+|(?<=starter_speed:\s-)\d+\.\d+|(?<=starter_speed:\s-)\d+|(?<=starter_speed\s-:)\d+\.\d+|(?<=starter_speed\s-:)\d+|(?<=starter_speed\s:\s-)\d+\.\d+|(?<=starter_speed\s-:\s)\d+|(?<=starter_speed:-)\d+\.\d+|(?<=starter_speed:-)\d+',item.strip())[0]),(starter_speed_entry.get())))))


    with open(file_path,'r+') as engine_to_write:
        engine_to_write.write(engine_script)
    engine_to_write.close()
    applied_changes()


def comboselectedintake(event):
    if turbo_intake_combobox.get() == 'Yes':
        number_of_intakes_title.place(x=10,y=110)
        number_of_intakes_entry.place(x=400,y=110,width=50)

        plenum_volume_title.place(x=10,y=140)
        plenum_volume_entry.place(x=400,y=140,width=50)
        plenum_volume_unit.place(x=450,y=140)
    else:
        number_of_intakes_title.place_forget()
        number_of_intakes_entry.place_forget()

        plenum_volume_title.place_forget()
        plenum_volume_entry.place_forget()
        plenum_volume_unit.place_forget()





def open_advance_editor():
    advance_window = Toplevel(root)
    slider_count=round((round(rev_limiter_rpm.get(), -3))/1000)
    size = str(40+25*(slider_count)) + "x" + str(150)
    print(size)
    advance_window.geometry(size)
    advance_window.resizable(False,False)
    advance_window.iconbitmap("ressources\Icon.ico")
    advance_window.title('Ignition Advace')



def reset_advance():
    a=1



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------- TKINTER RENDER ---------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#main window
root = Tk()
root.title('Engine Simulator ECU')
root.geometry('500x300')
root.iconbitmap("ressources\Icon.ico")


file_name = ''
file_path = ''
file_content = ''
engine_script = ''
slider_max = 0
redline_delta = 500
theme_combobox = 'theme'




get_settings()
initial_theme()




#top frame
top_frame = ttk.Frame(master=root)
top_frame.pack(fill='both')

top_frame.columnconfigure(0,weight=0)
top_frame.columnconfigure(1,weight=0)
top_frame.columnconfigure(2,weight=1)
top_frame.columnconfigure(3,weight=0)

#open engin button
open_button = ttk.Button(master=top_frame,text='Open engine',command=openfile)
open_button.grid(row=0,column=0,sticky=W)

#opened engine text
opened_engine_text = ttk.Label(master=top_frame,text='Opened Engine :')
opened_engine_text.grid(row=0,column=1,sticky=W)

#opened engine
opened_engine = ttk.Label(master=top_frame,textvariable=file_name)
opened_engine.grid(row=0,column=2,sticky=W)

#apply changes
apply_button = ttk.Button(master=top_frame,text='Apply',command=apply_changes)










#main frame
main_frame = ttk.Frame(master=root)
main_frame.pack(fill='both',expand=1)

#main notebook
main_notebook = ttk.Notebook(master=main_frame)
main_notebook.pack(fill='both',expand=1)










#tab 1
tab_1 = Frame(master=main_notebook,width=500,height=300,bg=maincolor)
tab_1.pack(fill='both',expand=1)

tab_1_logo = ImageTk.PhotoImage((Image.open('ressources\\main_menu_logos\\'+logo_theme)).resize((512, 512)))
tab_1_title = ttk.Label(master=tab_1,image=tab_1_logo)
tab_1_title.place(relx=0.5,y=110,anchor=CENTER)
tab_1_text = ttk.Label(master=tab_1,background=credits_background,text='''Made by Im0nMyWay                
Thanks to AngeTheMinimumWage, NotAngeTheGreat, AaronsLG and Cor''',font='SegoeUI 8')
tab_1_text.place(x=0,y=250,anchor=SW)







#tab 2
tab_2 = Frame(master=main_notebook,width=500,height=300,bg=maincolor)
tab_2.pack(fill='both',expand=1)

tab_2_title = ttk.Label(master=tab_2,text='Rev Limiter', background=maincolor,font='20',foreground=textcolor)
tab_2_title.place(relx=0.5,y=10,anchor=N)

#rev limiter rpm
rev_limiter_rpm = IntVar()
rev_limiter_rpm_title = ttk.Label(master=tab_2,text='Rev limiter RPM :',background=maincolor,foreground=textcolor)
rev_limiter_rpm_entry = ttk.Entry(master=tab_2,textvariable=rev_limiter_rpm)
rev_limiter_rpm_unit = ttk.Label(master=tab_2,text='rpm',background=maincolor,foreground=textcolor)

rev_limiter_rpm_title.place(x=10,y=50)
rev_limiter_rpm_entry.place(x=400,y=50,width=50)
rev_limiter_rpm_unit.place(x=450,y=50)

#rev limiter duration
rev_limiter_duration = IntVar()
rev_limiter_duration_title = ttk.Label(master=tab_2,text='Rev limiter duration :',background=maincolor,foreground=textcolor)
rev_limiter_duration_entry = ttk.Entry(master=tab_2,textvariable=rev_limiter_duration)
rev_limiter_duration_unit = ttk.Label(master=tab_2,text='s',background=maincolor,foreground=textcolor)

rev_limiter_duration_title.place(x=10,y=80)
rev_limiter_duration_entry.place(x=400,y=80,width=50)
rev_limiter_duration_unit.place(x=450,y=80)









#tab 4
tab_4 = Frame(master=main_notebook,width=500,height=300,background=maincolor)
tab_4.pack(fill='both',expand=1)

tab_4_title = ttk.Label(master=tab_4,text='Ignition advance',background=maincolor,font='20',foreground=textcolor)
tab_4_title.place(relx=0.5,y=10,anchor=N)
advance_button_text = ttk.Label(master=tab_4,text='Open advence settings :',background=maincolor,foreground=textcolor)
open_advance_button = ttk.Button(master=tab_4,text='Open advance graph',command=open_advance_editor)
reset_advance_text = ttk.Label(master=tab_4,text='Reset timing curve (not optimal) :',background=maincolor,foreground=textcolor)
reset_advance_button = ttk.Button(master=tab_4,text='Reset Advance',command=reset_advance)

advance_button_text.place(x=10,y=50)
open_advance_button.place(x=350,y=50,width=135)
reset_advance_text.place(x=10,y=80)
reset_advance_button.place(x=350,y=80,width=135)





#tab 3
tab_3 = Frame(master=main_notebook,width=500,height=300,bg=maincolor)
tab_3.pack(fill='both',expand=1)

tab_3_title = ttk.Label(master=tab_3,text='Intake', background=maincolor,font='20',foreground=textcolor)
tab_3_title.place(relx=0.5,y=10,anchor=N)

#idle throttle plate position
idle_throttle_plate_position = IntVar()
idle_throttle_plate_position_title = ttk.Label(master=tab_3,text='Throttle plate position at idle :',background=maincolor,foreground=textcolor)
idle_throttle_plate_position_entry = ttk.Entry(master=tab_3,textvariable=idle_throttle_plate_position)

idle_throttle_plate_position_title.place(x=10,y=50)
idle_throttle_plate_position_entry.place(x=375,y=50,width=75)

#turbo intake checkbutton
turbo_intake_combobox = ttk.Combobox(master=tab_3,background=maincolor,values=('No',"Yes"))
turbo_intake_combobox.set('Pick an option')
turbo_intake_combobox.bind('<<ComboboxSelected>>',comboselectedintake)
turbo_intake_combobox.place(x=350,y=80,width=100)
turbo_intake_title = ttk.Label(master=tab_3,text='Turbo Intake :',background=maincolor,foreground=textcolor)
turbo_intake_title.place(x=10,y=80)

#number of intakes
number_of_intakes = IntVar()
number_of_intakes_title = ttk.Label(master=tab_3,text='Number of turbos / Number of intakes :',background=maincolor,foreground=textcolor)
number_of_intakes_entry = ttk.Entry(master=tab_3,textvariable=number_of_intakes)

#plenum volume
plenum_volume = IntVar()
plenum_volume_title = ttk.Label(master=tab_3,text='Plenum Volume :',background=maincolor,foreground=textcolor)
plenum_volume_entry = ttk.Entry(master=tab_3,textvariable=plenum_volume)
plenum_volume_unit = ttk.Label(master=tab_3,text='L',background=maincolor,foreground=textcolor)









#tab 5
tab_5 = Frame(master=main_notebook,width=500,height=300,bg=maincolor)
tab_5.pack(fill='both',expand=1)

tab_5_title = ttk.Label(master=tab_5,text='Others', background=maincolor,font='20',foreground=textcolor)
tab_5_title.place(relx=0.5,y=10,anchor=N)

#simulation frequency
simulation_frequency = IntVar()
simulation_frequency_title = ttk.Label(master=tab_5,text='Simulation frequency :',background=maincolor,foreground=textcolor)
simulation_frequency_entry = ttk.Entry(master=tab_5,textvariable=simulation_frequency)
simulation_frequency_unit = ttk.Label(master=tab_5,text='Hz',background=maincolor,foreground=textcolor)

simulation_frequency_title.place(x=10,y=50)
simulation_frequency_entry.place(x=400,y=50,width=50)
simulation_frequency_unit.place(x=450,y=50)





#tab 6
tab_6 = Frame(master=main_notebook,width=500,height=300,bg=maincolor)
tab_6.pack(fill='both',expand=1)

tab_6_title = ttk.Label(master=tab_6,text='Starter',background=maincolor,font='20',foreground=textcolor)
tab_6_title.place(relx=0.5,y=10,anchor=N)

starter_speed = IntVar()
starter_speed_title = ttk.Label(master=tab_6,text='Starter speed :',background=maincolor,foreground=textcolor)
starter_speed_entry = ttk.Entry(master=tab_6,textvariable=starter_speed)
starter_speed_unit = ttk.Label(master=tab_6,text='rpm',background=maincolor,foreground=textcolor)

starter_torque = IntVar()
starter_torque_title = ttk.Label(master=tab_6,text='Starter torque :',background=maincolor,foreground=textcolor)
starter_torque_entry = ttk.Entry(master=tab_6,textvariable=starter_torque)
starter_torque_unit = ttk.Label(master=tab_6,text='lb.ft',background=maincolor,foreground=textcolor)

starter_speed_title.place(x=10,y=50)
starter_speed_entry.place(x=400,y=50,width=50)
starter_speed_unit.place(x=450,y=50)

starter_torque_title.place(x=10,y=80)
starter_torque_entry.place(x=400,y=80,width=50)
starter_torque_unit.place(x=450,y=80)




#tab 7
tab_7 = Frame(master=main_notebook,width=500,height=300,background=maincolor)
tab_7.pack(fill='both',expand=1)

tab_7_title = ttk.Label(master=tab_7,text='Settings',background=maincolor,font='20',foreground=textcolor)
tab_7_title.place(relx=0.5,y=10,anchor=N)

theme_combobox = ttk.Combobox(master=tab_7,background=maincolor,values=['Default','Dark','Clear'])
theme_combobox.set(current_theme)
theme_combobox.bind('<<ComboboxSelected>>',update_theme)
theme_combobox.place(x=350,y=50,width=100)
theme_title = ttk.Label(master=tab_7,text='Theme :',background=maincolor,foreground=textcolor)
theme_title.place(x=10,y=50)





#frame list
main_notebook.add(tab_1,text='Home')
main_notebook.add(tab_2,text='Rev Limiter')
main_notebook.add(tab_4,text='Ignition Advance')
main_notebook.add(tab_3,text='Intake')
main_notebook.add(tab_6,text='Starter')
main_notebook.add(tab_5,text='Others')
main_notebook.add(tab_7,text='Settings')




#run window
main_notebook.hide(1)
main_notebook.hide(2)
main_notebook.hide(3)
main_notebook.hide(4)
main_notebook.hide(5)
root.resizable(False,False)
root.mainloop()