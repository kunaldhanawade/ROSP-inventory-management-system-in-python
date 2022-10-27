from tkinter import*
from PIL import Image, ImageTk  # pip install pillow
import tkinter
from employee import employeeClass
from product import productClass
from sales import salesClass

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.state('zoomed') 
        self.root.title("Inventory management system")

        # screen width and height
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()

        # title designing
        title = Label(
            self.root,
            text="Inventory Management System", 
            font=("Times New Roman", 40, "bold"),   
            bg="black", 
            fg="white", 
            anchor="c", 
            padx=20
        ).place(x=0, y=0, relwidth=1, height=70)

        # Left menu
        LeftMenu = Frame(
            self.root, 
            bd=2, relief=RIDGE, 
            bg="grey"
        )
        LeftMenu.place(x=0, y=71, width=200)

        lbl_menu = Label(
            LeftMenu,
            text="MENU",
            font=("times new roman", 20, "bold"),
            bg="light grey"
        ).pack(side=TOP, fill=X)
        
        btn_employee = Button(LeftMenu,
            text="Empolyee",
            font=("times new roman", 20),
            bg="white",
            command=self.employee,
            bd=3,
            cursor="hand2"
        ).pack(side=TOP, fill=X)
        
        btn_product = Button(LeftMenu,
            text="Products",
            font=("times new roman", 20),
            bg="white",
            command=self.product,
            bd=3,
            cursor="hand2"
        ).pack(side=TOP, fill=X)
        
        btn_sales = Button(LeftMenu,
            text="Sales",
            font=("times new roman",
            20),
            bg="white",
            command=self.sales,
            bd=3,
            cursor="hand2"
        ).pack(side=TOP, fill=X)
        
        btn_exit = Button(LeftMenu,
            text="Exit",
            font=("times new roman", 20),
            bg="white",
            command=quit,
            bd=3,
            cursor="hand2"
        ).pack(side=TOP, fill=X)


        # Content image designing
        self.img1 = Image.open("main1.png")
        self.img1 = self.img1.resize((width-200, height-70), Image.ANTIALIAS)
        self.img1 = ImageTk.PhotoImage(self.img1)
        self.lbl_img = Label(self.root, image=self.img1)
        self.lbl_img.place(x=200, y=70)

    # defining function for employee
    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = employeeClass(self.new_win)

# defining function for product
    def product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = productClass(self.new_win)

# defining function for sales
    def sales(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = salesClass(self.new_win)

# # exit function
    def quit():
        root.mainloop()


# main modification
if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()
