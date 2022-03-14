from tkinter import *
root = Tk()
root.geometry('190x165')
root.title("BMI")
root.configure(bg ='#561594')
root.resizable(False , False)
def Calculate():
    h = Entry_Height.get()
    m = Entry_Mass.get()
    bmi = int(m) / (int(h) / 100)**2
    var1 =StringVar()
    Label(root , text= int(bmi) , bg = '#561594' ,fg ='#cde01b' ,font= ('bold'  , 15)).place(x =60 , y = 70)
    if bmi < 18.5:
        var1.set('Underweight ♥         ')
        Label(root, textvariable=var1, bg='#561594', fg='#cde01b', font=('bold', 12)).place(x=85, y=134)
    elif bmi > 18.5 and bmi < 25:
        var1.set('Healthy ♥♥          ')
        Label(root, textvariable=var1, bg='#561594', fg='#cde01b', font=('bold', 13)).place(x=85, y=134)
    elif bmi > 25 and bmi < 30:
        var1.set('Overweight ♥          ')
        Label(root, textvariable=var1, bg='#561594', fg='#cde01b', font=('bold', 13)).place(x=85, y=134)
    elif bmi >= 30:
        var1.set('Obese 💀             ')
        Label(root, textvariable=var1, bg='#561594', fg='#cde01b', font=('bold', 13)).place(x=85, y=134)
def exitt():
    exit()
label_Height = Label(root , text = 'Height:' , fg = '#cde01b' , bg='#561594'  , font = ('bold' , 15)).place(x =0 , y = 0)
label_Mass = Label(root , text = 'Mass:' , fg = '#cde01b' , bg='#561594'  , font = ('bold' , 15)).place(x =5 , y = 30)
label_bmi = Label(root , text = 'Bmi:' , fg = '#cde01b' , bg='#561594'  , font = ('bold' , 15)).place(x =20 , y = 70)
label_situation  = Label(root , text = 'Situation:' , fg = '#cde01b' , bg='#561594'  , font = ('bold' , 15)).place(x =0,y =130)
label_mark  = Label(root , text = '─────────────' , fg = '#cde01b' , bg='#561594'  , font = ('bold' , 15)).place(x =0 , y =100)
Entry_Height = Spinbox(root , from_ = 1  , to = 300 , state="readonly")
Entry_Mass = Spinbox(root , from_ = 1  , to = 300, state="readonly")
Entry_Height.place(x = 70 , y= 6 , width = 38 ,height = 25)
Entry_Mass.place(x = 70 , y= 35 , width = 38,height = 25)
btn_start = Button(root , text = 'Calculate' , command = Calculate , bg ='#561594' , fg = '#cde01b' , bd = 5 ,  activebackground= '#561594').place(x = 115 , y= 6 , height = 50)
btn_exit = Button(root , text = 'Exit' , command = exitt , bg ='#561594' , fg = '#cde01b' , bd = 5 ,  activebackground= '#561594').place(x = 115 , y= 60 , height = 50 , width = 65)
mainloop()