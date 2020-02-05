import tkinter
import time
import random
import tkinter.font as tkFont

# 建立視窗
win = tkinter.Tk()
win.title("Help Me!")
win.geometry("600x300")
win.configure(bg='#F0F8FF')

# define finish button
def finish_adding():
    wordlabel.grid_forget()
    wordbox.grid_forget()
    btn.grid_forget()
    listlabel.grid_forget()
    hide_btn.grid_forget()
    check_btn.grid_forget()
    finish_btn.grid_forget()
    clear_btn.grid_forget()
    addlabel.grid_forget()
    new_word_btn.place(x=125,y=60)
    play_btn.place(x=125,y=100)
    
# define add button的功能       
def addMes():
    # 判斷輸入值是否為空白、長度為0或已存在清單中，若是則不加入清單
    if len(str1.get()) != 0 and " " not in str1.get() and str1.get().lower() not in list1 and  str1.get().encode( 'UTF-8' ).isalpha():  
        list1.append(str1.get().lower())
        str3.set(str1.get().lower()+" is sucessfully added ")
        addlabel.grid(row=1,column=1)
        str2.set(list1)
        wordbox.delete(0, 'end')
    else:
        str3.set("Please enter another word!")
        addlabel.grid(row=1,column=1)
        wordbox.delete(0, 'end')
    
# define隱藏清單button的功能
def hide_list():
    listlabel.grid_forget()
    hide_btn.grid_forget()
    check_btn.grid(row=3,column=1)
    
# define查看清單button的功能
def check_list():
    listlabel.grid(row=2,column=1)
    check_btn.grid_forget()
    hide_btn.grid(row=3,column=1)

# define添加題目單字button的功能       
def enter_new_word():
    idiotlabel.grid_forget()
    wordlabel.grid(row=0, column=0)
    wordbox.grid(row=0,column=1)
    btn.grid(row=0,column=2)
    new_word_btn.place_forget()
    check_btn.grid(row=3,column=1)
    finish_btn.grid(row=0, column=3)
    clear_btn.grid(row=3, column=2)
    play_btn.place_forget()
    
# define清除清單中"最新加入元素"的button的功能
def clear():
    if len(list1) != 0:
        list1.pop()
        str2.set(list1)
    listlabel.grid(row=2,column=1)
    
