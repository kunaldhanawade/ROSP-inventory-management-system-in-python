from tkinter import*
from tkinter import ttk,messagebox
import sqlite3
class employeeClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()
        #=============================
        # All Variables==========
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        self.var_emp_id=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_utype=StringVar()
        self.var_salary=StringVar()


        #========searchFrame======
        SearchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)


        #=======options======
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Email","Name"),state='readonly',justify=CENTER,font=("time new roman",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)


        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white").place(x=410,y=10,width=150,height=30)


        #====title========
        title=Label(self.root,text="Emplyoee Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)



        #======content=====
        lbl_empid=Label(self.root,text="Emp ID",font=("goudy old style",15),bg="white").place(x=50,y=150)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=350,y=150)
        lbl_email=Label(self.root,text="Email Id",font=("goudy old style",15),bg="white").place(x=750,y=150)

        txt_empid=Entry(self.root,textvariable=self.var_emp_id,font=("goudy old style",15),bg="white").place(x=150,y=150,width=180)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="white").place(x=500,y=150,width=180)
        txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15),bg="white").place(x=850,y=150,width=180)



        #====row 2============
        lbl_utype=Label(self.root,text="User Type",font=("goudy old style",15),bg="lightyellow").place(x=350,y=200)
        
        txt_utype=Entry(self.root,textvariable=self.var_utype,font=("goudy old style",15),bg="lightyellow").place(x=500,y=200,width=180)
        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Admin","Employee"),state='readonly',justify=CENTER,font=("time new roman",15))
        cmb_utype.place(x=500,y=200,width=180)
        cmb_utype.current(0)



        lbl_salary=Label(self.root,text="Salary",font=("goudy old style",15),bg="white").place(x=350,y=250)
        txt_salary=Entry(self.root,textvariable=self.var_salary,font=("goudy old style",15),bg="lightyellow").place(x=500,y=250)
        

        #=======buttons======
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=400,y=300,width=110,height=25)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=520,y=300,width=110,height=25)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=640,y=300,width=110,height=25)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=760,y=300,width=110,height=25)


        #=====Employee Details====


        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)
        



        self.EmployeeTable=ttk.Treeview(emp_frame,columns=("eid","name","email","utype","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)

        self.EmployeeTable.heading("eid",text="EMP ID")
        self.EmployeeTable.heading("name",text="Name")
        self.EmployeeTable.heading("email",text="Email")
        self.EmployeeTable.heading("utype",text="User type")
        self.EmployeeTable.heading("salary",text="Salary")
        self.EmployeeTable["show"]="headings"
        self.EmployeeTable.pack(fill=BOTH,expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()
#========================================================================================
       
if __name__=="__main__":
     root=Tk()
     obj=employeeClass(root)
     root.mainloop()
