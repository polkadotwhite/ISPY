 
from turtle import *

# includes sequence, structure and colour
#1.7 is a full working version of Toolbox1 which can be used to explore symmetry and regular shapes including
# squares,rectangles, polygons, circles and stars, while learning to program with sequence and repetition and
# make use of simple user-defined functions with a single parameter.
# And complex 'Unplugged' Works. No 'Python 3' yet.
#Toolbox2 starts in 1.8

import time 
import math
import random

from tkinter import *
from tkinter import ttk
#from tkinter.ttk import * #don't have to use ttk prefix for themed widgets
from tkinter import font 

root = Tk()
root.title("Version 1.8: Crack the Code. Build the code. Look for symmetry. Fly red arrow to make patterns")
root.geometry("1250x660+10+10")#10px in from screen side (left x), 10px down from screen top (down y)
# - minus is x from right and y from bottom respectively


 

##*******************  event handler functions  ************
in_repeat_code=StringVar()
in_repeat_code.set("***")


paces= StringVar()
paces.set('10')

fpaces = StringVar()
fpaces.set('10')

rpaces = StringVar()
rpaces.set('10')

sqpaces = StringVar()
sqpaces.set('10')

degrees_left= StringVar()
degrees_left.set('360/4')

degrees_right= StringVar()
degrees_right.set('90')

magic1 = StringVar()
magic2 = StringVar()
magic1.set('1')
magic2.set('2')

pic=IntVar()
pic.set('')

appHighlightFont = font.Font(family='Courier New', size=16, weight='normal')
boldFont12 = font.Font(size = 12, weight="normal")
boldFont14 = font.Font(size = 14, weight="normal")
boldFont16 = font.Font(size = 16, weight="normal")
boldFont18 = font.Font(size = 18, weight="bold")

def define():
    print('entering  setting up define() for functions')
    # set up define for the next funi() i<=4, in python in the usual way +indentation,
    #and in upl with the --> operator.
    #set up the python code: def funi(): and then put in lines of code prefaced by 4 spaces until save is pressed
    #then turn funi to defined(colour)
    pass
def display_upl():
    # displays upl program in label_instruction box
    global allow
    global tb1
    global tb2
    global record    
    global frame3
    global frame4
    global ucode
    global ecode
    global uplshow
    global label_instruction
    global arc_record
    global arc_recordpy
    global arc_recordmypy
    global record
    global recordpy
    global recordmypy


    
    if allow == True:
        allow = False
        if  pyshow ==True:
            print("Click on 'Python 3' again to close window")
            allow=True
        else:
            if uplshow ==False:
                
                print("upl is", ''.join(record))
                print("uplshow is",uplshow)
                
                # clear space for recording unplugged program
                for child in frame3.winfo_children():
                    child.destroy()           
                print("frame4 and children, including pad1, are destroyed")            

                #reset frame3 onwards with upl program as message
                frame3 = Frame(root, bg="light yellow", padx=5, pady=0)
                frame3.grid(column=2, row=0, sticky=(N,E,W))
                frame3.columnconfigure(0, weight=1)
                frame3.rowconfigure(0, weight=1)
                frame3['borderwidth'] = 3
                frame3['relief'] = 'raised'

                inner_frame3 = Frame(frame3, bg = "light yellow", padx =5, pady = 5)
                inner_frame3.grid(column=0, row=0, sticky=(N,E,W,S)) 
                
                label_instruction = ttk.Label(inner_frame3, relief=RIDGE, textvariable = ucode, wraplength= 400, width=52,  font = boldFont14,\
                                       background = 'yellow',  padding="20 5 5 5")
                label_instruction.grid(column=0, row=0, sticky=(N,W,S,E))
                label_instruction['relief'] = 'raised'
                label_instruction['justify'] = 'left'# justifies within the line
                label_instruction['anchor'] = 'w' # moves to left of the box
                label_instruction['borderwidth'] = 5
                         
                ucode.set(''.join(record))            
                uplshow= True
                allow=True
                
                print("exiting display_upl, uplshow is, allow is",uplshow, allow)
                
            
            
            else:# uplshow is true, and allow is False, so toggle switch on 'unplugged' restore frame3 and toolbox1
                allow=True
                if tb1:
                    toolbox1()# resets frame3 onwards
                elif tb2:
                    toolbox2()
                allow=False
                arc_record + record
                record = arc_record
                arc_recordpy + recordpy                
                recordpy = arc_recordpy
                arc_recordmypy + recordmypy
                recordmypy = arc_recordmypy
                print("reset code in program_box and print record=", record, "recordmypy is", recordmypy)
                ttt=''.join(record)
                ecode.set(ttt)
                go=''.join(recordmypy)
                print('go is', go)
                
                ######################
                exec(go)
                ######################
                
                
                print(" restore to former displays; after display_upl and allow is", allow)
                print("uplshow is",uplshow)                       
                uplshow=False
                allow=True
    else:
        print('no entry to  display_upl(), spin out')   
    
def display_py():
    # displays Python 3 program in label_instruction box
    global allow
    global tb1
    global tb2
    global record    
    global frame3
    global frame4
    global ecode
    global pyshow
    global holding_py
    global holding_upl
    global label_instruction

    if allow == True:
        allow = False
        if uplshow==True:
            print("click on 'Unplugged' to close upl program first")
        elif  pyshow ==False:
            pylshow=True
            holding_upl=ecode.get()
            holding_py = ''.join(recordpy)
            print("holding_py is", holding_py)
            print(''.join(recordpy))
            print("pyshow is",pyshow)
            
            # clear space for recording Python 3 program
            for child in frame3.winfo_children():
                child.destroy()           
            print("frame4 and children, including pad1, are destroyed")            

            #reset frame3 onwards with python 3 program as message
            frame3 = Frame(root, bg="light yellow", padx=5, pady=20)
            frame3.grid(column=2, row=0, sticky=(N,E,W))
            frame3.columnconfigure(0, weight=1)
            frame3.rowconfigure(0, weight=1)
            frame3['borderwidth'] = 3
            frame3['relief'] = 'raised'

            inner_frame3 = Frame(frame3, bg = "light yellow", padx =5, pady = 5)
            inner_frame3.grid(column=0, row=0, sticky=(N,E,W,S)) 
            
            label_instruction = ttk.Label(inner_frame3, relief=RIDGE, textvariable = ucode, wraplength= 400, width=40,  font = boldFont12,\
                                   background = 'yellow',  padding="10 5 10 5")
            label_instruction.grid(column=0, row=0, sticky=(N,W,S,E))
            label_instruction['relief'] = 'raised'
            label_instruction['justify'] = 'left'# justifies within the line
            label_instruction['anchor'] = 'center' # moves to center of the box
            label_instruction['borderwidth'] = 5
            
            #label_instruction.configure(background = 'yellow')         
            ucode.set(''.join(recordpy))            
            pyshow= True
            allow=True
            
            print("exiting display_py, pyshow is, allow is",pyshow, allow)
            
            
            
        else:# pyshow is true, and allow is False, so toggle switch on 'Python 3' torestore frame3 and toolbox1
            allow=True
            if tb1:
                toolbox1()# resets frame3 onwards
            elif tb2:
                toolbox2()
                
            allow=False
            ecode.set(holding_upl)
            print(" restore to former displays; after display_py and allow is", allow)
            print("pyshow is",pyshow)                       
            pyshow=True
            allow=True
    else:
        print('no entry to  display_py(), spin out')   
    



