import tkinter
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
try:
 data=pandas.read_csv("./data/to_be_learned.csv")
except FileNotFoundError:
   data=pandas.read_csv("./data/french_words.csv")
   dict=data.to_dict(orient="records")
except pandas.errors.EmptyDataError:
    data = pandas.read_csv("./data/french_words.csv")
    dict = data.to_dict(orient="records")
else:
    dict=data.to_dict(orient="records")
c={}
def back():
    global c
    canvas.itemconfig(d,image=image1)
    canvas.itemconfig(t1,text="English",fill="white")
    canvas.itemconfig(t2,text=c["English"],fill="white")
    canvas.grid(row=0, column=0, rowspan=2, columnspan=2)

def random_word():
    global a,c
    c = random.choice(dict)
    window.after_cancel(a)
    canvas.itemconfig(d,image=image)
    canvas.itemconfig(t1,text="French",fill="black")
    canvas.itemconfig(t2,text=c["French"],fill="black")
    a=window.after(3000, back)
def tick():
    dict.remove(c)
    print(len(dict))
    data=pandas.DataFrame(dict)
    data.to_csv("./data/to_be_learned.csv",index=False)
    random_word()
window=tkinter.Tk()
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR,highlightthickness=0)
a = window.after(3000, back)
canvas=tkinter.Canvas(width=800,height=526)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
image=tkinter.PhotoImage(file="./images/card_front.png")
d=canvas.create_image(400,263,image=image)
t1=canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
t2=canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0,rowspan=2,columnspan=2)
right=tkinter.PhotoImage(file="./images/right.png")
button=tkinter.Button(image=right,highlightthickness=0,command=tick)
button.grid(row=2,column=0)
wrong=tkinter.PhotoImage(file="./images/wrong.png")
button1=tkinter.Button(image=wrong,highlightthickness=0,command=random_word)
button1.grid(row=2,column=1)
image1=tkinter.PhotoImage(file="./images/card_back.png")
random_word()
window.mainloop()

