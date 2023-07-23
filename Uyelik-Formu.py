from tkinter import *
from PIL import ImageTk, Image

window= Tk()

window.title("Uyelik Formu")
window.geometry("500x350+600+300")
window.resizable(height=False, width= False)
window.iconbitmap("icon.ico")
window.configure(bg="#D7C6EE")

# frame1 = Frame(window)
# frame1.grid(row=0, column=0) alttaki ile aynı
frame1 = Frame(window, bg="#D7C6EE")
frame1.grid(row=0, column=0)

frame2 = Frame(window, bg="#D7C6EE")
frame2.grid(row=0, column=1)

frame3 = Frame(window,  bg="#D7C6EE")
frame3.grid(row=0, column=2)

frame4 = Frame(window,  bg="#D7C6EE")
frame4.grid(row=1, column=2)

frame5 = Frame(window,bg="#D7C6EE" )
frame5.place(x=0, y=190)

cv = Canvas(frame5, bg="#D7C6EE", highlightthickness=0 )
cv.create_line(100,10 , 500,10)
cv.pack()

Label(frame1, text="Ad", font=("arial 12 bold"), bg="#D7C6EE", padx=5 , pady=5).pack()
Label(frame1, text="Soyad", font=("arial 12 bold"), bg="#D7C6EE", padx=8 , pady=5).pack()
Label(frame1, text="Yaş", font=("arial 12 bold"), bg="#D7C6EE", padx=8 , pady=5).pack()
Label(frame1, text="Doğum yılı", font=("arial 12 bold"), bg="#D7C6EE", padx=8 , pady=5).pack()
Label(frame1, text="cinsiyet", font=("arial 12 bold"), bg="#D7C6EE", padx=8 , pady=5).pack()

Label(frame2, text=":", font=("arial 12 bold"), bg="#D7C6EE", padx=5 , pady=5).pack()
Label(frame2, text=":", font=("arial 12 bold"), bg="#D7C6EE", padx=5 , pady=5).pack()
Label(frame2, text=":", font=("arial 12 bold"), bg="#D7C6EE", padx=5 , pady=5).pack()
Label(frame2, text=":", font=("arial 12 bold"), bg="#D7C6EE", padx=5 , pady=5).pack()
Label(frame2, text=":", font=("arial 12 bold"), bg="#D7C6EE", padx=5 , pady=5).pack()

Entry(frame3,font=("arial 12 bold"), bg="#ECE8F0", justify="center" ).pack(pady=5,padx=5)
Entry(frame3,font=("arial 12 bold"), bg="#ECE8F0", justify="center" ).pack(pady=5,padx=5)


Button(window, text= 'kaydet', font=('arial 13 bold'), bg='green', width=12).place(x=100, y=270)
Button(window, text= 'temizle', font=('arial 13 bold'), bg='yellow', width=12).place(x=260, y=270)

image = Image.open("nef.png")
image = image.resize((100,80))
photo = ImageTk.PhotoImage(image)


Button(window, text= 'foto', font=("arial", 20), image=photo , compound=TOP).place(x = 325 , y=11)

Spinbox(frame3, from_=18, to=78,width=19,font=("arial 12 bold"), bg="#ECE8F0", justify="center" ).pack(pady=5,padx=5)

optionList = [
    'ocak',
    'subat',
    'mart',
    'nisan'
]
sval = StringVar(frame3)
sval.set(optionList[0])
opm1 = OptionMenu(frame3, sval, *optionList)
opm1.config(font= 'times 12 bold',width='18', height='1')
opm1.pack(padx=3, pady=3)

ivar = IntVar()

def sel():
    selection = ' selection radiobutton val= ' + str(ivar.get())
    print(selection)
rd1 = Radiobutton(frame3, text = 'erkek', variable=ivar, value=1, command=sel)
rd2 = Radiobutton(frame3, text = 'kiz',  variable=ivar, value=2, command=sel)
rd1.pack(side='left')
rd2.pack(side='left')

cb1 = Checkbutton(frame4, text='formu okudum')
cb1.pack(pady= 5, padx=0)




window.mainloop()