def pad2():
    
    global allow
    global repeat_btn
    global tim
    global times
    global brackets
    global gobtn
    global label_instruction
    global frame3
    global frame4
    global pad_bo
    global tim
    global times
    global brackets
    global gobtnx   
    global label_instruction   
    global ok_repeat
    global gop
    global gou
    global gg
    global in_repeat_code   
    global f123
    global pen_is_down
    global my
    
    global ucode    
 
    
    ##################################  frame 4!T2  #######################################################


    programFont12 = font.Font(family='Courier New', size=12, weight='bold')
    programFont14 = font.Font(family='Courier New', size=14, weight='bold')   
    programFont16 = font.Font(family='Courier New', size=16, weight='bold')
    programFont18 = font.Font(family='Courier New', size=18, weight='bold')
    programFont20 = font.Font(family='Courier New', size=20, weight='bold')
    programFont24 = font.Font(family='Courier New', size=24, weight='bold')
    programFont32 = font.Font(family='Courier New', size=32, weight='bold')

    italicFont12 = font.Font(family='Arial', size=12, weight='normal')
    italicFont14 = font.Font(family='Arial', size=14, weight='normal')
    italicFont16 = font.Font(family='Arial', size=16, weight='normal')

    boldFont12= font.Font(family='Arial', size=12, weight='bold')
    boldFont14= font.Font(family='Arial', size=14, weight='bold')
    boldFont16= font.Font(family='Arial', size=16, weight='bold')
    boldFont18= font.Font(family='Arial', size=18, weight='bold')
    
    h_cement=2
    v_cement=2

    #for child in frame3.winfo_children():
                #child.destroy()
    

    frame4 = Frame(frame3, bg = "light yellow", padx=20, pady = 50)
    frame4.grid(row = 1, column = 0, sticky= (N,E,W,S) )
    
    fillerhvar= Frame(frame4,height=0, bg="light yellow")
    fillerhvar.grid(column=0, row=0, sticky=(N, W, E))
        
    pad_box = Frame(frame4)# silver keypad all instructions
    pad_box.grid(column=0, row=0, sticky=(N, W, E))
    pad_box['relief'] = 'raised'
    pad_box['borderwidth'] = 8
    pad_box['background'] = 'silver'
    pad_box['padx'] = 5
    pad_box['pady'] = 5
    
    #fillerh120= Frame(frame4,height=150, bg="light yellow")
    #fillerh120.grid(column=0, row=2, sticky=(N, W, E, S))

    #########################################   set up click pad   ###################################

    padhead = Label(pad_box, font= italicFont14, \
                    text="Toolbox 2: Symmetry, Colour and Repetition", width = 32, height = 2)
    padhead.grid(row=0, column=0, sticky = (N,E,W,S))  
    padhead['background'] = 'silver'

    heading1 = Label(pad_box, font= italicFont14, text="     instructions (built-in)", width = 25)
    #heading1.grid(row=1, column=0, sticky = (W))
    heading1['anchor'] = 'w'
    heading1['background'] = 'silver'
    
    mainframe = Frame(pad_box, borderwidth = 2, padx =1, pady = 0)#instructions built-in
    mainframe.grid(column=0, row=1, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe['background'] = 'silver'

    user_mainframe = Frame(pad_box, borderwidth = 2, padx =1, pady =0)#instructions user-built
    user_mainframe.grid(column=0, row=2, sticky=(N, W, E, S))
    user_mainframe.columnconfigure(0, weight=1)
    user_mainframe.rowconfigure(0, weight=1)
    user_mainframe['background'] = 'silver'

    ############################################### setting up separate frames in rows: no vertical misaligning

    user_mainframe1 = Frame(user_mainframe)
    user_mainframe1.grid(column=0, row=0, sticky=(N, W, E, S))
    user_mainframe1['background'] = 'silver'

    user_mainframe2 = Frame(user_mainframe)
    user_mainframe2.grid(column=0, row=1, sticky=(N, W, E, S))
    user_mainframe2['background'] = 'silver'

    user_mainframe3 = Frame(user_mainframe)
    user_mainframe3.grid(column=0, row=2, sticky=(N, W, E, S))
    user_mainframe3['background'] = 'silver'  

    user_mainframe4 = Frame(user_mainframe)
    user_mainframe4.grid(column=0, row=3, sticky=(N, W, E, S))
    user_mainframe4['background'] = 'silver'

    user_mainframe5 = Frame(user_mainframe)
    user_mainframe5.grid(column=0, row=4, sticky=(N, W, E, S))
    user_mainframe5['background'] = 'silver'

    user_mainframe6 = Frame(user_mainframe)
    user_mainframe6.grid(column=0, row=5, sticky=(N, W, E, S))
    user_mainframe6['background'] = 'silver'


    ###############################################################################################################
    
    mainframe1 = Frame(mainframe)
    mainframe1.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe1['background'] = 'silver'
    
    mainframe2 = Frame(mainframe)
    mainframe2.grid(column=0, row=1, sticky=(N, W, E, S))
    mainframe2['background'] = 'silver'
    
    mainframe3 = Frame(mainframe)
    mainframe3.grid(column=0, row=2, sticky=(N, W, E, S))
    mainframe3['background'] = 'silver'
    
    mainframe4 = Frame(mainframe)
    mainframe4.grid(column=0, row=3, sticky=(N, W, E, S))
    mainframe4['background'] = 'silver'
    
    mainframe5 = Frame(mainframe, bg="silver")
    mainframe5.grid(column=0, row=4, sticky=(N, W, E, S))
    
    mainframe6 = Frame(mainframe, bg="silver")
    mainframe6.grid(column=0, row=5, sticky=(N, W, E, S))
    
    mainframe7 = Frame(mainframe, bg="silver")
    mainframe7.grid(column=0, row=6, sticky=(N, W, E, S))

    mainframe8 = Frame(mainframe, bg="silver")
    mainframe8.grid(column=0, row=7, sticky=(N, W, E, S))

    mainframe9 = Frame(mainframe, bg="silver")
    mainframe9.grid(column=0, row=8, sticky=(N, W, E, S))

    mainframe10 = Frame(mainframe, bg="silver")
    mainframe10.grid(column=0, row=9, sticky=(N, W, E, S))

    mainframe11 = Frame(mainframe, bg="silver")
    mainframe11.grid(column=0, row=10, sticky=(N, W, E, S))

    mainframe12 = Frame(mainframe, bg="silver")
    mainframe12.grid(column=0, row=11, sticky=(N, W, E, S))

    mainframe13 = Frame(mainframe, bg="silver")
    mainframe13.grid(column=0, row=12, sticky=(N, W, E, S))
    

    mainframe14 = Frame(mainframe, bg="silver")
    mainframe14.grid(column=0, row=13, sticky=(N, W, E, S))

    mainframe15 = Frame(mainframe, bg="silver")
    mainframe15.grid(column=0, row=14, sticky=(N, W, E, S))
    
    ########################## program instructions ############################################
    
    programFont12 = font.Font(family='Courier New', size=12, weight='bold')
    programFont14 = font.Font(family='Courier New', size=14, weight='bold')   
    programFont16 = font.Font(family='Courier New', size=16, weight='bold')
    programFont18 = font.Font(family='Courier New', size=18, weight='bold')
    programFont20 = font.Font(family='Courier New', size=20, weight='bold')
    programFont24 = font.Font(family='Courier New', size=24, weight='bold')
    programFont32 = font.Font(family='Courier New', size=32, weight='bold')
    
    italicFont14 = font.Font(family='Arial', size=14, weight='normal')
    italicFont16 = font.Font(family='Arial', size=16, weight='normal')
            




    forward = Label(mainframe1, font= italicFont14, text="forward", width = 8)
    forward.grid(row=0, column=0, sticky = (W))
    forward['anchor'] = 'w'
    forward['background'] = 'silver'
                                            
    btn1 = Button(mainframe1, text="fd1", font= programFont14, bg = "light yellow", width = 5,command = stepout1)
    btn1.grid(column = 1, row =0, sticky = (N,W))        
    btn1['relief'] = 'raised'
    btn1['borderwidth'] = 5

    v_cem1 = Frame(mainframe1, bg= "silver", width = v_cement)
    v_cem1.grid(column=2, row= 0, sticky = (W))
    
    btn2 = Button(mainframe1, text="fd2", font= programFont14, bg = "light yellow", width = 5,command = stepout2)
    btn2.grid(column = 3, row =0, sticky = (N,W))
    btn2['relief'] = 'raised'
    btn2['borderwidth'] = 5

    v_cem2 = Frame(mainframe1, bg= "silver", width = v_cement)
    v_cem2.grid(column=4, row= 0, sticky = (W))
    
    btn3 = Button(mainframe1, text="fd3", font= programFont14, bg = "light yellow", width = 5,command = stepout3)
    btn3.grid(column = 5, row =0, sticky = (N,W))
    btn3['relief'] = 'raised'
    btn3['borderwidth'] = 5

    v_cem3 = Frame(mainframe1, bg= "silver", width = v_cement)
    v_cem3.grid(column=6, row= 0, sticky = (W)) 

    btn4 = Button(mainframe1, text="fd4", font= programFont14, bg = "light yellow", width = 5,command = stepout4)
    btn4.grid(column = 7, row =0, sticky = (N,W))
    btn4['relief'] = 'raised'
    btn4['borderwidth'] = 5

    v_cem4 = Frame(mainframe1, bg= "silver", width = v_cement)
    v_cem4.grid(column=8, row= 0, sticky = (W)) 

    btnchoose = Button(mainframe1, text="fd", font= programFont14, \
                       bg = "light yellow", width = 4,command = stepout_choose)
    btnchoose.grid(column = 9, row =0, sticky = (N,W))
    btnchoose['relief'] = 'raised'
    btnchoose['borderwidth'] = 5

    
    forward_entry = Entry(mainframe1, bd = 5, width = 2, textvariable = paces,  font= programFont14, bg = 'light yellow')
    forward_entry.grid(column=11, row=0, sticky= (N,W,E,S))
    #forward_entry.bind("<FocusIn>", forward_act)
    
    fillerm2= Frame(mainframe2, height=h_cement, bg= "silver")
    fillerm2.grid(column=0, row=0, sticky=(N, W, E))

    

    


    left_turn = Label(mainframe3, font= italicFont14, text="left turn", width = 8)
    left_turn.grid(column=0, row=0, sticky=(W))
    left_turn['background'] = 'silver'
    left_turn['anchor'] = 'w'

    
    
    btnleft = Button(mainframe3, text="lt", font= programFont14, bg = "light yellow", width = 5, command = left)
    btnleft.grid(column=1, row=0, sticky= (N,W))
    btnleft['relief'] = 'raised'
    btnleft['borderwidth'] = 5

    
    left_entry = Entry(mainframe3, bd = 5, width = 7, textvariable = degrees_left,  font= programFont14, bg = 'light yellow')
    left_entry.grid(column=2, row=0, sticky= (N,W,E,S))
    #left_entry.bind("<FocusIn>", left_act)
    
    #left_blank = Label(mainframe3, bd = 5, width = 5,   font= programFont14, bg = 'silver')
    #left_blank.grid(column=2, row=0, sticky= (N,W,E,S))
    
    filler2a= Frame(mainframe3, width =5)
    filler2a.grid(column=3, row=0, sticky=(N, W, E, S))
    filler2a['background'] = 'silver'
    

    pen_up = Button(mainframe3, text="penup", font= programFont14, bg = "light yellow", width = 5,  command = put_penup)
    pen_up.grid(column=4, row=0 , sticky= (N,W))
    pen_up['relief'] = 'raised'
    pen_up['borderwidth'] = 5
    pen_up['anchor'] = 'w'

    v_cem5 = Frame(mainframe3, bg= "silver", width = v_cement)
    v_cem5.grid(column=5, row= 0, sticky = (W)) 


    pen_down = Button(mainframe3, text="pendown", font= programFont14, bg = "light yellow", width = 7,  command = put_pendown)
    pen_down.grid(column=6, row=0 , sticky= (N,W))
    pen_down['relief'] = 'raised'
    pen_down['borderwidth'] = 5
    pen_down['anchor'] = 'w'

    v_cem6 = Frame(mainframe3, bg= "silver", width = v_cement)
    v_cem6.grid(column=7, row= 0, sticky = (W)) 

    hide = Button(mainframe3, text="hide", font= programFont14,  bg = "light blue", width = 3, command=hide_arrow, padx= 10)
    hide.grid(column=8, row=0, sticky= (E))
    hide['relief'] = 'raised'
    hide['borderwidth'] = 5

    fillerm4= Frame(mainframe4, height=h_cement, bg= "silver")
    fillerm4.grid(column=0, row=0, sticky=(N, W, E))
    
    right_turn = Label(mainframe5, font= italicFont14, text="right turn", width = 8)
    right_turn.grid(column=0, row=0, sticky=(W))
    right_turn['background'] = 'silver'
    right_turn['anchor'] = 'w'

    btnright = Button(mainframe5, text="rt", font = programFont14,  bg = "light yellow",\
                      width = 5, command = right)
    btnright.grid(column=1, row=0, sticky= (N,W))
    btnright['relief'] = 'raised'
    btnright['borderwidth'] = 5

    #right_blank = Label(mainframe5, bd = 5, width = 5,font= programFont14, bg = 'silver')
    #right_blank.grid(column=2, row=0, sticky= (N,W,E,S))

    
    right_entry = Entry(mainframe5, bd = 5, width = 7, textvariable = degrees_right,  font= programFont14, bg = 'light yellow')
    right_entry.grid(column=2, row=0, sticky= (N,W,E,S))
    #right_entry.bind("<FocusIn>", left_act)
    

    
    

    filler2= Frame(mainframe5, width = 5)
    filler2.grid(column=3, row=0, sticky=(N, W, E, S))
    filler2['background'] = 'silver'

    
    
    delete = Button(mainframe5, text="delete", font= programFont14,  bg = "light blue", width = 6, command = delete_op )
    delete.grid(column=5, row=0, sticky= (E))
    delete['relief'] = 'raised'
    delete['borderwidth'] = 5

    v_cem7 = Frame(mainframe5, bg= "silver", width = v_cement)
    v_cem7.grid(column=6, row= 0, sticky = (W)) 

    clear = Button(mainframe5, text="clear", font= programFont14,  bg = "light blue", width = 3, command=full_delete, padx= 10)
    clear.grid(column=7, row=0, sticky= (E))
    clear['relief'] = 'raised'
    clear['borderwidth'] = 5

    v_cem8 = Frame(mainframe5, bg= "silver", width = v_cement)
    v_cem8.grid(column=8, row= 0, sticky = (W)) 

    newline = Button(mainframe5, text="newline", font= programFont14,  bg = "light blue", width = 5, command=new_line, padx= 10)
    newline.grid(column=9, row=0, sticky= (E))
    newline['relief'] = 'raised'
    newline['borderwidth'] = 5

    

    
   ################################### repeat control structure #############################################################
    
    
    repeat_btn= Button(mainframe6, text="repeat", width = 6, font = programFont14, command = setup_repeat)
    repeat_btn.grid(column=0, row=1, sticky=(W))
    repeat_btn['background'] = 'light yellow'

    filler25= Frame(mainframe6, width = 4)
    filler25.grid(column=1, row=1, sticky=(N, W, E, S))
    filler25['background'] = 'silver'
    
    
    #times = StringVar()
    #times.set('')
    tim = Entry(mainframe6,bd = 5, width = 2, textvariable = times,  font= programFont14, bg = 'light yellow')
    tim.grid(column=2, row=1, sticky= (E,W))
    tim.bind("<FocusIn>", act)
    

    filler3= Frame(mainframe6, width = 2)
    filler3.grid(column=3, row=1, sticky=(N, W,E,S))
    filler3['background'] = 'silver'

    bracketleft = Label(mainframe6, text='[', font= programFont32, bg = "silver", width = 1)
    bracketleft.grid(column=4, row=1, sticky= (N))

    
    brackets = Label(mainframe6, text=in_repeat_code,textvariable = in_repeat_code, font= programFont18,\
                     bg = "light yellow", width = 32)
    brackets.grid(column=5, row=1, sticky= (W,E))
    brackets.configure(font=programFont12)
    in_repeat_code.set('***')

    bracketright = Label(mainframe6, text=']', font= programFont32, bg = "silver", width = 1)
    bracketright.grid(column=6, row=1, sticky= (N,W))

    filler4= Frame(mainframe6, width = 2)
    filler4.grid(column=7, row=1, sticky=(N, W, E, S))
    filler4['background'] = 'silver'

    gobtn = Button(mainframe6, text="do it", font= programFont16, bg = "light yellow",  command = execute_repeat, width = 5)
    gobtn.grid(column=8, row=1, sticky= (E,W))

     ################################################   functions  #############################################
    
    functions = Label(mainframe7, font= italicFont14, text="define", width = 8)
    functions.grid(column=0, row=0, sticky=(N,W,E,S))
    functions['background'] = 'silver'
    functions['anchor'] = 'w'

    fundef = Button(mainframe7, text="define", font= programFont14, bg = "light yellow", fg = "black", width = 6,command = define)
    fundef.grid(column = 1, row =0, sticky = (N,W))        
    fundef['relief'] = 'raised'
    fundef['borderwidth'] = 5
    fundef['anchor'] = 'w'
    
    funbtn1 = Button(mainframe7, text="fun1", font= programFont14, bg = "light yellow", fg = "black", width = 4,command = function1)
    funbtn1.grid(column = 2, row =0, sticky = (N,W))        
    funbtn1['relief'] = 'raised'
    funbtn1['borderwidth'] = 5
    funbtn1['anchor'] = 'w'


    funbtn2 = Button(mainframe7, text="fun2", font= programFont14, bg = "light yellow", fg = "black", width = 4,command = function2)
    funbtn2.grid(column = 3, row =0, sticky = (N,W))        
    funbtn2['relief'] = 'raised'
    funbtn2['borderwidth'] = 5
    funbtn2['anchor'] = 'w'

    funbtn3 = Button(mainframe7, text="fun3", font= programFont14, bg = "light yellow", fg = "black", width = 4,command = function2)
    funbtn3.grid(column = 4, row =0, sticky = (N,W))        
    funbtn3['relief'] = 'raised'
    funbtn3['borderwidth'] = 5
    funbtn3['anchor'] = 'w'

    funbtn4 = Button(mainframe7, text="fun4", font= programFont14, bg = "light yellow", fg = "black", width = 4,command = function2)
    funbtn4.grid(column = 5, row =0, sticky = (N,W))        
    funbtn4['relief'] = 'raised'
    funbtn4['borderwidth'] = 5
    funbtn4['anchor'] = 'w' 


    funbtn5 = Button(mainframe7, text="fun5", font= programFont14, bg = "light yellow", fg = "black", width = 4,command = function2)
    #funbtn5.grid(column = 6, row =0, sticky = (N,W))        
    funbtn5['relief'] = 'raised'
    funbtn5['borderwidth'] = 5
    funbtn5['anchor'] = 'w'
    #makebtn = Button(mainframe, text="make &", font= programFont14, bg = "light yellow", fg = "black", width = 6,command = make_fun)
    #makebtn.grid(column = 4, row =0, sticky = (N,E))        
    #makebtn['relief'] = 'raised'
    #makebtn['borderwidth'] = 5
    #makebtn['anchor'] = 'w'functions = Label(mainframe7, font= italicFont14, text="functions", width = 8)


    functions = Label(mainframe8, font= italicFont14, text="functions", width = 8)
    functions.grid(column=0, row=0, sticky=(N,W,E,S))
    functions['background'] = 'silver'
    functions['anchor'] = 'w'

    

    savebtn = Button(mainframe8, text="save in fun", font= programFont14, bg = "light yellow", fg = "black", width = 12,command = save)
    savebtn.grid(column = 1, row =0, sticky = (N,E))        
    savebtn['relief'] = 'raised'
    savebtn['borderwidth'] = 5
    savebtn['anchor'] = 'w'

    f123 = StringVar()
    f123.set('1')
    userfun = Entry(mainframe8,bd = 6, width = 1, textvariable = f123, font= programFont14, bg = 'light yellow')
    userfun.grid(column=2, row=0, sticky= (W,E))
    

   

     ######################################    colourT1 tabsT1    ########################################################
    
        
    colourlab =Label(user_mainframe2, font= italicFont14, text="colour", width = 8)
    colourlab.grid(column=0, row=0, sticky=(N,W,E,S))
    colourlab['background'] = 'silver'
    colourlab['anchor'] = 'w'

    cbtn1 = Button(user_mainframe2, text="red", font= programFont14, bg = "red", fg = "white", width = 5,command = red)
    cbtn1.grid(column = 1, row =0, sticky = (N,W))        
    cbtn1['relief'] = 'raised'
    cbtn1['borderwidth'] = 5

    v_cem10 = Frame(user_mainframe2, bg= "silver", width = v_cement)
    v_cem10.grid(column=2, row= 0, sticky = (W))
    

    
    cbtn2 = Button(user_mainframe2, text="blue", font= programFont14, bg = "blue",fg = "white", width = 5,command = blue)
    cbtn2.grid(column = 3, row =0, sticky = (N,E,W,S))
    cbtn2['relief'] = 'raised'
    cbtn2['borderwidth'] = 5

    v_cem11 = Frame(user_mainframe2, bg= "silver", width = v_cement)
    v_cem11.grid(column=4, row= 0, sticky = (W)) 

    
    cbtn3 = Button(user_mainframe2, text="green", font= programFont14, bg = "green",fg = "white", width = 5,command = green)
    cbtn3.grid(column = 5, row =0, sticky = (N,W))
    cbtn3['relief'] = 'raised'
    cbtn3['borderwidth'] = 5

    v_cem12 = Frame(user_mainframe2, bg= "silver", width = v_cement)
    v_cem12.grid(column=6, row= 0, sticky = (W)) 

    cbtn4 = Button(user_mainframe2, text="black", font= programFont14, bg = "black",fg = "white", width = 5,command = black)
    cbtn4.grid(column = 7, row =0, sticky = (N,W))
    cbtn4['relief'] = 'raised'
    cbtn4['borderwidth'] = 5

    v_cem13 = Frame(user_mainframe2, bg= "silver", width = v_cement)
    v_cem13.grid(column=8, row= 0, sticky = (W)) 

    cbtn5 = Button(user_mainframe2, text="gold", font= programFont14, bg = "gold",fg = "black", width = 5,command = gold)
    cbtn5.grid(column = 9, row =0, sticky = (N,W))
    cbtn5['relief'] = 'raised'
    cbtn5['borderwidth'] = 5

    v_cem14 = Frame(user_mainframe2, bg= "silver", width = v_cement)
    #v_cem14.grid(column=10, row= 0, sticky = (W)) 
    
    cbtn6 = Button(user_mainframe2, text="white", font= programFont14, bg = "white",fg = "black", width = 5,command = white)
    cbtn6.grid(column = 10, row =0, sticky = (N,W))
    cbtn6['relief'] = 'raised'
    cbtn6['borderwidth'] = 5


    ################################# magic box  ##########################################################

    magicbox = Label(user_mainframe1, font= italicFont14, text="magic box", width = 8)
    magicbox.grid(column=0, row=0, sticky=(N,W,E,S))
    magicbox['background'] = 'silver'
    magicbox['anchor'] = 'w'

    magicbtn1 = Button(user_mainframe1, text="box 1,0", font= programFont14, bg = "light green", fg = "black", width = 7,command = magic10)
    magicbtn1.grid(column = 1, row =0, sticky = (N,W))        
    magicbtn1['relief'] = 'raised'
    magicbtn1['borderwidth'] = 5
    magicbtn1['anchor'] = 'w'


    magicbtn2 = Button(user_mainframe1, text="box 0,1", font= programFont14, bg = "light green", fg = "black", width = 7,command = magic01)
    magicbtn2.grid(column = 2, row =0, sticky = (N,W))        
    magicbtn2['relief'] = 'raised'
    magicbtn2['borderwidth'] = 5
    magicbtn2['anchor'] = 'w'

    magicbtn3 = Button(user_mainframe1, text="box 1,1", font= programFont14, bg = "light green", fg = "black", \
                       width = 7,command = magic11)
    magicbtn3.grid(column = 3, row =0, sticky = (N,W))        
    magicbtn3['relief'] = 'raised'
    magicbtn3['borderwidth'] = 5
    magicbtn3['anchor'] = 'w'

    magicbtn4 = Button(user_mainframe1, text="box", font= programFont14, bg = "light green", fg = "black", width = 3,\
                       command = magic_trick)
    magicbtn4.grid(column = 4, row =0, sticky = (N,E))        
    magicbtn4['relief'] = 'raised'
    magicbtn4['borderwidth'] = 5
    magicbtn4['anchor'] = 'w'

    
    usermagic1 = Entry(user_mainframe1, bd = 6, width = 2, textvariable = magic1, font= programFont14, bg = 'light green')
    usermagic1.grid(column=5, row=0, sticky= (W,E))

    usermagic2 = Entry(user_mainframe1, bd = 6, width = 2, textvariable = magic2, font= programFont14, bg = 'light green')
    usermagic2.grid(column=6, row=0, sticky= (W,E))

    fillerm14= Frame(mainframe14, height=h_cement, bg= "silver")
    #fillerm14.grid(column=0, row=0, sticky=(N, W, E))
    
    
    ##################################  gridT1 sizes!T1 ##########################################

    
    #fillerx50= Frame(user_mainframe, height=h_cement, bg = "silver")
    #fillerx50.grid(column=0, row=4, sticky=(N, W, E))
    #user_mainframe3 = Frame(user_mainframe3,bg= "silver") # new frame to allow for varying width  of 'no grid' button
    #user_mainframe2.grid(column=0, row=0, sticky=(N,E,W,S))
    
    
##########################################end of def of pad2 ##########################################################


def pad1():
    global allow
    global repeat_btn
    global tim
    global times
    global brackets
    global gobtn
    '''
    global label_instruction
    global frame3
    global frame4
    global pad_box
    '''
    ##################################  frame 4  #######################################################

    h_cement=3
    v_cement=3
    print('entering pad1()')

    frame4 = Frame(frame3, bg = "light yellow", padx=3, pady = 20)
    frame4.grid(row = 1, column = 0, sticky= (N,E,W,S) )

    fillerh150= Frame(frame4,height=2, bg="light yellow")
    #fillerh150.grid(column=0, row=0, sticky=(N, W, E))
        
    pad_box = Frame(frame4, padx=0, pady =5)
    pad_box.grid(column=0, row=1, sticky=(N, W, E))
    pad_box['relief'] = 'raised'
    pad_box['borderwidth'] = 8
    pad_box['background'] = 'silver'
    pad_box['padx'] = 3
    pad_box['pady'] = 3
    
    fillerh120= Frame(frame4,height=10, bg="light yellow")
    fillerh120.grid(column=0, row=2, sticky=(N, W, E, S))

    #########################################   set up click pad   ###################################

    padhead = Label(pad_box, font= boldFont16, text=" Toolbox 1: Sequence, Symmetry and Repetition", width = 40, height = 2)
    padhead.grid(row=0, column=0, sticky = (N,E,W,S))
    padhead['background'] = 'silver'
    
    mainframe = Frame(pad_box, borderwidth = 2, padx =1, pady =10)
    mainframe.grid(column=0, row=1, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe['background'] = 'silver'
    
    mainframe1 = Frame(mainframe)
    mainframe1.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe1['background'] = 'silver'
    
    mainframe2 = Frame(mainframe)
    mainframe2.grid(column=0, row=1, sticky=(N, W, E, S))
    mainframe2['background'] = 'silver'
    
    mainframe3 = Frame(mainframe)
    mainframe3.grid(column=0, row=2, sticky=(N, W, E, S))
    mainframe3['background'] = 'silver'
    
    mainframe4 = Frame(mainframe)
    mainframe4.grid(column=0, row=3, sticky=(N, W, E, S))
    mainframe4['background'] = 'silver'
    
    mainframe5 = Frame(mainframe, bg="silver")
    mainframe5.grid(column=0, row=4, sticky=(N, W, E, S))
    
    mainframe6 = Frame(mainframe, bg="silver")
    mainframe6.grid(column=0, row=5, sticky=(N, W, E, S))
    
    mainframe7 = Frame(mainframe, bg="silver")
    mainframe7.grid(column=0, row=6, sticky=(N, W, E, S))

    mainframe8 = Frame(mainframe, bg="silver")
    mainframe8.grid(column=0, row=7, sticky=(N, W, E, S))

    mainframe9 = Frame(mainframe, bg="silver")
    mainframe9.grid(column=0, row=8, sticky=(N, W, E, S))

    mainframe10 = Frame(mainframe, bg="silver")
    mainframe10.grid(column=0, row=9, sticky=(N, W, E, S))

    mainframe11 = Frame(mainframe, bg="silver")
    mainframe11.grid(column=0, row=10, sticky=(N, W, E, S))

    mainframe12 = Frame(mainframe, bg="silver")
    mainframe12.grid(column=0, row=11, sticky=(N, W, E, S))

    mainframe13 = Frame(mainframe, bg="silver")
    mainframe13.grid(column=0, row=12, sticky=(N, W, E, S))
    

    mainframe14 = Frame(mainframe, bg="silver")
    mainframe14.grid(column=0, row=13, sticky=(N, W, E, S))

    mainframe15 = Frame(mainframe, bg="silver")
    mainframe15.grid(column=0, row=14, sticky=(N, W, E, S))
    
    ########################## program instructions ###########################################################
    programFont12 = font.Font(family='Courier New', size=12, weight='bold')
    programFont14 = font.Font(family='Courier New', size=14, weight='bold')   
    programFont16 = font.Font(family='Courier New', size=16, weight='bold')
    programFont18 = font.Font(family='Courier New', size=18, weight='bold')
    programFont20 = font.Font(family='Courier New', size=20, weight='bold')
    programFont24 = font.Font(family='Courier New', size=24, weight='bold')
    programFont32 = font.Font(family='Courier New', size=32, weight='bold')
    
    
            
    forward = Label(mainframe1, font= programFont14, text="forward", width = 10)
    forward.grid(row=0, column=0, sticky = (W))
    forward['anchor'] = 'w'
    forward['background'] = 'silver'
                             
    btn1 = Button(mainframe1, text="fd1", font= programFont14, bg = "light yellow", width = 5,command = stepout1)
    btn1.grid(column = 1, row =0, sticky = (N,W))        
    btn1['relief'] = 'raised'
    btn1['borderwidth'] = 5

    v_cem1 = Frame(mainframe1, bg= "silver", width = v_cement)
    v_cem1.grid(column=2, row= 0, sticky = (W))
    
    btn2 = Button(mainframe1, text="fd2", font= programFont14, bg = "light yellow", width = 5,command = stepout2)
    btn2.grid(column = 3, row =0, sticky = (N,W))
    btn2['relief'] = 'raised'
    btn2['borderwidth'] = 5

    v_cem2 = Frame(mainframe1, bg= "silver", width = v_cement)
    v_cem2.grid(column=4, row= 0, sticky = (W))
    
    btn3 = Button(mainframe1, text="fd3", font= programFont14, bg = "light yellow", width = 5,command = stepout3)
    btn3.grid(column = 5, row =0, sticky = (N,W))
    btn3['relief'] = 'raised'
    btn3['borderwidth'] = 5

    v_cem3 = Frame(mainframe1, bg= "silver", width = v_cement)
    v_cem3.grid(column=6, row= 0, sticky = (W)) 

    btn4 = Button(mainframe1, text="fd4", font= programFont14, bg = "light yellow", width = 5,command = stepout4)
    btn4.grid(column = 7, row =0, sticky = (N,W))
    btn4['relief'] = 'raised'
    btn4['borderwidth'] = 5

    v_cem4 = Frame(mainframe1, bg= "silver", width = v_cement)
    v_cem4.grid(column=8, row= 0, sticky = (W)) 

    btnchoose = Button(mainframe1, text="fd", font= programFont14, bg = "light yellow", width = 4,command = stepout_choose)
    btnchoose.grid(column = 9, row =0, sticky = (N,W))
    btnchoose['relief'] = 'raised'
    btnchoose['borderwidth'] = 5

    
    forward_entry = Entry(mainframe1, bd = 5, width = 2, textvariable = paces,  font= programFont14, bg = 'light yellow')
    forward_entry.grid(column=11, row=0, sticky= (N,W,E,S))
    #forward_entry.bind("<FocusIn>", forward_act)
    
    fillerm2= Frame(mainframe2, height=h_cement, bg= "silver")
    fillerm2.grid(column=0, row=0, sticky=(N, W, E))

    left_turn = Label(mainframe3, font= programFont14, text="left turn", width = 10)
    left_turn.grid(column=0, row=0, sticky=(W))
    left_turn['background'] = 'silver'
    left_turn['anchor'] = 'w'
    
    btnleft = Button(mainframe3, text="lt", font= programFont14, bg = "light yellow", width = 5, command = left)
    btnleft.grid(column=1, row=0, sticky= (N,W))
    btnleft['relief'] = 'raised'
    btnleft['borderwidth'] = 5    

    left_entry = Entry(mainframe3, bd = 5, width = 7, textvariable = degrees_left,  font= programFont14, bg = 'light yellow')
    left_entry.grid(column=2, row=0, sticky= (N,W,E,S))
    #left_entry.bind("<FocusIn>", left_act)
    
    left_blank = Label(mainframe3, bd = 5, width = 6,   font= programFont14, bg = 'silver')
    #left_blank.grid(column=2, row=0, sticky= (N,W,E,S))
    
    filler2a= Frame(mainframe3, width =5)
    filler2a.grid(column=3, row=0, sticky=(N, W, E, S))
    filler2a['background'] = 'silver'    

    pen_up = Button(mainframe3, text="penup", font= programFont14, bg = "light yellow", width = 5,  command = put_penup)
    pen_up.grid(column=4, row=0 , sticky= (N,W))
    pen_up['relief'] = 'raised'
    pen_up['borderwidth'] = 5
    pen_up['anchor'] = 'w'

    v_cem5 = Frame(mainframe3, bg= "silver", width = v_cement)
    v_cem5.grid(column=5, row= 0, sticky = (W)) 

    pen_down = Button(mainframe3, text="pendown", font= programFont14, bg = "light yellow", width = 7,  command = put_pendown)
    pen_down.grid(column=6, row=0 , sticky= (N,W))
    pen_down['relief'] = 'raised'
    pen_down['borderwidth'] = 5
    pen_down['anchor'] = 'w'

    v_cem6 = Frame(mainframe3, bg= "silver", width = v_cement)
    v_cem6.grid(column=7, row= 0, sticky = (W)) 

    hide = Button(mainframe3, text="hide", font= programFont14,  bg = "light yellow", width = 3, command=hide_arrow, padx= 10)
    hide.grid(column=8, row=0, sticky= (E))
    hide['relief'] = 'raised'
    hide['borderwidth'] = 5 

    

    fillerm4= Frame(mainframe4, height=h_cement, bg= "silver")
    fillerm4.grid(column=0, row=0, sticky=(N, W, E))
    
    right_turn = Label(mainframe5, font= programFont14, text="right turn", width = 10)
    right_turn.grid(column=0, row=0, sticky=(W))
    right_turn['background'] = 'silver'
    right_turn['anchor'] = 'w'

    btnright = Button(mainframe5, text="rt", font = programFont14,  bg = "light yellow", width = 5, command = right)
    btnright.grid(column=1, row=0, sticky= (N,W))
    btnright['relief'] = 'raised'
    btnright['borderwidth'] = 5

    right_blank = Label(mainframe5, bd = 5, width = 6,font= programFont14, bg = 'silver')
    right_blank.grid(column=2, row=0, sticky= (N,W,E,S))

    right_entry = Entry(mainframe5, bd = 5, width = 7, textvariable = degrees_right,  font= programFont14, bg = 'light yellow')
    right_entry.grid(column=2, row=0, sticky= (N,W,E,S))
    #right_entry.bind("<FocusIn>", left_act)

        
    
    filler2= Frame(mainframe5, width = 5)
    filler2.grid(column=3, row=0, sticky=(N, W, E, S))
    filler2['background'] = 'silver'
    
    
    delete = Button(mainframe5, text="delete", font= programFont14,  bg = "light blue", width = 6, command = delete_op )
    delete.grid(column=4, row=0, sticky= (E))
    delete['relief'] = 'raised'
    delete['borderwidth'] = 5

    v_cem7 = Frame(mainframe5, bg= "silver", width = v_cement)
    v_cem7.grid(column=5, row= 0, sticky = (W)) 

    clear = Button(mainframe5, text="clear", font= programFont14,  bg = "light blue", width = 3, command=full_delete, padx= 10)
    clear.grid(column=6, row=0, sticky= (E))
    clear['relief'] = 'raised'
    clear['borderwidth'] = 5

    v_cem8 = Frame(mainframe5, bg= "silver", width = v_cement)
    v_cem8.grid(column=7, row= 0, sticky = (W)) 

    newline = Button(mainframe5, text="newline", font= programFont14,  bg = "light blue", width = 5, command=new_line, padx= 10)
    newline.grid(column=8, row=0, sticky= (E))
    newline['relief'] = 'raised'
    newline['borderwidth'] = 5

    v_cem9 = Frame(mainframe5, bg= "silver", width = v_cement)
    v_cem9.grid(column=9, row= 0, sticky = (W)) 

    fillera50= Frame(mainframe5, height=h_cement, bg = "silver")
    fillera50.grid(column=0, row=1, sticky=(N, W, E))



   ################################### repeat control structure #############################################################
    
    
    repeat_btn= Button(mainframe6, text="repeat", width = 6, font = programFont16, command = setup_repeat)
    repeat_btn.grid(column=0, row=1, sticky=(W))
    repeat_btn['background'] = 'light yellow'
    repeat_btn['relief'] = 'raised'
    repeat_btn['borderwidth'] = 5
    

    filler25= Frame(mainframe6, width = 4)
    filler25.grid(column=1, row=1, sticky=(N, W, E, S))
    filler25['background'] = 'silver'
    
    
    times = StringVar()
    times.set('')
    tim = Entry(mainframe6,bd = 5, width = 2, textvariable = times,  font= programFont14, bg = 'light yellow')
    tim.grid(column=2, row=1, sticky= (E,W))
    tim.bind("<FocusIn>", act)
    

    filler3= Frame(mainframe6, width = 2)
    filler3.grid(column=3, row=1, sticky=(N, W,E,S))
    filler3['background'] = 'silver'

    bracketleft = Label(mainframe6, text='[', font= programFont32, bg = "silver", width = 1)
    bracketleft.grid(column=4, row=1, sticky= (N))

    
    brackets = Label(mainframe6, text=in_repeat_code,textvariable = in_repeat_code, font= programFont18,\
                     bg = "light yellow", width = 32)
    brackets.grid(column=5, row=1, sticky= (W,E))
    brackets.configure(font=programFont12)
    in_repeat_code.set('***')

    bracketright = Label(mainframe6, text=']', font= programFont32, bg = "silver", width = 1)
    bracketright.grid(column=6, row=1, sticky= (N,W))

    filler4= Frame(mainframe6, width = 2)
    filler4.grid(column=7, row=1, sticky=(N, W, E, S))
    filler4['background'] = 'silver'

    gobtn = Button(mainframe6, text="do it", font= programFont16, bg = "light yellow",  command = execute_repeat, width = 5)
    gobtn.grid(column=8, row=1, sticky= (E,W))
    gobtn['relief'] = 'raised'
    gobtn['borderwidth'] = 5


     ######################################    colour tabs    ########################################################
    
    
    colourlab = Label(mainframe7, font= programFont14, text="colour", width = 10)
    #colourlab.grid(column=0, row=0, sticky=(N,W,E,S))
    colourlab['background'] = 'silver'
    colourlab['anchor'] = 'w'

    cbtn1 = Button(mainframe7, text="red", font= programFont14, bg = "red", fg = "white", width = 5,command = red)
    #cbtn1.grid(column = 1, row =0, sticky = (N,W))        
    cbtn1['relief'] = 'raised'
    cbtn1['borderwidth'] = 5

    v_cem10 = Frame(mainframe7, bg= "silver", width = v_cement)
    #v_cem10.grid(column=2, row= 0, sticky = (W)) 

    
    cbtn2 = Button(mainframe7, text="blue", font= programFont14, bg = "blue",fg = "white", width = 5,command = blue)
    #cbtn2.grid(column = 3, row =0, sticky = (N,E,W,S))
    cbtn2['relief'] = 'raised'

    
    v_cem11 = Frame(mainframe7, bg= "silver", width = v_cement)
    #v_cem11.grid(column=4, row= 0, sticky = (W)) 

    
    cbtn3 = Button(mainframe7, text="green", font= programFont14, bg = "green",fg = "white", width = 6,command = green)
    #cbtn3.grid(column = 7, row =0, sticky = (N,W))
    cbtn3['relief'] = 'raised'
    cbtn3['borderwidth'] = 5

    v_cem12 = Frame(mainframe7, bg= "silver", width = v_cement)
    #v_cem12.grid(column=8, row= 0, sticky = (W)) 

    cbtn4 = Button(mainframe7, text="black", font= programFont14, bg = "black",fg = "white", width = 6,command = black)
    #cbtn4.grid(column = 9, row =0, sticky = (N,W))
    cbtn4['relief'] = 'raised'
    cbtn4['borderwidth'] = 5

    v_cem13 = Frame(mainframe7, bg= "silver", width = v_cement)
    #v_cem13.grid(column=10, row= 0, sticky = (W)) 

    cbtn5 = Button(mainframe7, text="gold", font= programFont14, bg = "gold",fg = "black", width = 6,command = gold)
    #cbtn5.grid(column = 11, row =0, sticky = (N,W))
    cbtn5['relief'] = 'raised'
    cbtn5['borderwidth'] = 5

    v_cem14 = Frame(mainframe7, bg= "silver", width = v_cement)
    #v_cem14.grid(column=12, row= 0, sticky = (W)) 
    
    cbtn6 = Button(mainframe7, text="white", font= programFont14, bg = "white",fg = "black", width = 6,command = white)
    #cbtn6.grid(column = 13, row =0, sticky = (N,W))
    cbtn6['relief'] = 'raised'
    cbtn6['borderwidth'] = 5





        ######################################    fetchT1 #########################################################


    #pad2 = Frame(pad_box, padx=5, pady =0, bg='silver')
    #pad2.grid(column=0, row=3, sticky=(N, W, E,S))
    #pad2['relief'] = 'raised'
    #pad2['borderwidth'] = 8
    #pad2['background'] = 'silver'
    #pad2['padx'] = 3
    #pad2['pady'] = 3

    
    #heading2 = Label(pad2, font= italicFont14, text="     instructions (user-built)", width = 25)
    #heading2.grid(row=0, column=0, sticky = (N,E,S,W))
    #heading2['anchor'] = 'w'
    #heading2['background'] = 'silver'

    about_turn = Label(mainframe8, font= programFont14, text="about turn", width = 10)
    #about_turn.grid(column=0, row=0, sticky=(W,E))
    about_turn['background'] = 'silver'
    about_turn['anchor'] = 'w'

    about_turn = Button(mainframe8, text="at", font= programFont14,  bg = "light green", width = 5, command = aboutturn )
    #about_turn.grid(column=1, row=0, sticky= (W))
    about_turn['relief'] = 'raised'
    about_turn['borderwidth'] = 5

    diagbtn = Button(mainframe8, text="diag", font= programFont14,  bg = "light green", width = 5, command = diagonal )
    #diagbtn.grid(column=2, row=0, sticky= (W))
    diagbtn['relief'] = 'raised'
    diagbtn['borderwidth'] = 5
    
    arcbtn = Button(mainframe8, text="arc", font= programFont14,  bg = "light green", width = 5, command = at )
    #arcbtn.grid(column=3, row=0, sticky= (W))
    arcbtn['relief'] = 'raised'
    arcbtn['borderwidth'] = 5 



    
    ufetch =Label(mainframe9, font= programFont14, text="fetch", width = 10)
    ufetch.grid(row=0, column=0, sticky = (W))
    ufetch['anchor'] = 'w'
    ufetch['background'] = 'silver'
                                            
    febtn1 = Button(mainframe9, text="fe1", font= programFont14, bg = "light green", width = 5,command = fetchout1)
    febtn1.grid(column = 1, row =0, sticky = (N,W))        
    febtn1['relief'] = 'raised'
    febtn1['borderwidth'] = 5

    v_cem20 = Frame(mainframe9, bg= "silver", width = v_cement)
    v_cem20.grid(column=2, row= 0, sticky = (W))
    
    febtn2 = Button(mainframe9, text="fe2", font= programFont14, bg = "light green", width = 5,command = fetchout2)
    febtn2.grid(column = 3, row =0, sticky = (N,W))
    febtn2['relief'] = 'raised'
    febtn2['borderwidth'] = 5

    v_cem21 = Frame(mainframe9, bg= "silver", width = v_cement)
    v_cem21.grid(column=4, row= 0, sticky = (W))
    
    febtn3 = Button(mainframe9, text="fe3", font= programFont14, bg = "light green", width = 5,command = fetchout3)
    febtn3.grid(column = 5, row =0, sticky = (N,W))
    febtn3['relief'] = 'raised'
    febtn3['borderwidth'] = 5

    v_cem22 = Frame(mainframe9, bg= "silver", width = v_cement)
    v_cem22.grid(column=6, row= 0, sticky = (W))

    febtn4 = Button(mainframe9, text="fe4", font= programFont14, bg = "light green", width = 5,command = fetchout4)
    febtn4.grid(column = 7, row =0, sticky = (N,W))
    febtn4['relief'] = 'raised'
    febtn4['borderwidth'] = 5

    v_cem23 = Frame(mainframe9, bg= "silver", width = v_cement)
    v_cem23.grid(column=8, row= 0, sticky = (W)) 

    
    #febtn5 = Button(user_mainframe, text="fe5", font= programFont14, bg = "light green", width = 5,command = stepout4)
    #febtn5.grid(column = 9, row = 1, sticky = (N,W))
    #febtn5['relief'] = 'raised'
    #febtn5['borderwidth'] = 5

    #v_cem24 = Frame(user_mainframe, bg= "silver", width = v_cement)
    #v_cem24.grid(column=10, row= 1, sticky = (W))
    
    
    fechoose = Button(mainframe9, text="fe", font= programFont14, bg = "light green", width = 3,command = fetchout_choose)
    fechoose.grid(column = 9, row = 0, sticky = (N,W))
    fechoose['relief'] = 'raised'
    fechoose['borderwidth'] = 5

    
    fetch_entry = Entry(mainframe9, bd = 5, width = 2, textvariable = fpaces, \
                        font= programFont14, bg = 'light green')
    fetch_entry.grid(column=10, row= 0, sticky= (N,W,S))
    #fetch_entry.bind("<FocusIn>", forward_act)

    


    #fillerm20= Frame(user_mainframe, height=h_cement, bg= "silver")
    #fillerm20.grid(column=0, row=2, sticky=(N, W, E))




    
    
    fillerm12= Frame(mainframe9, height= 3*h_cement, bg= "silver")
    #fillerm12.grid(column= 11, row=1, sticky=(N, W, E))
  
    #label_instruction.config(text="Use the toolbox set out below.",bg = "yellow")
    #label_instruction.grid(column=0, row=0, sticky=(N,W))

    #fillerm2001= Frame(pad2, height=3*h_cement, bg= "silver")
    #fillerm2001.grid(column=0, row=1, sticky=(N, W, E)) 
    
#####################################rectangle #################################    

    
    urect =Label(mainframe10, font= programFont14, text="rectangle", width = 10)
    urect.grid(row=0, column=0, sticky = (W))
    urect['anchor'] = 'w'
    urect['background'] = 'silver'
                                            
    rebtn1 = Button(mainframe10, text="re1", font= programFont14, bg = "light green", width = 5,command = rectout1)
    rebtn1.grid(column = 1, row =0, sticky = (N,W))        
    rebtn1['relief'] = 'raised'
    rebtn1['borderwidth'] = 5

    v_cem220 = Frame(mainframe10, bg= "silver", width = v_cement)
    v_cem220.grid(column=2, row= 0, sticky = (W))
    
    rebtn2 = Button(mainframe10, text="re2", font= programFont14, bg = "light green", width = 5,command = rectout2)
    rebtn2.grid(column = 3, row =0, sticky = (N,W))
    rebtn2['relief'] = 'raised'
    rebtn2['borderwidth'] = 5

    v_cem221 = Frame(mainframe10, bg= "silver", width = v_cement)
    v_cem221.grid(column=4, row= 0, sticky = (W))
    
    rebtn3 = Button(mainframe10, text="re3", font= programFont14, bg = "light green", width = 5,command = rectout3)
    rebtn3.grid(column = 5, row =0, sticky = (N,W))
    rebtn3['relief'] = 'raised'
    rebtn3['borderwidth'] = 5

    v_cem222 = Frame(mainframe10, bg= "silver", width = v_cement)
    v_cem222.grid(column=6, row= 0, sticky = (W))

    rebtn4 = Button(mainframe10, text="re4", font= programFont14, bg = "light green", width = 5,command = rectout4)
    rebtn4.grid(column = 7, row =0, sticky = (N,W))
    rebtn4['relief'] = 'raised'
    rebtn4['borderwidth'] = 5

    v_cem223 = Frame(mainframe10, bg= "silver", width = v_cement)
    v_cem223.grid(column=8, row= 0, sticky = (W)) 

    
    #febtn5 = Button(user_mainframe, text="fe5", font= programFont14, bg = "light green", width = 5,command = stepout4)
    #febtn5.grid(column = 9, row = 1, sticky = (N,W))
    #febtn5['relief'] = 'raised'
    #febtn5['borderwidth'] = 5

    #v_cem24 = Frame(user_mainframe, bg= "silver", width = v_cement)
    #v_cem24.grid(column=10, row= 1, sticky = (W))
    
    
    rechoose = Button(mainframe10, text="re", font= programFont14, bg = "light green", width = 3,command = rectout_choose)
    rechoose.grid(column = 9, row = 0, sticky = (N,W))
    rechoose['relief'] = 'raised'
    rechoose['borderwidth'] = 5

    
    retch_entry = Entry(mainframe10, bd = 5, width = 2, textvariable = rpaces, \
                        font= programFont14, bg = 'light green')
    retch_entry.grid(column=10, row= 0, sticky= (N,W,S))

   

    
    #fetch_entry.bind("<FocusIn>", forward_act)


    #fillerm20= Frame(user_mainframe, height=h_cement, bg= "silver")
    #fillerm20.grid(column=0, row=2, sticky=(N, W, E))




    
    
    fillerm12= Frame(mainframe9, height= 3*h_cement, bg= "silver")
    #fillerm12.grid(column= 11, row=1, sticky=(N, W, E))
  
    #label_instruction.config(text="Use the toolbox set out below.",bg = "yellow")
    #label_instruction.grid(column=0, row=0, sticky=(N,W))

    #fillerm2001= Frame(pad2, height=3*h_cement, bg= "silver")
    #fillerm2001.grid(column=0, row=1, sticky=(N, W, E))

    
#####################################rectangle #################################    

    
    usq =Label(mainframe11, font= programFont14, text="square", width = 10)
    usq.grid(row=0, column=0, sticky = (W))
    usq['anchor'] = 'w'
    usq['background'] = 'silver'
                                            
    sqbtn1 = Button(mainframe11, text="sq1", font= programFont14, bg = "light green", width = 5,\
                    command = sqout1)
    sqbtn1.grid(column = 1, row =0, sticky = (N,W))        
    sqbtn1['relief'] = 'raised'
    sqbtn1['borderwidth'] = 5

    v_cem320 = Frame(mainframe11, bg= "silver", width = v_cement)
    v_cem320.grid(column=2, row= 0, sticky = (W))
    
    sqbtn2 = Button(mainframe11, text="sq2", font= programFont14, bg = "light green", width = 5,command = sqout2)
    sqbtn2.grid(column = 3, row =0, sticky = (N,W))
    sqbtn2['relief'] = 'raised'
    sqbtn2['borderwidth'] = 5

    v_cem321 = Frame(mainframe11, bg= "silver", width = v_cement)
    v_cem321.grid(column=4, row= 0, sticky = (W))
    
    sqbtn3 = Button(mainframe11, text="sq3", font= programFont14, bg = "light green", width = 5,command = sqout3)
    sqbtn3.grid(column = 5, row =0, sticky = (N,W))
    sqbtn3['relief'] = 'raised'
    sqbtn3['borderwidth'] = 5

    v_cem322 = Frame(mainframe11, bg= "silver", width = v_cement)
    v_cem322.grid(column=6, row= 0, sticky = (W))

    sqbtn4 = Button(mainframe11, text="sq4", font= programFont14, bg = "light green", width = 5,command = sqout4)
    sqbtn4.grid(column = 7, row =0, sticky = (N,W))
    sqbtn4['relief'] = 'raised'
    sqbtn4['borderwidth'] = 5

    v_cem323 = Frame(mainframe11, bg= "silver", width = v_cement)
    v_cem323.grid(column=8, row= 0, sticky = (W))

    sqchoose = Button(mainframe11, text="sq", font= programFont14, bg = "light green", width = 3,command = sqout_choose)
    sqchoose.grid(column = 9, row = 0, sticky = (N,W))
    sqchoose['relief'] = 'raised'
    sqchoose['borderwidth'] = 5


    sqtch_entry = Entry(mainframe11, bd = 5, width = 2, textvariable = sqpaces, \
                    font= programFont14, bg = 'light green')
    sqtch_entry.grid(column=10, row= 0, sticky= (N,W,S))
    '''
    sqchoose = Button(mainframe12, text="sq", font= programFont14, bg = "light green", width = 3,command = sqout_choose)
    sqchoose.grid(column = 9, row = 0, sticky = (N,W))
    sqchoose['relief'] = 'raised'
    sqchoose['borderwidth'] = 5

    sqtch_entry = Entry(mainframe12, bd = 5, width = 2, textvariable = sqpaces, \
                        font= programFont14, bg = 'light green')
    sqtch_entry.grid(column=10, row= 0, sticky= (N,W,S))
    #fetch_entry.bind("<FocusIn>", forward_act)
    '''
    v_cem323 = Frame(mainframe12, bg= "silver", width = v_cement)
    v_cem323.grid(column=11, row= 0, sticky = (W)) 


    #pybtn = Button(mainframe11, text="python", font= programFont14, bg = "light blue", width = 6,\
                   #command = python_prog)
    #pybtn.grid(column = 11, row = 0, sticky = (N,W))
    #pybtn['relief'] = 'raised'
    #pybtn['borderwidth'] = 5

    
    #febtn5 = Button(user_mainframe, text="fe5", font= programFont14, bg = "light green", width = 5,command = stepout4)
    #febtn5.grid(column = 9, row = 1, sticky = (N,W))
    #febtn5['relief'] = 'raised'
    #febtn5['borderwidth'] = 5

    #v_cem24 = Frame(user_mainframe, bg= "silver", width = v_cement)
    #v_cem24.grid(column=10, row= 1, sticky = (W))
    
    

    col = "light yellow"
    filler502= Frame(frame4, height=200, bg=col)
    filler502.grid(column=0, row=3, sticky=(N, W, E))




    
    
    #fillerm12= Frame(mainframe9, height= 3*h_cement, bg= "silver")
    #fillerm12.grid(column= 11, row=1, sticky=(N, W, E))
  
    #label_instruction.config(text="Use the toolbox set out below.",bg = "yellow")
    #label_instruction.grid(column=0, row=0, sticky=(N,W))

    #fillerm2001= Frame(pad2, height=3*h_cement, bg= "silver")
    #fillerm2001.grid(column=0, row=1, sticky=(N, W, E)) 
    

   




    ##############################################
    allow=True    
    #full_delete()
    allow=False
    ##############################################
    
    print('exiting full_delete(), cool')
    allow=True

    
    

############################################################################################################


def gridset():
    global p
    
    if p==100:
        my.pensize(2)
        my.speed(8)            
    elif p==75:
        my.pensize(2)
        my.speed(8)
    elif p==50:
        my.pensize(2)
        my.speed(0)
    elif p==25:
        my.pensize(2)
        my.speed(0)
    elif p==12:    
        my.pensize(2)
        my.speed(0)
    elif p==6:
        my.pensize(2)
        my.speed(0)
    else:
        print("hangfire in gridset, p?", p)
    

####################################################  re  fe sq ############################################ 


def re(pixels):
    global p
    print('in re(rp)')
    for mm in range(2):
        my.fd(pixels)
        my.lt(90)
        my.fd(p)
        my.lt(90)
   
def rectout1():
    rectangle_milly(1)
    
def rectout2():
    rectangle_milly(2)

def rectout3():
    rectangle_milly(3)

def rectout4():
    rectangle_milly(4)

def rectout_choose():# see stepout_choose
    '''caters for a variable number of paces forward with return'''
    
    global allow
    global top
    global gop
    global gou
    global gg
    global ok_repeat
    global in_repeat_code
    global brackets
    global steps
    global paces
    global rpaces

    if allow:
        allow=False
        print('in fetchout_choose()')
        ddd = rpaces.get()        
        if ddd.isdigit():###&&&&& test  value entered                
            steps = int(ddd)
            pix = steps*p
            if ok_repeat == True:
                print("ok_repeat in rectout_choose")
                gg = gg + 1
                gop.append('\n    re(' + str(pix) + ')')
                #gop.append('\n    re(steps*p)')
                gou.append('re' + ddd + ' ')
                
                sss=''.join(gou)            
                in_repeat_code.set(sss)
            else:
                
                top = top+1
                record.append("re" + str(steps) + ' ')# for rectangle
                recordmypy.append('\nre(' + str(pix) + ')')
                #recordmypy.append('\nre(steps*p)')
                print('in rectout_choose, not in repeat, steps is', steps)
                print("pen_is_down is", pen_is_down)
                if pen_is_down:
                    my.down()
                else:
                    my.up()
                    
                my.st()
                gridset()  

                re(pix)# this is the screen action depending on the grid size.
                
                #####################    
                allow=True        
                ecode.set(''.join(record))#displays via ecode in program_box
                allow=False
                ###################### 
                
                
                
        else:
            # deal with no digit
            print('no digit in re[]')
    
        allow = True
    else:
        print('in rectout_choose(), spin')
        
    
def rectangle_milly(rp):
    ''' use rp as parameter because p is a global var! '''
    global allow
    global top
    global gg    
    global pen_is_down
    global p
    global steps
    global paces
    global fpaces
    global rpaces
    if allow:
        allow= False
        print('enter rectangle_milly()')
        print("pen_is_down is", pen_is_down)
        if pen_is_down:
            my.down()
        else:
            my.up()

        my.st()
        gridset()
        steps=rp
        pix=steps*p # pixel equivalent on grid
        print('rectangle_milly, rp is', rp, 'steps is', steps, 'p is', p)

        if ok_repeat == True:
            print("ok in repeat rectangle_milly")

            #####################
            allow=True
            check_box() #checks the repeat box value
            allow=False
            #####################
            
                        
                        
            gg  = gg + 1
            gop.append('\n    re(' + str(pix) + ')')            
            gou.append('re' + str(steps) +' ')
            
            print("gop is", gop)
            print("gou is", gou)
            
            sss=''.join(gou)            
            in_repeat_code.set(sss)            
       
            
        else:                        
            top = top+1            
            print("in rectangle_milly not repeat")

            re(pix) #action on the grid
            
            record.append('re' + str(steps) + ' ')# for records
            recordmypy.append('\nre(' + str(pix) + ')')            
                
            #####################    
            allow=True        
            ecode.set(''.join(record))#displays via ecode in program_box
            allow=False
            ######################          
                
        allow=True
    else:
        print('in fetch_milly, spin, wait for another interrupt')




##############################################################################################################




def fe(rpaces):
    for mm in range(2):
        my.fd(rpaces)
        my.lt(90)
        my.lt(90)
   
    
def fetchout1():
    fetch_milly(1)
    
def fetchout2():
    fetch_milly(2)

def fetchout3():
    fetch_milly(3)

def fetchout4():
    fetch_milly(4)

def fetchout_choose():# see stepout_choose
    '''caters for a variable number of paces forward with return'''
    
    global allow
    global top
    global gop
    global gou
    global gg
    global ok_repeat
    global in_repeat_code
    global brackets
    global steps
    global paces

    if allow:
        allow=False
        print('in fetchout_choose()')
        ddd = fpaces.get()        
        if ddd.isdigit():###&&&&& test  value entered                
            steps = int(ddd)
            pix = steps*p
            if ok_repeat == True:
                print("ok_repeat in fetchout_choose")
                gg  = gg + 1
                gop.append('\n    fe(' + str(pix) + ')')
                #gg  = gg + 1 gop.append('\n    fetch(steps*p)')
                gou.append('fe' + ddd + ' ')
                sss=''.join(gou)            
                in_repeat_code.set(sss)
            else:# not in repeat, in fetchout_choose()
                print("not in repeat, in fetchout_choose()")
                top = top+1
                record.append("fe" + str(steps) + ' ')# for forward
                recordmypy.append('\nfe(' + str(pix) + ')')
                
                print('in fetchout_choose, not in repeat, steps is', steps)
                print("pen_is_down is", pen_is_down)
                if pen_is_down:
                    my.down()
                else:
                    my.up()
                    
                my.st()
                gridset()  

                fe(pix)# this is the screen action depending on the grid size.
                
                #####################    
                allow=True        
                ecode.set(''.join(record))#displays via ecode in program_box
                allow=False
                ######################                
        else:
            # deal with no digit
            print('no digit in fe[]')
    
        allow = True
    else:
        print('in fetchout_choose(), spin')
        
    

def fetch_milly(rp):
    ''' use rp as parameter because p is a global var! '''
    global allow
    global top
    global gg    
    global pen_is_down
    global p
    global steps
    global paces
    global fpaces
    if allow:
        allow= False
        print('enter fetch_milly()')
        print("pen_is_down is", pen_is_down)
        if pen_is_down:
            my.down()
        else:
            my.up()

        my.st()
        gridset()
        steps=rp
        pix=steps*p # pixel equivalent on grid
        print('rp is', rp, 'steps is', steps, 'p is', p)

        if ok_repeat == True:
            print("ok in repeat fetch_milly")

            #####################
            allow=True
            check_box() #checks the repeat box value
            allow=False
            #####################
            
                        
            gg = gg + 1            
            gop.append('\n    fe(' + str(pix) + ')')            
            gou.append('fe' + str(steps) +' ')
            
            print("gop is", gop)
            print("gou is", gou)
            
            sss=''.join(gou)            
            in_repeat_code.set(sss)            
       
            
        else:
                        
            top = top+1      
            
            print("in drive_milly not repeat")
            fe(pix) #action on the grid
            
            record.append('fe' + str(steps) + ' ')# for records
            recordmypy.append('\nfe(' + str(pix) + ')')
                             
            
                
            #####################    
            allow=True        
            ecode.set(''.join(record))#displays via ecode in program_box
            allow=False
            ######################
            
            
                
        allow=True
    else:
        print('in fetch_milly, spin, wait for another interrupt')



    

def square(rpaces):
    for mm in range(4):
        my.fd(rpaces)
        my.lt(90)
        

def sqout1():
    global allow
    global gop
    global gou
    global gg
    global ok_repeat
    global in_repeat_code
    global brackets

    if allow:
        allow= False
    
        if ok_repeat == True:

            #####################
            allow=True
            check_box() # checks out the repeat box value
            allow=False
            #####################
            
            print("ok sq1")
            gg = gg + 1
            gop.append('\n    square(p)')
            print("gop is", gop)
            gou.append('sq1 ')
            
            sss=''.join(gou)            
            in_repeat_code.set(sss)
            
        else:
            allow= True
            square_milly(1)
            print("1 rpace square")
        allow = True
    else:
        print('in sqout1(), spin')

    
    

def sqout2():
    global allow
    global gop
    global gou
    global gg
    global ok_repeat
    global in_repeat_code
    global brackets

    if allow:
        allow= False
    
        if ok_repeat == True:

            #####################
            allow=True
            check_box() # checks out the repeat box value
            allow=False
            #####################
            
            print("ok repeat, sq2")
            gg = gg + 1
            gop.append('\n    square(2*p)')
            print("gop is", gop)
            gou.append('sq2 ')
            
            sss=''.join(gou)            
            in_repeat_code.set(sss)
            
        else:
            allow= True
            square_milly(2)
            print("2 paces square")
        allow = True
    else:
        print('in sqout2(), spin')
    

def sqout3():
    global allow
    global gop
    global gou
    global gg
    global ok_repeat
    global in_repeat_code
    global brackets

    if allow:
        allow= False
    
        if ok_repeat == True:

            #####################
            allow=True
            check_box() # checks out the repeat box value
            allow=False
            #####################
            
            print("ok repeat, sq3")
            gg = gg + 1
            gop.append('\n    square(3*p)')
            print("gop is", gop)
            gou.append('sq3 ')
            
            sss=''.join(gou)            
            in_repeat_code.set(sss)
            
        else:
            allow= True
            square_milly(3)
            print("3 paces square")
        allow = True
    else:
        print('in sqout3(), spin')




def sqout4():

    global allow
    global gop
    global gou
    global gg
    global ok_repeat
    global in_repeat_code
    global brackets

    if allow:
        allow= False
    
        if ok_repeat == True:

            #####################
            allow=True
            check_box() # checks out the repeat box value
            allow=False
            #####################
            
            print("ok repeat, sq4")
            gg = gg + 1
            gop.append('\n    square(4*p)')
            print("gop is", gop)
            gou.append('sq4 ')
            
            sss=''.join(gou)            
            in_repeat_code.set(sss)
            
        else:
            allow= True
            square_milly(4)
            print("2 paces square")
        allow = True
    else:
        print('in sqout2(), spin')
    

def sqout_choose():# see stepout_choose
    '''caters for a variable number of paces forward in a square with return'''
    #&&&&&&&&&&&&&&&&&&&&
    global allow
    global top
    global gop
    global gou
    global gg
    global ok_repeat
    global in_repeat_code
    global brackets
    global steps
    global paces

    if allow:
        allow=False
        print('in sqout_choose()')
        ddd = sqpaces.get()        
        if ddd.isdigit():###&&&&& test  value entered                
            steps = int(ddd)
            if ok_repeat == True:
                print("ok_repeat in sqout_choose")
                gg = gg + 1
                gop.append('\n    square(' + ddd + '*p)')
                gou.append('sq' + ddd + ' ')
                
                sss=''.join(gou)            
                in_repeat_code.set(sss)
            else:
                
                top = top+1
                record.append("sq" + str(steps) + ' ')# for square
                recordmypy.append('\nsquare(steps*p)')

                print('record is', record)
                print('recordmypy is', recordmypy)
                
                print('in sqout_choose, not in repeat, steps is', steps)
                print("pen_is_down is", pen_is_down)
                if pen_is_down:
                    my.down()
                else:
                    my.up()
                    
                my.st()
                gridset()   

                square(steps*p)# this is the screen action depending on the grid size.
                
                #####################    
                allow=True        
                ecode.set(''.join(record))#displays via ecode in program_box
                allow=False
                ###################### 
                
                
                
        else:
            # deal with no digit
            print('no digit in sq[]')
    
        allow = True
    else:
        print('in sqout_choose(), spin')
        

def square_milly(rp):
    ''' use rp as parameter because p is a global var! '''
    global allow
    global top
    global gg    
    global pen_is_down
    global p
    global steps
    global paces
    global fpaces
    global sqpaces
    if allow:
        allow= False
        print('enter square_milly()')
        print("pen_is_down is", pen_is_down)
        if pen_is_down:
            my.down()
        else:
            my.up()

        my.st()
        gridset()# set speed and penwidth for different grids      

    
        if ok_repeat == True:

            #####################
            allow=True
            check_box() # checks out the repeat box value
            allow=False
            #####################

            
            print("in square_milly, rp is", rp)
            steps=rp
            print("ok sq" + str(steps))
            gg = gg + 1
            gop.append('\n    square(' + ddd + '*p)')
            #gop.append('\n    square(steps*p)')
            print("gop is", gop)
            gou.append('sq' + str(steps) + ' ')
            
            sss=''.join(gou)            
            in_repeat_code.set(sss)
            
        else:
            allow= True            
            top = top+1        
            if rp == 1:
                print("in drive_milly sq1")
                square(1*p)
                
                record.append("sq1 ")# for forward
                recordmypy.append('\nsquare(p)')
                
                print('record is', record)
                print('recordmypy is', recordmypy)                 
                allow=True
            elif rp ==2:
                square(2*p)
                
                record.append("sq2 ")# for forward
                recordmypy.append('\nsquare(2*p)')

                print('record is', record)
                print('recordmypy is', recordmypy)
                allow=True
            elif rp == 3:
                square(3*p)
                
                record.append("sq3 ")# for forward
                recordmypy.append('\nsquare(3*p)') 
                allow=True
            elif  rp == 4:
                square(4*p)
                
                record.append("sq4 ")# for forward
                recordmypy.append('\nsquare(4*p)') 
                allow=True
            
            else:                
                allow=True
                
            #####################    
            allow=True        
            ecode.set(''.join(record))#displays via ecode in program_box
            allow=False
            ######################
            
            
                
        allow=True
    else:
        print('in y, spin, wait for another interrupt')




 
def stepout_choose():
    '''caters for a variable number of paces forward'''
    #&&&&&&&&&&&&&&&&&&&&
    global allow
    global top
    global gop
    global gou
    global gg
    global ok_repeat
    global in_repeat_code
    global brackets
    global steps
    global paces

    if allow:
        allow=False
        print('in stepout_choose()')
        ddd = paces.get()        
        if ddd.isdigit():###&&&&& test  value entered                
            steps = int(ddd)
            pix=steps*p # pixel equivalent on grid
            
            if ok_repeat == True:
                print("ok_repeat in stepout_choose")         
                gg = gg + 1            
                gop.append('\n    my.fd(' + str(pix) + ')')            
                gou.append('fd' + str(steps) + ' ')
                print("gop is", gop)
                print("gou is", gou)
                
                sss=''.join(gou)            
                in_repeat_code.set(sss)
                
            else:
                
                top = top+1
                record.append("fd" + str(steps) + ' ')# for forward                
                recordmypy.append('\nmy.fd(' + str(pix) + ')')

                print('record is', record)
                print('recordmypy is', recordmypy)
                
                print('in stepout_choose, not in repeat, steps is', steps)
                print("pen_is_down is", pen_is_down)
                if pen_is_down:
                    my.down()
                else:
                    my.up()
                    
                my.st()
                gridset()   

                my.fd(pix)# this is the screen action depending on the grid size.
                
                #####################    
                allow=True        
                ecode.set(''.join(record))#displays via ecode in program_box
                allow=False
                ###################### 
                
                
                
        else:
            # deal with no digit
            print('no digit in fd[]')
    
        allow = True
    else:
        print('in stepout_choose(), spin')
        
    
def diag():
    global allow
    global p
    
    my.lt(45)
    my.fd(math.sqrt(2)*p)
    my.rt(45)

def at():
    print('in at()')
    my.lt(90)
    my.lt(90)


      
def drive_milly(fn = None):
    global allow
    global top
    
    global pen_is_down
    global p
    global steps
    global paces
    global uplshow
    #allow=True ##&&&&&&&
    print('enter drive_milly')
    
    if allow == True:
        allow=False
        print("pen_is_down is", pen_is_down)
        if pen_is_down:
            my.down()
        else:
            my.up()

        my.st()
        gridset()     

        top = top+1        
        if fn == "Up" or fn=='1':
            print("in drive_milly fd1")

            steps=1
            pix=steps*p # pixel equivalent on grid
            # update record (upl), recordmypy (exec) recordpy (for python display)
            record.append("fd1 ")# for forward 1
            recordmypy.append('\nmy.fd(' + str(pix) + ')')
            recordpy.append('\nfd(' + str(pix) + ')')
            print("record is", record)           
            my.fd(pix)#on-screen action
                             
            allow=True
        elif fn == "d" or fn=='2':
            steps=2
            pix=steps*p # pixel equivalent on grid
            # update record (upl), recordmypy (exec) recordpy (for python display)
            record.append("fd2 ")# for forward 2
            recordmypy.append('\nmy.fd(' + str(pix) + ')')
            recordpy.append('\nfd(' + str(pix) + ')')
                       
            my.fd(pix)#on-screen action        
           
            allow=True
        elif fn == "t" or fn=='3':
            steps=3
            pix=steps*p # pixel equivalent on grid
            # update record (upl), recordmypy (exec) recordpy (for python display)
            record.append("fd3 ")# for forward 3
            recordmypy.append('\nmy.fd(' + str(pix) + ')')
            recordpy.append('\nfd(' + str(pix) + ')')
                       
            my.fd(pix)#on-screen action
            
            allow=True
        elif  fn=='4':
            steps=4
            pix=steps*p # pixel equivalent on grid
            # update record (upl), recordmypy (exec) recordpy (for python display)
            record.append("fd4 ")# for forward 4
            recordmypy.append('\nmy.fd(' + str(pix) + ')')
            recordpy.append('\nfd(' + str(pix) + ')')
                       
            my.fd(pix)#on-screen action
            
            allow=True
        
        elif fn=='diag':
            diag()
            record.append("diag ")# for forward
            recordmypy.append('\ndiag()')
            allow=True

        elif fn=='at':
            print(" in fn=='at'")
            at()
            record.append("at ")# for about turn
            recordmypy.append('\nat()')           
            allow = True # let other events in now
            
        else: # alternative is fd()
            allow=True
        if uplshow:    
            #####################    
            allow=True        
            ecode.set(''.join(record))#displays via ecode in program_box
            allow=False
            ######################
            print('record is', record)
            print('recordmypy is', recordmypy)
            print('recordpy is', recordpy)
        else:
            ecode.set(''.join(record))
                           
        allow=True
    else:
        print('in drive_milly, spin, wait for another interrupt')

def single():
    # move 1 pace forward
    drive_milly("Up")

def double():
    # move 2 paces forward
    drive_milly("d")

def treble():
    # move 5 paces forward
    drive_milly("t")      

def left():
    global allow
    global top # index for record
    global gop
    global gou
    global gg
    global ok_repeat         
    global fix_angle
    global sss
    allow=True ###&&&&&& sort

    if allow:
        allow=False
        print('entering left()')
        
            

        
        angle = degrees_left.get()#&&& test value range/validity
        print('angle is', angle)
        x = int(eval(angle))
        fix_angle = x
        print('fix_angle is', fix_angle, 'angle is', angle )
        if fix_angle is angle:
            print('yes')
        else:
            print('no')

###################################### in left() inside repeat  ####################################################
    
        if ok_repeat == True:#&&& finish

             
            
            print("in left(), and in repeat...")
            if fix_angle == 90:
                gg = gg + 1
                gop.append('\n    my.lt(90)')
                gou.append('lt ')
            else:
                gg = gg + 1
                gop.append('\n    my.lt(' + angle + ')')
                gou.append('lt(' + angle + ')')
                
                        
            print("in left(), gop is ",gop, "gou is", gou) 
            sss=''.join(gou)            
            in_repeat_code.set(sss)

        else:# in left() not in repeat
            
            my.st()                
            my.left(fix_angle)               
            top = top+1
            if fix_angle == 90:
                record.append('lt ')# for right turn
                recordmypy.append('\nmy.lt(' + angle + ')')
            else:
                record.append('lt(' + angle + ')')# for left turn
                recordmypy.append('\nmy.lt(' + angle + ')')
                
            ecode.set(''.join(record))                         
            
        my.st()
        allow = True # let other events in now
            #else:
             #   print("hangfire left()")
    else:
        print('in left(), spin')

    

            

def right():
    
    global allow
    global top # index for record
    global gop
    global gou
    global gg
    global ok_repeat         
    global fix_angle
    global sss
    allow=True ###&&&&&& sort

    if allow:
        allow=False

        print('entering right()')
        
            

        
        angle = degrees_right.get()#&&& test value range/validity
        print('angle is', angle)
        x = int(eval(angle))
        fix_angle = x
        print('fix_angle is', fix_angle, 'angle is', angle )
        if fix_angle is angle:
            print('yes')
        else:
            print('no')

###################################### in left() inside repeat  ####################################################
    
        if ok_repeat == True:#&&& finish

                   
            print("in right(), and in repeat...")
            if fix_angle == 90:
                gg = gg + 1
                gop.append('\n    my.rt(90)')
                gou.append('rt ')
            else:
                gg = gg + 1
                gop.append('\n    my.rt(' + angle + ')')
                gou.append('rt(' + angle + ')')
                
                        
            print("in right(), gop is ",gop, "gou is", gou) 
            sss=''.join(gou)            
            in_repeat_code.set(sss)

        else:# in right() not in repeat
            
            my.st()                
            my.right(fix_angle)               
            top = top+1
            if fix_angle == 90:
                record.append('rt ')# for left turn
                recordmypy.append('\nmy.rt(' + angle + ')')
            else:
                record.append('rt(' + angle + ')')# for left turn
                recordmypy.append('\nmy.rt(' + angle + ')')
                
            ecode.set(''.join(record))                
                            
            
        my.st()
        allow = True # let other events in now
            #else:
             #   print("hangfire right()")
    else:
        print('in right(), spin')

    
            



def aboutturn():
    drive_milly('at')
    

def delete_op():
# reverses and deletes the effect of the last instruction
# 
    global allow
    global ok_repeat
    global top #top points to top of stack. When record is empty, record =[''] top = 0 
    global gou
    global gg
    global gop
    global pen_is_down
    global record
    global recordr
    global colour
    global tim
    global repeat_btn
    global brackets
    global gobtn

    #  see fdchoose and fechoose
    
    if allow ==  True:
        allow =False
        print('record is', record)
        if ok_repeat == True:# inside repeat loop building
            print("in delete_op and repeat")
            print("gou and gg", gou, gg)
            print("gop and gg", gop, gg)
            if gg == -1: # no entries in repeat, so either in repeat key or times key so:
                # time to start over
                tim.configure(background='light yellow')
                repeat_btn.configure(background = 'light yellow') 
                brackets.configure(background='light yellow')
                gobtn.configure(background = 'light yellow')
                ecode.set(''.join(record))
                times.set('')
                in_repeat_code.set('start repeat again')       
                
                recordr = []
            elif times.get()=='' and gg != -1:# hangfire because in repeat with a false start 
                in_repeat_code.set('<-- enter number of repeats first')
                #reset repeat conditions
                gou=[] 
                gop=[]
                gg=-1
                
            
            else:                
                print("gou is", gou, "gg is", gg, "gop is", gop)
                del(gou[gg])# deletes latest entry in repeat code list
                del(gop[gg])#   "
                gg=gg-1
                print("gou and gg", gou, gg)
                print("gop and gg", gop, gg)
               
                sss=''.join(gou)            
                in_repeat_code.set(sss)
                print('upl code is', sss)  
            allow=True
                   
        else: # not inside a repeat loop
            print('in delete_op(), not in repeat')
            if top >= 0:
                print("inside delete_op, not in repeat loop, record is", record)
                print("top = ", top)# 
                print('pen_is_down',pen_is_down)
                print('record[top] is', record[top])
                instruction=record[top]
            
                my.speed(0)
                
                #instead of all this code for different instructions, just remove   the last instruction from record
                # and redraw record[top-1]
                                    
                
                reset_turtle_canvas()
                print('recordmypy',recordmypy)
                print('recordmypy[top]',recordmypy[top])
                del(record[top])
                del(recordmypy[top])
                top=top-1
                sss=''.join(record)
                ecode.set(sss)
                go=''.join(recordmypy)
                print('go is', go)

                ######################
                exec(go)
                ######################
                             
                allow=True
                
                
                
                  
            else:#
                if top == -1:
                    my.down()
                    pen_is_down =True
                    print('top is ******', top)
                    print(' exiting delete_op, record at beginning, no more deletes record is empty', record)
                    rrr=''.join(record)
                    print('in delete_op, rrr is', rrr)
                    ecode.set(rrr)
                else:
                    print('in delete_op, baffled, top is', top)
            allow= True
    else:
        print('hangfire delete_op')
    
    #print('exiting delete_op, top is', top, 'record[top] is', record[top])

        
        
            




##################################event function declarations #########################


def full_delete(): ##&&&&&&&&&& no repeats to handle
    ''' handler function for 'c' key, part of the event driven set up and full delete operates to
    clear screen and existing record and recordmypy. But also as a clear before and after a function is defined.
    in the first case, record and recordmypy are set to empty, function definitions fun1, ... are retained. In the second case,
    the existing record and recordmypy are saved and held, and reinstated with the joint old function defs together with the
    new one.
    The full script_listpy is user_functionspy + recordmypy(including function calls)
    The full script_list for upl is arc_record  which is fun_headers + record
    '''
    
    
    global allow # controls interrupts from pad and keyboard events
    global top
    global hold_top
    global ok_repeat # inside a repeat loop
    global in_repeat_code #  code in repeat structure
    global ucode
    global ecode
    global record #list for fully built user program (but see arc_record  and fun headers)
    global recordpy
    global recordmypy
    global j # index for program on display in program_box
    global gg #index for program instructions in gou and gop in repeat code
    global p
    global n
    global pen_is_down
    global ok_function
    global arc_record # what remains after clear as stored upl if required, recordmypy is restored with program in pycode
    global arc_recordpy
    global arc_recordmypy #if required
    
    allow=True###&&&&&&
 
    if allow==True:
        allow=False

        arc_recordmypy = recordmypy # save recordmypy and record to re-unite with updated user_functions
        arc_record = record     #and fun_headers if required
        arc_recordpy = recordpy # store python version to print or renew
        hold_top = top # reinstate if full_delete() is part of a function definition.
        
        # clear screen and reset arrows
        ja.speed(0)
        ja.reset()
        si.speed(0)
        si.clear()
        si.reset()
        my.speed(0)
        my.clear
        my.reset()
        screen.bgcolor("white") # Set the background color
        si.ht()

        #####################
        allow=True      
        reset_turtle_canvas()
        allow=False
        #####################
        
        cv.after(500, lambda: cv.focus_force())#3reset all collective variables&&&&&&&&&&&&

        ############################reset initialisation   #######################################
         
        # some global variables need to retain their values for reset
        # e.g. p,n,fun1,2,3 ie user_functionspy all the arcs e.g arc_record 
        ok_repeat=False #   out of a repeat loop so reset variables in repeat loop      
        gg=-1 # counter for 'gou' of upl instr in a repeat loop        
        go = "" # text python program(code) for repeat as a string
        gop =[] #equivalent python program to gou for 'exec'
        gou = [] # text upl program for repeat as a list
        print('in full_delete, arc_record is', arc_record, 'arc_recordpy is', arc_recordmypy,'arc_recordmypy is', arc_recordmypy)
        ecode.set('')
        allow=True
        top=-1
        record=[]
        recordpy=[]
        recordmypy=[]
        ####################################################
        #toolButton1.invoke() # invokes toggle for pad/solutions
        ###################################################
        
        pen_is_down = True
        my.down() 
        allow = True
    else:
        print('in full_delete, spin')

    print('exiting full_delete, allow is,', allow)
    my.down()
    pen_is_down = True

    
        
    
   

    

    



def python_prog():
    global allow
    global record
    global pythonshow
    global frame4
    global pad_box
    global ucode

    pad_box = Frame(frame4, padx=50, pady = 0, bg = "light yellow")
    pad_box.grid(column=0, row=0, sticky=(N, W, E))
    pad_box['relief'] = 'raised'
    pad_box['borderwidth'] = 8
    pad_box['background'] = 'silver'
    pad_box['padx'] = 3
    pad_box['pady'] = 3
    
    #fillerh120= Frame(frame4,height=50, bg="light yellow")
    #fillerh120.grid(column=0, row=1, sticky=(N, W, E, S)) 
    
    #ucode = StringVar()
    label_instruction = ttk.Label(pad_box, relief=RIDGE, textvariable = ucode, wraplength= 350, width=30, \
                                  font = programFont14,   background = 'light green',  padding="50,0,50,0")
    label_instruction.grid(column=0, row=0, sticky=(N,W))
    label_instruction['relief'] = 'raised'
    label_instruction['justify'] = 'left'# justifies within the line
    label_instruction['anchor'] = 'nw' # moves to nw corner of the box
    label_instruction['borderwidth'] = 7
    #ucode.set('~~~~')
    #root.attributes("-topmost", True)
    headline= "from turtle import *\n"
        
    if  pythonshow ==True:
        pythonshow= False
        label_instruction.config(background= 'yellow',wraplength= 350, width=30, font = programFont14, padding="25,0,25,0" )
        ucode.set(headline + ''.join(record))
        frame3.after(100, lambda: frame3.focus_force())# 
    else:
        for child in frame4.winfo_children():
                child.destroy()
        pad1()
        #ucode.set('')
        pythonshow=True
        

def grid_dim(pace=100,nofsq=5):
    global allow
    global no_grid
    global p
    global n

    p=pace
    n=nofsq
    no_grid = False
    print('entering grid_dim()')
    if allow==True:
        allow = False
       
        print('pace,  nofsq are:', pace, nofsq)
        my.speed(0)    
        if pace ==100:
            ja.resizemode("user")
            ja.shapesize(1.5,1.5,1.5)
            si.resizemode("user")
            si.shapesize(1.5,1.5,1.5)
            my.resizemode("user")
            my.shapesize(1.5,1.5,1.5)
            my.pensize(5)
            my.color("black")            
        elif pace ==50:    
            ja.resizemode("user")
            ja.shapesize(1,1,1)
            si.resizemode("user")
            si.shapesize(1,1,1)
            ja.resizemode("user")
            ja.shapesize(1,1,1)
            my.resizemode("user")
            my.shapesize(1,1,1)
            my.pensize(3)
            my.color("black")         
        elif pace==25:    
            ja.resizemode("user")
            ja.shapesize(0.5,0.5,0.5)    
            si.resizemode("user")
            si.shapesize(0.5,0.5,0.5)
            ja.resizemode("user")
            ja.shapesize(0.5,0.5,0.5)
            my.resizemode("user")
            my.shapesize(0.5,0.5,0.5)
            my.pensize(2)
            my.color("black")
        elif pace==12:
            ja.resizemode("user")
            ja.shapesize(0.25,0.25,0.25)    
            si.resizemode("user")
            si.shapesize(0.25,0.25,0.25)
            ja.resizemode("user")
            ja.shapesize(0.25,0.25,0.25)
            my.resizemode("user")
            my.shapesize(0.25,0.25,0.25)
            my.pensize(2)
            my.color("black")
        elif pace==6:
            ja.resizemode("user")
            ja.shapesize(0.12,0.12,0.12)    
            si.resizemode("user")
            si.shapesize(0.12,0.12,0.12)
            ja.resizemode("user")
            ja.shapesize(0.12,0.12,0.12)
            my.resizemode("user")
            my.shapesize(0.12,0.12,0.12)
            my.pensize(2)
            my.color("black") 
            
        else:
            print(" hangfire, in grid_dim()")      
                       
        full_delete() 
        allow=True
    else:
        print('spin out of grid_dim')

     

def grid_5():
    global pen_is_down
    grid_dim(100,5)
    my.down()
    pen_is_down = True
    
    
    
def grid_10():
    global pen_is_down
    
    grid_dim(50,10)
    my.down()
    pen_is_down = True
    
def grid_20():
    global pen_is_down
    grid_dim(25,20)
    my.down()
    pen_is_down = True

def grid_40():
    global pen_is_down
    grid_dim(12,40)
    my.down()
    pen_is_down = True

def grid_80():
    global pen_is_down
    grid_dim(6,80)
    my.down()
    pen_is_down = True


def gridless():
    global no_grid
    global pen_is_down
    no_grid = True
    print('entering gridless')
    reset_turtle_canvas()
    my.down()
    pen_is_down = True 

def hope():
    print('entering hope')
######################################   functions    ##################################################

def execute_record():
    exec(fff)


    ##################################save  user functions f123 location123  ####################################

def save():# &&&&&&&&&#
    
    global record
    global recordmypy
    global top
    global arc_recordmypy
    global arc_record
    global arc_top

    global fun1_is_set
    global fun2_is_set
    global ok_function
    global user_functionspy# holds definitions of fun1,... in pycode
    global user_functions #    "                   "    in upl
    global f123 # StringVar for save() points to fun1/2/3
    global prefixpy1

    global allow 
    global p
    global n
    global pen_is_down       
    global in_repeat_code # for error message
    

    allow= True
    if allow:
        allow=False
        ok_function=True
        
        arc_recordmypy = recordmypy
        arc_record = record
        arc_top = top
                 
        location123= f123.get()
        if location123.isdigit():            
            u=location123
            index = int(u)
            if index > 0 and index <=4:
                print('ready to save in fun,index is',index)
                if index ==1 and fun1_is_set == False:
                    fun1_is_set = True
                
                elif index == 2 and fun2_is_set == False:
                    fun2_is_set = True
                
                elif index ==3 and fun3_is_set == False:
                    fun3_is_set = True
                
                elif index ==4 and fun4_is_set == False:
                    fun4_is_set = True
                
                else:
                    print('in save, no more function space')

                
                #pycode ########################################
                
                #prefixpy1 = "\np = (" + str(p) + ")"#changing a list to a string no!

                
                fun_headpy = ['\ndef fun1():\n    my.down()'] #assumes pen is down is start status 
                fun_callpy = ['\nfun1()']
                
                fun_bodypy=[]                        
                print('in save()1,recordmypy is', recordmypy)
                
                for instr in recordmypy:# add format indentation for function
                     vvv=instr.replace("\n","\n    ")
                     print('vvv is', vvv)
                     fun_bodypy = fun_bodypy + [vvv]
                     print('fun_bodypy is', fun_bodypy)
      
                fun_scriptpy = fun_headpy + fun_bodypy 
                print('in save()2, fun_scriptpy is', fun_scriptpy)
                print('instr is', instr)# 
                                   
                go123 = ''.join(fun_scriptpy)
                print("go123 is", go123)                  
                
                user_functionspy[index] = go123
                print('user_functionspy = ', user_functionspy)

                ################################################
                allow = True
                ecode.set(''.join(record))#displays via ecode in program_box
                allow= False          

                # upl code #########################################

                fun_head = ['fun' + str(index)+ ' --> ']
                fun_body = [''.join(record)] #hold code for 
                fun_call = ['fun1 '] ###&&&& for now 
                fun_script = fun_head + fun_body
                print('in save()3, recordmypy is ', recordmypy)
                
                top = 1
                hold_top = top
                ####################
                allow=True
                full_delete()
                allow=False
                ####################
                
                ecode.set(''.join(fun_script))
                
                print("index is", index)
                #record = hrecord
                #recordmypy = hrecordmypy
                #top = hold_top 
                #print(' in save() - end, recordmypy is', recordmypy)
                
                
                #exec(user_functionspy[index])                    
                allow=True           
            else:
                print("location123 is", location)
                in_repeat_code.set('enter number 1-3 for f box')
                print('mistake')
            allow=True
        else:
            print('fun1 is already set, use fun2?')###&&&& identify which one
        allow=True            
    else:
        print('in save()), spin out')
    
    
    
    

def function1():

    global record
    global recordmypy
    global top
    global arc_recordmypy
    global arc_record
    global arc_top
    global gg

    global fun1_is_set
    global fun2_is_set
    global ok_function
    global user_functionspy# holds definitions of fun1,... in pycode
    global user_functions #    "                   "    in upl
    global f123 # StringVar for save() points to fun1/2/3
    global prefixpy1

    global allow 
    global p
    global n
    global pen_is_down       
    global in_repeat_code # for error message
    
    allow = True
    if allow:
        allow=False
        if ok_function: # check that fun1 has been defined and saved 
            if ok_repeat:               
                in_repeat_code.set('fun1 ')###&&&& fun1 for now
                gg = gg + 1
                gou.append('fun1 ')
                gop.append('\n    fun1()')
                
                # hand back to repeat
            else:
                print('entering function1, user_functionspy[1] is', user_functionspy[1])
                exec('print(" about to execute fun1")')

                head_programpy = ''.join(user_functionspy)# link string header programs in pycode
                print('head_programpy is', head_programpy)
                #funbody = recordmypy + ['\nfun1()']
                # program to be executed is function call
                programpy = head_programpy + '\nfun1()' # fun1 for now
                # then
                print('in save()2, programpy is', programpy)
                print('recordmypy is', recordmypy)                              
                ecode.set(''.join(record))
                
                exec(programpy) # executes function call then the recordmypy afterwards is:
                # head_programpy or ''.join(user_functionspy) followed by pycode before call, followed by the call and including the call.
                # that is recordmypy currently (def without + function call)We might need to separate the recordmypy from user_functionspy.
        else:
            print('in fun1, ok_function is false')
            #&&& send message in_repeat? that function is not defined
        
        #exec('colour_square(my,"red")')
        #print('uf = ',  user_functionspy)
        #exec(user_functionspy[1])

        '''
        record_python = '\nmy.color("red")\nmy.fd(p)\nmy.lt(90)\nmy.fd(p)\nmy.rt(90)' 
        prefix = "\np = (" + str(p) + ")" 
        fff = prefix + record_python
        
        #fff = prefix + qqq + "\nsquaref(my)"
        print("fff is ", fff)
        exec(fff)
        time.sleep(1)
        exec(fff)
        hope()
        exec('hope()')
        #grid_10() 
        #red_all(my)
        #exec('red_all(my)')
        '''
        
        allow = True
    else:
        print('in function1, spin out')




def function2():
    global p
    global allow
    global f123
    if allow:
        allow=False
        print('entering function2, user_functionspy[2] is', user_functionspy[2])        
        if ok_function:
            if ok_repeat:                
                in_repeat_code.set('fun2 ')###&&&& fun1 for now
                gg = gg + 1
                gou.append('fun2 ')
                gop.append('\n    fun2()')
                
                # hand back to repeat
            else:
                print('entering function2, user_functionspy[2] is', user_functionspy[2])
                exec('print(" about to execute fun2")')

                head_programpy = ''.join(user_functionspy)# link string header programs in pycode
                print('head_programpy is', head_programpy)
                #funbody = recordmypy + ['\nfun1()']
                # program to be executed is function call
                programpy = head_programpy + '\nfun2()' # fun2 for now
                # then
                print('in save()2, programpy is', programpy)
                print('recordmypy is', recordmypy)                              
                ecode.set(''.join(record))
                
                exec(programpy) # executes function call then the recordmypy afterwards is:
                # head_programpy or ''.join(user_functionspy) followed by pycode before call, followed by the call and including the call.
                # that is recordmypy currently (def without + function call)We might need to separate the recordmypy from user_functionspy.
        
                
        #exec('colour_square(my,"red")')
        #print('uf = ',  user_functionspy)
        #exec(user_functionspy[1])
                
                
        #record_python = '\nmy.color("red")\nmy.fd(p)\nmy.lt(90)\nmy.fd(p)\nmy.rt(90)' 
        #prefix = "\np = (" + str(p) + ")" 
        fff = prefix + record_python
        
        #fff = prefix + qqq + "\nsquaref(my)"
        print("fff is ", fff)
        #exec(fff)
        #time.sleep(1)
        #exec(fff)
        #hope()
        #exec('hope()')
        #grid_10() 
        #red_all(my)
        #exec('red_all(my)')
               
        allow = True
    else:
        print('in function1, spin out')

    


    #qqq = "def squaref(tt):" + "\n    tt.begin_fill()" + "\n    for ii in range(4):" + "\n    tt.fd(p)" + "\n    tt.lt(90)" + "    tt.end_fill()
    #qqq = "\ndef squaref(tt):" + "\n    for ii in range(4):" + "\n        tt.fd(p)" + "\n        tt.lt(90)" 

    
    if allow:
        allow=False
        #record_python = '\nmy.fd(p)\nmy.lt(90)\nmy.fd(p)\nmy.rt(90)'
        record_python = '\nmy.fd(p)\nmy.lt(90)\nmy.fd(p)\nmy.rt(90)'
        prefix = "\np = (" + str(p) + ")" + "\nmy.down()"
        #fff = prefix + record_python
        
        fff = prefix + record_python + '\nred_all(my)'
        print("fff is ", fff)
        exec(fff)
        

    allow = True
    

def new_line():
    global p
    global allow
    global f123
    global record
    global recordmypy
    global top

    x=['\n']
    top = top+1
    record.append('\\\n')
    recordmypy.append(' ')
    
    print('record is', record)
    uuu=''.join(record)
    print('uuu is', uuu)
    ecode.set(uuu)
    
def hide_arrow():
    global p
    global allow
    global f123
    global record
    if allow:
        allow = False #&&&&& look at in repeat and enter as an instruction in record and recordmypy
        ja.ht()
        my.ht()
        si.ht()
        allow = True
    else:
        print('in hide_arrow, spin')

def magic(tt, abraca, dabra):
    global allow
    allow=True
    if allow:
        allow=False
        print('abraca =', abraca)
        print('dabra = ', dabra)
        for cc in range(2):                
            tt.fd(abraca*p)
            tt.lt(90)
            tt.fd(dabra*p)
            tt.lt(90)
        allow=True
    else:
        print('in magic, spin')



    
def magic10():
    magic(my,1,0)

def magic01():
    magic(my,0,1)

def magic11():
    magic(my,1,1)

def magic_trick():
    global allow
    global record
    global recordmypy
    global ok_repeat
    global gou
    global gop
    global gg
    global top
    global smoke
    global mirrors
    
    if allow:
        allow=False
        x=magic1.get()
        y=magic2.get()

        
        if x.isdigit() and y.isdigit:#test repeat value entered                
            smoke= int(x)
            mirrors = int(y)
            print('smoke=', smoke, 'mirrors = ', mirrors)
            if smoke >= -80 and smoke <= 80 and mirrors >= -80 and mirrors <= 80:
                if ok_repeat:# in repeat
                    print('ok_repeat is', ok_repeat)
                    gg = gg + 1
                    gou.append('\n    box' + x + ',' + y + ' ')
                    gop.append('\n    magic(my,smoke,mirrors)')
                    
                else:# not in repeat
                    print('smoke is', smoke, 'mirrors is', mirrors)
                    allow=True
                    magic(my,smoke,mirrors)
                    allow=False
                    recordmypy = recordmypy + ['\nmagic(my,smoke,mirrors)']
                    record = record + ['\nbox' + x +',' + y + ' ']
                    ecode.set(''.join(record))
                    top=top+1
                    allow=True
                
            else:
                print("enter integers in the boxes")
        else:
            print("enter integers in the boxes")               
        
        allow=True
    else:
        print('in magic_trick(), spin')



def act(event):
    global allow
    global ok_repeat
    print('act')
    if allow:
        allow=False
        if ok_repeat==False:
            in_repeat_code.set("click 'repeat' \nto start")
        allow = True
    else:
        print('in act(), spin')

def make_fun():
    global allow
    global ok_function
    if allow:
        allow=False
        ok_function = True
        allow=True
    else:
        print('in make_fun, spin')


def forward_act():
    global allow
    global ok_repeat
    if allow:
        allow = False
        if ok_repeat == False:
            print("click 'repeat' first")
            in_repeat_code.set("click 'repeat' first")
        allow = True



def diagonal():
    drive_milly('diag')
       
def toolbox1() :#switches to instruction pad 1 
    
    global allow
    global first_time
    global tim
    global ok_repeat
    global gop
    global gou
    global gg
    global in_repeat_code
    global holding_message
    global frame3
    global frame4
    global pad_box
    global pad_label
    global label_instruction
    global ucode
    global ecode
    global tb1
    global tb2
    global brackets
    global times
    global f123
    global pen_is_down
    global my
    global toolButton1   

    tb1=True
    tb2=False
    frame3.destroy()    
    #frame4.destroy()
    #pad_box.destroy()
    #padhead.destroy()
    #update()
    frame3 = Frame(root, bg="light yellow", padx=2, pady=20)
    frame3.grid(column=2, row=0, sticky=(N,E,W))
    #frame3.columnconfigure(0, weight=1)
    #frame3.rowconfigure(0, weight=1)
    frame3['borderwidth'] = 3
    frame3['relief'] = 'raised'   

    inner_frame3 = Frame(frame3, bg = "light yellow", padx =5, pady = 5)
    inner_frame3.grid(column=0, row=0, sticky=(N,E,W,S)) 



    ucode = StringVar()
    label_instruction = ttk.Label(inner_frame3, relief=RIDGE, textvariable = ucode, wraplength= 550, width=60,  font = boldFont12,\
                            background = 'light green',  padding="20 15 20 15")
    label_instruction.grid(column=0, row=0, sticky=(N,W))
    label_instruction['relief'] = 'raised'
    label_instruction['justify'] = 'left'# justifies within the line
    label_instruction['anchor'] = 'center' # moves to center of the box
    label_instruction['borderwidth'] = 5
     

    
    label_instruction.config(wraplength= 600, width=75,  font = boldFont12)                                    #padding=" 2 2 2 2" )
    ucode.set("                              Toolbox 1\n1. Use the  click/touch drawing screen pad\
 below, to build your program.\n2. Clear the screen when you need by clicking the 'clear' button.\n3. Fly the\
  red arrow for your next assignment.\n4. Use the 'repeat' sequence whenever your code repeats itself.")
    
    if allow:
        allow=False
        print('entering toolbox1() ************* and allow is true')        
        
        
        
         ################################ START OF GRID SET UP PROGRAM  ActionT1! #######################################


                     
              
        # just clear screen, reset grid quickly (and re-draw pad), else introduce pad from start.
         ################################
        allow=True
        pad1()
        full_delete()
        
        allow=False
        ##################################
        
        
        
        program_box.configure(background='light yellow',wraplength= 440, width = 40, padding="0", font=boldFont16)  
        
        ecode.set("                    Program Record\n\nYour program is recorded here,\
as you build it, an instruction at a time. Use the 'newline' button in Toolbox 1 to arrange your code to pick out\
the repetitions in your code.n\n\n\n\n")
        
            

        allow=True
                       
    else:
        print('in toolbox1, spin')
            
                
        ################################################ end of  action!T1 ############################################################

           
def toolbox2():    

    print('entering toolbox2')
    
    global allow
    
    global label_instruction
    
    global frame3
    global tim
    global ok_repeat
    global gop
    global gou
    global gobtn
    global gg
    global in_repeat_code
    global repeat_btn
    global brackets
    global times
    global f123
    global pen_is_down
    global my
    global ucode
   
    if allow:
        allow=False
        
        for child in frame3.winfo_children():
                child.destroy()
                
        frame3 = Frame(root, bg="light yellow", padx=5, pady=50)
        frame3.grid(column=2, row=0, sticky=(N,E,W))
        #frame3.columnconfigure(0, weight=1)
        #frame3.rowconfigure(0, weight=1)
        frame3['borderwidth'] = 3
        frame3['relief'] = 'raised'
        
        inner_frame3 = Frame(frame3, bg = "light yellow", padx =5, pady = 2)
        inner_frame3.grid(column=0, row=0, sticky=(N,W)) 
        


        
        
        ucode=StringVar()
        
        label_instruction=ttk.Label(inner_frame3,textvariable = ucode, wraplength= 380, width=43,  font = boldFont12,\
                                background = 'light green',  padding="8 15 8 15")
        label_instruction.grid(column=0, row=0, sticky=(N,W))
        label_instruction['relief'] = 'raised'
        label_instruction['justify'] = 'left'# justifies within the line
        label_instruction['anchor'] = 'center' # moves to center of the box
        label_instruction['borderwidth'] = 3

         
        v_cem101 = Frame(inner_frame3, bg= "light yellow", width = 20)
        v_cem101.grid(column=1, row= 0, sticky = (W))

        


      
            
           
        col = "light yellow"
        filler502= Frame(frame3, height=2, bg=col)
        filler502.grid(column=0, row=1, sticky=(N, W, E))



        label_instruction.config(background = "light green",font=boldFont12, width= 75, wraplength =550, padding="5 10 5 10" )
        ucode.set("                       Toolbox 2\n To define a function: Click 'define',  draw your shape, then\
    #click 'save'. To use the function click on the 'fun' version you have defined, starting with fun1  ")

        print("exiting toobox2(), about to enter pad2()")
        allow=True   
        pad2()
    else:
        print("Spin out before Toolbox2")
    
    
def toolbox3():    

    print('entering toolbox3')
    
    global allow
    global missionCount
    global label_instruction
    global frame2
    global frame3
    global tim
    global ok_repeat
    global gop
    global gou
    global gobtn
    global gg
    global in_repeat_code
    global repeat_btn
    global brackets
    global times
    global f123
    global pen_is_down
    global my
    global wb1
    global wb2
    global wb3
    global ucode
    global missionbox
    global wb1
    global wb2
    global wb3
    global missionbox
    global in_toolbox1
    global in_toolbox2
    global in_toolbox3
    global insol


    programFont12 = font.Font(family='Courier New', size=12, weight='bold')
    programFont14 = font.Font(family='Courier New', size=14, weight='bold')   
    programFont16 = font.Font(family='Courier New', size=16, weight='bold')
    programFont18 = font.Font(family='Courier New', size=18, weight='bold')
    programFont20 = font.Font(family='Courier New', size=20, weight='bold')
    programFont24 = font.Font(family='Courier New', size=24, weight='bold')
    programFont32 = font.Font(family='Courier New', size=32, weight='bold')

    italicFont14 = font.Font(family='Arial', size=14, weight='normal')
    italicFont16 = font.Font(family='Arial', size=16, weight='normal') 
        
    pad = True
    print("pad is",pad)
           
    frame3 = Frame(root, bg="light yellow", padx=5, pady=5)
    frame3.grid(column=2, row=0, sticky=(N,E,W))
    #frame3.columnconfigure(0, weight=1)
    #frame3.rowconfigure(0, weight=1)
    frame3['borderwidth'] = 3
    frame3['relief'] = 'raised'
    
    inner_frame3 = Frame(frame3, bg = "light yellow", padx =5, pady = 2)
    inner_frame3.grid(column=0, row=0, sticky=(N,W)) 
    


    
    
    ucode=StringVar()
    
    label_instruction=ttk.Label(inner_frame3,textvariable = ucode, wraplength= 380, width=43,  font = boldFont12,\
                            background = 'light green',  padding="8 15 8 15")
    label_instruction.grid(column=0, row=0, sticky=(N,W))
    label_instruction['relief'] = 'raised'
    label_instruction['justify'] = 'left'# justifies within the line
    label_instruction['anchor'] = 'center' # moves to center of the box
    label_instruction['borderwidth'] = 3

     
    v_cem101 = Frame(inner_frame3, bg= "light yellow", width = 20)
    v_cem101.grid(column=1, row= 0, sticky = (W))

    


  
        
       
    col = "light yellow"
    filler502= Frame(frame3, height=2, bg=col)
    filler502.grid(column=0, row=1, sticky=(N, W, E))



    label_instruction.config(background = "light green",font=boldFont12, width= 75, wraplength =550, padding="5 10 5 10" )
    ucode.set("                       Toolbox 2\n To define a function: Click 'define',  draw your shape, then\
click 'save'. To use the function click on the 'fun' version you have defined, starting with fun1  ")

    print("exiting toobox2(), about to enter pad2()")
       
    pad2()
    
    

     
######################################   drawing pad action  ##################################################

def toolbox4():#switches to instruction tool box 
    
    global allow
    global missionCount
    global label_instruction
    global frame3
    global tim
    global ok_repeat
    global gop
    global gou
    global gg
    global in_repeat_code
    global repeat_btn
    global gobtn
    global brackets
    global times
    global f123
    global pen_is_down
    global my
    global wb1
    global wb2
    global wb3
    global missionbox
    global ucode
    
    global in_toolbox1
    global in_toolbox2
    global in_toolbox3

    print("enter toolbox4")
    

    

    wb1=True
    wb2=False
    wb3=False
    

    wb3=True
    wb2=False
    wb1=False
        
    print("enter toolbox3")
    pad = True
    print("pad is",pad)

    
    
    
    label_instruction=ttk.Label(inner_frame3, wraplength= 380, width=43,  font = boldFont12,\
                            background = 'yellow',  padding="8 15 8 15")
    label_instruction.grid(column=0, row=0, sticky=(N,W))
    label_instruction['relief'] = 'raised'
    label_instruction['justify'] = 'left'# justifies within the line
    label_instruction['anchor'] = 'center' # moves to center of the box
    label_instruction['borderwidth'] = 3

    ucode.set(" Welcome  ")

        
    
    #label_instruction=ttk.Label(inner_frame3,relief=RIDGE,wraplength= 380, width=43,  font = boldFont12,)
   # text="1. Use the Click/Touch Drawing Pad below or the arrow keys on your keyboard. \n2. Click on 'Set Next Program' for the next \
#program to appear in the program box.\n\
#3. Follow the code instructions  to fly the red arrow. \n4. When you have finished the drawing,\
#Click 'Solutions' to test your answer.")
   
    label_instruction.grid(column=0, row=0, sticky=(N,W))
    label_instruction['relief'] = 'raised'
    label_instruction['justify'] = 'left'# justifies within the line
    label_instruction['anchor'] = 'center' # moves to center of the box
    label_instruction['borderwidth'] = 3
       
    
       
    ##################################  frame 4  #######################################################

    h_cement=3
    v_cement=3
    

    frame4 = Frame(frame3, bg = "light yellow", padx=5, pady = 10)
    frame4.grid(row = 2, column = 0, sticky= (N,E,W,S) )

    #fillerh150= Frame(frame4,height=150, bg="light yellow")
    #fillerh150.grid(column=0, row=0, sticky=(N, W, E))
        
    pad_box = Frame(frame4, padx=25, pady =10, bg = "light yellow")
    pad_box.grid(column=0, row=2, sticky=(N, W, E))
    pad_box['relief'] = 'raised'
    pad_box['borderwidth'] = 8
    pad_box['background'] = 'silver'
    pad_box['padx'] = 3
    pad_box['pady'] = 3
    
    fillerh120= Frame(frame4,height=50, bg="light yellow")
    fillerh120.grid(column=0, row=1, sticky=(N, W, E, S))

    #########################################   set up click pad   ###################################

    padhead = Label(pad_box, font= boldFont16, text=" Toolbox 3: Patterns and Functions",\
                    width = 50, height = 1, pady = 15)
    padhead.grid(row=0, column=0, sticky = (N,E,W,S))
    padhead['background'] = 'silver'
    
    mainframe = Frame(pad_box, borderwidth = 2, padx =1, pady =10)
    mainframe.grid(column=0, row=1, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe['background'] = 'silver'
    
    mainframe1 = Frame(mainframe)
    mainframe1.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe1['background'] = 'silver'
    
    mainframe2 = Frame(mainframe)
    mainframe2.grid(column=0, row=1, sticky=(N, W, E, S))
    mainframe2['background'] = 'silver'
    
    mainframe3 = Frame(mainframe)
    mainframe3.grid(column=0, row=2, sticky=(N, W, E, S))
    mainframe3['background'] = 'silver'
    
    mainframe4 = Frame(mainframe)
    mainframe4.grid(column=0, row=3, sticky=(N, W, E, S))
    mainframe4['background'] = 'silver'
    
    mainframe5 = Frame(mainframe, bg="silver")
    mainframe5.grid(column=0, row=4, sticky=(N, W, E, S))
    
    mainframe6 = Frame(mainframe, bg="silver")
    mainframe6.grid(column=0, row=5, sticky=(N, W, E, S))
    
    mainframe7 = Frame(mainframe, bg="silver")
    mainframe7.grid(column=0, row=6, sticky=(N, W, E, S))

    mainframe8 = Frame(mainframe, bg="silver")
    mainframe8.grid(column=0, row=7, sticky=(N, W, E, S))

    mainframe9 = Frame(mainframe, bg="silver")
    mainframe9.grid(column=0, row=8, sticky=(N, W, E, S))

    mainframe10 = Frame(mainframe, bg="silver")
    mainframe10.grid(column=0, row=9, sticky=(N, W, E, S))

    mainframe11 = Frame(mainframe, bg="silver")
    mainframe11.grid(column=0, row=10, sticky=(N, W, E, S))

    mainframe12 = Frame(mainframe, bg="silver")
    mainframe12.grid(column=0, row=11, sticky=(N, W, E, S))

    mainframe13 = Frame(mainframe, bg="silver")
    mainframe13.grid(column=0, row=12, sticky=(N, W, E, S))
    

    mainframe14 = Frame(mainframe, bg="silver")
    mainframe14.grid(column=0, row=13, sticky=(N, W, E, S))

    mainframe15 = Frame(mainframe, bg="silver")
    mainframe15.grid(column=0, row=14, sticky=(N, W, E, S))
    
    ########################## program instructions ###########################################################
    
            
    forward = Label(mainframe1, font= programFont14, text="forward", width = 10)
    forward.grid(row=0, column=0, sticky = (W))
    forward['anchor'] = 'w'
    forward['background'] = 'silver'
                                            
    btn1 = Button(mainframe1, text="fd1", font= programFont14, bg = "light yellow", width = 5,command = stepout1)
    btn1.grid(column = 1, row =0, sticky = (N,W))        
    btn1['relief'] = 'raised'
    btn1['borderwidth'] = 5

    v_cem1 = Frame(mainframe1, bg= "silver", width = v_cement)
    v_cem1.grid(column=2, row= 0, sticky = (W))
    
    btn2 = Button(mainframe1, text="fd2", font= programFont14, bg = "light yellow", width = 5,command = stepout2)
    btn2.grid(column = 3, row =0, sticky = (N,W))
    btn2['relief'] = 'raised'
    btn2['borderwidth'] = 5

    v_cem2 = Frame(mainframe1, bg= "silver", width = v_cement)
    v_cem2.grid(column=4, row= 0, sticky = (W))
    
    btn3 = Button(mainframe1, text="fd3", font= programFont14, bg = "light yellow", width = 5,command = stepout3)
    btn3.grid(column = 5, row =0, sticky = (N,W))
    btn3['relief'] = 'raised'
    btn3['borderwidth'] = 5

    v_cem3 = Frame(mainframe1, bg= "silver", width = v_cement)
    v_cem3.grid(column=6, row= 0, sticky = (W)) 

    btn4 = Button(mainframe1, text="fd4", font= programFont14, bg = "light yellow", width = 5,command = stepout4)
    btn4.grid(column = 7, row =0, sticky = (N,W))
    btn4['relief'] = 'raised'
    btn4['borderwidth'] = 5

    v_cem4 = Frame(mainframe1, bg= "silver", width = v_cement)
    v_cem4.grid(column=8, row= 0, sticky = (W)) 

    btnchoose = Button(mainframe1, text="fd", font= programFont14, bg = "light yellow", width = 4,command = stepout_choose)
    btnchoose.grid(column = 9, row =0, sticky = (N,W))
    btnchoose['relief'] = 'raised'
    btnchoose['borderwidth'] = 5

    
    forward_entry = Entry(mainframe1, bd = 5, width = 2, textvariable = paces,  font= programFont14, bg = 'light yellow')
    forward_entry.grid(column=11, row=0, sticky= (N,W,E,S))
    #forward_entry.bind("<FocusIn>", forward_act)
    
    fillerm2= Frame(mainframe2, height=h_cement, bg= "silver")
    fillerm2.grid(column=0, row=0, sticky=(N, W, E))

    

    


    left_turn = Label(mainframe3, font= programFont14, text="left turn", width = 10)
    left_turn.grid(column=0, row=0, sticky=(W))
    left_turn['background'] = 'silver'
    left_turn['anchor'] = 'w'

    
    
    btnleft = Button(mainframe3, text="lt", font= programFont14, bg = "light yellow", width = 5, command = left)
    btnleft.grid(column=1, row=0, sticky= (N,W))
    btnleft['relief'] = 'raised'
    btnleft['borderwidth'] = 5

    left_entry = Entry(mainframe3, bd = 5 , width = 7, textvariable = degrees_left,  font= programFont14, bg = 'light yellow')
    left_entry.grid(column=2, row=0, sticky= (N,W,E,S))
    #left_entry.bind("<FocusIn>", left_act)
    
    #left_blank = Label(mainframe3, bd = 5, width = 6,   font= programFont14, bg = 'silver')
    #left_blank.grid(column=2, row=0, sticky= (N,W,E,S))
    
    filler2a= Frame(mainframe3, width =5)
    filler2a.grid(column=3, row=0, sticky=(N, W, E, S))
    filler2a['background'] = 'silver'
    

    pen_up = Button(mainframe3, text="penup", font= programFont14, bg = "light yellow", width = 5,  command = put_penup)
    pen_up.grid(column=4, row=0 , sticky= (N,W))
    pen_up['relief'] = 'raised'
    pen_up['borderwidth'] = 5
    pen_up['anchor'] = 'w'

    v_cem5 = Frame(mainframe3, bg= "silver", width = v_cement)
    v_cem5.grid(column=5, row= 0, sticky = (W)) 


    pen_down = Button(mainframe3, text="pendown", font= programFont14, bg = "light yellow", width = 7,  command = put_pendown)
    pen_down.grid(column=6, row=0 , sticky= (N,W))
    pen_down['relief'] = 'raised'
    pen_down['borderwidth'] = 5
    pen_down['anchor'] = 'w'

    v_cem6 = Frame(mainframe3, bg= "silver", width = v_cement)
    v_cem6.grid(column=7, row= 0, sticky = (W)) 

    hide = Button(mainframe3, text="hide", font= programFont14,  bg = "light yellow", width = 3, command=hide_arrow, padx= 10)
    hide.grid(column=8, row=0, sticky= (E))
    hide['relief'] = 'raised'
    hide['borderwidth'] = 5

    fillerm4= Frame(mainframe4, height=h_cement, bg= "silver")
    fillerm4.grid(column=0, row=0, sticky=(N, W, E))
    
    right_turn = Label(mainframe5, font= programFont14, text="right turn", width = 10)
    right_turn.grid(column=0, row=0, sticky=(W))
    right_turn['background'] = 'silver'
    right_turn['anchor'] = 'w'

    btnright = Button(mainframe5, text="rt", font = programFont14,  bg = "light yellow", width = 5, command = right)
    btnright.grid(column=1, row=0, sticky= (N,W))
    btnright['relief'] = 'raised'
    btnright['borderwidth'] = 5

    right_blank = Label(mainframe5, bd = 5, width = 6,font= programFont14, bg = 'silver')
    right_blank.grid(column=2, row=0, sticky= (N,W,E,S))

    right_entry = Entry(mainframe5, bd = 5, width = 7, textvariable = degrees_right,  font= programFont14, bg = 'light yellow')
    right_entry.grid(column=2, row=0, sticky= (N,W,E,S))
    #right_entry.bind("<FocusIn>", left_act)

        
    
    filler2= Frame(mainframe5, width = 5)
    filler2.grid(column=3, row=0, sticky=(N, W, E, S))
    filler2['background'] = 'silver'
    
    
    delete = Button(mainframe5, text="delete", font= programFont14,  bg = "light blue", width = 6, command = delete_op )
    delete.grid(column=4, row=0, sticky= (E))
    delete['relief'] = 'raised'
    delete['borderwidth'] = 5

    v_cem7 = Frame(mainframe5, bg= "silver", width = v_cement)
    v_cem7.grid(column=5, row= 0, sticky = (W)) 

    clear = Button(mainframe5, text="clear", font= programFont14,  bg = "light blue", width = 3, command=full_delete, padx= 10)
    clear.grid(column=6, row=0, sticky= (E))
    clear['relief'] = 'raised'
    clear['borderwidth'] = 5

    v_cem8 = Frame(mainframe5, bg= "silver", width = v_cement)
    v_cem8.grid(column=7, row= 0, sticky = (W)) 

    newline = Button(mainframe5, text="newline", font= programFont14,  bg = "light blue", width = 5, command=new_line, padx= 10)
    newline.grid(column=8, row=0, sticky= (E))
    newline['relief'] = 'raised'
    newline['borderwidth'] = 5

    v_cem9 = Frame(mainframe5, bg= "silver", width = v_cement)
    v_cem9.grid(column=9, row= 0, sticky = (W)) 

    fillera50= Frame(mainframe5, height=h_cement, bg = "silver")
    fillera50.grid(column=0, row=1, sticky=(N, W, E))


    



    

    ################################### repeat control structure #############################################################
    
    
    repeat_btn= Button(mainframe6, text="repeat", width = 6, font = programFont16, command = setup_repeat)
    repeat_btn.grid(column=0, row=1, sticky=(W))
    repeat_btn['background'] = 'light yellow'

    filler25= Frame(mainframe6, width = 4)
    filler25.grid(column=1, row=1, sticky=(N, W, E, S))
    filler25['background'] = 'silver'
    
    
    times = StringVar()
    times.set('')
    tim = Entry(mainframe6,bd = 5, width = 2, textvariable = times,  font= programFont14, bg = 'light yellow')
    tim.grid(column=2, row=1, sticky= (E,W))
    tim.bind("<FocusIn>", act)
    

    filler3= Frame(mainframe6, width = 2)
    filler3.grid(column=3, row=1, sticky=(N, W,E,S))
    filler3['background'] = 'silver'

    bracketleft = Label(mainframe6, text='[', font= programFont32, bg = "silver", width = 1)
    bracketleft.grid(column=4, row=1, sticky= (N))

    
    brackets = Label(mainframe6, text=in_repeat_code,textvariable = in_repeat_code, font= programFont18,\
                     bg = "light yellow", width = 32)
    brackets.grid(column=5, row=1, sticky= (W,E))
    brackets.configure(font=programFont12)
    in_repeat_code.set('***')

    bracketright = Label(mainframe6, text=']', font= programFont32, bg = "silver", width = 1)
    bracketright.grid(column=6, row=1, sticky= (N,W))

    filler4= Frame(mainframe6, width = 2)
    filler4.grid(column=7, row=1, sticky=(N, W, E, S))
    filler4['background'] = 'silver'

    gobtn = Button(mainframe6, text="do it", font= programFont16, bg = "light yellow",  command = execute_repeat, width = 5)
    gobtn.grid(column=8, row=1, sticky= (E,W))

    ####################################################  filler  ###########################################

    fillerb50= Frame(mainframe8, height=10, bg= "silver")
    #fillerb50.grid(column=0, row=0, sticky=(N, W, E))

    ################################################   functions  #############################################
    
    functions = Label(mainframe7, font= programFont14, text="functions", width = 10)
    functions.grid(column=0, row=0, sticky=(N,W,E,S))
    functions['background'] = 'silver'
    functions['anchor'] = 'w'

    funbtn1 = Button(mainframe7, text="fun1", font= programFont14, bg = "light yellow", fg = "black", width = 5,command = function1)
    funbtn1.grid(column = 1, row =0, sticky = (N,W))        
    funbtn1['relief'] = 'raised'
    funbtn1['borderwidth'] = 5
    funbtn1['anchor'] = 'w'


    funbtn2 = Button(mainframe7, text="fun2", font= programFont14, bg = "light yellow", fg = "black", width = 5,command = function2)
    funbtn2.grid(column = 2, row =0, sticky = (N,W))        
    funbtn2['relief'] = 'raised'
    funbtn2['borderwidth'] = 5
    funbtn2['anchor'] = 'w'

    funbtn3 = Button(mainframe7, text="fun3", font= programFont14, bg = "light yellow", fg = "black", width = 5,command = function2)
    funbtn3.grid(column = 3, row =0, sticky = (N,W))        
    funbtn3['relief'] = 'raised'
    funbtn3['borderwidth'] = 5
    funbtn3['anchor'] = 'w'

    funbtn4 = Button(mainframe7, text="fun4", font= programFont14, bg = "light yellow", fg = "black", width = 5,command = function2)
    funbtn4.grid(column = 4, row =0, sticky = (N,W))        
    funbtn4['relief'] = 'raised'
    funbtn4['borderwidth'] = 5
    funbtn4['anchor'] = 'w' 

    #makebtn = Button(mainframe, text="make &", font= programFont14, bg = "light yellow", fg = "black", width = 6,command = make_fun)
    #makebtn.grid(column = 4, row =0, sticky = (N,E))        
    #makebtn['relief'] = 'raised'
    #makebtn['borderwidth'] = 5
    #makebtn['anchor'] = 'w'

    savebtn = Button(mainframe7, text="save in fun", font= programFont14, bg = "light yellow", fg = "black", width = 11,command = save)
    savebtn.grid(column = 5, row =0, sticky = (N,E))        
    savebtn['relief'] = 'raised'
    savebtn['borderwidth'] = 5
    savebtn['anchor'] = 'w'

    f123 = StringVar()
    f123.set('1')
    userfun = Entry(mainframe7,bd = 6, width = 1, textvariable = f123, font= programFont14, bg = 'light yellow')
    userfun.grid(column=6, row=0, sticky= (W,E))

    
    ####################################### colour buttons  ################################################
    
    fillerm10= Frame(mainframe10, height=h_cement, bg= "silver")
    #fillerm10.grid(column=0, row=0, sticky=(N, W, E))
    
    


     ######################################    colour tabs    ########################################################
    
    
    colourlab = Label(mainframe8, font= programFont14, text="colour", width = 10)
    colourlab.grid(column=0, row=0, sticky=(N,W,E,S))
    colourlab['background'] = 'silver'
    colourlab['anchor'] = 'w'

    cbtn1 = Button(mainframe8, text="red", font= programFont14, bg = "red", fg = "white", width = 5,command = red)
    cbtn1.grid(column = 1, row =0, sticky = (N,W))        
    cbtn1['relief'] = 'raised'
    cbtn1['borderwidth'] = 5

    v_cem10 = Frame(mainframe8, bg= "silver", width = v_cement)
    v_cem10.grid(column=2, row= 0, sticky = (W)) 

    
    cbtn2 = Button(mainframe8, text="blue", font= programFont14, bg = "blue",fg = "white", width = 5,command = blue)
    cbtn2.grid(column = 3, row =0, sticky = (N,E,W,S))
    cbtn2['relief'] = 'raised'
    cbtn2['borderwidth'] = 5

    v_cem11 = Frame(mainframe8, bg= "silver", width = v_cement)
    v_cem11.grid(column=4, row= 0, sticky = (W)) 

    
    cbtn3 = Button(mainframe8, text="green", font= programFont14, bg = "green",fg = "white", width = 6,command = green)
    cbtn3.grid(column = 7, row =0, sticky = (N,W))
    cbtn3['relief'] = 'raised'
    cbtn3['borderwidth'] = 5

    v_cem12 = Frame(mainframe8, bg= "silver", width = v_cement)
    v_cem12.grid(column=8, row= 0, sticky = (W)) 

    cbtn4 = Button(mainframe8, text="black", font= programFont14, bg = "black",fg = "white", width = 6,command = black)
    cbtn4.grid(column = 9, row =0, sticky = (N,W))
    cbtn4['relief'] = 'raised'
    cbtn4['borderwidth'] = 5

    v_cem13 = Frame(mainframe8, bg= "silver", width = v_cement)
    v_cem13.grid(column=10, row= 0, sticky = (W)) 

    cbtn5 = Button(mainframe8, text="gold", font= programFont14, bg = "gold",fg = "black", width = 6,command = gold)
    cbtn5.grid(column = 11, row =0, sticky = (N,W))
    cbtn5['relief'] = 'raised'
    cbtn5['borderwidth'] = 5

    v_cem14 = Frame(mainframe8, bg= "silver", width = v_cement)
    v_cem14.grid(column=12, row= 0, sticky = (W)) 
    
    cbtn6 = Button(mainframe8, text="white", font= programFont14, bg = "white",fg = "black", width = 6,command = white)
    cbtn6.grid(column = 13, row =0, sticky = (N,W))
    cbtn6['relief'] = 'raised'
    cbtn6['borderwidth'] = 5
    
    #fillerm12= Frame(mainframe6, height=h_cement, bg= "silver")
    #fillerm12.grid(column= 0, row=1, sticky=(N, W, E))
    

                          
    #label_instruction.config(text="Use the toolbox set out below.",bg = "yellow")
    #label_instruction.grid(column=0, row=0, sticky=(N,W))
    


   
    ####################################### magicbox   #####################################################
        
        
    #fillerm2001= Frame(pad2, height=3*h_cement, bg= "silver")
    #fillerm2001.grid(column=0, row=1, sticky=(N, W, E))

    about_turn = Label(mainframe9, font= programFont14, text="about turn", width = 10)
    about_turn.grid(column=0, row=0, sticky=(W,E))
    about_turn['background'] = 'silver'
    about_turn['anchor'] = 'w'

    about_turn = Button(mainframe9, text="at", font= programFont14,  bg = "light green", width = 5, command = aboutturn )
    about_turn.grid(column=1, row=0, sticky= (W))
    about_turn['relief'] = 'raised'
    about_turn['borderwidth'] = 5

    diagbtn = Button(mainframe9, text="diag", font= programFont14,  bg = "light green", width = 5, command = diagonal )
    diagbtn.grid(column=2, row=0, sticky= (W))
    diagbtn['relief'] = 'raised'
    diagbtn['borderwidth'] = 5
    
    arcbtn = Button(mainframe9, text="arc", font= programFont14,  bg = "light green", width = 5, command = at )
    #arcbtn.grid(column=3, row=0, sticky= (W))
    arcbtn['relief'] = 'raised'
    arcbtn['borderwidth'] = 5
        


    magicbox = Label(user_mainframe4, font= programFont14, text="magic box", width = 10)
    magicbox.grid(column=0, row=0, sticky=(N,W,E,S))
    magicbox['background'] = 'silver'
    magicbox['anchor'] = 'w'

    magicbtn1 = Button(user_mainframe4, text="box 1,0", font= programFont14, bg = "light green", fg = "black", width = 7,command = magic10)
    magicbtn1.grid(column = 1, row =0, sticky = (N,W))        
    magicbtn1['relief'] = 'raised'
    magicbtn1['borderwidth'] = 5
    magicbtn1['anchor'] = 'w'


    magicbtn2 = Button(user_mainframe4, text="box 0,1", font= programFont14, bg = "light green", fg = "black", width = 7,command = magic01)
    magicbtn2.grid(column = 2, row =0, sticky = (N,W))        
    magicbtn2['relief'] = 'raised'
    magicbtn2['borderwidth'] = 5
    magicbtn2['anchor'] = 'w'

    magicbtn3 = Button(user_mainframe4, text="box 1,1", font= programFont14, bg = "light green", fg = "black", width = 7,command = magic11)
    magicbtn3.grid(column = 3, row =0, sticky = (N,W))        
    magicbtn3['relief'] = 'raised'
    magicbtn3['borderwidth'] = 5
    magicbtn3['anchor'] = 'w'

    magicbtn4 = Button(user_mainframe4, text="box", font= programFont14, bg = "light green", fg = "black", width = 3,command = magic_trick)
    magicbtn4.grid(column = 4, row =0, sticky = (N,E))        
    magicbtn4['relief'] = 'raised'
    magicbtn4['borderwidth'] = 5
    magicbtn4['anchor'] = 'w'

    
    usermagic1 = Entry(user_mainframe4,bd = 6, width = 2, textvariable = magic1, font= programFont14, bg = 'light green')
    usermagic1.grid(column=5, row=0, sticky= (W,E))

    usermagic2 = Entry(user_mainframe4,bd = 6, width = 2, textvariable = magic2, font= programFont14, bg = 'light green')
    usermagic2.grid(column=6, row=0, sticky= (W,E))

    fillerm14= Frame(user_mainframe5, height=h_cement, bg= "silver")
    fillerm14.grid(column=0, row=0, sticky=(N, W, E))
    
    #   ########################################################

    
    
    usq= Label(mainframe8, font= programFont14, text="square", width = 10)
    usq.grid(row=0, column=0, sticky = (W))
    usq['anchor'] = 'w'
    usq['background'] = 'silver'
                                            
    sqbtn1 = Button(mainframe8, text="sq1", font= programFont14, bg = "light yellow", width = 5,command = stepout1)
    sqbtn1.grid(column = 1, row =0, sticky = (N,W))        
    sqbtn1['relief'] = 'raised'
    sqbtn1['borderwidth'] = 5
    
    sqbtn2 = Button(mainframe8, text="sq2", font= programFont14, bg = "light yellow", width = 5,command = stepout2)
    sqbtn2.grid(column = 2, row =0, sticky = (N,W))
    sqbtn2['relief'] = 'raised'
    sqbtn2['borderwidth'] = 5
    
    sqbtn3 = Button(mainframe8, text="sq3", font= programFont14, bg = "light yellow", width = 5,command = stepout3)
    sqbtn3.grid(column = 3, row =0, sticky = (N,W))
    sqbtn3['relief'] = 'raised'
    sqbtn3['borderwidth'] = 5

    sqbtn4 = Button(mainframe8, text="sq4", font= programFont14, bg = "light yellow", width = 5,command = stepout4)
    sqbtn4.grid(column = 4, row =0, sticky = (N,W))
    sqbtn4['relief'] = 'raised'
    sqbtn4['borderwidth'] = 5

    sqbtn5 = Button(mainframe8, text="sq5", font= programFont14, bg = "light yellow", width = 5,command = stepout4)
    sqbtn5.grid(column = 4, row =0, sticky = (N,W))
    sqbtn5['relief'] = 'raised'
    sqbtn5['borderwidth'] = 5 
    
    
    ######################################    fetch#    ########################################################

    
    ufetch = Label(mainframe9, font= programFont14, text="fetch", width = 10)
    ufetch.grid(row=0, column=0, sticky = (W))
    ufetch['anchor'] = 'w'
    ufetch['background'] = 'silver'
                                            
    febtn1 = Button(mainframe9, text="fe1", font= programFont14, bg = "light yellow", width = 5,command = stepout1)
    febtn1.grid(column = 1, row =0, sticky = (N,W))        
    febtn1['relief'] = 'raised'
    febtn1['borderwidth'] = 5
    
    febtn2 = Button(mainframe9, text="fe2", font= programFont14, bg = "light yellow", width = 5,command = stepout2)
    febtn2.grid(column = 2, row =0, sticky = (N,W))
    febtn2['relief'] = 'raised'
    febtn2['borderwidth'] = 5
    
    febtn3 = Button(mainframe9, text="fe3", font= programFont14, bg = "light yellow", width = 5,command = stepout3)
    febtn3.grid(column = 3, row =0, sticky = (N,W))
    febtn3['relief'] = 'raised'
    febtn3['borderwidth'] = 5

    febtn4 = Button(mainframe9, text="fe4", font= programFont14, bg = "light yellow", width = 5,command = stepout4)
    febtn4.grid(column = 4, row =0, sticky = (N,W))
    febtn4['relief'] = 'raised'
    febtn4['borderwidth'] = 5

    febtn5 = Button(mainframe9, text="fe5", font= programFont14, bg = "light yellow", width = 5,command = stepout4)
    febtn5.grid(column = 4, row =0, sticky = (N,W))
    febtn5['relief'] = 'raised'
    febtn5['borderwidth'] = 5 

    ######################################    rectangles#    ########################################################

    urectangle = Label(mainframe10, font= programFont14, text="rectangle", width = 10)
    urectangle.grid(row=0, column=0, sticky = (W))
    urectangle['anchor'] = 'w'
    urectangle['background'] = 'silver'
                                            
    rebtn1 = Button(mainframe10, text="re1", font= programFont14, bg = "light yellow", width = 5,command = stepout1)
    rebtn1.grid(column = 1, row =0, sticky = (N,W))        
    rebtn1['relief'] = 'raised'
    rebtn1['borderwidth'] = 5
    
    rebtn2 = Button(mainframe10, text="re2", font= programFont14, bg = "light yellow", width = 5,command = stepout2)
    rebtn2.grid(column = 2, row =0, sticky = (N,W))
    rebtn2['relief'] = 'raised'
    rebtn2['borderwidth'] = 5
    
    rebtn3 = Button(mainframe10, text="re3", font= programFont14, bg = "light yellow", width = 5,command = stepout3)
    rebtn3.grid(column = 3, row =0, sticky = (N,W))
    rebtn3['relief'] = 'raised'
    rebtn3['borderwidth'] = 5
    
    rebtn4 = Button(mainframe10, text="re4", font= programFont14, bg = "light yellow", width = 5,command = stepout4)
    rebtn4.grid(column = 4, row =0, sticky = (N,W))
    rebtn4['relief'] = 'raised'
    rebtn4['borderwidth'] = 5

    rebtn5 = Button(mainframe10, text="re5", font= programFont14, bg = "light blue", width = 5,command = stepout4)
    rebtn5.grid(column = 4, row =0, sticky = (N,W))
    rebtn5['relief'] = 'raised'
    rebtn5['borderwidth'] = 5 
    


    
 ##################################  grid sizes #######################################################


    gridlab = Label(mainframe15, font= programFont14, text="grid size", width = 10)
    gridlab.grid(column=0, row=0, sticky=(N,W,E,S))
    gridlab['background'] = 'silver'
    gridlab['anchor'] = 'w'
   
    btn_grid5 = Button(mainframe15, text=" 5x5", font= programFont14, bg = "light blue", width = 5,  command = grid_5)
    btn_grid5.grid(column=1, row=0, sticky= (N,W))
    btn_grid5['relief'] = 'raised'
    btn_grid5['borderwidth'] = 5
    btn_grid5['anchor'] = 'w'

    v_cem30 = Frame(mainframe15, bg= "silver", width = v_cement)
    v_cem30.grid(column=2, row= 0, sticky = (W)) 

    btn_grid10 = Button(mainframe15, text="10x10", font= programFont14, bg = "light blue", width = 5,  command = grid_10)
    btn_grid10.grid(column=3, row=0, sticky= (N,W))
    btn_grid10['relief'] = 'raised'
    btn_grid10['borderwidth'] = 5
    btn_grid10['anchor'] = 'w'

    v_cem31 = Frame(mainframe15, bg= "silver", width = v_cement)
    v_cem31.grid(column=4, row= 0, sticky = (W))  

    
    
    btn_grid20 = Button(mainframe15, text="20x20", font= programFont14, bg = "light blue", width = 5,  command = grid_20)
    btn_grid20.grid(column=5, row=0, sticky= (N,W))
    btn_grid20['relief'] = 'raised'
    btn_grid20['borderwidth'] = 5
    btn_grid20['anchor'] = 'w'

    v_cem32 = Frame(mainframe15, bg= "silver", width = v_cement)
    v_cem32.grid(column=5, row= 0, sticky = (W)) 
    
    btn_grid40 = Button(mainframe15, text="40x40", font= programFont14, bg = "light blue", width = 5,  command = grid_40)
    btn_grid40.grid(column=6, row=0, sticky= (N,W))
    btn_grid40['relief'] = 'raised'
    btn_grid40['borderwidth'] = 5
    btn_grid40['anchor'] = 'w'

    v_cem33 = Frame(mainframe15, bg= "silver", width = v_cement)
    v_cem33.grid(column=7, row= 0, sticky = (W)) 

    btn_grid80 = Button(mainframe15, text="80x80", font= programFont14, bg = "light blue", width = 5,  command = grid_80)
    btn_grid80.grid(column=8, row=0, sticky= (N,W))
    btn_grid80['relief'] = 'raised'
    btn_grid80['borderwidth'] = 5
    btn_grid80['anchor'] = 'w'


    v_cem34 = Frame(mainframe15, bg= "silver", width = v_cement)
    v_cem34.grid(column=9, row= 0, sticky = (W)) 

    

    
    btn_nogrid = Button(mainframe15, text="no grid", font= programFont14, bg = "light blue", width = 7, command = gridless)
    btn_nogrid.grid(column=10, row=0, sticky= (N,W))
    btn_nogrid['relief'] = 'raised'
    btn_nogrid['borderwidth'] = 5
    btn_nogrid['anchor'] = 'w'

    fillerm15= Frame(mainframe15, height=10, bg= "silver")
    fillerm15.grid(column=0, row=1, sticky=(N, W, E))
    
    lower_frame4 =Frame(frame4, bg="light yellow", height=250 )
    lower_frame4.grid(column=0, row=3, sticky=(N,E,W,S))
    lower_frame4.rowconfigure(0, weight=1)

    #f123=StringVar()
    #in_repeat_code.set("***")
    #brackets = Label(mainframe5, text='f123',textvariable = f123, font= programFont16, bg = "light yellow", width = 24)
    #brackets.grid(column=5, row=1, sticky= (W,E))

    
    allow=True
       

def stepout1():
    global allow
    global gop
    global gou
    global gg
    global ok_repeat
    global in_repeat_code
    global brackets
    allow=True
    if allow:
        allow= False
    
        if ok_repeat == True:

            #####################
            allow=True
            check_box() #checks the repeat box value
            allow=False
            #####################

            
            print("ok in repeat fd1")

            steps=1
            pix=steps*p # pixel equivalent on grid
            gg = gg + 1            
            gop.append('\n    my.fd(' + str(pix) + ')')            
            gou.append('fd1 ')
            
            print("gop is", gop)
            print("gou is", gou)
            
            sss=''.join(gou)            
            in_repeat_code.set(sss)            
        else:#not in repeat
            allow= True
            drive_milly("1")
            print("1 pace")
        allow = True
    else:
        print('in stepout1(), spin')
        
def stepout2():
    global allow
    global gop
    global gou
    global gg
    global ok_repeat
    global in_repeat_code
    global brackets
    
    if allow:
        allow= False
    
        if ok_repeat == True:

            #####################
            allow=True
            check_box() #checks the repeat box value
            allow=False
            #####################

            
            print("ok in repeat fd2")

            steps=2
            pix=steps*p # pixel equivalent on grid
            gg = gg + 1            
            gop.append('\n    my.fd(' + str(pix) + ')')            
            gou.append('fd2 ')
            
            print("gop is", gop)
            print("gou is", gou)
            
            sss=''.join(gou)            
            in_repeat_code.set(sss)            
        else:
            allow= True
            drive_milly("2")
            print("2 paces")
        allow = True
    else:
        print('in stepout2(), spin')

    
def stepout3():
    global allow
    global gop
    global gou
    global gg
    global ok_repeat
    global in_repeat_code
    global brackets
    
    if allow:
        allow= False
    
        if ok_repeat == True:

            #####################
            allow=True
            check_box() #checks the repeat box value
            allow=False
            #####################

            
            print("ok in repeat fd1")

            steps=3
            pix=steps*p # pixel equivalent on grid
            gg = gg + 1            
            gop.append('\n    my.fd(' + str(pix) + ')')            
            gou.append('fd3 ')
            
            print("gop is", gop)
            print("gou is", gou)
            
            sss=''.join(gou)            
            in_repeat_code.set(sss)            
        else:
            allow= True
            drive_milly("3")
            print("3 paces")
        allow = True
    else:
        print('in stepout3(), spin')
        
    

def stepout4():
    global allow
    global gop
    global gou
    global gg
    global ok_repeat
    global in_repeat_code
    global brackets
    
    if allow:
        allow= False
    
        if ok_repeat == True:

            #####################
            allow=True
            check_box() #checks the repeat box value
            allow=False
            #####################

            
            print("ok in repeat fd4")

            steps=4
            pix=steps*p # pixel equivalent on grid
            gg = gg + 1            
            gop.append('\n    my.fd(' + str(pix) + ')')            
            gou.append('fd4 ')
            
            print("gop is", gop)
            print("gou is", gou)
            
            sss=''.join(gou)            
            in_repeat_code.set(sss)            
        else:
            allow= True
            drive_milly("4")
            print("4 paces")
        allow = True
    else:
        print('in stepout1(), spin')

def put_penup():
    global gop
    global gou
    global gg
    global pen_is_down
    global top
    global record
    global allow
    if allow == True:
        allow=False
        if ok_repeat == True:
            if pen_is_down:
                pen_is_down=False #and change status
                gg = gg + 1
                gop.append('\n    my.up()')
                gou.append('up ')
                
                sss=''.join(gou)            
                in_repeat_code.set(sss)
                allow=True
            else:
                print('already up1, no change to pen_is_down')
                gg = gg + 1
                gop.append('\n    my.up()')
                gou.append('up ')
                
                sss=''.join(gou)            
                in_repeat_code.set(sss)
                allow=True
            
        else:# not inside repeat    
            if pen_is_down:
                pen_is_down=False #and change status
                my.up()
                print("in put_penup pen_is_down is", pen_is_down)
                top = top+1
                record.append('up ')# for forward
                recordmypy.append('\nmy.up() ')# for forward
                sss=''.join(record)
                ecode.set(sss)
                allow=True
            else:
                print('already up2, no change in pen_is_down')
                print("in put_penup pen_is_down is", pen_is_down)
                top = top+1
                record.append('up ')# for forward
                recordmypy.append('\nmy.up() ')# for forward
                sss=''.join(record)
                ecode.set(sss)
                allow=True       
    else:
        print("spin in put_penup")

def put_pendown():
    global gop
    global gou
    global gg
    global pen_is_down
    global top
    global record
    global allow

    if allow == True:
        allow=False
        if ok_repeat == True:
            print("ok_repeat put_pendown")
            if pen_is_down: # no change in pen_is_down
                gg = gg + 1
                gop.append('\n    my.down()')
                gou.append('down ')
                
                sss=''.join(gou)            
                in_repeat_code.set(sss)
                allow=True            
                print('already down1, no change in pen_is_down')
            else:
                gg = gg + 1
                pen_is_down=True                
                gop.append('\n    my.down()')
                gou.append('down ')
                
                sss=''.join(gou)            
                in_repeat_code.set(sss)
                
        else:#(not inside repeat)
            if pen_is_down == False:
                pen_is_down=True#andchange status
                my.down()
                print("in put_pendown pen_is_down is", pen_is_down)
                top = top+1
                record.append('down ')# for forward
                recordmypy.append('\nmy.down() ')# for forward
                sss=''.join(record)
                ecode.set(sss)
                allow=True
            else:
                print('already down2, no change in pen_is_down')
                print("in put_pendown pen_is_down is", pen_is_down)
                top = top+1
                record.append('down ')# for forward
                recordmypy.append('\nmy.down() ')# for forward
                sss=''.join(record)
                ecode.set(sss)
                allow=True
                
    else:
        print("spin in put_pendown and wait for further interrupts")
    

#########################################  colours   ############################################################


def colour_square(tt, colour):
    global top
    global allow
    global gop
    global gou
    global gg
    global ok_repeat
    global in_repeat_code
    global brackets
    global pen_is_down
    
    allow=True##&&&&&sort
    
    print("top=", top)
    print("allow=", allow)    
    print("pen_is_down =", pen_is_down)    
    print("entering colour_sq")
    
    if allow == True:
        allow = False
        tt.color("black", colour)
        print("colour is", colour)
        if pen_is_down == False:
            tt.penup()
        else:
            tt.pendown()
            
        tt.begin_fill()

        for ii in range(4):
            tt.fd(p)
            tt.lt(90)    

        tt.end_fill()
        
        tt.st()
        allow=True
    else:
        print("spin in colour_square")

def colour_all(tt, colour):
    global top
    global allow
    global record
    global recordmypy
    global gop
    global gou
    global gg
    global ok_repeat
    global in_repeat_code
    global brackets
    global pen_is_down
    
    print("top is", top)
    print("allow=", allow)    
    print("ok_repeat =", ok_repeat)    
    print("pen_is_down =", pen_is_down)

    
    
    if ok_repeat == True: # no drawing: in repeat section to be saved for repeat execution
        if allow==True:
            allow=False
            if pen_is_down:
                tt.color("black", colour)
                tt.down()                
                sss=''.join(gou)            
                in_repeat_code.set(sss)
            else:                               
                tt.up()                
                sss=''.join(gou)            
                in_repeat_code.set(sss)
            gg = gg + 1    
            print("ok_repeat is", ok_repeat, "colour is",colour)
            if colour == "red":
                gop.append('\n    colour_square(my,"red")')# &&&&&&&&&& put in call or inline code
            
            elif colour == "blue":
                gop.append('\n    colour_square(my,"blue")')#

            elif colour == "green":
                gop.append('\n    colour_square(my,"green")')

            elif colour == "gold":
                gop.append('\n    colour_square(my,"gold")')

            elif colour == "black":
                gop.append('\n    colour_square(my,"black")')

            elif colour == "white":
                gop.append('\n    colour_square(my,"white")')

            gou.append(colour + ' ')
            
            sss=''.join(gou)            
            in_repeat_code.set(sss)
            print('in colour_all, repeat code is:', sss)
            allow=True
            
    else: #going to draw  not in repeat-- usual execution each instruction as it appears       
        print(" drawing square not in repeat -- colour is", colour)
        if allow == True:
            allow = False #lock out other events until instruction is completed
            if pen_is_down: # black border to square colouring               
                if p==100:
                    tt.pensize(2)                    
                elif p==50:    
                    tt.pensize(2)
                elif p==25:    
                    tt.pensize(2)
                elif p==12:    
                    tt.pensize(2)
                elif p==6:    
                    tt.pensize(2)
                else:
                    print("hangfire in colour_all, p?")
                tt.down()
                
            else:
                tt.up()
             
            record.append(colour + ' ')
            recordmypy.append('\ncolour_square(my,colour)')
            top = top+1
            allow=True
            colour_square(my, colour)
            allow= True
            ecode.set(''.join(record))#displays via ecode in program_box
            allow=True
            
                
        else:
            print("spin in colour_all")







def red():
    print("red1")
    allow=True
    
    colour_all(my, "red" )

def redsquare():
    my.color("black","red")
    my.begin_fill()
    for kk in range(4):
        my.fd(p)
        my.lt(90)
    my.end_fill()

def blue():
    global p
    print('blue1')
    allow=True
    colour_all(my,"blue")

def green():
    print("green1")
    colour_all(my, "green")
    #colour_square(my,"green")

def black():
    print("black1")
    colour_all(my, "black")
    #colour_square(my,"black")

def gold():
    print("gold1")
    colour_all(my, "gold")
    #colour_square(my,"black")

def white():
    print("white1")
    colour_all(my, "white")    
    
    #colour_square(my,"black")




def check_box():
    global allow
    global tim
    global gop
    global gou
    global gg
    global timesrep
    global ok_repeat
    global repeat_btn
    global brackets

    allow=True ##&&&&&&
    ok_repeat=True
    if allow:
        allow=False
        if ok_repeat:
            # move this forward to drive_milly, left right red,blue etc and fun123
            uuu= times.get()            
            if uuu == '' and  ok_repeat:
                in_repeat_code.set("enter the number of repeats after clicking 'repeat'\npress pad keys\n\
to enter your code to repeat")
                gop=[]
                gou=[]
                gg=-1
                return False
            else:           
                print( "in exec and gop is", gop)
                print( "in exec and gou is", gou)
                #in_repeat_code.set("press pad keys\n to enter your code to repeat ")
                    
            ############## new version of repeat $$$$$$$  ####################################

            if uuu.isdigit():###&&&&& test repeat value entered                
                timesrep= int(uuu)
                print('in check_box(), timesrep is', timesrep)
                if timesrep > 0 and timesrep <= 100:
                    # repeat_box_number goes green and brackets_box too
                    tim.configure(background='light green')
                    brackets.configure(background = 'light green') 
                    #in_repeat_code.set("")
                    return True
                else:
                        all_set2 = False
                        in_repeat_code.set('see error box repeat number out of bounds')
                
            else:
                print("timesrep is", timesrep)
                in_repeat_code.set('enter a whole number in repeat  box')
                print('in execute_repeat(), mistake in box entry')
                return False
        else:
            print('in check_box(), but ok_repeat not true')
            in_repeat_code.set("start repeat instruction again, click 'repeat'")
            return False
                
        allow = True
    else:
        print('in check_box, spin')
        return False
    allow=True
    
    
def setup_repeat():
    global allow
    global ok_repeat
    global repeat_btn
    global record
    global recordmypy
    global p
    global steps
    global n
    global go
    global gop
    global gou
    global gobtn
    global record
    global recordr
    global gg
    global tim
    global times
    global prefixpy1
    global all_set
    global arc_fun
    global arc_funpy
    global ucode
    global label_instruction

    print('999')
    allow=True##&&&&
    if allow:
        ok_repeat = True
        repeat_btn.configure(background = 'light green')
        tim.after(50, lambda: tim.focus_force())
        in_repeat_code.set('<-- enter number of repeats\n then click code buttons')
        gop=[]
        gou=[]
        gg=-1
        

        
        
        allow=False
        
        times.set('')
        tim.configure(background = 'light green')
        #label_instruction.config(background = "light green" )
        #ucode.set("to use repeat:\n click 'repeat'\n2. enter number of repeats\n3.\
#press code buttons for code\n4. click 'do it'")
        #in_repeat_code.set('<-- enter number\n of repeats')
        
        #record = [''.join(arc_fun)]#?
        #recordmypy = [''. join(arc_funpy)]#?
        allow=True
        
        
      
       
            
    else:
        print("hangfire in setuprepeat")

    print('in setup_repeat')
    
    #print ("focus is:",root.focus_get())
    #if root.focus_get() == tim.focus_get():
    #    print('yes')
    #else:
    #    print('no')
            
    

def execute_repeat():# executes the repeat statement when 'do it' is pressed
    global allow
    global ok_repeat
    global record
    global top
    global recordmypy
    global p
    global n
    global go
    global gop
    global steps
    global gou
    global gobtn
    global tim
    global times
    global timesrep
    global repeat_btn
    global top
    global prefixpy1
    global user_functionspy
    global sss
    

    allow = True###&&&&&&&&&&&&check this out
    if check_box():
        print('check_box is', check_box())
        allow=True    
        if allow==True:
            allow = False
            uuu= times.get()
            if ok_repeat == False:
                in_repeat_code.set("click 'repeat' to start")
            elif uuu == '':
                in_repeat_code.set("enter number of \nrepeats after clicking 'repeat'")
            else:           
                print( "in exec and gop is", gop)
                print( "in exec and gou is", gou)
                #in_repeat_code.set("enter number after 'repeat'")
                
        ############## new version of repeat $$$$$$$  ####################################
                '''
                if uuu.isdigit():###&&&&& test repeat value entered                
                    timesrep= int(uuu)
                    if timesrep > 0 and timesrep <= 80:
                        tim.configure(background='light green')
                '''
                gobtn.configure(background = 'light green')
                print('in execute_repeat(), go is green')
                
                
                #put the upl code together
                zzz = '\nrepeat '+ str(timesrep) + "[" + ''.join(gou) + "]"
                repeat_script = [zzz] #just the head statement of upl so far...
                record = record + repeat_script #(lists)
                top=top+1
                print(' in execute_repeat(), record is', record)
                ecode.set(''.join(record))#put in string form
                print(''.join(record))

                #put the python code together
                repeat_headpy=['\nfor count in range(' + str(timesrep) + '):']
                #prefixpy1 = for_str # join up the preamble for pycode in lists
                #print('prefixpy1 is',prefixpy1)
                #link pycode from the repeat statement       
                print('gop is', gop)
                sh = repeat_headpy + gop
                print('sh is', sh)
                shs = ''.join(sh)
                print('shs is', shs)
                sss=[shs]# makes the repeat instruction into one instruction in python
                repeat_scriptpy = user_functionspy + sss 
                
                #repeat_scriptpy = user_functionspy + repeat_headpy + gop # gives whole program linking  pycode from the repeat statement  
                #(for function save if code needed as a function)        
                go = ''.join(repeat_scriptpy)
                
                print("go is", go)

                recordmypy = recordmypy + sss
                print('record is', record)

                ######################
                exec(go)
                ######################

                #time.sleep(2)
                
                tim.configure(background='light yellow')
                repeat_btn.configure(background = 'light yellow') 
                brackets.configure(background='light yellow')
                gobtn.configure(background = 'light yellow') 
                
                
                #go = '\nfor count in range(2):\n    fun1()'
                #exec('\ndef fun1():\n    my.fd(p)\n    my.lt(90)\n    my.fd(p)\n    my.rt(90)\nfor count in range(2):\n    fun1()')
                #exec(go)# execute the pycode for repeat statement
                '''    
                    else:
                        all_set2 = False
                        in_repeat_code.set('see error box repeat number out of bounds')
                
                else:
                    print("timesrep is", timesrep)
                    in_repeat_code.set('enter number in box')
                    print('mistake')
                '''
                ###########################################   old version of repeat ##########################################################
                '''    
                print('gop is', gop)
                gou=gou*timesrep   
                

                
                print( "modded gou is", gou)
                record=record + gou
                i = i + len(gou)
                print("i is", i)
                print("record is", record)
                
                
                go = ''.join(gop)
                print("go is", go)
                for nn in range(timesrep):
                    exec(go)
                '''

                #####################################################################################################

                ###&&&&&&&&&&&& any other variables to reset?
                # other global variables to hold
                go =''# reset python executable python string repeat code to empty
                gop=[]# reset adjustable list python code
                
                timesrep=0
                
                gou = [] #reset upl repeat list code
                gg=-1 # reset counter for gop and gou
                 
                ok_repeat = False
                in_repeat_code.set('**')
                times.set('')
            allow=True
        else:
            print("in execute_repeat(), spin")
        cv.after(100, lambda: cv.focus_force())#2
    else:
        print( 'check_box is False', check_box())
        tim.configure(background='light yellow')
        repeat_btn.configure(background = 'light yellow') 
        brackets.configure(background='light yellow')
        gobtn.configure(background = 'light yellow') 
        in_repeat_code.set("start again, click 'repeat'")
        ok_repeat=False
    allow=True


def reset_turtle_canvas():
##############################################################################

 #Method 1: stacking horizontal and vertical RETURN lines -- fetch(pixels)

###############################################################################



    def refetch(pixels):
        for count in range(2):
            si.fd(pixels)
            si.lt(90)
            si.lt(90)

    def stacklines(n,length,p):
        # gets in position to draw a stack of n lines of length l
        for k in range(n):
            si.lt(90)
            si.fd(p)
            si.rt(90)
            refetch(length*p)
            
    def arrayoflines(n,colour,p):
        # lines stacked two ways to give required array    
        si.up()
        si.color(colour)
        si.down()
        refetch((n-1)*p)
        stacklines(n-1,n-1,p)
        si.rt(90)
        stacklines(n-1,n-1,p)
        si.fd((n-1)*p)
        si.rt(90)
        si.fd((n-1)*p)
        si.rt(90)
        si.rt(90)
        #time.sleep(0.5)

    ###############################################################################

                        #Method 2: stacking a row of squares

    ###############################################################################

    def sq(pixels):
        for count in range(4):
            si.fd(pixels)
            si.lt(360/4)
            
    def rowofsquares(n,p):
        # draws a row of n touching unit squares
        for pp in range(n):
            sq(p)
            si.fd(p)
            
        si.lt(90)
        si.lt(90)
        si.fd(n*p)
        si.lt(90)
        si.lt(90 )
        
    def arrayofsquares(n,colour,p):
        # draws an nxn array of touching unit squares
        si.down()
        for steps in range(n):
            rowofsquares(n,p)
            si.up()
            si.lt(90)
            si.fd(p)
            si.rt(90)
            si.down()
            
        si.up()
        si.rt(90)
        si.fd(n*p)
        si.lt(90)
        

    ###############################################################################

        #Method 3: Stacking a row of rectangles turning at top and repeating

    ###############################################################################    

    def rectangle(length,p):
        for i in range(2):
            si.fd(length)
            si.lt(90)
            si.fd(p)
            si.lt(90)
        
    def stackofrectangles(n,p):
        for j in range(n):
            rectangle(n*p,p)
            si.lt(90)
            si.fd(p)
            si.rt(90)
            
            
    def arrayofrectangles(n,colour,p):
        # rectangles stacked two ways to give required array    
        si.up()
        si.color(colour)
        si.down()
        stackofrectangles(n,p)
        si.rt(90)
        stackofrectangles(n,p)
        si.fd(n*p)
        si.rt(90)
        si.fd(n*p)
        si.rt(90)
        si.rt(90)
        


    ###############################################################################

        #Method 4: Stacking a row of rectangles turning at top
        #and drawing vertical lines

    ###############################################################################    

    def rectangle(length,p):
        for i in range(2):
            si.fd(length)
            si.lt(90)
            si.fd(p)
            si.lt(90)
        
    def stackofrectangles(n,p):
        for j in range(n):
            rectangle(n*p,p)
            si.lt(90)
            si.fd(p)
            si.rt(90)
            
            
    def stackofrectanglesandlines(n, colour,p):
        stackofrectangles(n,p)
        si.rt(90)
        stacklines(n-1,n,p)
        si.fd(n*p)
        si.rt(90)
        si.fd((n-1)*p)
        si.lt(180)

    ###############################################################################

        #Method 5: Set up surrounding square and drawing set of lines
        #both horizontally and vertically

    ###############################################################################    

    def resquare(length):
        for i in range(4):
            si.fd(length)
            si.lt(360/4)
               
    def outsqandlines(n, colour,p):
        resquare(n*p)
        stacklines(n-1, n, p)
        si.lt(90)
        si.fd(p) 
        si.lt(90)
        si.lt(90)
        stacklines(n-1, n,p)
        si.fd(n*p)
        si.rt(90)
        si.fd((n-1)*p)
        si.lt(90)
        si.lt(90)


    ###############################################################################

        #Method 6: TESSELLATION OF SQUARES ON THE DIAGONALS

    ###############################################################################     



    def stair(p):
        si.fd(p)
        si.lt(90)
        si.fd(p)
        si.rt(90)

    def halfsq(p):
        si.fd(p)
        si.lt(90)
        si.fd(p)
        si.lt(90)

    def staircase(n,p):
        for i in range(n):
            stair(p)
                
    def tess(n,p):
        if n == 1:
            for j in range(4):
                si.fd(p)
                si.lt(90)

        else:
            for i in range(2):
                staircase(n-1,p)
                halfsq(p)


    def stairblock(n,p):
        for x in range(n,0, -1):
            tess(x,p)
            si.fd(p)
        
        si.lt(180)
        si.fd(n*p)
        si.lt(180)



    def tessellate(n, colour,p):
        si.up()
        si.color(colour)
        si.down()
        
        for y in range(2):
            stairblock(n,p)
            si.fd(n*p)
            si.lt(90)
            si.fd(n*p)
            si.lt(90)
        
    ###############################################################################

        #Method 7: ONE ROLL TESSELLATION OF SQUARES ON THE OPPOSITE DIAGONALS

    ###############################################################################     
             

    def oneroll(n, colour,p):
        si.up()
        si.color(colour)
        si.down()
        si.up()
        si.fd((n)*p)
        si.down()
        for j in range(1, n+1, 1):
            si.bk(p)
            tess(j,p)

        for j in range(n-1, 0, -1):
            si.lt(90)
            si.fd(p)
            si.rt(90)
            tess(j,p)
        si.rt(90)
        si.fd((n-1)*p)
        si.lt(90)
        


        
    ################# START OF GRID SET UP PROGRAM #######################################

    #Now add the Shape to the Screen’s shapelist and use it:
    # sptation set up at (0,0)

    def dock(tt, p):
        tt.penup()
        tt.st()
        tt.speed(0)
        tt.lt(180)
        if n!=5:
            qq=(int(n/2)-1)*p
            print("qq is", qq)
        else:
            qq=150
            
        tt.fd(qq)
        tt.lt(90)
        tt.fd(qq)
        tt.st()
        tt.lt(90)
        tt.speed(0)
        

    print('entering reset_turtle_canvas; no_grid = ', no_grid)
    
    ja.shape("spacestation")
    ja.ht()
    ja.penup()

    si.ht()
    si.shape("starshapegrey")#silva the blue arrowgrid_dim()
    si.pensize(1)
    si.color("blue")
    si.ht()

    my.shape("starshapered") #milly the red arrowbot
    my.pensize(2)
    my.color("red")
    
    si.ht()
    my.clear()
    my.reset()
    si.clear()
    si.reset()
    ja.clear()
    ja.reset()
    
    if p==100:
        ja.resizemode("user")
        ja.shapesize(1.5,1.5,1.5)
        si.resizemode("user")
        si.shapesize(1.5,1.5,1.5)
        my.resizemode("user")
        my.shapesize(1.5,1.5,1.5)
        my.pensize(2)
        my.color("black")
        
    elif p==50:    
        ja.resizemode("user")
        ja.shapesize(1,1,1)
        si.resizemode("user")
        si.shapesize(1,1,1)
        ja.resizemode("user")
        ja.shapesize(1,1,1)
        my.resizemode("user")
        my.shapesize(1,1,1)
        my.pensize(2)
        my.color("black")         
    elif p==25:    
        ja.resizemode("user")
        ja.shapesize(0.5,0.5,0.5)    
        si.resizemode("user")
        si.shapesize(0.5,0.5,0.5)
        ja.resizemode("user")
        ja.shapesize(0.5,0.5,0.5)
        my.resizemode("user")
        my.shapesize(0.5,0.5,0.5)
        my.pensize(2)
        my.color("black")
    elif p==12:
        ja.resizemode("user")
        ja.shapesize(0.25,0.25,0.25)    
        si.resizemode("user")
        si.shapesize(0.25,0.25,0.25)
        si.ht()
        ja.resizemode("user")
        ja.shapesize(0.25,0.25,0.25)
        my.resizemode("user")
        my.shapesize(0.25,0.25,0.25)
        my.pensize(2)
        my.color("black")
    
    elif p==6:
        ja.resizemode("user")
        ja.shapesize(0.12,0.12,0.12)    
        si.resizemode("user")
        si.shapesize(0.12,0.12,0.12)
        si.ht()
        ja.resizemode("user")
        ja.shapesize(0.12,0.12,0.12)
        my.resizemode("user")
        my.shapesize(0.12,0.12,0.12)
        my.pensize(2)
        my.color("black") 
        
    else:
        print(" hangfire, in start grid set")
        

   
    dock(ja,p) #move the dock station to the designated origin for operations
    dock(si,p)    
    dock(my,p)

    print('no_grid = ', no_grid)
    if no_grid==False:
        #move to starting point to draw the grid
        
        si.ht()
        si.pensize(1)
        si.color("grey")
        si.st()
        si.up()
        si.rt(90)
        si.fd(p)
        si.rt(90)
        si.fd(p)
        si.lt(180)
        si.down()
        
            
        #system program starts
        colour = "grey"
        if p < 50:
            dicethrow = 1 # quickest drawing solution
            si.ht()
            si.speed(0)
        else:
            pass
            #dicethrow = random.randint(1,7)
        dicethrow = 8
        if dicethrow == 1:
            arrayoflines(n+1,colour,p)
        elif dicethrow == 2:
            arrayofrectangles(n,colour,p)
        elif dicethrow == 3:
            arrayofsquares(n, colour,p)
        elif dicethrow == 4:
            stackofrectanglesandlines(n, colour,p)
        elif dicethrow == 5:
            outsqandlines(n, colour,p)
        elif dicethrow == 6:
            tessellate(n, colour,p)
        elif dicethrow == 7:
            oneroll(n, colour,p)
        elif dicethrow == 8:
            sqdiag(n,colour,p)
        else:
            print("hangfire2")
        si.speed(0)
        si.penup()
        si.fd(700)# blue arrow exits on another mission
        my.down() #setting red arrow ready to fire off
        my.st()
    else:
        print("in reset_turtle_canvas, no grid")
        
    my.pendown()# making sure red arrow is ready to draw

    #Dock the red arrow and get ready for cracking the code    
    #root.wm_attributes("-topmost", 1)   # Make sure window remains on top
    # root.focus()                        # Set focus to window
    #cv.after(500, lambda: root.focus_force())
    #root.wm_attributes("-topmost", 1)
    #cv.focus_force()

################################################### PRINT the python code ################################################



def print_programpy():
    global allow
    global top
    global recordmypy
    
    
    if allow == True:
        allow = False
        recordmypy = pycode + recordmypy
        print(recordmypy)
        #label_instruction.configure(font=programFont14, background='light green', width = 35)
        for j in recordmypy:
            print(j, end = ' ')
            ucode.set(''.join(recordmypy))
            #ecode.set(''.join(recordmypy))
        allow=True
    else:
        print('in print_programpy(), spin')
    pass          

######################################## Method 1 arrays of lines ####################################################              
              


def refetch(pixels):
    si.speed(0)
    si.st()
    for count in range(2):
        si.fd(pixels)
        si.lt(90)
        si.lt(90)

def stacklines(n,length,p):
    # gets in position to draw a stack of n lines of length l
    for k in range(n):
        si.lt(90)
        si.fd(p)
        si.rt(90)
        refetch(length*p)
        
def arrayoflines(n,colour,p):
    # lines stacked two ways to give required array    
    si.up()
    si.color(colour)
    si.down() 
    refetch((n-1)*p)
    stacklines(n-1,n-1,p)
    si.rt(90)
    stacklines(n-1,n-1,p)
    si.fd((n-1)*p)
    si.rt(90)
    si.fd((n-1)*p)
    si.rt(90)
    si.rt(90)
    time.sleep(0.5)

###############################################################################

                    #Method 2: stacking a row of squares

###############################################################################

def sq(pixels):
    si.speed(0)
    for count in range(4):
        si.fd(pixels)
        si.lt(360/4)
        
def rowofsquares(n,p):
    # draws a row of n touching unit squares
    for pp in range(n):
        sq(p)
        si.fd(p)
        
    si.lt(90)
    si.lt(90)
    si.fd(n*p)
    si.lt(90)
    si.lt(90 )
    
def arrayofsquares(n,colour,p):
    # draws an nxn array of touching unit squares
    si.down()
    for steps in range(n):
        rowofsquares(n,p)
        si.up()
        si.lt(90)
        si.fd(p)
        si.rt(90)
        time.sleep(0.2)
        si.down()
        
    si.up()
    si.rt(90)
    si.fd(n*p)
    si.lt(90)
    

###############################################################################

    #Method 3: Stacking a row of rectangles turning at top and repeating

###############################################################################    

def rectangle(length,p):
    si.speed(0)
    for i in range(2):
        si.fd(length)
        si.lt(90)
        si.fd(p)
        si.lt(90)
    
def stackofrectangles(n,p):
    for j in range(n):
        rectangle(n*p,p)
        si.lt(90)
        si.fd(p)
        si.rt(90)
        time.sleep(0.2)
        
def arrayofrectangles(n,colour,p):
    # rectangles stacked two ways to give required array    
    si.up()
    si.color(colour)
    si.down()
    stackofrectangles(n,p)
    si.rt(90)
    stackofrectangles(n,p)
    si.fd(n*p)
    si.rt(90)
    si.fd(n*p)
    si.rt(90)
    si.rt(90)
    



###############################################################################

    #Method 4: Stacking a row of rectangles turning at top
    #and drawing vertical lines

###############################################################################    

def rectangle(length,p):
    si.speed(0)
    for i in range(2):
        si.fd(length)
        si.lt(90)
        si.fd(p)
        si.lt(90)
    
def stackofrectangles(n,p):
    for j in range(n):
        rectangle(n*p,p)
        si.lt(90)
        si.fd(p)
        si.rt(90)
        time.sleep(0.2)
        
def stackofrectanglesandlines(n, colour,p):
    stackofrectangles(n,p)
    time.sleep(0.5)
    si.rt(90)
    stacklines(n-1,n,p)
    si.fd(n*p)
    si.rt(90)
    si.fd((n-1)*p)
    si.lt(180)

###############################################################################

    #Method 5: Set up surrounding square and drawing set of lines
    #both horizontally and vertically

###############################################################################    

def resquare(length):
    si.speed(0)
    for i in range(4):
        si.fd(length)
        si.lt(360/4)
           
def outsqandlines(n, colour,p):
    resquare(n*p)
    stacklines(n-1, n, p)
    si.lt(90)
    si.fd(p) 
    si.lt(90)
    si.lt(90)
    stacklines(n-1, n,p)
    si.fd(n*p)
    si.rt(90)
    si.fd((n-1)*p)
    si.lt(90)
    si.lt(90)


###############################################################################

    #Method 6: TESSELLATION OF SQUARES ON THE DIAGONALS

###############################################################################     



def stair(p):
    si.fd(p)
    si.lt(90)
    si.fd(p)
    si.rt(90)

def halfsq(p):
    si.fd(p)
    si.lt(90)
    si.fd(p)
    si.lt(90)

def staircase(n,p):
    for i in range(n):
        stair(p)
            
def tess(n,p):
    si.speed(0)    
    if n == 1:
        for j in range(4):
            si.fd(p)
            si.lt(90)

    else:
        for i in range(2):
            staircase(n-1,p)
            halfsq(p)


def stairblock(n,p):
    for x in range(n,0, -1):
        tess(x,p)
        si.fd(p)
    
    si.lt(180)
    si.fd(n*p)
    si.lt(180)



def tessellate(n, colour,p):
    si.up()
    si.color(colour)
    si.down()
    
    for y in range(2):
        stairblock(n,p)
        si.fd(n*p)
        si.lt(90)
        si.fd(n*p)
        si.lt(90)
    
###############################################################################

    #Method 7: ONE ROLL TESSELLATION OF SQUARES ON THE OPPOSITE DIAGONALS

###############################################################################     
         

def oneroll(n, colour,p):
    si.up()
    si.color(colour)
    si.down()
    si.up()
    si.fd((n)*p)
    si.down()
    si.speed(0)
    for j in range(1, n+1, 1):
        si.bk(p)
        tess(j,p)

    for j in range(n-1, 0, -1):
        si.lt(90)
        si.fd(p)
        si.rt(90)
        tess(j,p)
    si.rt(90)
    si.fd((n-1)*p)
    si.lt(90)

###############################################################################

    #Method 8: squares and diagonal replay

###############################################################################

def sqdiag(n, colour, p):
    si.speed(0)
    si.color(colour)
    def squared(q):        
        for count in range(4):
            si.fd(q*p)
            si.lt(90)
    for ll in range(2):
        for nn in range(n):
            squared(nn)
        for r in range(2):
            si.fd(n*p)
            si.lt(90)
        
        
    
            



    
    
###############################################################################

    #Method 9: GENII WITH THE MAGIC BOX

############################################################################### 

def genii(n, colour, p):
    print('genii starts here')
    si.speed(0)
    
    magic(si,1,1)

    si.fd(p)
    si.rt(90)
    ############################

    s=2
    while s<= n:
        si.lt(90)
        si.fd(1*p)
        si.lt(90)

        
        
        for i in range(s):
            magic(si,1,1)
            si.fd(p)
        si.lt(90)
        for i in range(s):
            magic(si,1,1)
            si.fd(p)

        si.lt(180)

        for i in range(s+1):
            magic(si,1,1)
            si.fd(p)
        si.rt(90)
        for i in range(s):
            magic(si,1,-1)
            si.fd(p)

        s=s+2

    si.rt(90)
    si.fd((s-1)*p)
    si.lt(180)
    #time.sleep(1)

    

################# START OF GRID SET UP PROGRAM #######################################

#Now add the Shape to the Screen’s shapelist and use it:
# station set up at (0,0)



def dock(tt, p):
    tt.penup()
    tt.st()
    tt.speed(0)
    tt.lt(180)
    if n!=5:
        qq=(int(n/2))*p
        print("qq is", qq)
    else:
        qq=250
        
    tt.fd(qq)
    tt.lt(90)
    tt.fd(qq-p)
    tt.st()
    tt.lt(90)
    
    



def rockstar():
    screen.bgcolor("black") # Set the background color
    si.clear()
    si.penup()
    si.goto(-95, 200)
    si.pendown()
    si.color("gold")
    si.write('Rock Star', align='left', font=("Arial", 24, "bold")) 

    def star5(side):
        for moves in range(5):
            my.fd(side)
            my.rt(2*360/5)     
    my.pensize(1)
    my.color("gold", "black")
    my.speed(0)
    my.clear()
    my.up()
    my.goto(-290,0)
    my.down()

    my.begin_fill()
    for moves in range(56):
        star5(300)
        my.fd(5) # moves 72 pixels
    my.end_fill()    

    time.sleep(0)
    
    my.ht()


#my.color("black","red")

def jive_five():
    si.clear()
    screen.bgcolor("black") # Set the background color
    si.penup()
    si.goto(-75, 200)
    si.pendown()
    si.color("gold")
    si.write('Five Jive', align='left', font=("Arial", 24, "bold")) 

    def star5(side):
        for moves in range(5):
            my.fd(side)
            my.rt(2*360/5)     
    my.pensize(1)
    my.color("gold", "blue")
    my.speed(8)
    my.pensize(2)
    my.clear()
    my.up()
    my.goto(0,-50)
    my.down()

    my.begin_fill()   
    for moves in range(5):
        star5(200)
        my.lt(2*360/5)
    my.end_fill()    

    time.sleep(0)
    
    my.ht()

def sblue():
    
    p=25
    si.up()
    si.color('grey', 'blue')
    si.begin_fill()
    for z in range(4):
        si.fd(p)
        si.lt(90)

    si.end_fill()

def swhite():
    
    p=25
    si.up()
    si.color('grey', 'white')
    si.begin_fill()
    for z in range(4):
        si.fd(p)
        si.lt(90)

    si.end_fill()

def spurs_eight():
    
    screen.bgcolor("white") # Set the background color
    p=25
    pen_is_down=False
    
    si.up()
    si.goto(-200,0)
    si.lt(90)
    si.fd(2*p)
    si.rt(90)
    si.speed(0)
    for moves in range(8):
        si.up()
        sblue()
        si.fd(p)
        si.lt(180)
        sblue()
        si.lt(180)
        swhite()
        si.fd(p)
        si.lt(180)
        swhite()
        si.lt(180)
        si.ht()
        ja.ht()
        my.ht()

    si.lt(90)
    si.fd(p)
    si.lt(90)
    si.down()
    for z in range(2):
        si.fd(16*p)
        si.lt(90)
        si.fd(2*p)
        si.lt(90)
    
   
def swing_eight():   
    si.clear()
    screen.bgcolor("white") # Set the background color
    si.penup()
    si.goto(-120, 200)
    si.pendown()
    si.color("black")
    si.write('Swing Eight', align='left', font=("Arial", 24, "bold")) 

    def octagon(side):
        for moves in range(8):
            my.fd(side)
            my.lt(360/8)     
    my.pensize(2)
    my.color("gold", "black")
    my.speed(8)
    my.clear()
    my.up()
    my.goto(0,-50)
    my.down()

    my.begin_fill()
    for moves in range(8):
        octagon(80)
        my.lt(360/8)
    my.end_fill()    

    time.sleep(0) 

def blank():
    pass

print("in set up")

######################################## !  frame01!   ###########################################################
programFont12 = font.Font(family='Arial', size=10, weight='normal')
programFont14 = font.Font(family='Courier New', size=14, weight='bold')   
programFont16 = font.Font(family='Courier New', size=16, weight='bold')
programFont18 = font.Font(family='Courier New', size=18, weight='bold')
programFont20 = font.Font(family='Courier New', size=20, weight='bold')
programFont24 = font.Font(family='Courier New', size=24, weight='bold')
programFont32 = font.Font(family='Courier New', size=32, weight='bold')

frame1 =Frame(root, bg="light yellow")
frame1.grid(column=0, row=0, sticky=(N,E,W))
frame1.rowconfigure(0, weight=1)
frame1['borderwidth'] = 3
frame1['relief'] = 'raised'
frame1['padx'] = 5
frame1['pady'] = 5
frame1.takefocus = 1

# set up the canvas for drawing
cv = ScrolledCanvas(frame1,width =480, height = 480)
cv.grid(column=0, row=0, sticky=(N))
cv.after(300, lambda: root.focus_force())

ecode = StringVar()
program_box = ttk.Label(frame1, relief=RIDGE, textvariable = ecode,  wraplength= 300, width = 52, padding="5 0 5 0", font=boldFont18)
program_box.grid(column=0, row=1, sticky =(N,S) )
program_box['relief'] = 'raised'
program_box['justify'] = 'left'# justifies within the line
program_box['anchor'] = 'n' # moves to left of the box
program_box['borderwidth'] = 3
program_box['background'] = 'light green'


lower_frame1 =Frame(frame1, bg="light yellow", height=250 )
lower_frame1.grid(column=0, row=2, sticky=(N,E,W,S))
lower_frame1.rowconfigure(0, weight=1)

program_box.configure(background='yellow',wraplength= 400, width = 40, padding="0", font=boldFont16)  
ecode.set("\n Examples of the unique patterns you will be able to design with the Toolboxes on this course.\n\n\n\n\n")


############################################## frame02!   ###########################################

## frame 02 is transferred in this form to all templates which utilise frame 02 with # deletes


frame2 = Frame(root, bg="light yellow", pady=75)
frame2.grid(column=1, row=0, sticky=(N,E,W))
frame2.columnconfigure(0, weight=1)
frame2.rowconfigure(0, weight=1)
frame2['borderwidth'] = 3
frame2['relief'] = 'raised'
#frame2['padding'] = '0' #ltrb

################### 10 branch tree in frame 2 #################################################################

box = Frame(frame2, background="light yellow"  )# container
box.grid(row = 0, column = 0, sticky = (N,E,W))



tools = Frame(frame2, background="light yellow"  )# container
tools.grid(row = 1, column = 0, sticky = (N,E,W))

grids = Frame(frame2, background="light yellow" )
grids.grid(row=2, column=0, sticky =(N,E,W))
#####################  branch 1 box  ###########################################

space10= Frame(box,height=10, bg="light yellow")
space10.grid(column=0, row=0, sticky=(N, W, E))






##################### branch 2  tools  #########################################
tool_lab = Label(tools, text="Toolboxes",font= programFont12, height=1, background="light yellow")
tool_lab.grid(column=0, row=0,sticky=(N))

toolButton1 = Button(tools, text = "Toolbox 1",font= programFont12, height = 1,width=9, command = toolbox1, background = "light blue")
toolButton1.grid(column=0, row=1, sticky=(N,W,E))
toolButton1['relief'] = 'raised'
toolButton1['borderwidth'] = 5
 
toolButton2 = Button(tools, text = "Toolbox 2", font= programFont12, width=9, height = 1, command = toolbox2, background = "light blue")
toolButton2.grid(column=0, row=2, sticky=(N,W,E))
toolButton2['relief'] = 'raised'
toolButton2['borderwidth'] = 5

toolButton3 = Button(tools, text = "Toolbox 3", font= programFont12, height = 1, width=9,command = toolbox3, background = "light blue")
toolButton3.grid(column=0, row=3, sticky=(N,W,E))
toolButton3['relief'] = 'raised'
toolButton3['borderwidth'] = 5

space1017= Frame(tools,height=2, bg="light yellow")
space1017.grid(column=0, row=4, sticky=(N, W, E))

uplbtn = Button(tools, text="'Unplugged'", font= programFont12,  bg = "light blue", height=1, width = 9,\
                command = display_upl)
uplbtn.grid(column = 0, row = 6, sticky = (N,W,E))
uplbtn['relief'] = 'raised'
uplbtn['borderwidth'] = 5

v_lab1 = Label(tools, bg= "light yellow", text= "Languages", font= programFont12, height = 1)
v_lab1.grid(column=0, row= 5, sticky = (N,W,E)) 


pybtn = Button(tools, text=" Python 3 ", font= programFont12, bg = "light blue", width = 9,command = display_py)
#pybtn.grid(column = 0, row = 7, sticky = (N,W, E))
pybtn['relief'] = 'raised'
pybtn['borderwidth'] = 5       



##################################  grid sizes #######################################################

v_lab2= Label(grids, height=1, bg= "light yellow", font= programFont12,  text="  Grids  ", width=7)
v_lab2.grid(column=0, row=0, sticky=(N, W, E))

btn_grid5 = Button(grids, text="   5 x 5  ", font= programFont12,  bg = "light blue", width = 9,  command = grid_5)
btn_grid5.grid(column=0, row=1, sticky= (N))
btn_grid5['relief'] = 'raised'
btn_grid5['borderwidth'] = 5
btn_grid5['anchor'] = 'w'

btn_grid10 = Button(grids, text="  10 x 10 ", font= programFont12, bg = "light blue", height = 1, width = 9,  command = grid_10)
btn_grid10.grid(column=0, row=2, sticky= (N))
btn_grid10['relief'] = 'raised'
btn_grid10['borderwidth'] = 5
btn_grid10['anchor'] = 'w'

btn_grid20 = Button(grids, text="  20 x 20 ", font= programFont12, bg = "light blue", width = 9,  command = grid_20)
btn_grid20.grid(column=0, row=3, sticky= (N))
btn_grid20['relief'] = 'raised'
btn_grid20['borderwidth'] = 5
btn_grid20['anchor'] = 'w'

btn_grid40 = Button(grids, text="  40 x 40 ", font= programFont12, bg = "light blue", width = 9,  command = grid_40)
btn_grid40.grid(column=0, row=4, sticky= (N))
btn_grid40['relief'] = 'raised'
btn_grid40['borderwidth'] = 5
btn_grid40['anchor'] = 'w'

btn_grid80 = Button(grids, text="  80 x 80 ",font= programFont12, bg = "light blue", width = 9,  command = grid_80)
btn_grid80.grid(column=0, row=5, sticky= (N))
btn_grid80['relief'] = 'raised'
btn_grid80['borderwidth'] = 5
btn_grid80['anchor'] = 'w'





btn_nogrid = Button(grids, text="Invisible grid", font= programFont12, bg = "light blue", width = 9, command = gridless)
btn_nogrid.grid(column=0, row=6, sticky= (N))
btn_nogrid['relief'] = 'raised'
btn_nogrid['borderwidth'] = 5
btn_nogrid['anchor'] = 'w'


####################################################  filler  ###########################################






##################################   Frame03!   #########################################################

frame3 = Frame(root, bg="light yellow", padx=5, pady=20)
frame3.grid(column=2, row=0, sticky=(N,E,W))
#frame3.columnconfigure(0, weight=1)
#frame3.rowconfigure(0, weight=1)
frame3['borderwidth'] = 3
frame3['relief'] = 'raised'



inner_frame3 = Frame(frame3, bg = "light yellow", padx =5, pady = 10)
inner_frame3.grid(column=0, row=0, sticky=(N,E,W,S)) 



ucode = StringVar()
label_instruction = ttk.Label(inner_frame3, relief=RIDGE, textvariable = ucode, wraplength= 600, width=75,  font = boldFont12,\
                        background = 'light green',  padding="20 15 20 15")
label_instruction.grid(column=0, row=0, sticky=(N,W))
label_instruction['relief'] = 'raised'
label_instruction['justify'] = 'left'# justifies within the line
label_instruction['anchor'] = 'center' # moves to center of the box
label_instruction['borderwidth'] = 5
 


label_instruction.config(wraplength= 600, width=75,  font = boldFont12)                                    #padding=" 2 2 2 2" )
ucode.set("                              Toolbox 1\n1. Use the  click/touch drawing screen pad\
below, to build your program.\n2. Clear the screen when you need by clicking the 'clear' button.\n3. Fly the\
red arrow for your next assignment.\n4. Use the 'repeat' sequence whenever your code repeats itself.")
    


'''
frame3 = Frame(root, bg="light yellow", padx=5, pady=0)
frame3.grid(column=2, row=0, sticky=(N,E,W))
#frame3.columnconfigure(0, weight=1)
#frame3.rowconfigure(0, weight=1)
#frame3['borderwidth'] = 3
#frame3['relief'] = 'raised'

inner_frame3 = Frame(frame3, bg = "light yellow", padx =5, pady = 5)
inner_frame3.grid(column=0, row=0, sticky=(N,E,W,S)) 



ucode = StringVar()
label_instruction = ttk.Label(inner_frame3, relief=RIDGE, textvariable = ucode, wraplength= 550, width=60,  font = boldFont12,\
                        background = 'light green',  padding="20 15 20 15")
label_instruction.grid(column=0, row=0, sticky=(N,W))
label_instruction['relief'] = 'raised'
label_instruction['justify'] = 'left'# justifies within the line
label_instruction['anchor'] = 'center' # moves to center of the box
label_instruction['borderwidth'] = 5



#padding_f3 = Frame(inner_frame3, background = '', height = 150, width=2)
#padding_f3.grid(column=1, row=0, sticky=(N,W,E,S))

#padding_f3.configure(height=padding_f3["height"],width=padding_f3["width"])
#padding_f3.grid_propagate(0)# no propagation so padding holds the depth so the pad should remain stable 
'''





##################################  frame 4  #######################################################

h_cement=3
v_cement=3


frame4 = Frame(frame3, bg = "light yellow", padx=3, pady = 20)
frame4.grid(row = 1, column = 0, sticky= (N,E,W,S) )

fillerh150= Frame(frame4,height=2, bg="light yellow")
#fillerh150.grid(column=0, row=0, sticky=(N, W, E))
    
pad_box = Frame(frame4, padx=0, pady =5)
pad_box.grid(column=0, row=1, sticky=(N, W, E))
pad_box['relief'] = 'raised'
pad_box['borderwidth'] = 8
pad_box['background'] = 'silver'
pad_box['padx'] = 3
pad_box['pady'] = 3

fillerh120= Frame(frame4,height=10, bg="light yellow")
fillerh120.grid(column=0, row=2, sticky=(N, W, E, S))

#########################################   set up click pad   ###################################

padhead = Label(pad_box, font= boldFont16, text=" Toolbox 1: Sequence, Symmetry and Repetition", width = 40, height = 2)
padhead.grid(row=0, column=0, sticky = (N,E,W,S))
padhead['background'] = 'silver'

mainframe = Frame(pad_box, borderwidth = 2, padx =1, pady =10)
mainframe.grid(column=0, row=1, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe['background'] = 'silver'

mainframe1 = Frame(mainframe)
mainframe1.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe1['background'] = 'silver'

mainframe2 = Frame(mainframe)
mainframe2.grid(column=0, row=1, sticky=(N, W, E, S))
mainframe2['background'] = 'silver'

mainframe3 = Frame(mainframe)
mainframe3.grid(column=0, row=2, sticky=(N, W, E, S))
mainframe3['background'] = 'silver'

mainframe4 = Frame(mainframe)
mainframe4.grid(column=0, row=3, sticky=(N, W, E, S))
mainframe4['background'] = 'silver'

mainframe5 = Frame(mainframe, bg="silver")
mainframe5.grid(column=0, row=4, sticky=(N, W, E, S))

mainframe6 = Frame(mainframe, bg="silver")
mainframe6.grid(column=0, row=5, sticky=(N, W, E, S))

mainframe7 = Frame(mainframe, bg="silver")
mainframe7.grid(column=0, row=6, sticky=(N, W, E, S))

mainframe8 = Frame(mainframe, bg="silver")
mainframe8.grid(column=0, row=7, sticky=(N, W, E, S))

mainframe9 = Frame(mainframe, bg="silver")
mainframe9.grid(column=0, row=8, sticky=(N, W, E, S))

mainframe10 = Frame(mainframe, bg="silver")
mainframe10.grid(column=0, row=9, sticky=(N, W, E, S))

mainframe11 = Frame(mainframe, bg="silver")
mainframe11.grid(column=0, row=10, sticky=(N, W, E, S))

mainframe12 = Frame(mainframe, bg="silver")
mainframe12.grid(column=0, row=11, sticky=(N, W, E, S))

mainframe13 = Frame(mainframe, bg="silver")
mainframe13.grid(column=0, row=12, sticky=(N, W, E, S))


mainframe14 = Frame(mainframe, bg="silver")
mainframe14.grid(column=0, row=13, sticky=(N, W, E, S))

mainframe15 = Frame(mainframe, bg="silver")
mainframe15.grid(column=0, row=14, sticky=(N, W, E, S))

########################## program instructions ###########################################################
programFont12 = font.Font(family='Courier New', size=12, weight='bold')
programFont14 = font.Font(family='Courier New', size=14, weight='bold')   
programFont16 = font.Font(family='Courier New', size=16, weight='bold')
programFont18 = font.Font(family='Courier New', size=18, weight='bold')
programFont20 = font.Font(family='Courier New', size=20, weight='bold')
programFont24 = font.Font(family='Courier New', size=24, weight='bold')
programFont32 = font.Font(family='Courier New', size=32, weight='bold')


        
forward = Label(mainframe1, font= programFont14, text="forward", width = 10)
forward.grid(row=0, column=0, sticky = (W))
forward['anchor'] = 'w'
forward['background'] = 'silver'
                         
btn1 = Button(mainframe1, text="fd1", font= programFont14, bg = "light yellow", width = 5,command = stepout1)
btn1.grid(column = 1, row =0, sticky = (N,W))        
btn1['relief'] = 'raised'
btn1['borderwidth'] = 5

v_cem1 = Frame(mainframe1, bg= "silver", width = v_cement)
v_cem1.grid(column=2, row= 0, sticky = (W))

btn2 = Button(mainframe1, text="fd2", font= programFont14, bg = "light yellow", width = 5,command = stepout2)
btn2.grid(column = 3, row =0, sticky = (N,W))
btn2['relief'] = 'raised'
btn2['borderwidth'] = 5

v_cem2 = Frame(mainframe1, bg= "silver", width = v_cement)
v_cem2.grid(column=4, row= 0, sticky = (W))

btn3 = Button(mainframe1, text="fd3", font= programFont14, bg = "light yellow", width = 5,command = stepout3)
btn3.grid(column = 5, row =0, sticky = (N,W))
btn3['relief'] = 'raised'
btn3['borderwidth'] = 5

v_cem3 = Frame(mainframe1, bg= "silver", width = v_cement)
v_cem3.grid(column=6, row= 0, sticky = (W)) 

btn4 = Button(mainframe1, text="fd4", font= programFont14, bg = "light yellow", width = 5,command = stepout4)
btn4.grid(column = 7, row =0, sticky = (N,W))
btn4['relief'] = 'raised'
btn4['borderwidth'] = 5

v_cem4 = Frame(mainframe1, bg= "silver", width = v_cement)
v_cem4.grid(column=8, row= 0, sticky = (W)) 

btnchoose = Button(mainframe1, text="fd", font= programFont14, bg = "light yellow", width = 4,command = stepout_choose)
btnchoose.grid(column = 9, row =0, sticky = (N,W))
btnchoose['relief'] = 'raised'
btnchoose['borderwidth'] = 5


forward_entry = Entry(mainframe1, bd = 5, width = 2, textvariable = paces,  font= programFont14, bg = 'light yellow')
forward_entry.grid(column=11, row=0, sticky= (N,W,E,S))
#forward_entry.bind("<FocusIn>", forward_act)

fillerm2= Frame(mainframe2, height=h_cement, bg= "silver")
fillerm2.grid(column=0, row=0, sticky=(N, W, E))

left_turn = Label(mainframe3, font= programFont14, text="left turn", width = 10)
left_turn.grid(column=0, row=0, sticky=(W))
left_turn['background'] = 'silver'
left_turn['anchor'] = 'w'

btnleft = Button(mainframe3, text="lt", font= programFont14, bg = "light yellow", width = 5, command = left)
btnleft.grid(column=1, row=0, sticky= (N,W))
btnleft['relief'] = 'raised'
btnleft['borderwidth'] = 5    

left_entry = Entry(mainframe3, bd = 5, width = 7, textvariable = degrees_left,  font= programFont14, bg = 'light yellow')
left_entry.grid(column=2, row=0, sticky= (N,W,E,S))
#left_entry.bind("<FocusIn>", left_act)

left_blank = Label(mainframe3, bd = 5, width = 6,   font= programFont14, bg = 'silver')
#left_blank.grid(column=2, row=0, sticky= (N,W,E,S))

filler2a= Frame(mainframe3, width =5)
filler2a.grid(column=3, row=0, sticky=(N, W, E, S))
filler2a['background'] = 'silver'    

pen_up = Button(mainframe3, text="penup", font= programFont14, bg = "light yellow", width = 5,  command = put_penup)
pen_up.grid(column=4, row=0 , sticky= (N,W))
pen_up['relief'] = 'raised'
pen_up['borderwidth'] = 5
pen_up['anchor'] = 'w'

v_cem5 = Frame(mainframe3, bg= "silver", width = v_cement)
v_cem5.grid(column=5, row= 0, sticky = (W)) 

pen_down = Button(mainframe3, text="pendown", font= programFont14, bg = "light yellow", width = 7,  command = put_pendown)
pen_down.grid(column=6, row=0 , sticky= (N,W))
pen_down['relief'] = 'raised'
pen_down['borderwidth'] = 5
pen_down['anchor'] = 'w'

v_cem6 = Frame(mainframe3, bg= "silver", width = v_cement)
v_cem6.grid(column=7, row= 0, sticky = (W)) 

hide = Button(mainframe3, text="hide", font= programFont14,  bg = "light yellow", width = 3, command=hide_arrow, padx= 10)
hide.grid(column=8, row=0, sticky= (E))
hide['relief'] = 'raised'
hide['borderwidth'] = 5 



fillerm4= Frame(mainframe4, height=h_cement, bg= "silver")
fillerm4.grid(column=0, row=0, sticky=(N, W, E))

right_turn = Label(mainframe5, font= programFont14, text="right turn", width = 10)
right_turn.grid(column=0, row=0, sticky=(W))
right_turn['background'] = 'silver'
right_turn['anchor'] = 'w'

btnright = Button(mainframe5, text="rt", font = programFont14,  bg = "light yellow", width = 5, command = right)
btnright.grid(column=1, row=0, sticky= (N,W))
btnright['relief'] = 'raised'
btnright['borderwidth'] = 5

right_blank = Label(mainframe5, bd = 5, width = 6,font= programFont14, bg = 'silver')
right_blank.grid(column=2, row=0, sticky= (N,W,E,S))

right_entry = Entry(mainframe5, bd = 5, width = 7, textvariable = degrees_right,  font= programFont14, bg = 'light yellow')
right_entry.grid(column=2, row=0, sticky= (N,W,E,S))
#right_entry.bind("<FocusIn>", left_act)

    

filler2= Frame(mainframe5, width = 5)
filler2.grid(column=3, row=0, sticky=(N, W, E, S))
filler2['background'] = 'silver'


delete = Button(mainframe5, text="delete", font= programFont14,  bg = "light blue", width = 6, command = delete_op )
delete.grid(column=4, row=0, sticky= (E))
delete['relief'] = 'raised'
delete['borderwidth'] = 5

v_cem7 = Frame(mainframe5, bg= "silver", width = v_cement)
v_cem7.grid(column=5, row= 0, sticky = (W)) 

clear = Button(mainframe5, text="clear", font= programFont14,  bg = "light blue", width = 3, command=full_delete, padx= 10)
clear.grid(column=6, row=0, sticky= (E))
clear['relief'] = 'raised'
clear['borderwidth'] = 5

v_cem8 = Frame(mainframe5, bg= "silver", width = v_cement)
v_cem8.grid(column=7, row= 0, sticky = (W)) 

newline = Button(mainframe5, text="newline", font= programFont14,  bg = "light blue", width = 5, command=new_line, padx= 10)
newline.grid(column=8, row=0, sticky= (E))
newline['relief'] = 'raised'
newline['borderwidth'] = 5

v_cem9 = Frame(mainframe5, bg= "silver", width = v_cement)
v_cem9.grid(column=9, row= 0, sticky = (W)) 

fillera50= Frame(mainframe5, height=h_cement, bg = "silver")
fillera50.grid(column=0, row=1, sticky=(N, W, E))



################################### repeat control structure #############################################################


repeat_btn= Button(mainframe6, text="repeat", width = 6, font = programFont16, command = setup_repeat)
repeat_btn.grid(column=0, row=1, sticky=(W))
repeat_btn['background'] = 'light yellow'
repeat_btn['relief'] = 'raised'
repeat_btn['borderwidth'] = 5


filler25= Frame(mainframe6, width = 4)
filler25.grid(column=1, row=1, sticky=(N, W, E, S))
filler25['background'] = 'silver'


times = StringVar()
times.set('')
tim = Entry(mainframe6,bd = 5, width = 2, textvariable = times,  font= programFont14, bg = 'light yellow')
tim.grid(column=2, row=1, sticky= (E,W))
tim.bind("<FocusIn>", act)


filler3= Frame(mainframe6, width = 2)
filler3.grid(column=3, row=1, sticky=(N, W,E,S))
filler3['background'] = 'silver'

bracketleft = Label(mainframe6, text='[', font= programFont32, bg = "silver", width = 1)
bracketleft.grid(column=4, row=1, sticky= (N))


brackets = Label(mainframe6, text=in_repeat_code,textvariable = in_repeat_code, font= programFont18,\
                 bg = "light yellow", width = 32)
brackets.grid(column=5, row=1, sticky= (W,E))
brackets.configure(font=programFont12)
in_repeat_code.set('***')

bracketright = Label(mainframe6, text=']', font= programFont32, bg = "silver", width = 1)
bracketright.grid(column=6, row=1, sticky= (N,W))

filler4= Frame(mainframe6, width = 2)
filler4.grid(column=7, row=1, sticky=(N, W, E, S))
filler4['background'] = 'silver'

gobtn = Button(mainframe6, text="do it", font= programFont16, bg = "light yellow",  command = execute_repeat, width = 5)
gobtn.grid(column=8, row=1, sticky= (E,W))
gobtn['relief'] = 'raised'
gobtn['borderwidth'] = 5


 ######################################    colour tabs    ########################################################


colourlab = Label(mainframe7, font= programFont14, text="colour", width = 10)
#colourlab.grid(column=0, row=0, sticky=(N,W,E,S))
colourlab['background'] = 'silver'
colourlab['anchor'] = 'w'

cbtn1 = Button(mainframe7, text="red", font= programFont14, bg = "red", fg = "white", width = 5,command = red)
#cbtn1.grid(column = 1, row =0, sticky = (N,W))        
cbtn1['relief'] = 'raised'
cbtn1['borderwidth'] = 5

v_cem10 = Frame(mainframe7, bg= "silver", width = v_cement)
#v_cem10.grid(column=2, row= 0, sticky = (W)) 


cbtn2 = Button(mainframe7, text="blue", font= programFont14, bg = "blue",fg = "white", width = 5,command = blue)
#cbtn2.grid(column = 3, row =0, sticky = (N,E,W,S))
cbtn2['relief'] = 'raised'


v_cem11 = Frame(mainframe7, bg= "silver", width = v_cement)
#v_cem11.grid(column=4, row= 0, sticky = (W)) 


cbtn3 = Button(mainframe7, text="green", font= programFont14, bg = "green",fg = "white", width = 6,command = green)
#cbtn3.grid(column = 7, row =0, sticky = (N,W))
cbtn3['relief'] = 'raised'
cbtn3['borderwidth'] = 5

v_cem12 = Frame(mainframe7, bg= "silver", width = v_cement)
#v_cem12.grid(column=8, row= 0, sticky = (W)) 

cbtn4 = Button(mainframe7, text="black", font= programFont14, bg = "black",fg = "white", width = 6,command = black)
#cbtn4.grid(column = 9, row =0, sticky = (N,W))
cbtn4['relief'] = 'raised'
cbtn4['borderwidth'] = 5

v_cem13 = Frame(mainframe7, bg= "silver", width = v_cement)
#v_cem13.grid(column=10, row= 0, sticky = (W)) 

cbtn5 = Button(mainframe7, text="gold", font= programFont14, bg = "gold",fg = "black", width = 6,command = gold)
#cbtn5.grid(column = 11, row =0, sticky = (N,W))
cbtn5['relief'] = 'raised'
cbtn5['borderwidth'] = 5

v_cem14 = Frame(mainframe7, bg= "silver", width = v_cement)
#v_cem14.grid(column=12, row= 0, sticky = (W)) 

cbtn6 = Button(mainframe7, text="white", font= programFont14, bg = "white",fg = "black", width = 6,command = white)
#cbtn6.grid(column = 13, row =0, sticky = (N,W))
cbtn6['relief'] = 'raised'
cbtn6['borderwidth'] = 5





    ######################################    fetchT1 #########################################################




about_turn = Label(mainframe8, font= programFont14, text="about turn", width = 10)
#about_turn.grid(column=0, row=0, sticky=(W,E))
about_turn['background'] = 'silver'
about_turn['anchor'] = 'w'

about_turn = Button(mainframe8, text="at", font= programFont14,  bg = "light green", width = 5, command = aboutturn )
#about_turn.grid(column=1, row=0, sticky= (W))
about_turn['relief'] = 'raised'
about_turn['borderwidth'] = 5

diagbtn = Button(mainframe8, text="diag", font= programFont14,  bg = "light green", width = 5, command = diagonal )
#diagbtn.grid(column=2, row=0, sticky= (W))
diagbtn['relief'] = 'raised'
diagbtn['borderwidth'] = 5

arcbtn = Button(mainframe8, text="arc", font= programFont14,  bg = "light green", width = 5, command = at )
#arcbtn.grid(column=3, row=0, sticky= (W))
arcbtn['relief'] = 'raised'
arcbtn['borderwidth'] = 5 




ufetch =Label(mainframe9, font= programFont14, text="fetch", width = 10)
ufetch.grid(row=0, column=0, sticky = (W))
ufetch['anchor'] = 'w'
ufetch['background'] = 'silver'
                                        
febtn1 = Button(mainframe9, text="fe1", font= programFont14, bg = "light green", width = 5,command = fetchout1)
febtn1.grid(column = 1, row =0, sticky = (N,W))        
febtn1['relief'] = 'raised'
febtn1['borderwidth'] = 5

v_cem20 = Frame(mainframe9, bg= "silver", width = v_cement)
v_cem20.grid(column=2, row= 0, sticky = (W))

febtn2 = Button(mainframe9, text="fe2", font= programFont14, bg = "light green", width = 5,command = fetchout2)
febtn2.grid(column = 3, row =0, sticky = (N,W))
febtn2['relief'] = 'raised'
febtn2['borderwidth'] = 5

v_cem21 = Frame(mainframe9, bg= "silver", width = v_cement)
v_cem21.grid(column=4, row= 0, sticky = (W))

febtn3 = Button(mainframe9, text="fe3", font= programFont14, bg = "light green", width = 5,command = fetchout3)
febtn3.grid(column = 5, row =0, sticky = (N,W))
febtn3['relief'] = 'raised'
febtn3['borderwidth'] = 5

v_cem22 = Frame(mainframe9, bg= "silver", width = v_cement)
v_cem22.grid(column=6, row= 0, sticky = (W))

febtn4 = Button(mainframe9, text="fe4", font= programFont14, bg = "light green", width = 5,command = fetchout4)
febtn4.grid(column = 7, row =0, sticky = (N,W))
febtn4['relief'] = 'raised'
febtn4['borderwidth'] = 5

v_cem23 = Frame(mainframe9, bg= "silver", width = v_cement)
v_cem23.grid(column=8, row= 0, sticky = (W)) 


#febtn5 = Button(user_mainframe, text="fe5", font= programFont14, bg = "light green", width = 5,command = stepout4)
#febtn5.grid(column = 9, row = 1, sticky = (N,W))
#febtn5['relief'] = 'raised'
#febtn5['borderwidth'] = 5

#v_cem24 = Frame(user_mainframe, bg= "silver", width = v_cement)
#v_cem24.grid(column=10, row= 1, sticky = (W))


fechoose = Button(mainframe9, text="fe", font= programFont14, bg = "light green", width = 3,command = fetchout_choose)
fechoose.grid(column = 9, row = 0, sticky = (N,W))
fechoose['relief'] = 'raised'
fechoose['borderwidth'] = 5


fetch_entry = Entry(mainframe9, bd = 5, width = 2, textvariable = fpaces, \
                    font= programFont14, bg = 'light green')
fetch_entry.grid(column=10, row= 0, sticky= (N,W,S))
#fetch_entry.bind("<FocusIn>", forward_act)




#fillerm20= Frame(user_mainframe, height=h_cement, bg= "silver")
#fillerm20.grid(column=0, row=2, sticky=(N, W, E))






fillerm12= Frame(mainframe9, height= 3*h_cement, bg= "silver")
#fillerm12.grid(column= 11, row=1, sticky=(N, W, E))

#label_instruction.config(text="Use the toolbox set out below.",bg = "yellow")
#label_instruction.grid(column=0, row=0, sticky=(N,W))

#fillerm2001= Frame(pad2, height=3*h_cement, bg= "silver")
#fillerm2001.grid(column=0, row=1, sticky=(N, W, E)) 

#####################################rectangle #################################    


urect =Label(mainframe10, font= programFont14, text="rectangle", width = 10)
urect.grid(row=0, column=0, sticky = (W))
urect['anchor'] = 'w'
urect['background'] = 'silver'
                                        
rebtn1 = Button(mainframe10, text="re1", font= programFont14, bg = "light green", width = 5,command = rectout1)
rebtn1.grid(column = 1, row =0, sticky = (N,W))        
rebtn1['relief'] = 'raised'
rebtn1['borderwidth'] = 5

v_cem220 = Frame(mainframe10, bg= "silver", width = v_cement)
v_cem220.grid(column=2, row= 0, sticky = (W))

rebtn2 = Button(mainframe10, text="re2", font= programFont14, bg = "light green", width = 5,command = rectout2)
rebtn2.grid(column = 3, row =0, sticky = (N,W))
rebtn2['relief'] = 'raised'
rebtn2['borderwidth'] = 5

v_cem221 = Frame(mainframe10, bg= "silver", width = v_cement)
v_cem221.grid(column=4, row= 0, sticky = (W))

rebtn3 = Button(mainframe10, text="re3", font= programFont14, bg = "light green", width = 5,command = rectout3)
rebtn3.grid(column = 5, row =0, sticky = (N,W))
rebtn3['relief'] = 'raised'
rebtn3['borderwidth'] = 5

v_cem222 = Frame(mainframe10, bg= "silver", width = v_cement)
v_cem222.grid(column=6, row= 0, sticky = (W))

rebtn4 = Button(mainframe10, text="re4", font= programFont14, bg = "light green", width = 5,command = rectout4)
rebtn4.grid(column = 7, row =0, sticky = (N,W))
rebtn4['relief'] = 'raised'
rebtn4['borderwidth'] = 5

v_cem223 = Frame(mainframe10, bg= "silver", width = v_cement)
v_cem223.grid(column=8, row= 0, sticky = (W)) 


#febtn5 = Button(user_mainframe, text="fe5", font= programFont14, bg = "light green", width = 5,command = stepout4)
#febtn5.grid(column = 9, row = 1, sticky = (N,W))
#febtn5['relief'] = 'raised'
#febtn5['borderwidth'] = 5

#v_cem24 = Frame(user_mainframe, bg= "silver", width = v_cement)
#v_cem24.grid(column=10, row= 1, sticky = (W))


rechoose = Button(mainframe10, text="re", font= programFont14, bg = "light green", width = 3,command = rectout_choose)
rechoose.grid(column = 9, row = 0, sticky = (N,W))
rechoose['relief'] = 'raised'
rechoose['borderwidth'] = 5


retch_entry = Entry(mainframe10, bd = 5, width = 2, textvariable = rpaces, \
                    font= programFont14, bg = 'light green')
retch_entry.grid(column=10, row= 0, sticky= (N,W,S))




#fetch_entry.bind("<FocusIn>", forward_act)


#fillerm20= Frame(user_mainframe, height=h_cement, bg= "silver")
#fillerm20.grid(column=0, row=2, sticky=(N, W, E))






fillerm12= Frame(mainframe9, height= 3*h_cement, bg= "silver")
#fillerm12.grid(column= 11, row=1, sticky=(N, W, E))

#label_instruction.config(text="Use the toolbox set out below.",bg = "yellow")
#label_instruction.grid(column=0, row=0, sticky=(N,W))

#fillerm2001= Frame(pad2, height=3*h_cement, bg= "silver")
#fillerm2001.grid(column=0, row=1, sticky=(N, W, E))


#####################################rectangle #################################    


usq =Label(mainframe11, font= programFont14, text="square", width = 10)
usq.grid(row=0, column=0, sticky = (W))
usq['anchor'] = 'w'
usq['background'] = 'silver'
                                        
sqbtn1 = Button(mainframe11, text="sq1", font= programFont14, bg = "light green", width = 5,\
                command = sqout1)
sqbtn1.grid(column = 1, row =0, sticky = (N,W))        
sqbtn1['relief'] = 'raised'
sqbtn1['borderwidth'] = 5

v_cem320 = Frame(mainframe11, bg= "silver", width = v_cement)
v_cem320.grid(column=2, row= 0, sticky = (W))

sqbtn2 = Button(mainframe11, text="sq2", font= programFont14, bg = "light green", width = 5,command = sqout2)
sqbtn2.grid(column = 3, row =0, sticky = (N,W))
sqbtn2['relief'] = 'raised'
sqbtn2['borderwidth'] = 5

v_cem321 = Frame(mainframe11, bg= "silver", width = v_cement)
v_cem321.grid(column=4, row= 0, sticky = (W))

sqbtn3 = Button(mainframe11, text="sq3", font= programFont14, bg = "light green", width = 5,command = sqout3)
sqbtn3.grid(column = 5, row =0, sticky = (N,W))
sqbtn3['relief'] = 'raised'
sqbtn3['borderwidth'] = 5

v_cem322 = Frame(mainframe11, bg= "silver", width = v_cement)
v_cem322.grid(column=6, row= 0, sticky = (W))

sqbtn4 = Button(mainframe11, text="sq4", font= programFont14, bg = "light green", width = 5,command = sqout4)
sqbtn4.grid(column = 7, row =0, sticky = (N,W))
sqbtn4['relief'] = 'raised'
sqbtn4['borderwidth'] = 5

v_cem323 = Frame(mainframe11, bg= "silver", width = v_cement)
v_cem323.grid(column=8, row= 0, sticky = (W)) 


#febtn5 = Button(user_mainframe, text="fe5", font= programFont14, bg = "light green", width = 5,command = stepout4)
#febtn5.grid(column = 9, row = 1, sticky = (N,W))
#febtn5['relief'] = 'raised'
#febtn5['borderwidth'] = 5

#v_cem24 = Frame(user_mainframe, bg= "silver", width = v_cement)
#v_cem24.grid(column=10, row= 1, sticky = (W))


sqchoose = Button(mainframe11, text="sq", font= programFont14, bg = "light green", width = 3,command = sqout_choose)
sqchoose.grid(column = 9, row = 0, sticky = (N,W))
sqchoose['relief'] = 'raised'
sqchoose['borderwidth'] = 5


sqtch_entry = Entry(mainframe11, bd = 5, width = 2, textvariable = sqpaces, \
                    font= programFont14, bg = 'light green')
sqtch_entry.grid(column=10, row= 0, sticky= (N,W,S))
#fetch_entry.bind("<FocusIn>", forward_act)




#fillerm20= Frame(user_mainframe, height=h_cement, bg= "silver")
#fillerm20.grid(column=0, row=2, sticky=(N, W, E))






fillerm12= Frame(mainframe9, height= 3*h_cement, bg= "silver")
#fillerm12.grid(column= 11, row=1, sticky=(N, W, E))

#label_instruction.config(text="Use the toolbox set out below.",bg = "yellow")
#label_instruction.grid(column=0, row=0, sticky=(N,W))

#fillerm2001= Frame(pad2, height=3*h_cement, bg= "silver")
#fillerm2001.grid(column=0, row=1, sticky=(N, W, E)) 












############################### After structure Set up:INITIALISATION OF VARIABLES #####################################







programFont12 = font.Font(family='Courier New', size=12, weight='bold')
programFont14 = font.Font(family='Courier New', size=14, weight='bold')   
programFont16 = font.Font(family='Courier New', size=16, weight='bold')
programFont18 = font.Font(family='Courier New', size=18, weight='bold')
programFont20 = font.Font(family='Courier New', size=20, weight='bold')
programFont24 = font.Font(family='Courier New', size=24, weight='bold')
programFont32 = font.Font(family='Courier New', size=32, weight='bold')
   
italicFont14 = font.Font(family='Arial', size=14, weight='normal')
italicFont16 = font.Font(family='Arial', size=16, weight='normal')

########################### initialising the variables p, user_functionspy ####################################

################################# global objects   ############################################################

allow=True #allows events to operate. prevents events interrupting each other
tb1 = False # in toolbox1
tb2 = False
tb3 = False
p=100 # grid square size in pixels 
n=5 # 5x5 grid
no_grid = False
timesrep=0
uplshow=False # displayed version of upl program
pyshow=False
pen_is_down=True #default is  pendown for drawing so act on action
ok_repeat=False # action in or out of a repeat loop
steps=''
#paces.set('10')
go = "" # text python program(code) for repeat as a string
gop =[] #equivalent python program in a list to the upl program in gou when setting up 'repeat' structure
gou = [] # text upl program for repeat as a list
gg=-1 # counter for 'gou' of upl instr inside a repeat loop and gop
fix_angle = 0
record = []# list holding record of 'unplugged' program, upl, button press 'unplugged' to be printed in Python Interactive shell
recordpy = []#py code for display program, button press 'python'
recordmypy = []# mypy code for execution
pycode = ['from turtle import *\n']

uuu = ''.join(record)

top = -1# counter for 'record'  list of upl instructions, top points to the  top instruction in record, recordmypy
fun1=''
fun1_is_set = False
fun2=''
fun2_is_set = False
fun3=''
fun3_is_set = False
fun4=''
fun4_is_set = False

arc_fun = ['','','','',''] # what remains after 'clear' is held here
arc_funpy = ['','','','',''] # "     "      "     "




user_functionspy = ['', fun1, fun2, fun3, fun4]

#toolButton1.invoke() # invokes toolbox1() for pad

for child in root.winfo_children(): child.grid_configure(padx=2, pady=0)

#root.bind("<Return>", callback)




######################################################################################################################

#                                         Set up Turtle canvas

#######################################################################################################################
    

#set up red and blue arrows in the space station 

my = RawTurtle(cv)# set up my as a raw turtle to operate on the scrolled canvas
my.ht()
screen = my.getscreen()# name and set screen inside cv canvas
my.ht()
screen.screensize(480,480)
screen.setworldcoordinates(-300,-300, 300, 300) # set the window gridding
my.ht()
screen.bgcolor("white") # Set the background color
my.ht()
#screen.title("Hijinks with the Turtles") # Change the window title: not possible in RawTurtle?
#screen.turtles() # doesn't appear to work either

si= RawTurtle(cv) # silva the spaceship blue arrowbot
si.ht()

ja = RawTurtle(cv) # jack the docking spacestation
ja.ht()
#set spacestation up
s = Shape("compound")
poly1 = ((0,-5),(15,-12.5),(0,10),(-15,-12.5))
s.addcomponent(poly1, "white", "black")
poly2 = ((15,-12.5),(15,-17.5))
s.addcomponent(poly2, "white", "black")
poly3 = ((-15,-12.5),(-15,-17.5))
s.addcomponent(poly3, "white", "black")
#poly4 = ((10,-20),(-10,-20))
#s.addcomponent(poly4, "white", "white")
#poly5 = ((-10,-20),(-15,-25))
#s.addcomponent(poly5, "white", "black")
screen.register_shape("spacestation",s)

r = Shape("compound")
poly1 = ((0,0),(10,-5),(0,10),(-10,-5))
r.addcomponent(poly1, "red", "black")
#Now add the Shape to the Screen’s shapelist and use it:
screen.register_shape("starshapered", r)

b = Shape("compound")
poly1 = ((0,0),(10,-5),(0,10),(-10,-5))
b.addcomponent(poly1, "blue", "black")

#Now add the Shape to the Screen’s shapelist and use it:
screen.register_shape("starshapegrey", b)

g = Shape("compound")
poly1 = ((0,0),(10,-5),(0,10),(-10,-5))
g.addcomponent(poly1, "green", "black")
#Now add the Shape to the Screen’s shapelist and use it:
screen.register_shape("starshapegreen", g)

root.wm_attributes("-topmost", 1)
root.focus_force()

'''
Parameters:	
arg – object to be written to the TurtleScreen
move – True/False
align – one of the strings “left”, “center” or right”
font – a triple (fontname, fontsize, fonttype)
Write text - the string representation of arg - at the current turtle position according to align (“left”, “center” or right”) and with the given font. If move is true, the pen is moved to the bottom-right corner of the text. By default, move is False.

>>> turtle.write("Home = ", True, align="center")
>>> turtle.write((0,0), True)
'''
   


fillerh120= Frame(frame4,height=150, bg="light yellow")
fillerh120.grid(column=0, row=2, sticky=(N, W, E, S))

root.wm_attributes("-topmost", 1)
root.focus_force()

allow=False
dicethrow = random.randint(1,4)
#dicethrow = 5
if dicethrow == 1:
    swing_eight()
if dicethrow == 2:
    jive_five()
if dicethrow==3:
    rockstar()
if dicethrow==4:
    spurs_eight()
#if dicethrow==5:
time.sleep(0.5)   
allow = True
toolbox1()



##******************* event handler functions************

# The next functions are our "event handlers".

# These lines "wire up" keypresses to the handlers we've defined.

#forward use uparrow key or 1 key to move forward 1 pacemy.bk(p)
#       similarly d or 2 key for 2 paces forward
#           and   t or 5 key for 5 paces forward

screen.onkey(single, "Up")
screen.onkey(single, "1")
screen.onkey(double, "d")
screen.onkey(double, "2")
screen.onkey(treble, "t")
screen.onkey(treble, "3")
#screen.onkey(aboutturn, "a")
screen.onkey(print_programpy, "p")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(quit, "q")
#screen.onkey(smooth, "space")
screen.onkey(delete_op, "Delete")
#screen.onkey(print_program, "u")




        
    

def main():
    pad=True
    screen.listen()
    root.mainloop()

if __name__ ==  "__main__":
    main()


'''Both modules and instances create their own namespaces,
and the syntax for accessing names contained in each, called attributes,
is the same. In this case the attribute we are selecting is a data item
from an instance.'''



'''canvas.bgcolor('yellow')
    canvas.bgpic("slide0opener.gif")
    canvas.title("page 0: turtle hijinks")
    print('display0 executed')'''

'''We can refer to keys on the keyboard by their character code (as we did in
line 26), or by their symbolic names. Some of the symbolic names to try are
Cancel (the Break key), BackSpace, Tab, Return(the Enter key),
Shift_L (any Shift key), Control_L (any Control key), Alt_L (any Alt key),
Pause, Caps_Lock, Escape, Prior (Page Up), Next (Page Down), End, Home,
Left, Up, Right, Down, Print, Insert, Delete, F1, F2, F3, F4, F5, F6, F7,
F8, F9, F10, F11, F12, Num_Lock, and Scroll_Lock.'''


############################################## ucode! ecode! #####################################################


