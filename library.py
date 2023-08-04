from tkinter import *
from tkinter import ttk



class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        lbltitle=Label(self.root,text="AHA LIBRARY MANAGEMENT",bg ="Maroon", fg="white",bd =20,relief =RIDGE,font =("times new roman ", 50 ,"bold" ),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE ,padx=20,bg="Maroon")
        frame.place(x=0,y=110,width =1550,height=400)

        #Dataframeleft

        DataFrameLeft=LabelFrame(frame,text="Member Information",bg ="Maroon", fg="white",bd =12,relief =RIDGE,font =("times new roman ", 12 ,"bold" ))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        lblMember=Label(DataFrameLeft,bg="Maroon",fg="White",text="Member Type",font=("times new roman ", 12 ,"bold" ),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        coMember=ttk.Combobox(DataFrameLeft,font=("times new roman ", 12 ,"bold" ),width=27,state="readonly")
        coMember["value"]=("Admin Staff","Student","Lecturer")
        coMember.grid(row=0,column=1)

        lblPRN=Label(DataFrameLeft,bg="Maroon",fg="White",text="PRN No ",font=("times new roman ", 12 ,"bold" ),padx=2,pady=6)
        lblPRN.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,font=("times new roman ", 12 ,"bold" ),width=28)
        txtPRN_NO.grid(row=1,column=1)

        lblTitle=Label(DataFrameLeft,bg="Maroon",fg="White",text="PRN No ",font=("times new roman ", 12 ,"bold" ),padx=2,pady=6)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("times new roman ", 12 ,"bold" ),width=28)
        txtTitle.grid(row=2,column=1)

        lblFirstName=Label(DataFrameLeft,bg="Maroon",fg="White",text="First Name ",font=("times new roman ", 12 ,"bold" ),padx=2,pady=6)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("times new roman ", 12 ,"bold" ),width=28)
        txtFirstName.grid(row=3,column=1)

        lblLastName=Label(DataFrameLeft,bg="Maroon",fg="White",text="Last Name  ",font=("times new roman ", 12 ,"bold" ),padx=2,pady=6)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("times new roman ", 12 ,"bold" ),width=28)
        txtLastName.grid(row=4,column=1)

        lblAddress1=Label(DataFrameLeft,bg="Maroon",fg="White",text="Address Pri ",font=("times new roman ", 12 ,"bold" ),padx=2,pady=6)
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("times new roman ", 12 ,"bold" ),width=28)
        txtAddress1.grid(row=5,column=1)

        lblAddress2=Label(DataFrameLeft,bg="Maroon",fg="White",text="Address Sec ",font=("times new roman ", 12 ,"bold" ),padx=2,pady=6)
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("times new roman ", 12 ,"bold" ),width=28)
        txtAddress2.grid(row=6,column=1)

        lblPostCode=Label(DataFrameLeft,bg="Maroon",fg="White",text="Post Code ",font=("times new roman ", 12 ,"bold" ),padx=2,pady=6)
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,font=("times new roman ", 12 ,"bold" ),width=28)
        txtPostCode.grid(row=7,column=1)

        lblMobile=Label(DataFrameLeft,bg="Maroon",fg="White",text="Mobile",font=("times new roman ", 12 ,"bold" ),padx=2,pady=6)
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("times new roman ", 12 ,"bold" ),width=28)
        txtMobile.grid(row=8,column=1)

        lblBookId=Label(DataFrameLeft,bg="Maroon",fg="White",text="Book ID ",font=("times new roman ", 12 ,"bold" ),padx=2,pady=6)
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,font=("times new roman ", 12 ,"bold" ),width=28)
        txtBookId.grid(row=1,column=3)

        lblBookTitle=Label(DataFrameLeft,bg="Maroon",fg="White",text="Book Title ",font=("times new roman ", 12 ,"bold" ),padx=2,pady=6)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("times new roman ", 12 ,"bold" ),width=28)
        txtBookTitle.grid(row=1,column=3)

        lblAuthor=Label(DataFrameLeft,bg="Maroon",fg="White",text="Author Name  ",font=("times new roman ", 12 ,"bold" ),padx=2,pady=6)
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor=Entry(DataFrameLeft,font=("times new roman ", 12 ,"bold" ),width=28)
        txtAuthor.grid(row=2,column=3)

        lblDateBorrowed=Label(DataFrameLeft,bg="Maroon",fg="White",text="Date Borrowed ",font=("times new roman ", 12 ,"bold" ),padx=2,pady=6)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("times new roman ", 12 ,"bold" ),width=28)
        txtDateBorrowed.grid(row=3,column=3)

        lblDateDue=Label(DataFrameLeft,bg="Maroon",fg="White",text="Date Due ",font=("times new roman ", 12 ,"bold" ),padx=2,pady=6)
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,font=("times new roman ", 12 ,"bold" ),width=28)
        txtDateDue.grid(row=4,column=3)

        lblDaysonbook=Label(DataFrameLeft,bg="Maroon",fg="White",text="Days on book",font=("times new roman ", 12 ,"bold" ),padx=2,pady=6)
        lblDaysonbook.grid(row=5,column=2,sticky=W)
        txtDaysonbook=Entry(DataFrameLeft,font=("times new roman ", 12 ,"bold" ),width=28)
        txtDaysonbook.grid(row=5,column=3)

        lblLateReturnFine=Label(DataFrameLeft,bg="Maroon",fg="White",text="Late Return Fine ",font=("times new roman ", 12 ,"bold" ),padx=2,pady=6)
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,font=("times new roman ", 12 ,"bold" ),width=28)
        txtLateReturnFine.grid(row=6,column=3)


        lblDateOverDue=Label(DataFrameLeft,bg="Maroon",fg="White",text="Date Over Due ",font=("times new roman ", 12 ,"bold" ),padx=2,pady=6)
        lblDateOverDue.grid(row=7,column=2,sticky=W)
        txtDateOverDue=Entry(DataFrameLeft,font=("times new roman ", 12 ,"bold" ),width=28)
        txtDateOverDue.grid(row=7,column=3)


        lblActualPrice=Label(DataFrameLeft,bg="Maroon",fg="White",text="Actual Price ",font=("times new roman ", 12 ,"bold" ),padx=2,pady=6)
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,font=("times new roman ", 12 ,"bold" ),width=28)
        txtActualPrice.grid(row=8,column=3)


        DataFrameRight=LabelFrame(frame,text="Book Details",bg ="Maroon", fg="white",bd =12,relief =RIDGE,font =("times new roman ", 12 ,"bold" ))
        DataFrameRight.place(x=901,y=5,width=540,height=350)

        #Buttons Frame

        framebutton=Frame(self.root,bd=12,relief=RIDGE ,padx=20,bg="Maroon")
        framebutton.place(x=0,y=510,width =1550,height=70)

        #Information Frame
        frameInformation=Frame(self.root,bd=12,relief=RIDGE ,padx=20,bg="Maroon")
        frameInformation.place(x=0,y=580,width =1550,height=220)

        
       
if __name__=="__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()
    
