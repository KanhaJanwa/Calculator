from tkinter import *

root=Tk()

root.title('Calculator')
root.configure(background='khaki')
root.geometry('400x300')

expression=" "
equation=StringVar()


def press(num):
    global expression
    expression=expression+str(num)
    equation.set(expression)

def equal():
    global expression
    total=str(eval(expression))
    equation.set(total)
    expression=" "

def clear():
    t1.delete(first=0,last=200)

# LAMBDA - argument leke expression deta h
# eval - evaluate krta h int m


t1=Entry(root,width='38',text=equation,fg='red',bg='orange',font=('times',15,'italic'))
t1.place(x=10,y=10)

btn1=Button(root,text='1',width='10',command=lambda:press('1'),fg='black',bg='gray79',activebackground='green',font=('times',9,'bold'))
btn1.place(x=10,y=60)

btn4=Button(root,text='4',width='10',fg='black',bg='gray79',command=lambda:press('4'),activebackground='green',font=('times',9,'bold'))
btn4.place(x=10,y=100)

btn7=Button(root,text='7',width='10',fg='black',bg='gray79',command=lambda:press('7'),activebackground='green',font=('times',9,'bold'))
btn7.place(x=10,y=140)

btn2=Button(root,text='2',width='10',fg='black',bg='gray79',command=lambda:press('2'),activebackground='green',font=('times',9,'bold'))
btn2.place(x=110,y=60)

btn5=Button(root,text='5',width='10',fg='black',bg='gray79',activebackground='green',command=lambda:press('5'),font=('times',9,'bold'))
btn5.place(x=110,y=100)

btn8=Button(root,text='8',width='10',fg='black',bg='gray79',activebackground='green',command=lambda:press('8'),font=('times',9,'bold'))
btn8.place(x=110,y=140)

btn3=Button(root,text='3',width='10',fg='black',bg='gray79',activebackground='green',command=lambda:press('3'),font=('times',9,'bold'))
btn3.place(x=210,y=60)

btn6=Button(root,text='6',width='10',fg='black',bg='gray79',activebackground='green',command=lambda:press('6'),font=('times',9,'bold'))
btn6.place(x=210,y=100)

btn9=Button(root,text='9',width='10',fg='black',bg='gray79',activebackground='green',font=('times',9,'bold'),command=lambda:press('9'))
btn9.place(x=210,y=140)

btn0=Button(root,text='0',width='10',fg='black',bg='gray79',activebackground='green',command=lambda:press('0'),font=('times',9,'bold'))
btn0.place(x=110,y=180)

btn11=Button(root,text='clear',width='10',fg='black',bg='gray79',activebackground='green',command=clear,font=('times',9,'bold'))
btn11.place(x=10,y=180)

btn12=Button(root,text='=',width='10',fg='black',bg='gray79',activebackground='green',command=equal,font=('times',9,'bold'))
btn12.place(x=210,y=180)

btn13=Button(root,text='+',width='10',fg='black',bg='gray79',activebackground='green',command=lambda:press('+'),font=('times',9,'bold'))
btn13.place(x=310,y=60)

btn14=Button(root,text='-',width='10',fg='black',bg='gray79',activebackground='green',command=lambda:press('-'),font=('times',9,'bold'))
btn14.place(x=310,y=100)

btn15=Button(root,text='*',width='10',fg='black',bg='gray79',activebackground='green',command=lambda:press('*'),font=('times',9,'bold'))
btn15.place(x=310,y=140)

btn16=Button(root,text='/',width='10',fg='black',bg='gray79',activebackground='green',command=lambda:press('/'),font=('times',9,'bold'))
btn16.place(x=310,y=180)

root.mainloop()