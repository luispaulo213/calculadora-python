from tkinter import *
from tkinter import ttk
#cores
cor1 = "#1e1f1e" #preto
cor2 = "#feffff" #branco
cor3 = "#808080" #azul
cor4 = "#ff4d4d" #salmão
cor5 = "#6b0700" #vermelho escuro
#criar uma janela para exibir o código
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg = cor1)
#visor
frameVisor = Frame(janela, width=235, height=50, bg=cor2)
frameVisor.grid(row=0, column=0)
#corpo da calculadora\
frameCorpo = Frame(janela, width=235, height=268)
frameCorpo.grid(row=1, column = 0)
textvalue = StringVar()
allvalue = ""
def inputvalue(event):
    global allvalue
    allvalue= allvalue + str(event)
    textvalue.set(allvalue)
def carcular():
    global allvalue
    resultado = eval(allvalue)
    print(resultado)
    textvalue.set(str(resultado))
def faxina():
    global allvalue
    allvalue = ""
    textvalue.set("")
#criando label
labelNumeros = Label(frameVisor, textvariable= textvalue, width = 16, height = 2, padx=7, relief=FLAT, anchor="e",justify=RIGHT, font=('Ivy18'),bg=cor2, fg=cor1)
labelNumeros.place(x=0,y=0)
#criando botões
b1 = Button(frameCorpo,command=faxina,text="C", width=11,height=2, bg=cor4, font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b1. place(x=0,y=0)
b2 = Button(frameCorpo,command=lambda : inputvalue("%") ,text="%", width=5,height=2, bg=cor4, font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b2. place(x=118,y=0)
b3 = Button(frameCorpo,command=lambda : inputvalue("/"),text="/", width=5,height=2, bg=cor5, font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b3. place(x=177,y=0)
b4 = Button(frameCorpo,command=lambda : inputvalue("7"),text="7", width=5,height=2, bg=cor4, font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b4. place(x=0,y=52)  
b5 = Button(frameCorpo,command=lambda : inputvalue("8"),text="8", width=5,height=2, bg=cor4, font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b5. place(x=59,y=52)
b6 = Button(frameCorpo,command=lambda : inputvalue("9"),text="9", width=5,height=2, bg=cor4, font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b6. place(x=118,y=52)
b7 = Button(frameCorpo,command=lambda : inputvalue("*"),text="X", width=5,height=2, bg=cor5, font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b7. place(x=177,y=52)
b8 = Button(frameCorpo,command=lambda : inputvalue("4"),text="4", width=5,height=2, bg=cor4, font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b8. place(x=0,y=104)
b9 = Button(frameCorpo,command=lambda : inputvalue("5"),text="5", width=5,height=2, bg=cor4, font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b9. place(x=59,y=104)
b10 = Button(frameCorpo,command=lambda : inputvalue("6"),text="6", width=5,height=2, bg=cor4, font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b10. place(x=118,y=104)
b11 = Button(frameCorpo,command=lambda : inputvalue("-"),text="-", width=5,height=2, bg=cor5, font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b11. place(x=177,y=104)
b12 = Button(frameCorpo,command=lambda : inputvalue("1"),text="1", width=5,height=2, bg=cor4, font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b12. place(x=0,y=153)
b13 = Button(frameCorpo,command=lambda : inputvalue("2"),text="2", width=5,height=2, bg=cor4, font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b13. place(x=59.,y=153)
b14 = Button(frameCorpo,command=lambda : inputvalue("3"),text="3", width=5,height=2, bg=cor4, font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b14. place(x=118,y=153)
b15 = Button(frameCorpo,command=lambda : inputvalue("+"),text="+", width=5,height=2, bg=cor5, font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b15. place(x=177,y=153)
b16 = Button(frameCorpo,command=lambda : inputvalue("0"),text="0", width=11,height=3, bg=cor4, font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b16. place(x=0,y=205)
b17 = Button(frameCorpo,command=lambda : inputvalue("."),text=".", width=5,height=3, bg=cor4, font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b17. place(x=118,y=205)
b18 = Button(frameCorpo,command=carcular,text="=", width=5,height=3, bg=cor5, font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b18. place(x=177,y=205)
# executa janela
janela.mainloop()