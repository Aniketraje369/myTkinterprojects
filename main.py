import tkinter as tk
from tkinter import *
import math,random,os
from tkinter import messagebox as tmsg
class billApplication:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("My Billing Software")
        bg_color="#ec9706"
        text_color="white"
        title = Label(self.root,text="Restaurant Billing Software- By Aniket Raje",bd=12,relief=GROOVE,bg=bg_color, font=("times new roman",30,"bold"),fg=text_color, pady=2).pack(fill=X)

        #-----------------------------------Variables-----------------------------------

        #soups
        self.tomatoSoup = IntVar()
        self.cornSoup = IntVar()
        self.sourSoup = IntVar()
        self.pannerSoup = IntVar()
        self.chickenSoup = IntVar()
        self.italianSoup = IntVar()
        
        #snacks
        self.pannerPakora = IntVar()
        self.chickenPakora = IntVar()
        self.fishPakora = IntVar()
        self.fishFinger = IntVar()
        self.chicken65 = IntVar()
        self.chickenHoney = IntVar()

        #desserts
        self.shahiTukra = IntVar()
        self.falooda = IntVar()
        self.rasmalai = IntVar()
        self.pistachio = IntVar()
        self.chocoChip = IntVar()
        self.chocoVanilla = IntVar()

        #tandori
        self.chickenTandori = IntVar()
        self.CheeseKebab = IntVar()
        self.afghaniTandori = IntVar()
        self.chickenTangri = IntVar()
        self.seekhKebab = IntVar()

        #Roti
        self.tandoriRoti = IntVar()
        self.rumaliRoti = IntVar()
        self.butterNaan = IntVar()
        self.garlicNaan = IntVar()
        self.lacchaParatha = IntVar()
        

        #drinks
        self.bisleri = IntVar()
        self.coke = IntVar()
        self.sprite = IntVar()
        self.redBull = IntVar()
        self.thumbsUp = IntVar()
        
        #total
        self.soupsPrice = StringVar()
        self.snacksPrice = StringVar()
        self.drinksPrice = StringVar()
        self.dessertsPrice = StringVar()
        self.tandoriPrice = StringVar()
        self.rotiPrice = StringVar()
        
        self.totalAmount = StringVar()
        self.gst_Amount = StringVar()
        self.Amountwith_Gst = StringVar()
        
        #customer
        self.customerName = StringVar()
        self.customerPhone = StringVar()
        self.customerBill_no = StringVar()
        x = random.randint(1000,9999)
        self.customerBill_no.set(str(x))
        self.search_bill = StringVar()

        #-----------------------------------Variables End-----------------------------------

        f1 = LabelFrame(self.root,text="Customer Details",bd=10,relief=GROOVE, font="lucida 15 bold", fg="gold",bg=bg_color)
        f1.place(x=0,y=80, relwidth=1)
        
        customerName_label = Label(f1,text="Customer Name",bg=bg_color,fg=text_color,font="lucida 18 bold").grid(row=0,column=0,padx=5,pady=5)
        customerName_text = Entry(f1,width=12,textvariable=self.customerName,font="arial 15",bd=6,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=5)

        customerPhone_label = Label(f1,text="Customer Phone no.",bg=bg_color,fg=text_color,font="lucida 18 bold").grid(row=0,column=2,padx=5,pady=5)
        customerPhone_text = Entry(f1,width=12,textvariable=self.customerPhone,font="arial 15",bd=6,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=5)

        customerBill_label = Label(f1,text="Customer Bill no.",bg=bg_color,fg=text_color,font="lucida 18 bold").grid(row=0,column=4,padx=5,pady=5)
        customerBill_text = Entry(f1,width=12,textvariable=self.search_bill,font="arial 15",bd=6,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=5)

        bill_btn = Button(f1,text="Search",command=self.findBill,width=12,bd=7,font="arial 12 bold").grid(row=0,column=6,pady=10,padx=15)

#------------------------------------------Soups-------------------------------------------#

        f2 = LabelFrame(self.root,text="SOUPS",bd=10,relief=GROOVE, font="lucida 15 bold", fg="gold",bg=bg_color)
        f2.place(x=0,y=183, width=400,height=450)
        
        soups1_label = Label(f2,text="Tomato Soup",font="courier 16 bold",bg=bg_color,fg="pink").grid(row=0,column=0,padx=5,pady=10,sticky="w")
        soups1_entry = Entry(f2,width=4,textvariable=self.tomatoSoup,font="courier 16 bold", bd=5, relief=SUNKEN).grid(row=0,column=1,padx=5,pady=10)
        
        soups2_label = Label(f2,text="Corn Soup",font="courier 16 bold",bg=bg_color,fg="pink").grid(row=1,column=0,padx=5,pady=10,sticky="w")
        soups2_entry = Entry(f2,width=4,textvariable=self.cornSoup,font="courier 16 bold", bd=5, relief=SUNKEN).grid(row=1,column=1,padx=5,pady=10)
        
        soups3_label = Label(f2,text="Sour Soup",font="courier 16 bold",bg=bg_color,fg="pink").grid(row=2,column=0,padx=5,pady=10,sticky="w")
        soups3_entry = Entry(f2,width=4,textvariable=self.sourSoup,font="courier 16 bold", bd=5, relief=SUNKEN).grid(row=2,column=1,padx=5,pady=10)
        
        soups4_label = Label(f2,text="Paneer Soup",font="courier 16 bold",bg=bg_color,fg="pink").grid(row=3,column=0,padx=5,pady=10,sticky="w")
        soups4_entry = Entry(f2,textvariable=self.pannerSoup,width=4,font="courier 16 bold", bd=5, relief=SUNKEN).grid(row=3,column=1,padx=5,pady=10)
        
        soups5_label = Label(f2,text="Chicken Soup",font="courier 16 bold",bg=bg_color,fg="pink").grid(row=4,column=0,padx=5,pady=10,sticky="w")
        soups5_entry = Entry(f2,width=4,textvariable=self.chickenSoup,font="courier 16 bold", bd=5, relief=SUNKEN).grid(row=4,column=1,padx=5,pady=10)
        
        soups6_label = Label(f2,text="Italian Soup",font="courier 16 bold",bg=bg_color,fg="pink").grid(row=5,column=0,padx=5,pady=10,sticky="w")
        soups6_entry = Entry(f2,width=4,textvariable=self.italianSoup,font="courier 16 bold", bd=5, relief=SUNKEN).grid(row=5,column=1,padx=5,pady=10)


