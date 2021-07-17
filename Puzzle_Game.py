from tkinter import *
from tkinter import messagebox
import random

def clicked1():
    global i
    if i<=8:
        i=i+1
        cell1.configure(text=i)
    elif i>8:
        i=0
        cell1.configure(text=i)
        
def clicked2():
    global j
    if j<=8:
        j+=1
        cell2.configure(text=j)
    elif j>8:
        j=0
        cell2.configure(text=j)

def clicked3():
    global k
    if k<=8:
        k+=1
        cell3.configure(text=k)
    elif k>8:
        k=0
        cell3.configure(text=k)
        
def clicked4():
    global l
    if l<=8:
        l+=1
        cell4.configure(text=l)
    elif l>8:
        l=0
        cell4.configure(text=l)

def clicked5():
    global m
    if m<=8:
        m+=1
        cell5.configure(text=m)
    elif m>8:
        m=0
        cell5.configure(text=m)

def clicked6():
    global n
    if n<=8:
        n+=1
        cell6.configure(text=n)
    elif n>8:
        n=0
        cell6.configure(text=n)

def clicked7():
    global p
    if p<=8:
        p+=1
        cell7.configure(text=p)
    elif p>8:
        p=0
        cell7.configure(text=p)

def clicked8():
    global q
    if q<=8:
        q+=1
        cell8.configure(text=q)
    elif q>8:
        q=0
        cell8.configure(text=q)

def clicked9():
    global r
    if r<=8:
        r+=1
        cell9.configure(text=r)
    elif r>8:
        r=0
        cell9.configure(text=r)

def enter():
    global life, i, j, k, l, m, n, p, q, r, key
    life=life+1

    if life<=10:
        label_life.config(text=f'{life}/10')
        
    if i == key[0]:
        label_r1.config(bg='light green')
        label_c1.config(bg='light green')
    else:
        label_r1.config(bg='black')
        label_c1.config(bg='black')
    if j==key[1]:
        label_r2.config(bg='light green')
        label_c4.config(bg='light green')
    else:
        label_r2.config(bg='black')
        label_c4.config(bg='black')
    if k==key[2]:
        label_r3.config(bg='light green')
        label_c7.config(bg='light green')
    else:
        label_r3.config(bg='black')
        label_c7.config(bg='black')
    if l==key[3]:
        label_r4.config(bg='light green')
        label_c2.config(bg='light green')
    else:
        label_r4.config(bg='black')
        label_c2.config(bg='black')
    if m==key[4]:
        label_r5.config(bg='light green')
        label_c5.config(bg='light green')
    else:
        label_r5.config(bg='black')
        label_c5.config(bg='black')
    if n==key[5]:
        label_r6.config(bg='light green')
        label_c8.config(bg='light green')
    else:
        label_r6.config(bg='black')
        label_c8.config(bg='black')
    if p==key[6]:
        label_r7.config(bg='light green')
        label_c3.config(bg='light green')
    else:
        label_r7.config(bg='black')
        label_c3.config(bg='black')
    if q==key[7]:
        label_r8.config(bg='light green')
        label_c6.config(bg='light green')
    else:
        label_r8.config(bg='black')
        label_c6.config(bg='black')
    if r==key[8]:
        label_r9.config(bg='light green')
        label_c9.config(bg='light green')
    else:
        label_r9.config(bg='black')
        label_c9.config(bg='black')

