import tkinter
from tkinter import *
import random
from tkinter import messagebox

window = Tk()
window.title("Jumbled Word Game")

window.geometry("500x500+500+150")
window.configure(background="#B5DEAD")

answers = ["apple","mango","banana","achieve","london","evening","servant","receiver","london","ferrari","hollow","horror","master","morning", "bottle","pen","router","copy","narrow","wide","dive","love","block","right","simple","deaf","single","knight","hope"]
words = ["plpea","gnoma","annaba","hveeica","oonndl","egvnine","aestnrv","iceever","lndono","rrreifa","wllhoo","oohrrr","rtemsa","nnrgimo","lttobe","enp","ourrte","ypco","rraonw","wdie","ievd","elov","klboc","ightr","plmsie","dfea","glneis","ghtkni","opeh"]

num = random.randrange(0,len(words),1)
score = 0
total = 0
s = ""

score_lbl = Label(window)

def default(): 
    global words, num, word_lbl
    word_lbl.config(text = words[num])

def reset(): 
    global words, num, word_lbl
    num = random.randrange(0,len(words),1)
    word_lbl.config(text = words[num])
    answerbox.delete(0,END)

def checkans(): 
    global answers, words, num, score, total, s, score_lbl
    total = total + 1
    answer = answerbox.get()
    if answer == answers[num]: 
        score = score + 1
        messagebox.showinfo("YEAH", "It is correct")
    else : 
        messagebox.showerror("NOO", "It is not correct")
    s = "Score : "+ str(score) + "/" + str(total)
    score_lbl.forget()
    score_lbl = Label(window, text = s, font = ("ariel", 25, "bold"), bg = "#B5DEAD", fg = "#061A40")
    score_lbl.pack(side = LEFT)
    reset()

main_lbl = Label(window, text="Jumbled Word Game", font=("ariel", 30), bg="#B5DEAD", fg="#809848")
main_lbl.pack(pady = 5)
word_lbl = Label(window, font=("ariel", 22), bg="#B5DEAD", fg="#442220")
word_lbl.pack(pady=30, ipady=10, ipadx=10)

val = StringVar()
answerbox = Entry(window, textvariable=val, width=30)
answerbox.pack(ipadx=5, ipady=5)

check_btn = Button(window,text="Check",font=("ariel", 20, "bold"),width=10,bg="#8AC4FF",fg="#7A7978",command = checkans)
check_btn.pack(pady=40)
reset_btn = Button(window,text="Reset",font=("ariel", 20, "bold"),width=10,bg="#7A7978",fg="#8AC4FF", command = reset)
reset_btn.pack()



default()

window.mainloop()