# define開始遊戲button的功能 (包含整個遊戲流程)   
def start_game():
    
    if len(str2.get()) == 0:
        idiotlabel.grid(row=1,column=1)
        return
        
    else:
        
        #define 輸入答案的函數
        def enter():
            
            input_ = input_answer.get().lower()
            input_answer.delete(0, 'end')
            
            if times.get() > 0:

                if not input_.encode( 'UTF-8' ).isalpha():
                   result1.set("Please enter another word! Remain "+str(times.get())+" times")
                   return
                
                if input_ == ans.get():
                    result2.set("You win!The correct answer is "+"".join(ans.get()))
                    cv.create_oval(220,50,320,150,fill='cornsilk')
                    cv.create_line(260,100,260,110)
                    cv.create_line(280,100,280,110)
                    cv.create_arc(260, 110, 280,130, start=180, extent=180,fill='orangered')
                    times.set(-1)
                    return
                
                correct_word = 0

                for i in range(0,len(ans.get())):
                    if ans.get()[i] == input_:
                        temp[i] = input_
                        correct_word += 1
            
                if "-" not in temp:
                    result2.set("You win!The correct answer is "+"".join(ans.get()))
                    cv.create_oval(220,50,320,150,fill='cornsilk')
                    cv.create_line(260,100,260,110)
                    cv.create_line(280,100,280,110)
                    cv.create_arc(260, 110, 280,130, start=180, extent=180,fill='orangered')
                    times.set(-1)
                    return
                
                if correct_word == 0:
                    times.set(times.get()-1)
                    
                result1.set("Remain "+str(times.get())+" times. The answer now is "+"".join(temp))
                result2.set("".join(temp))
                draw(times.get())
        
            if times.get() == 0:
                draw(times.get())
                result2.set("IDIOT!The answer is "+"".join(ans.get()))
                times.set(-1)

        #define 繪圖的函數        
        def draw(times:int):
            if times == 9:
                cv.create_oval(220,50,320,150,fill='white')
            elif times == 8:    
                cv.create_line(270,150,270,250)
            elif times == 7:
                cv.create_line(220,190,270,160)
            elif times == 6:
                cv.create_line(270,160,320,180)

            elif times == 5:
                cv.create_line(250,300,270,250)
            elif times == 4:
                cv.create_line(290,300,270,250)
            elif times == 3:
                #alive
                cv.create_line(260,100,260,110)
            elif times == 2:
                cv.create_line(280,100,280,110)
            elif times == 1:
                cv.create_arc(260,120,280,120, start=0, extent=180)
            elif times == 0:
                #die
                cv.create_line(260,100,250,110)
                cv.create_line(250,100,260,110)
                cv.create_line(280,100,290,110)
                cv.create_line(290,100,280,110)
                cv.create_oval(240,20,300,40,fill='yellow')
                cv.create_oval(245,25,295,35,fill='white')
            else:
                return
            
        #define 重新開始的函數
        def restart():
            secwin.destroy()
            start_game()

        #設定次數
        times = tkinter.IntVar()
        times.set(10)
        #設定結果的變數
        result1 = tkinter.StringVar()
        result2 = tkinter.StringVar()
        #選擇題目
        ans = tkinter.StringVar()
        ans.set(random.choice(list1))
        #設定顯示的_
        temp = list("-"*len(ans.get()))
    
        secwin=tkinter.Toplevel(win)  #建立新的子視窗，可以有多個子視窗
        secwin.geometry("500x500")
        secwin.title("Start game")    #子視窗的標題
        secwin.configure(bg = "lavender")
        lab1=tkinter.Label(secwin, text="The vocabulary you want to guess has "+str(len(ans.get()))+" alphabets",bg = "lavender")
        input_answer = tkinter.Entry(secwin, width=20)  #建立一個Entry元件
        btn=tkinter.Button(secwin, text="Confirm", command=enter)  #建立一個Button的元件
        result_1 = tkinter.Label(secwin,textvariable = result1,bg = "lavender")
        result_2 = tkinter.Label(secwin,textvariable = result2,bg = "lavender",font = ft)
        cv = tkinter.Canvas(secwin,bg = "lavender",height='500',width='500')
        cv.create_line(270,50,270,10)
        cv.create_line(180,10,270,10)
        cv.create_line(180,10,180,350)
        cv.create_line(180,350,270,350)
    
        restart_btn = tkinter.Button(secwin,text = "Restart",command = restart)
   

        lab1.pack()
        input_answer.pack()
        btn.pack()
        result_1.pack()
        result_2.pack()
        restart_btn.pack()
        cv.pack()

# define 字串物件
str3=tkinter.StringVar()
str2=tkinter.StringVar()
str1=tkinter.StringVar()

# define 基礎元件
ft = tkFont.Font(size=16)
addlabel=tkinter.Label(win,textvariable=str3,bg='#F0F8FF',font = ft)
btn = tkinter.Button(win,text='Add',command=addMes,font = ft)
wordbox= tkinter.Entry(win,textvariable=str1,font = ft)
wordlabel= tkinter.Label(win, text="Enter the word",bg='#F0F8FF',font = ft)
idiotlabel= tkinter.Label(win, text="IDIOT!Enter the word!",bg='#F0F8FF',font = ft)
hide_btn=tkinter.Button(win, text="Hide the words",command=hide_list,font = ft)
check_btn=tkinter.Button(win, text="Show the words",command=check_list,font = ft)
new_word_btn=tkinter.Button(win,text="Enter new word",command=enter_new_word,font = ft)
finish_btn=tkinter.Button(win, text='Finish',command=finish_adding,font = ft)
clear_btn=tkinter.Button(win, text='Clear',command=clear,font = ft)
play_btn=tkinter.Button(win,text="Start",command=start_game,font = ft)
listlabel=tkinter.Label(win,wraplength=200, justify='left',textvariable=str2,bg='#F0F8FF',font = ft)

new_word_btn.place(x=125,y=60)
play_btn.place(x=125,y=100)

# define 題目清單
list1=['internationalization','legistimate','configuration','elaborate','traumatically','significant']
str2.set(list1)

win.mainloop()