#Condition for Game Passed, all the labels to be green

    if life <=10:
        
        if (label_r1['bg']=='light green' and label_r2['bg']=='light green' and
            label_r3['bg']=='light green' and label_r4['bg']=='light green' and
            label_r5['bg']=='light green' and label_r6['bg']=='light green' and
            label_r7['bg']=='light green' and label_r8['bg']=='light green' and
            label_r9['bg']=='light green' and label_c1['bg']=='light green' and
            label_c2['bg']=='light green' and label_c3['bg']=='light green' and
            label_c4['bg']=='light green' and label_c5['bg']=='light green' and
            label_c6['bg']=='light green' and label_c7['bg']=='light green' and
            label_c8['bg']=='light green' and label_c9['bg']=='light green'):            
            restart=(messagebox.askyesno('Game Result',
                                         "You Won !!!\nWant to play again??"))
            if restart==1:

                solution=[0,1,2,3,4,5,6,7,8,9]
                key=random.choices(solution, k=9)
                
                i,j,k,l,m,n,p,q,r,life=0,0,0,0,0,0,0,0,0,0
                cell1.configure(text=i)
                cell2.configure(text=j)
                cell3.configure(text=k)
                cell4.configure(text=l)
                cell5.configure(text=m)
                cell6.configure(text=n)
                cell7.configure(text=p)
                cell8.configure(text=q)
                cell9.configure(text=r)

                label_r1.config(bg='black')
                label_r2.config(bg='black')
                label_r3.config(bg='black')
                label_r4.config(bg='black')
                label_r5.config(bg='black')
                label_r6.config(bg='black')
                label_r7.config(bg='black')
                label_r8.config(bg='black')
                label_r9.config(bg='black')
                label_c1.config(bg='black')
                label_c2.config(bg='black')
                label_c3.config(bg='black')
                label_c4.config(bg='black')
                label_c5.config(bg='black')
                label_c6.config(bg='black')
                label_c7.config(bg='black')
                label_c8.config(bg='black')
                label_c9.config(bg='black')

                life=0
                label_life.config(text=f'{life}/10')
                
            else:
                game.destroy()
            
        elif life>=10:
            restart=(messagebox.askyesno('Game Result',
                                         "You Lost !!!\nWant to play again??"))
            if restart==1:

                solution=[0,1,2,3,4,5,6,7,8,9]
                key=random.choices(solution, k=9)

                i,j,k,l,m,n,p,q,r,life=0,0,0,0,0,0,0,0,0,0
                cell1.configure(text=i)
                cell2.configure(text=j)
                cell3.configure(text=k)
                cell4.configure(text=l)
                cell5.configure(text=m)
                cell6.configure(text=n)
                cell7.configure(text=p)
                cell8.configure(text=q)
                cell9.configure(text=r)

                label_r1.config(bg='black')
                label_r2.config(bg='black')
                label_r3.config(bg='black')
                label_r4.config(bg='black')
                label_r5.config(bg='black')
                label_r6.config(bg='black')
                label_r7.config(bg='black')
                label_r8.config(bg='black')
                label_r9.config(bg='black')
                label_c1.config(bg='black')
                label_c2.config(bg='black')
                label_c3.config(bg='black')
                label_c4.config(bg='black')
                label_c5.config(bg='black')
                label_c6.config(bg='black')
                label_c7.config(bg='black')
                label_c8.config(bg='black')
                label_c9.config(bg='black')

                label_life.config(text=f'{life}/10')
                
            else:
                game.destroy()
        
        
game=Tk()
game.geometry('350x350')
game.title("Puzzle")
game.configure(background='black')
i=0
j=0
k=0
l=0
m=0
n=0
p=0
q=0
r=0
life=0

solution=[0,1,2,3,4,5,6,7,8,9]
key=random.choices(solution, k=9)

#Button/Element creation
cell1=Button(game, text=i, bg='black', font='calibri 15 bold',
             fg='light green', padx=15, pady=15, command=clicked1)
cell1.grid(row=0, column=0)

cell2=Button(game, text=j, bg='black', font='calibri 15 bold',
             fg='light green', padx=15, pady=15, command=clicked2)
cell2.grid(row=0, column=1)

cell3=Button(game, text=k, bg='black', font='calibri 15 bold',
             fg='light green', padx=15, pady=15, command=clicked3)
cell3.grid(row=0, column=2)

cell4=Button(game, text=l, bg='black', font='calibri 15 bold',
             fg='light green', padx=15, pady=15, command=clicked4)