#------------------------------------------Snacks-------------------------------------------#


        f3 = LabelFrame(self.root,text="SNACKS",bd=10,relief=GROOVE, font="lucida 15 bold", fg="gold",bg=bg_color)
        f3.place(x=380,y=183, width=400,height=450)
        
        snack1_label = Label(f3,text="Paneer Pakora",font="courier 16 bold",bg=bg_color,fg="pink").grid(row=0,column=0,padx=5,pady=10,sticky="w")
        snack1_entry = Entry(f3,width=4,textvariable=self.pannerPakora,font="courier 16 bold", bd=5, relief=SUNKEN).grid(row=0,column=1,padx=5,pady=10)
        
        snack2_label = Label(f3,text="Chicken Pakora",font="courier 16 bold",bg=bg_color,fg="pink").grid(row=1,column=0,padx=5,pady=10,sticky="w")
        snack2_entry = Entry(f3,width=4,textvariable=self.chickenPakora,font="courier 16 bold", bd=5, relief=SUNKEN).grid(row=1,column=1,padx=5,pady=10)
        
        snack3_label = Label(f3,text="Fish Pakora",font="courier 16 bold",bg=bg_color,fg="pink").grid(row=2,column=0,padx=5,pady=10,sticky="w")
        snack3_entry = Entry(f3,width=4,textvariable=self.fishPakora,font="courier 16 bold", bd=5, relief=SUNKEN).grid(row=2,column=1,padx=5,pady=10)
        
        snack4_label = Label(f3,text="Fish Finger",font="courier 16 bold",bg=bg_color,fg="pink").grid(row=3,column=0,padx=5,pady=10,sticky="w")
        snack4_entry = Entry(f3,width=4,textvariable=self.fishFinger,font="courier 16 bold", bd=5, relief=SUNKEN).grid(row=3,column=1,padx=5,pady=10)
        
        snack5_label = Label(f3,text="Chicken 65",font="courier 16 bold",bg=bg_color,fg="pink").grid(row=4,column=0,padx=5,pady=10,sticky="w")
        snack5_entry = Entry(f3,width=4,textvariable=self.chicken65,font="courier 16 bold", bd=5, relief=SUNKEN).grid(row=4,column=1,padx=5,pady=10)
        
        snack6_label = Label(f3,text="Chicken Honey",font="courier 16 bold",bg=bg_color,fg="pink").grid(row=5,column=0,padx=5,pady=10,sticky="w")
        snack6_entry = Entry(f3,width=4,textvariable=self.chickenHoney,font="courier 16 bold", bd=5, relief=SUNKEN).grid(row=5,column=1,padx=5,pady=10)


#------------------------------------------Desserts and Ice cream-------------------------------------------#


        f4 = LabelFrame(self.root,text="Desserts & Ice Cream",bd=10,relief=GROOVE, font="lucida 15 bold", fg="gold",bg=bg_color)
        f4.place(x=750,y=183, width=400,height=450)
        
        snack1_label = Label(f4,text="Shahi Tukra",font="courier 16 bold",bg=bg_color,fg="pink").grid(row=0,column=0,padx=5,pady=10,sticky="w")
        snack1_entry = Entry(f4,width=4,textvariable=self.shahiTukra,font="courier 16 bold", bd=5, relief=SUNKEN).grid(row=0,column=1,padx=5,pady=10)
        
        snack2_label = Label(f4,text="Kesar Falooda",font="courier 16 bold",bg=bg_color,fg="pink").grid(row=1,column=0,padx=5,pady=10,sticky="w")
        snack2_entry = Entry(f4,width=4,textvariable=self.falooda,font="courier 16 bold", bd=5, relief=SUNKEN).grid(row=1,column=1,padx=5,pady=10)
        
        snack3_label = Label(f4,text="Rasmalai",font="courier 16 bold",bg=bg_color,fg="pink").grid(row=2,column=0,padx=5,pady=10,sticky="w")
        snack3_entry = Entry(f4,width=4,textvariable=self.rasmalai,font="courier 16 bold", bd=5, relief=SUNKEN).grid(row=2,column=1,padx=5,pady=10)
        
        snack4_label = Label(f4,text="Pistachio",font="courier 16 bold",bg=bg_color,fg="pink").grid(row=3,column=0,padx=5,pady=10,sticky="w")
        snack4_entry = Entry(f4,width=4,textvariable=self.pistachio,font="courier 16 bold", bd=5, relief=SUNKEN).grid(row=3,column=1,padx=5,pady=10)
        
        snack5_label = Label(f4,text="Choco Chip",font="courier 16 bold",bg=bg_color,fg="pink").grid(row=4,column=0,padx=5,pady=10,sticky="w")
        snack5_entry = Entry(f4,width=4,textvariable=self.chocoChip,font="courier 16 bold", bd=5, relief=SUNKEN).grid(row=4,column=1,padx=5,pady=10)
        
        snack6_label = Label(f4,text="Choco Vanilla",font="courier 16 bold",bg=bg_color,fg="pink").grid(row=5,column=0,padx=5,pady=10,sticky="w")
        snack6_entry = Entry(f4,width=4,textvariable=self.chocoVanilla,font="courier 16 bold", bd=5, relief=SUNKEN).grid(row=5,column=1,padx=5,pady=10)


