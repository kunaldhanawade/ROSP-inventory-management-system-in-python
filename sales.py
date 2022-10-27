from sqlite3.dbapi2 import Cursor
from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3
import os

class salesClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()

        #============= Variables ==================
        self.bill_list = []
        self.var_invoice=StringVar()
        

         #====title========
        title=Label(self.root,text="View Customer Bill",font=("goudy old style",30),bg="#0f4d7d",fg="white").place(x=0,y=0,width=1100)

        lbl_invoice = Label(self.root, text="Invoice", font=("Times new roman",15),bg ="white").place(x=50,y=100)
        txt_invoice = Entry(self.root, textvariable=self.var_invoice, font=("Times new roman",15),bg ="light yellow").place(x=160,y=100,width=180,height=28)

        btn_search = Button (self.root, text= "Search",command=self.search , font=("Times New roman",15,"bold") ,bg="light grey",fg="black",cursor = 'hand2').place(x=360,y=100,width=120,height=28)
        btn_clear = Button (self.root, text= "Clear",command=self.clear,font=("Times New roman",15,"bold") ,bg="Light grey",fg="black",cursor = 'hand2').place(x=490,y=100,width=120,height=28)

        #========== Bill Lists ==========
        sales_Frame = Frame(self.root,bd=3,relief=RIDGE)
        sales_Frame.place(x=50,y=140,width=200,height=300)


        scrolly = Scrollbar(sales_Frame,orient=VERTICAL) 
        self.sales_List = Listbox(sales_Frame,font=("goudy old style",15),bg = "white" ,yscrollcommand= scrolly.set)
        self.sales_List.pack(fill=BOTH,expand=1)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.sales_List.yview)
        self.sales_List.bind("<ButtonRelease-1>", self.get_data)
        #========== Bill Area ==========

        
        bill_Frame = Frame(self.root,bd=3,relief=RIDGE)
        bill_Frame.place(x=280,y=140,width=410,height=300)

        lbl_title2=Label(bill_Frame,text="Customer Bill Area",font=("goudy old style",20),bg= "black",fg="white").pack(side=TOP,fill=X)

        scrolly2 = Scrollbar(bill_Frame,orient=VERTICAL) 
        self.bill_area = Listbox(bill_Frame,font=("goudy old style",15),bg = "light grey" ,yscrollcommand= scrolly2.set)
        self.bill_area.pack(fill=BOTH,expand=1)
        scrolly2.pack(side=RIGHT,fill=Y)
        scrolly2.config(command=self.bill_area.yview)


        # ================ Image ================
        self.bill_photo = Image.open("sales.png")
        self.bill_photo=self.bill_photo.resize((350,315), Image.ANTIALIAS)
        self.bill_photo=ImageTk.PhotoImage(self.bill_photo)

        lbl_image = Label(self.root,image = self.bill_photo) 
        lbl_image.place(x=700,y=110)
        
        self.show()

if __name__=="__main__":
     root=Tk()
     obj=salesClass(root)
     root.mainloop()