cell4.grid(row=1, column=0)

cell5=Button(game, text=m, bg='black', font='calibri 15 bold',
             fg='light green', padx=15, pady=15, command=clicked5)
cell5.grid(row=1, column=1)

cell6=Button(game, text=n, bg='black', font='calibri 15 bold',
             fg='light green', padx=15, pady=15, command=clicked6)
cell6.grid(row=1, column=2)

cell7=Button(game, text=p, bg='black', font='calibri 15 bold',
             fg='light green', padx=15, pady=15, command=clicked7)
cell7.grid(row=2, column=0)

cell8=Button(game, text=q, bg='black', font='calibri 15 bold',
             fg='light green', padx=15, pady=15, command=clicked8)
cell8.grid(row=2, column=1)

cell9=Button(game, text=r, bg='black', font='calibri 15 bold',
             fg='light green', padx=15, pady=15, command=clicked9)
cell9.grid(row=2, column=2)

#Gap creation with Label widget
column_gap=Label(game, bg='black').grid(row=0, columnspan=3, column=3)
row_gap=(Label(game, font='times 1', height=1, bg='black').grid
         (row=3, column=0))
column_gap_life=Label(game, bg='black').grid(row=0, column=12)


#Enter button
enter=Button(game, text='Enter', bg='black', font='calibri 15 bold', height=2,
             fg='light green', command=enter)

enter.grid(rowspan=3, row=4, columnspan=6, column=6)

#Label to display the number of correct cells

label_r1=Label(game, bg='black', relief=RIDGE)
label_r1.grid(row=0, column=7)
label_r2=Label(game, bg='black', relief=RIDGE)
label_r2.grid(row=0, column=9)
label_r3=Label(game, bg='black', relief=RIDGE)
label_r3.grid(row=0, column=11)

label_r4=Label(game, bg='black', relief=RIDGE)
label_r4.grid(row=1, column=7)
label_r5=Label(game, bg='black', relief=RIDGE)
label_r5.grid(row=1, column=9)
label_r6=Label(game, bg='black', relief=RIDGE)
label_r6.grid(row=1, column=11)

label_r7=Label(game, bg='black', relief=RIDGE)
label_r7.grid(row=2, column=7)
label_r8=Label(game, bg='black', relief=RIDGE)
label_r8.grid(row=2, column=9)
label_r9=Label(game, bg='black', relief=RIDGE)
label_r9.grid(row=2, column=11)

label_c1=Label(game, bg='black', font='times 1', height=1, width=15, relief=RIDGE)
label_c1.grid(row=4, column=0)
label_c2=Label(game, bg='black', font='times 1', height=1, width=15, relief=RIDGE)
label_c2.grid(row=5, column=0)
label_c3=Label(game, bg='black', font='times 1', height=1, width=15, relief=RIDGE)
label_c3.grid(row=6, column=0)

label_c4=Label(game, bg='black', font='times 1', height=1, width=15, relief=RIDGE)
label_c4.grid(row=4, column=1)
label_c5=Label(game, bg='black', font='times 1', height=1, width=15, relief=RIDGE)
label_c5.grid(row=5, column=1)
label_c6=Label(game, bg='black', font='times 1', height=1, width=15, relief=RIDGE)
label_c6.grid(row=6, column=1)

label_c7=Label(game, bg='black', font='times 1', height=1, width=15, relief=RIDGE)
label_c7.grid(row=4, column=2)
label_c8=Label(game, bg='black', font='times 1', height=1, width=15, relief=RIDGE)
label_c8.grid(row=5, column=2)
label_c9=Label(game, bg='black', font='times 1', height=1, width=15, relief=RIDGE)
label_c9.grid(row=6, column=2)

#Label to show the chances/lives lapsed

label_life=Label(game, font='calibri 12', bg='black', fg='light green',
                 text=f'{life}/10')
label_life.grid(row=5, column=13)

#Element on window

game.mainloop()
