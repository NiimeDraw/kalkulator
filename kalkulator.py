from tkinter import*
window=Tk()

def click(item):
    global expression
    expression+=str(item)
    input_teks.set(expression)

def tmbl_clear(): 
    global expression 
    expression = "" 
    input_teks.set("")

def btn_equal():
    global expression
    result = str(eval(expression))
    input_teks.set(result)
    expression=""

expression=""
input_teks=StringVar()

frame1=Frame(window, bg="blue", width=500, height=300)
frame1.pack()

frame2=Frame(window, bg="green", width=500, height=300)
frame2.pack()

label1=Label(frame1, text="KALKULATOR ", font=("Arial", 9))
label1.pack(pady=20, padx=20)

label2=Label(frame1, text="Wildan Khoirul Kamil XII PPLG 1", font=("Arial", 9), textvariable=input_teks)
label2.pack(pady=20, padx=20)

button1=Button(frame2, text="C", width=10, bg="red", fg="white", command =lambda:tmbl_clear())
button1.grid(row=0, column=1, columnspan=2, pady=20, padx=20)

button3=Button(frame2, text="/", bg="grey", fg="white",command=lambda:click("/") )
button3.grid(row=0, column=3, pady=20, padx=20)

button4=Button(frame2, text="", bg="grey", fg="white",command=lambda:click("") )
button4.grid(row=0, column=4, pady=20, padx=20)

button5=Button(frame2, text="7", command=lambda:click("7"))
button5.grid(row=1, column=1, pady=20, padx=20)

button6=Button(frame2, text="8", command=lambda:click("8"))
button6.grid(row=1, column=2, pady=20, padx=20)

button7=Button(frame2, text="9", command=lambda:click("9"))
button7.grid(row=1, column=3, pady=20, padx=20)

button8=Button(frame2, text="+", bg="grey", fg="white", command=lambda:click("+"))
button8.grid(row=1, column=4, pady=20, padx=20)

button9=Button(frame2, text="4",command=lambda:click("4"))
button9.grid(row=2, column=1, pady=20, padx=20)

button10=Button(frame2, text="5",command=lambda:click("5") )
button10.grid(row=2, column=2, pady=20, padx=20)

button11=Button(frame2, text="6", command=lambda:click("6"))
button11.grid(row=2, column=3, pady=20, padx=20)

button12=Button(frame2, text="-",bg="grey", fg="white",command=lambda:click("-") )
button12.grid(row=2, column=4, pady=20, padx=20)

button13=Button(frame2, text="1", command=lambda:click("1"))
button13.grid(row=3, column=1, pady=20, padx=20)

button14=Button(frame2, text="2",command=lambda:click("2"))
button14.grid(row=3, column=2, pady=20, padx=20)

button15=Button(frame2, text="3",command=lambda:click("3") )
button15.grid(row=3, column=3, pady=20, padx=20)

button16=Button(frame2, text="=", height=4,bg="grey", fg="white", command = lambda:btn_equal())
button16.grid(row=3, rowspan=2, column=4, pady=20, padx=20)

button17=Button(frame2, text="0", width=10, command=lambda:click("0"))
button17.grid(row=4, column=1, columnspan=2, pady=20, padx=20)

button18=Button(frame2, text=".",bg="grey", fg="white",command=lambda:click(".") )
button18.grid(row=4, column=3, pady=20, padx=20)


window.mainloop()