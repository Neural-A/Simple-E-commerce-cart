import customtkinter
from customtkinter import*
from customtkinter import CTkLabel
import CartFuncs


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

mycart = CartFuncs.CartFunctions()
def _addingtolist():
    items = [
        e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get()
    ]
    prices = [
        p1.get(),p2.get(),p3.get(),p4.get(),
        p5.get(),p6.get()
    ]
    another = CTkToplevel()
    another.title("YOUR CHECKOUT")
    another.geometry("200x200")
    SubTot = 0
    for i in prices:

        if i == ' ':
            i = 0
            SubTot += 1
        else:
            SubTot += prices[i]
            i+=1

    labb = CTkLabel(master =another,text =f"YOUR ITEMS\n"
                                          f"\n{items[0]}\n"
                                          f"\n{items[1]}\n"
                                          f"\n{items[2]}\n"
                                          f"\n{items[3]}\n"
                                          f"\n{items[4]}\n"
                                          f"\n{items[5]}\n"
                                          f"\nTotal: {SubTot}\n",font=("Consolas",10))
    labb.place(x = 70,y= 10)

    another.mainloop()

def removing(element):
    items = [
        e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get()
    ]
    for i in items:
        if element == i:
            items.remove(i)

#--------------------------------------------------------------------------------
window = CTk()
window.title("CART")
window.geometry("400x500")

#Frames--------------------------------------------------------------------------
Fr1 = CTkFrame(master=window,width=375,height=50)
Fr1.place(x = 10, y= 20)
#------
Fr2 = CTkFrame(master=window,width=375,height=300)
Fr2.place(x = 10, y= 85)
#------
Fr3 = CTkFrame(master=window,width=375,height=90)
Fr3.place(x = 10, y= 400)
#------

#-----------Buttons-------------------------------------------------------------

btn =  CTkButton(master=Fr3, text = "Proceeed to checkout",font=("Consolas",10))
btn.place(x = 120, y = 60)

btn1 =  CTkButton(master=Fr3, text = "ADD ITEMS",font=("Consolas",10),command=_addingtolist )
btn1.place(x = 10, y = 10)

btn1 =  CTkButton(master=Fr3, text = "REMOVE ITEMS",font=("Consolas",10),command=removing)
btn1.place(x = 220, y = 10)

#----------Labels--------------------------------------------------------------

l1 = CTkLabel(master= Fr1,text ="E-COMMERCE CART", font=("Consolas",20))
l1.place(x = 110, y= 10)

l2 = CTkLabel(master= Fr2,text ="ITEMS:", font=("Consolas",10))
l2.place(x = 30, y= 10)

l2 = CTkLabel(master= Fr2,text ="PRICE:", font=("Consolas",10))
l2.place(x = 300, y= 10)

#--------Entry-----------------------------------------------------------------

e1 = CTkEntry(master=Fr2, width=100)
e1.place(x=20,y=50)

e2 = CTkEntry(master=Fr2, width=100)
e2.place(x=20,y=90)

e3 = CTkEntry(master=Fr2, width=100)
e3.place(x=20,y=130)

e4 = CTkEntry(master=Fr2, width=100)
e4.place(x=20,y=170)

e5 = CTkEntry(master=Fr2, width=100)
e5.place(x=20,y=210)

e6 = CTkEntry(master=Fr2, width=100)
e6.place(x=20,y=250)

#2
p1 = CTkEntry(master=Fr2, width=100)
p1.place(x=250,y=50)

p2 = CTkEntry(master=Fr2, width=100)
p2.place(x=250,y=90)

p3 = CTkEntry(master=Fr2, width=100)
p3.place(x=250,y=130)

p4 = CTkEntry(master=Fr2, width=100)
p4.place(x=250,y=170)

p5 = CTkEntry(master=Fr2, width=100)
p5.place(x=250,y=210)

p6 = CTkEntry(master=Fr2, width=100)
p6.place(x=250,y=250)

#----------------------------------------------------------------------------

window.mainloop()