#---------------------------------Bill Area----------------------------------------#

        f5 = Frame(self.root,bd=10,relief=GROOVE)
        f5.place(x=1145,y=183, width=450,height=569)
        
        bill_title = Label(f5,text="Bill Area", font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scroll_y = Scrollbar(f5,orient=VERTICAL)
        self.textarea = Text(f5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)



#-------------------------------Tandori&kebab-------------------------------------------#

        f7 = LabelFrame(self.root,text="Tandori & Kebabs",bd=10,relief=GROOVE, font="lucida 15 bold", fg="gold",bg=bg_color)
        f7.place(x=0,y=613, width=400,height=383)
        
        soups1_label = Label(f7,text="Chicken Tandori",font="courier 16 bold",bg=bg_color,fg="pink").grid(row=0,column=0,padx=5,pady=10,sticky="w")
        soups1_entry = Entry(f7,width=4,textvariable=self.chickenTandori,font="courier 16 bold", bd=5, relief=SUNKEN).grid(row=0,column=1,padx=5,pady=10)
        
        soups2_label = Label(f7,text="Cheese Kebab",font="courier 16 bold",bg=bg_color,fg="pink").grid(row=1,column=0,padx=5,pady=10,sticky="w")
        soups2_entry = Entry(f7,width=4,textvariable=self.CheeseKebab,font="courier 16 bold", bd=5, relief=SUNKEN).grid(row=1,column=1,padx=5,pady=10)
        
        soups3_label = Label(f7,text="Afghani Tandori",font="courier 16 bold",bg=bg_color,fg="pink").grid(row=2,column=0,padx=5,pady=10,sticky="w")
        soups3_entry = Entry(f7,width=4,textvariable=self.afghaniTandori,font="courier 16 bold", bd=5, relief=SUNKEN).grid(row=2,column=1,padx=5,pady=10)
        
        soups4_label = Label(f7,text="Chicken Tangri",font="courier 16 bold",bg=bg_color,fg="pink").grid(row=3,column=0,padx=5,pady=10,sticky="w")
        soups4_entry = Entry(f7,width=4,textvariable=self.chickenTangri,font="courier 16 bold", bd=5, relief=SUNKEN).grid(row=3,column=1,padx=5,pady=10)
        
        soups5_label = Label(f7,text="Seekh Kebab",font="courier 16 bold",bg=bg_color,fg="pink").grid(row=4,column=0,padx=5,pady=10,sticky="w")
        soups5_entry = Entry(f7,width=4,textvariable=self.seekhKebab,font="courier 16 bold", bd=5, relief=SUNKEN).grid(row=4,column=1,padx=5,pady=10)



#-------------------------------Roti & Naan-------------------------------------------#

        f8 = LabelFrame(self.root,text="Roti & Naan",bd=10,relief=GROOVE, font="lucida 15 bold", fg="gold",bg=bg_color)
        f8.place(x=380,y=613, width=400,height=383)
        
        soups1_label = Label(f8,text="Tandori Roti",font="courier 16 bold",bg=bg_color,fg="pink").grid(row=0,column=0,padx=5,pady=10,sticky="w")
        soups1_entry = Entry(f8,width=4,textvariable=self.tandoriRoti,font="courier 16 bold", bd=5, relief=SUNKEN).grid(row=0,column=1,padx=5,pady=10)
        
        soups2_label = Label(f8,text="Rumali Roti",font="courier 16 bold",bg=bg_color,fg="pink").grid(row=1,column=0,padx=5,pady=10,sticky="w")
        soups2_entry = Entry(f8,width=4,textvariable=self.rumaliRoti,font="courier 16 bold", bd=5, relief=SUNKEN).grid(row=1,column=1,padx=5,pady=10)
        
        soups3_label = Label(f8,text="Butter Naan",font="courier 16 bold",bg=bg_color,fg="pink").grid(row=2,column=0,padx=5,pady=10,sticky="w")
        soups3_entry = Entry(f8,width=4,textvariable=self.butterNaan,font="courier 16 bold", bd=5, relief=SUNKEN).grid(row=2,column=1,padx=5,pady=10)
        
        soups4_label = Label(f8,text="Garlic Naan",font="courier 16 bold",bg=bg_color,fg="pink").grid(row=3,column=0,padx=5,pady=10,sticky="w")
        soups4_entry = Entry(f8,width=4,textvariable=self.garlicNaan,font="courier 16 bold", bd=5, relief=SUNKEN).grid(row=3,column=1,padx=5,pady=10)
        
        soups5_label = Label(f8,text="Laccha Paratha",font="courier 16 bold",bg=bg_color,fg="pink").grid(row=4,column=0,padx=5,pady=10,sticky="w")
        soups5_entry = Entry(f8,width=4,textvariable=self.lacchaParatha,font="courier 16 bold", bd=5, relief=SUNKEN).grid(row=4,column=1,padx=5,pady=10)



#-------------------------------Drinks-------------------------------------------#

        f9 = LabelFrame(self.root,text="Drinks",bd=10,relief=GROOVE, font="lucida 15 bold", fg="gold",bg=bg_color)
        f9.place(x=750,y=613, width=400,height=383)
        
        soups1_label = Label(f9,text="Bisleri",font="courier 16 bold",bg=bg_color,fg="pink").grid(row=0,column=0,padx=5,pady=10,sticky="w")
        soups1_entry = Entry(f9,width=4,textvariable=self.bisleri,font="courier 16 bold", bd=5, relief=SUNKEN).grid(row=0,column=1,padx=5,pady=10)
        
        soups2_label = Label(f9,text="Coke",font="courier 16 bold",bg=bg_color,fg="pink").grid(row=1,column=0,padx=5,pady=10,sticky="w")
        soups2_entry = Entry(f9,width=4,textvariable=self.coke,font="courier 16 bold", bd=5, relief=SUNKEN).grid(row=1,column=1,padx=5,pady=10)
        
        soups3_label = Label(f9,text="Sprite",font="courier 16 bold",bg=bg_color,fg="pink").grid(row=2,column=0,padx=5,pady=10,sticky="w")
        soups3_entry = Entry(f9,width=4,textvariable=self.sprite,font="courier 16 bold", bd=5, relief=SUNKEN).grid(row=2,column=1,padx=5,pady=10)
        
        soups4_label = Label(f9,text="Red Bull",font="courier 16 bold",bg=bg_color,fg="pink").grid(row=3,column=0,padx=5,pady=10,sticky="w")
        soups4_entry = Entry(f9,width=4,textvariable=self.redBull,font="courier 16 bold", bd=5, relief=SUNKEN).grid(row=3,column=1,padx=5,pady=10)
        
        soups5_label = Label(f9,text="Thumbs Up",font="courier 16 bold",bg=bg_color,fg="pink").grid(row=4,column=0,padx=5,pady=10,sticky="w")
        soups5_entry = Entry(f9,width=4,textvariable=self.thumbsUp,font="courier 16 bold", bd=5, relief=SUNKEN).grid(row=4,column=1,padx=5,pady=10)




#--------------------------------------Bill Menu-----------------------------------------------------
        f6 = LabelFrame(self.root,text="Bill Menu",bd=10,relief=GROOVE, font="lucida 15 bold", fg="gold",bg=bg_color)
        f6.place(x=0,y=983, relwidth=1,height=300)

        m1_lbl = Label(f6,text="Total Soups Price",bg=bg_color,fg=text_color,font="courier 15 bold").grid(row=0,column=0,padx=10,pady=1,sticky="w")
        m1_txt = Entry(f6,width=8,textvariable=self.soupsPrice,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl = Label(f6,text="Total Snacks Price",bg=bg_color,fg=text_color,font="courier 15 bold").grid(row=1,column=0,padx=10,pady=1,sticky="w")
        m2_txt = Entry(f6,width=8,textvariable=self.snacksPrice,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3_lbl = Label(f6,text="Total Desserts Price",bg=bg_color,fg=text_color,font="courier 15 bold").grid(row=2,column=0,padx=10,pady=1,sticky="w")
        m3_txt = Entry(f6,width=8,textvariable=self.dessertsPrice,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        m4_lbl = Label(f6,text="Total Tandori Price",bg=bg_color,fg=text_color,font="courier 15 bold").grid(row=0,column=2,padx=10,pady=1,sticky="w")
        m4_txt = Entry(f6,width=8,textvariable=self.tandoriPrice,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        m5_lbl = Label(f6,text="Total Roti Price",bg=bg_color,fg=text_color,font="courier 15 bold").grid(row=1,column=2,padx=10,pady=1,sticky="w")
        m5_txt = Entry(f6,width=8,textvariable=self.rotiPrice,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        m6_lbl = Label(f6,text="Total Drinks Price",bg=bg_color,fg=text_color,font="courier 15 bold").grid(row=2,column=2,padx=10,pady=1,sticky="w")
        m6_txt = Entry(f6,width=8,textvariable=self.drinksPrice,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)


        btn_Frame = Frame(f6,bd=7,relief=GROOVE)
        btn_Frame.place(x=863,width=700,height=105)
        
        total_btn = Button(btn_Frame,command=self.total,text="Total",bg=bg_color,width=12,bd=5,font="arial 12 bold",fg=text_color,pady=15).grid(row=0,column=0,padx=5,pady=5)
        
        gBill_btn = Button(btn_Frame,text="Generate Bill",command=self.bill_area,bg=bg_color,width=12,bd=5,font="arial 12 bold",fg=text_color,pady=15).grid(row=0,column=1,padx=5,pady=5)
        
        clear_btn = Button(btn_Frame,text="Clear",command=self.clearData,bg=bg_color,width=12,bd=5,font="arial 12 bold",fg=text_color,pady=15).grid(row=0,column=2,padx=5,pady=5)
        
        exit_btn = Button(btn_Frame,text="Exit",bg=bg_color,width=12,bd=5,font="arial 12 bold",fg=text_color,pady=15,command=quit).grid(row=0,column=3,padx=5,pady=5)

        # self.welcome_bill()

        # Total

        
        f10 = LabelFrame(self.root,text="Total",bd=10,relief=GROOVE, font="lucida 15 bold", fg="gold",bg=bg_color)
        f10.place(x=1140,y=840, width=450,height=163)
        
        c1_lbl = Label(f10,text="Total Amount",bg=bg_color,fg=text_color,font="courier 15 bold").grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt = Entry(f10,width=8,textvariable=self.totalAmount,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2_lbl = Label(f10,text="GST Amount(5%)",bg=bg_color,fg=text_color,font="courier 15 bold").grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt = Entry(f10,width=8,textvariable=self.gst_Amount,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3_lbl = Label(f10,text="Amount with GST",bg=bg_color,fg=text_color,font="courier 15 bold").grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt = Entry(f10,width=8,textvariable=self.Amountwith_Gst,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        f11 = LabelFrame(self.root,bd=10,relief=GROOVE, font="lucida 15 bold", fg="gold",bg="white")
        f11.place(x=1140,y=745, width=450,height=93)
        
        saveBtn = Button(f11,text="Save",command=self.saveBill,bg=bg_color,width=12,bd=5,font="arial 12 bold",fg=text_color,pady=4,padx=10).grid(row=0,column=0,padx=19,pady=10)
        
        printBtn = Button(f11,text="Print",command=self.printBill,bg=bg_color,width=12,bd=5,font="arial 12 bold",fg=text_color,pady=4,padx=10).grid(row=0,column=1,padx=19,pady=10)
        
        
        #---------------------------prices-----------------------------

        #soups
        self.tomatoSoup_price = 110
        self.cornSoup_price = 120
        self.sourSoup_price = 120
        self.pannerSoup_price = 160
        self.chickenSoup_price = 180
        self.italianSoup_price = 210

        #snacks
        self.pannerPakora_price = 180
        self.chickenPakora_price = 230
        self.fishPakora_price = 240
        self.fishFinger_price = 240
        self.chicken65_price = 260
        self.chickenHoney_price = 300 

        #desserts
        self.shahiTukra_price = 90
        self.falooda_price = 120
        self.rasmalai_price = 120
        self.pistachio_price = 180
        self.chocoChip_price = 160
        self.chocoVanilla_price = 120

        #tandori
        self.chickenTandori_price = 400
        self.cheeseKebab_price = 360
        self.afghaniTandori_price = 420
        self.chickenTangri_price = 380
        self.seekhKebab_price = 280

        #roti
        self.tandoriRoti_price = 20
        self.rumaliRoti_price = 20
        self.butterRoti_price = 60
        self.garlicRoti_price = 70
        self.lacchaRoti_price = 35

        #drinks
        self.bisleri_price = 20
        self.coke_price = 55
        self.sprite_price = 65
        self.redBull_price = 120
        self.thumbsUp_price = 60

        #---------------------------prices End-----------------------------
        
    def total(self):
            
            self.totalSoups_price =float(
                    (self.tomatoSoup.get()*self.tomatoSoup_price)+
                    (self.cornSoup.get()*self.cornSoup_price)+
                    (self.sourSoup.get()*self.sourSoup_price)+
                    (self.pannerSoup.get()*self.pannerSoup_price)+
                    (self.chickenSoup.get()*self.chickenSoup_price)+
                    (self.italianSoup.get()*self.italianSoup_price)
            )
            self.soupsPrice.set("Rs. "+str(round(self.totalSoups_price)))
            
            self.totalsnacks_price =float(
                    (self.pannerPakora.get()*self.pannerPakora_price)+
                    (self.chickenPakora.get()*self.chickenPakora_price)+
                    (self.fishPakora.get()*self.fishPakora_price)+
                    (self.fishFinger.get()*self.fishFinger_price)+
                    (self.chicken65.get()*self.chicken65_price)+
                    (self.chickenHoney.get()*self.chickenHoney_price)
            )
            self.snacksPrice.set("Rs. "+str(round(self.totalsnacks_price)))
            
            self.totaldrinks_price =float(
                    (self.bisleri.get()*self.bisleri_price)+
                    (self.coke.get()*self.coke_price)+
                    (self.sprite.get()*self.sprite_price)+
                    (self.redBull.get()*self.redBull_price)+
                    (self.thumbsUp.get()*self.thumbsUp_price)
            )
            self.drinksPrice.set("Rs. "+str(round(self.totaldrinks_price)))

            
            self.totaltandori_price =float(
                    (self.chickenTandori.get()*self.chickenTandori_price)+
                    (self.CheeseKebab.get()*self.cheeseKebab_price)+
                    (self.afghaniTandori.get()*self.afghaniTandori_price)+
                    (self.chickenTangri.get()*self.chickenTangri_price)+
                    (self.seekhKebab.get()*self.seekhKebab_price)
            )
            self.tandoriPrice.set("Rs. "+str(round(self.totaltandori_price)))
            
            self.totalroti_price =float(
                    (self.tandoriRoti.get()*self.tandoriRoti_price)+
                    (self.rumaliRoti.get()*self.rumaliRoti_price)+
                    (self.butterNaan.get()*self.butterRoti_price)+
                    (self.garlicNaan.get()*self.garlicRoti_price)+
                    (self.lacchaParatha.get()*self.lacchaRoti_price)
            )
            self.rotiPrice.set("Rs. "+str(round(self.totalroti_price)))
            
            self.totaldesserts_price =float(
                    (self.shahiTukra.get()*self.shahiTukra_price)+
                    (self.falooda.get()*self.falooda_price)+
                    (self.rasmalai.get()*self.rasmalai_price)+
                    (self.pistachio.get()*self.pistachio_price)+
                    (self.chocoChip.get()*self.chocoChip_price)+
                    (self.chocoVanilla.get()*self.chocoVanilla_price)
            )
            self.dessertsPrice.set("Rs. "+str(round(self.totaldesserts_price)))
            
            self.total_price = float(
                    self.totalSoups_price +
                    self.totalsnacks_price +
                    self.totaldesserts_price +
                    self.totaltandori_price +
                    self.totalroti_price +
                    self.totaldrinks_price
            )
            self.totalAmount.set("Rs. "+ str(round(self.total_price)))
            self.gstprice = round(self.total_price*0.05)
            self.gst_Amount.set("Rs. "+ str(self.gstprice))
            self.Amountwith_Gst.set("Rs. "+ str(round(self.total_price+self.gstprice)))
            self.newAmountPaid = str(round(self.total_price+self.gstprice))
            
    def welcome_bill(self):
            self.textarea.delete('1.0',END)
            self.textarea.insert(END,"\t\tFood King\n")
            self.textarea.insert(END,"\tTaloja-phase1,Navi-Mumbai 410208\n")
            self.textarea.insert(END,"\tPhone no:9988776655\n\n")
            self.textarea.insert(END,f"Bill no:{self.customerBill_no.get()}\n")
            self.textarea.insert(END,f"Customer Name:{self.customerName.get()}\n")
            self.textarea.insert(END,f"Customer Phone no:{self.customerPhone.get()}\n")
            self.textarea.insert(END,f"________________________________________\n")
            self.textarea.insert(END,f"Items\t\tQty Item-Price Price\n")
            self.textarea.insert(END,f"________________________________________\n\n")


    def bill_area(self):
            self.total()
            if self.customerName.get()=="" or self.customerPhone.get()=="":
                    tmsg.showerror("Alert","Customers Details are compulsory!")
            elif self.total_price == 0:
                    tmsg.showerror("Alert", "Please select atleast one item to print the Bill!")
            else:    
                self.welcome_bill()
                # print(self.total_price == 0)
                #soups
                if self.totalSoups_price != 0:
                        self.textarea.insert(END,f"\t\t*Soups*\n")
                        
                if self.tomatoSoup.get() != 0:
                        #     self.textarea.insert(END,"hi")
                        self.textarea.insert(END,f"Tomato Soup     {self.tomatoSoup.get()}    {self.tomatoSoup_price}        {self.tomatoSoup.get()*self.tomatoSoup_price}\n")
                
                if self.cornSoup.get() != 0:
                        #     self.textarea.insert(END,"hi")
                        self.textarea.insert(END,f"Corn Soup       {self.cornSoup.get()}    {self.cornSoup_price}        {self.cornSoup.get()*self.cornSoup_price}\n")
                
                if self.sourSoup.get() != 0:
                        #     self.textarea.insert(END,"hi")
                        self.textarea.insert(END,f"Sour Soup       {self.sourSoup.get()}    {self.sourSoup_price}        {self.sourSoup.get()*self.sourSoup_price}\n")
                
                if self.pannerSoup.get() != 0:
                        #     self.textarea.insert(END,"hi")
                        self.textarea.insert(END,f"Paneer Soup     {self.pannerSoup.get()}    {self.pannerSoup_price}        {self.pannerSoup.get()*self.pannerSoup_price}\n")
                
                if self.chickenSoup.get() != 0:
                        self.textarea.insert(END,f"Chicken Soup    {self.chickenSoup.get()}    {self.chickenSoup_price}        {self.chickenSoup.get()*self.chickenSoup_price}\n")
                
                if self.italianSoup.get() != 0:
                        self.textarea.insert(END,f"Italian Soup    {self.italianSoup.get()}    {self.italianSoup_price}        {self.italianSoup.get()*self.italianSoup_price}\n")

                #snacks
                
                if self.totalsnacks_price != 0:
                        self.textarea.insert(END,f"\n\t\t*Snacks*\n")
                if self.pannerPakora.get() != 0:
                        self.textarea.insert(END,f"Paneer Pakora   {self.pannerPakora.get()}    {self.pannerPakora_price}        {self.pannerPakora.get()*self.pannerPakora_price}\n")
                
                if self.chickenPakora.get() != 0:
                        self.textarea.insert(END,f"Chicken Pakora  {self.chickenPakora.get()}    {self.chickenPakora_price}        {self.chickenPakora.get()*self.chickenPakora_price}\n")
                
                if self.fishPakora.get() != 0:
                        self.textarea.insert(END,f"Fish Pakora     {self.fishPakora.get()}    {self.fishPakora_price}        {self.fishPakora.get()*self.fishPakora_price}\n")
                
                if self.fishFinger.get() != 0:
                        self.textarea.insert(END,f"Fish Finger     {self.fishFinger.get()}    {self.fishFinger_price}        {self.fishFinger.get()*self.fishFinger_price}\n")
                
                if self.chicken65.get() != 0:
                        self.textarea.insert(END,f"Chicken65       {self.chicken65.get()}    {self.chicken65_price}        {self.chicken65.get()*self.chicken65_price}\n")
                
                if self.chickenHoney.get() != 0:
                        self.textarea.insert(END,f"Chicken Honey   {self.chickenHoney.get()}    {self.chickenHoney_price}        {self.chickenHoney.get()*self.chickenHoney_price}\n")


                #dessets
                
                if self.totaldesserts_price != 0:
                        self.textarea.insert(END,f"\n\t*Desserts & Ice Cream*\n")
                if self.shahiTukra.get() != 0:
                        self.textarea.insert(END,f"Shahi Tukra     {self.shahiTukra.get()}    {self.shahiTukra_price}        {self.shahiTukra.get()*self.shahiTukra_price}\n")
                
                if self.falooda.get() != 0:
                        self.textarea.insert(END,f"Kesar Falooda   {self.falooda.get()}    {self.falooda_price}        {self.falooda.get()*self.falooda_price}\n")
                
                if self.rasmalai.get() != 0:
                        self.textarea.insert(END,f"Rasmalai        {self.rasmalai.get()}    {self.rasmalai_price}        {self.rasmalai.get()*self.rasmalai_price}\n")
                
                if self.pistachio.get() != 0:
                        self.textarea.insert(END,f"Pistachio       {self.pistachio.get()}    {self.pistachio_price}        {self.pistachio.get()*self.pistachio_price}\n")
                
                if self.chocoChip.get() != 0:
                        self.textarea.insert(END,f"Choco Chip      {self.chocoChip.get()}    {self.chocoChip_price}        {self.chocoChip.get()*self.chocoChip_price}\n")
                
                if self.chocoVanilla.get() != 0:
                        self.textarea.insert(END,f"Choco Vanilla   {self.chocoVanilla.get()}    {self.chocoVanilla_price}        {self.chocoVanilla.get()*self.chocoVanilla_price}\n")
                

                #Tandori 
                
                if self.totaltandori_price != 0:
                        self.textarea.insert(END,f"\n\t*Tandori & Kebab*\n")
                if self.chickenTandori.get() != 0:
                        self.textarea.insert(END,f"ChickenTandori  {self.chickenTandori.get()}    {self.chickenTandori_price}        {self.chickenTandori.get()*self.chickenTandori_price}\n")
                
                if self.CheeseKebab.get() != 0:
                        self.textarea.insert(END,f"Cheese Kebab    {self.CheeseKebab.get()}    {self.cheeseKebab_price}        {self.CheeseKebab.get()*self.cheeseKebab_price}\n")
                
                if self.afghaniTandori.get() != 0:
                        self.textarea.insert(END,f"AfghaniTandori  {self.afghaniTandori.get()}    {self.afghaniTandori_price}        {self.afghaniTandori.get()*self.afghaniTandori_price}\n")
                
                if self.chickenTangri.get() != 0:
                        self.textarea.insert(END,f"Chicken Tangri  {self.chickenTangri.get()}    {self.chickenTangri_price}        {self.chickenTangri.get()*self.chickenTangri_price}\n")
                
                if self.seekhKebab.get() != 0:
                        self.textarea.insert(END,f"Seekh Kebab     {self.seekhKebab.get()}    {self.seekhKebab_price}        {self.seekhKebab.get()*self.seekhKebab_price}\n")


                #roti
                
                if self.totalroti_price != 0:
                        self.textarea.insert(END,f"\n\t\t*Roti & Naan*\n")
                if self.tandoriRoti.get() != 0:
                        self.textarea.insert(END,f"Tandori Roti    {self.tandoriRoti.get()}    {self.tandoriRoti_price}        {self.tandoriRoti.get()*self.tandoriRoti_price}\n")
                
                if self.rumaliRoti.get() != 0:
                        self.textarea.insert(END,f"Rumali Roti     {self.rumaliRoti.get()}    {self.rumaliRoti_price}        {self.rumaliRoti.get()*self.rumaliRoti_price}\n")
                
                if self.butterNaan.get() != 0:
                        self.textarea.insert(END,f"Butter Naan     {self.butterNaan.get()}    {self.butterRoti_price}        {self.butterNaan.get()*self.butterRoti_price}\n")
                
                if self.garlicNaan.get() != 0:
                        self.textarea.insert(END,f"Garlic Naan     {self.garlicNaan.get()}    {self.garlicRoti_price}        {self.garlicNaan.get()*self.garlicRoti_price}\n")
                
                if self.lacchaParatha.get() != 0:
                        self.textarea.insert(END,f"Laccha Paratha  {self.lacchaParatha.get()}    {self.lacchaRoti_price}        {self.lacchaParatha.get()*self.lacchaRoti_price}\n")

                #drinks
                
                if self.totaldrinks_price != 0:
                        self.textarea.insert(END,f"\n\t\t*Drinks*\n")
                if self.bisleri.get() != 0:
                        self.textarea.insert(END,f"Bisleri         {self.bisleri.get()}    {self.bisleri_price}        {self.bisleri.get()*self.bisleri_price}\n")

                if self.coke.get() != 0:
                        self.textarea.insert(END,f"Coke            {self.coke.get()}    {self.coke_price}        {self.coke.get()*self.coke_price}\n")

                if self.sprite.get() != 0:
                        self.textarea.insert(END,f"Sprite          {self.sprite.get()}    {self.sprite_price}        {self.sprite.get()*self.sprite_price}\n")

                if self.redBull.get() != 0:
                        self.textarea.insert(END,f"Red Bull        {self.redBull.get()}    {self.redBull_price}        {self.redBull.get()*self.redBull_price}\n")

                if self.thumbsUp.get() != 0:
                        self.textarea.insert(END,f"ThumbsUp        {self.thumbsUp.get()}    {self.thumbsUp_price}        {self.thumbsUp.get()*self.thumbsUp_price}\n")

                if self.total_price != 0:
                        self.textarea.insert(END,f"\n----------------------------------------\n")
                        self.textarea.insert(END,f"\n   Total Amount: Rs. {int(self.total_price)}")
                        self.textarea.insert(END,f"\n   GST Amount(5%): Rs. {int(self.gstprice)}")
                        self.textarea.insert(END,f"\n   Amount to be Paid: Rs. {self.newAmountPaid}")
                        self.textarea.insert(END,f"\n________________________________________\n")
                # self.saveBill()

    def saveBill(self):
            self.bill_area()
            if self.customerName.get()=="" or self.customerPhone.get()=="":
                #     tmsg.showerror("Alert","Customers Details are compulsory!")
                pass
            elif self.total_price == 0:
                #     tmsg.showerror("Alert", "Please select atleast one item to print the Bill!")
                pass
            else:
                self.billData = self.textarea.get(1.0,END)
                f1 = open("customerBills/"+str(self.customerBill_no.get())+".txt","w")
                f1.write(self.billData)
                f1.close()


    def printBill(self):
            file_path = "customerBills\\"+ str(self.customerBill_no.get()) +".txt"
        #     file_path = r"customerBills\7048.txt"
            os.startfile(file_path,'print')

    def findBill(self):
            present = "no"
            for i in os.listdir("customerBills/"):
                    if i.split('.')[0] == self.search_bill.get():
                            
                            f1 = open(f"customerBills/{i}","r")
                            self.textarea.delete('1.0',END)
                            for d in f1:
                                self.textarea.insert(END,d)
                            f1.close()
                            present = "yes"

            if present == "no":
                            
                            tmsg.showerror("Error","Invalid Bill no.")

    def clearData(self):
            
            
        #soups
        self.tomatoSoup.set(0)
        self.cornSoup.set(0)
        self.sourSoup.set(0)
        self.pannerSoup.set(0)
        self.chickenSoup.set(0)
        self.italianSoup.set(0)
        
        #snacks
        self.pannerPakora.set(0)
        self.chickenPakora.set(0)
        self.fishPakora.set(0)
        self.fishFinger.set(0)
        self.chicken65.set(0)
        self.chickenHoney.set(0)

        #desserts
        self.shahiTukra.set(0)
        self.falooda.set(0)
        self.rasmalai.set(0)
        self.pistachio.set(0)
        self.chocoChip.set(0)
        self.chocoVanilla.set(0)

        #tandori
        self.chickenTandori.set(0)
        self.CheeseKebab.set(0)
        self.afghaniTandori.set(0)
        self.chickenTangri.set(0)
        self.seekhKebab.set(0)

        #Roti
        self.tandoriRoti.set(0)
        self.rumaliRoti.set(0)
        self.butterNaan.set(0)
        self.garlicNaan.set(0)
        self.lacchaParatha.set(0)
        

        #drinks
        self.bisleri.set(0)
        self.coke.set(0)
        self.sprite.set(0)
        self.redBull.set(0)
        self.thumbsUp.set(0)
        
        #total
        self.soupsPrice.set("")
        self.snacksPrice.set("")
        self.drinksPrice.set("")
        self.dessertsPrice.set("")
        self.tandoriPrice.set("")
        self.rotiPrice.set("")
        
        self.totalAmount.set("")
        self.gst_Amount.set("")
        self.Amountwith_Gst.set("")
        
        #customer
        self.customerName.set("")
        self.customerPhone.set("")
        self.customerBill_no.set("")
        x = random.randint(1000,9999)
        self.customerBill_no.set(str(x))
        self.search_bill.set("")
        
        self.customerBill_no.set("")
        x = random.randint(1000,9999)
        self.customerBill_no.set(str(x))
        self.search_bill.set("")
        self.welcome_bill()

            

root = Tk() 
obj = billApplication(root)



root.mainloop()