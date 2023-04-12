
import tkinter as rk
import datetime
from tkinter import messagebox
from tkinter import ttk
import random
import mysql.connector as mani
mycon=mani.connect(host="localhost",user="root",password='$$$$$$$$',database="MYdatabase")
curdor=mycon.cursor(buffered=True)
list2=[]
list4=[]
list5=[]
a,b,g1,rooj1=0,0,0,0
#This creates and enters data in required tables:-
def railways():
    curdor.execute("CREATE TABLE info(username VARCHAR(39),pass VARCHAR(20))")
    curdor.execute("CREATE TABLE Railways(trainnam VARCHAR(50),Place VARCHAR(20),Reacpla VARCHAR(69),Depttime VARCHAR(16),Reactime VARCHAR(16),Fare INT)")
    curdor.execute('CREATE TABLE booked(name Varchar(56),age int,gender Varchar(10),referenceno int)')
    sql="INSERT INTO Railways(trainnam,Place,Reacpla,Depttime,Reactime,Fare) VALUES (%s,%s,%s,%s,%s,%s)"
    val=("Chambal Express","Mathura","Hawrah","4:15PM","6:45AM",2400)
    curdor.execute(sql,val) 	
    val1=("Chitrakoot Express","Lucknow","Madanmahal","5.30PM","7.35AM",1235) 
    curdor. execute(sql, val1)
    val2=("Lucknow Mail","Lucknow","New Delhi","2.55PM","6PM",1500)
    curdor.execute(sql,val2)
    val3=("Agra-Bhopal Section","Agra","Bhopal","2.10PM","5.25PM",340)
    curdor.execute(sql,val3)
    val4=("Allahabad-Haridwar Express","Allahbad","Haridwar","2.15AM","11.30PM",3520)
    curdor.execute(sql,val4)
    val5=("Jan Sadhran Express","Gorakhpur","Amritsar","6.35AM","10.45PM",1460)
    curdor.execute(sql,val5)
    val6=("Antyodaya Express","Gorakhpur","Mumbai","12.20AM","8.30AM",2460)
    curdor.execute(sql,val6)
    val7=("Intercity Express","Bareily","NewDelhi","10.10AM","4.45PM",267)
    curdor.execute(sql,val7)
    val8=("AgraCantt-NewDelhi Express","Agra cantt","New Delhi","10.20AM","6.00PM",330)
    curdor.execute(sql,val8)
    val9=("Taj Express","Hazrat Nizzamudin","Jhansi","2.00PM","7.00AM",685)
    curdor.execute(sql,val9)
    val10=("Dakshin Express","Hazrat Nizzamudin","Hyderabad Deccan","4.45AM","11.35PM",2950)
    curdor.execute(sql,val10)
    val11=("Utsarg Express","kanpur","Chappra","8.40AM","4.45PM",645)
    curdor.execute(sql,val11)
    val12=("Gondwana Express","Hazrat Nizzamudin","Raigarh","7.05PM","3.20PM",2245)
    curdor.execute(sql,val12)
    val13=("Gomti Express","Lucknow NR","New Delhi","2.55PM","6.00AM",1500)
    curdor.execute(sql,val13)
    val14=("Mandore Express","Jodhpur","New Delhi","6.45AM","8.00PM",550)
    curdor.execute(sql,val14)
    val15=("Janshtabdi Express","Hazrat Nizzamudin","Ajmer","11.25PM","4.35",575)
    curdor.execute(sql,val15)
    val16=("Ala Hazrat Express","Bareily Junction","Bhuj","2.00PM","6.00AM",2245)
    curdor.execute(sql,val16)
    val17=("Sharn Shakti Express","Kanpur Central","New Delhi","6.30AM","11.45PM",445)
    curdor.execute(sql,val17)
railways() 
#Remove the upper (#) if running for first time
window = rk.Tk()
window.geometry("500x500")
window.title('Welcome:-')
window.resizable(0,0)
window.configure(background="royal blue")
op=rk.Label(window,text="Indian Railways",anchor='center',bg="royal blue",font="none 50 italic underline",fg="white").grid(row=1,column=1,columnspan=30,pady=30)
op=rk.StringVar()
def aisahibanaya(ae):
        global k1,k2
        sql2="select Depttime,Reactime from Railways where trainnam=%s"
        val=(ae,)
        curdor.execute(sql2,val)
        nn=curdor.fetchone()
        nm=list(nn)
        k1=nm[0]
        k2=nm[1]
#Here this function shows details on booking
def showdetails():
	window74.destroy()
	global window4,c
	window4=rk.Tk()
	window4.geometry("650x700")
	window4.resizable(0,0)
	window4.config(bg="light green")
	z1=random.randint(1,15)
	z2=random.randint(1,15)
	z3=random.randint(1,250)
	for i in range(0,f2):
		cbi=('''------------------------------------------------------ 
                              INDIAN RAILWAYS
                              
                       WELCOME TO INDIAN RAILWAYS:-                    
            Your ticket is booked as per following details:-
            Name                         '{}'
            Age                              {}
            Gender                       {}
            Reference no.             {}
            Train                     '{}'
            Date                       {},2020
            Departure  time           '{}'
            Arrival time               '{}'
            Platform no.                  {}
            Coach & seat no.         S{},{}
            Fare                           {}/- only
            (keep this reference no. for further references)
                    AAPKI YATRA MANGAL MAY HO:-)
        ---------------------------------------------------------''').format(list2[0+(f2-1)*i].get(),
            list2[1+(f2-1)*i].get(),list2[(len(list2)-f2)+i],list5[i],x1,rrrkkk,k1,k2,
            z1,z2,z3+i,x2)
		show=rk.Message(window4,text=cbi,aspect=3000)
		show.config(bg="light yellow",font=("times",10,"italic"))
		show.pack()
	sc=rk.Button(window4,text="Exit",font=("Aharoni",12),bg="coral",command=thanks)
	sc.pack()
	fc=rk.Button(window4,text="Main Menu",font=("Aharoni",12),bg="coral",command=smss)
	fc.pack()
def thanks():
    window69.destroy()
    window4.destroy()
    window.destroy()
#This function cancels the tickets            
def cancelled():
    global rooj1
    for i in range(0,bo):
        query=('select * from booked where name=%s and age=%s and referenceno=%s')
        values=(list4[0+3*i].get(),int(list4[1+3*i].get()),int(list4[2+3*i].get()))
        curdor.execute(query,values)
        ask=curdor.fetchone()
        if ask==None:
            messagebox.showerror('No record exists for',list4[0+3*i].get())
        if ask!=None:
            query2=('Delete from booked where name=%s and age=%s and referenceno=%s')
            value=(list4[0+3*i].get(),int(list4[1+3*i].get()),int(list4[2+3*i].get()),)
            curdor.execute(query2,value)
            mycon.commit()
            sd='Ticket cancelled for',list4[0+3*i].get()
            messagebox.showinfo('Cancelled',sd)
        rooj1=1
        adddata()
def cancelling():
    window.configure(bg="light blue")
    global bo,ii2,kk2,ll2,mm2,aa2,bb2,dd2
    bb1.destroy()
    di.destroy()
    ck.destroy()
    bo=rty.get()
    for i in range(0,bo):
        cc2=rk.StringVar()
        ff2=rk.StringVar()
        rr2=rk.StringVar()
        ii2=rk.Label(window,text="Passenger name",font=("Algerian",15),bg="light yellow")
        ii2.grid(row=13+(4*i),column=6,pady=2+(2*i))
        kk2=rk.Entry(window,textvariable=ff2)
        kk2.grid(row=13+(4*i),column=7,ipady=1+(2*i))
        list4.append(kk2)
        ll2=rk.Label(window,text="Passenger age",font=("Algerian",15),bg="light yellow")
        ll2.grid(row=14+(4*i),column=6,pady=2+(2*i))
        mm2=rk.Entry(window,textvariable=rr2)
        mm2.grid(row=14+(4*i),column=7,ipady=1+(2*i))
        list4.append(mm2)
        aa2=rk.Label(window,text="Reference No.",font=("Algerian",15),bg="light yellow")
        aa2.grid(row=15+(4*i),column=6,pady=2+(2*i))
        bb2=rk.Entry(window,textvariable=cc2)
        bb2.grid(row=15+(4*i),column=7,pady=1+(2*i))
        list4.append(bb2)        
    dd2=rk.Button(window,text="Submit",font=("Aharoni",19),bg="coral",command=cancelled)
    dd2.grid(row=25,column=6,pady=20)        
def cancel():
    global rty,bb1,di,ck
    rty=rk.IntVar()
    b4.destroy()
    b6.destroy()
    b5.destroy()
    di=rk.Label(window,text='How many tickets you want to cancel?',font=('Aharoni',14),bg='light yellow')
    di.grid(row=14,column=4,pady=20)
    ck=rk.Entry(window,textvariable=rty,font=("Arial",15))
    ck.grid(row=14,column=5,ipady=8)
    bb1=rk.Button(window,text="Submit",font=("Aharoni",19),bg="coral",command=cancelling)
    bb1.grid(row=17,column=4,pady=40)
#Used to know timings of a particular train:-    
def opp():
	b7.destroy()
	e6.destroy()
	ff1.destroy()
	f=(kkk.get())
	sql2="select Depttime,Reactime from Railways where trainnam=%s"
	val=(f,)
	curdor.execute(sql2,val)
	nn=curdor.fetchall()
	aisahibanaya(f)
	for o in range(0,1):
		v=nn[o]
		k1=v[0]
		k2=v[1]
		k1=str(k1)
		k2=str(k2)
		p="Train departure time-:"
		q="Train arrival time-:"
		ssr=p+k1+','+q+k2
		messagebox.showinfo("Train timings",ssr)
#Selection of Train to know the time of:-        
def xxx():
	window.configure(bg="sky blue")
	global kkk,b7,e6,ff1
	kkk=rk.StringVar()
	b6.destroy()
	ff1=rk.Label(window,text="Train name",font=("Algerian",17),bg="light yellow")
	ff1.grid(row=14,column=10,pady=20)
	e6=ttk.Combobox(window,width=32,textvariable=kkk)
	e6['values']=("Chambal Express","Sharn Shakti Express","Ala Hazrat Express","Janshtabdi Express","Mandore Express","Gomti Express","Gondwana Express",
   "Utsarg Express","Dakshin Express","Taj Express","Agracantt-New Delhi Express","Intercity Express","Antyodaya Express","Jan Sandhran Express","Allahabad-Haridwar Express",
   "Agra-Bhopal Section","Lucknow Mail","Chitrakoot Express","Chambal Express")
	e6.grid(row=14,column=11,ipady=5)
	e6.current()
	b7=rk.Button(window,text="Search",font=("Aharoni",19),bg="coral",command=opp)
	b7.grid(row=16,column=11,pady=40)
def proceed1():
    global window74
    window74=rk.Tk()
    window74.geometry("670x280")
    window74.resizable(0,0)
    window74.config(bg="white")
    justice=random.randint(2000,3000)
    frr=datetime.datetime.now()
    ssr=('''                ————————————————————————
                  *Transaction Successful*
     
               Amount Transferred        {}
               
               Transaction Id        {}
               
               Transaction date and Time    {}  
               ——————————————————————————''').format(s1,justice,frr)
    micheal=rk.Message(window74,text=ssr,aspect=2000)
    micheal.config(font=("times",10,"italic"),bg="light yellow")
    micheal.pack()
    messagebox.showinfo("Booked","Thanks for booking ticket")
    showdetails()
def lenovo():
	window69.configure(bg="aquamarine")
	global lmao,enterno,lol
	mau.destroy()
	mp.destroy()
	jk.destroy()
	lmao=rk.IntVar()
	lol=rk.StringVar()
	lol1=rk.StringVar()
	lol2=rk.IntVar()
	number=rk.Label(window69,text="Credit card no.",font=("Algerian",15),bg="light yellow")
	number.grid(row=5,column=0,pady=20)
	enterno=rk.Entry(window69,textvariable=lmao,font=("Arial",15))
	enterno.grid(row=5,column=1,ipady=6)
	pogo=rk.Label(window69,text="Name",font=("Algerian",15),bg="light yellow")
	pogo.grid(row=7,column=0,pady=20)
	entrykaro=rk.Entry(window69,textvariable=lol,font=("Arial",15))
	entrykaro.grid(row=7,column=1,ipady=6)
	pogo1=rk.Label(window69,text="Exp",font=("Algerian",15),bg="light yellow")
	pogo1.grid(row=9,column=0,pady=20)
	entrykaro1=rk.Entry(window69,textvariable=lol1,font=("Arial",15))
	entrykaro1.grid(row=9,column=1,ipady=3)
	pogo2=rk.Label(window69,text="CVV",font=("Algerian",15),bg="light yellow")
	pogo2.grid(row=11,column=0,pady=20)
	entrykaro=rk.Entry(window69,textvariable=lol2,font=("Arial",15))
	entrykaro.grid(row=11,column=1,ipady=3)
	amount=rk.Label(window69,text='Amount to be paid:-'+s1,font=("Algerian",15),bg="light yellow")
	amount.grid(row=13,column=0,pady=20)    
	proceed=rk.Button(window69,text="Proceed Billing",font=("Aharoni",19),bg="coral",command=proceed1)
	proceed.grid(row=14,column=1,pady=40)
def rms():
	global rrrkkk,mau,mp,jk,window69
	window2.destroy()
	mmm=(opk.get())
	rrr=(opppk.get())
	rrrkkk=mmm+rrr
	window69=rk.Tk()
	window69.geometry("750x550")
	window69.config(bg="light blue")
	mau=rk.Label(window69,text="Mode of payment",font=("Algerian",15),bg="light yellow")
	mau.grid(row=1,column=1,pady=20)
	mp=rk.Button(window69,text="Credit Card",font=("Aharoni",19),bg="coral",command=lenovo)
	mp.grid(row=3,column=0,pady=40)
	jk=rk.Button(window69,text="Paytm",font=("Aharoni",19),bg="coral",command=paytm)
	jk.grid(row=3,column=3,pady=40)    
def paytm():
    window69.configure(bg="aquamarine")
    mau.destroy()
    mp.destroy()
    jk.destroy()
    noe1=rk.IntVar()
    no=rk.Label(window69,text='Enter phone number:',font=("Algerian",15),bg="light yellow")
    no.grid(row=3,column=2,pady=20)
    noe=rk.Entry(window69,textvariable=noe1,font=("Arial",10))
    noe.grid(row=3,column=3,ipady=4)
    amount=rk.Label(window69,text='Amount to be paid:-'+s1,font=("Algerian",15),bg="light yellow")
    amount.grid(row=5,column=2,pady=30)
    proceed=rk.Button(window69,text="Proceed Billing",font=("Aharoni",19),bg="coral",command=proceed1)
    proceed.grid(row=8,column=3,pady=40)            
def smss():
        global rooj
        c=[kk,ii,ll,e69,e56,mm,pop,rr1,rr2,fck,bb]
        for i in c:
            i.destroy()
        rooj=1
        adddata()
#Asks user if they want to book the tickets:-    
def xx():
	global window2,list5,c
	window2=rk.Tk()
	window2.geometry("450x200")
	window2.resizable(0,0)
	window2.config(bg="light yellow")
	p=("You have to pay   {}/-").format(s1)
	msg=rk.Label(window2,text=p,font="none 15 italic underline")
	msg.grid(row=2,column=2,columnspan=5,pady=10)
	mrrk=rk.Button(window2,text="Pay it",font=("Aharoni",14),bg="coral",command=rms)
	mrrk.grid(row=15,column=5,pady=20)
	sc=rk.Button(window2,text="Cancel",font=("Aharoni",14),bg="coral",command=smss)
	sc.grid(row=15,column=7,pady=20)
	for i in range(0,f2):
            c=random.randint(1,100)
            while c in list5:
                c=random.randint(1,100)
            list5.append(c)
            sql1=("insert into booked values('{}',{},'{}',{})").format(list2[0+2*i].get()
            ,list2[1+2*i].get(),list2[(len(list2)-f2)+i],c+i)
            curdor.execute(sql1)
            mycon.commit()
def insert(x):
    list2.append(x)
#Takes passengers information:-            
def gk():
	global f2,list2,s1,ff,rr,mm,kk,ii,ll,e69,pop,rr1,rr2,fck,bb,e56,opk,opppk,radio1
	f2=(lk.get())
	for z in range(0,f2):
		mg.destroy()
		s2.destroy()
		ek.destroy()
		s1=f2*x2
		s1=str(s1)
		ff=rk.StringVar()
		rr=rk.StringVar()
		opk=rk.StringVar()
		opppk=rk.StringVar()
		radio1=rk.IntVar()
		radio2=rk.IntVar()
		ii=rk.Label(window,text="Passenger name",font=("Algerian",14),bg="light yellow")
		ii.grid(row=13+(3*z),column=8,pady=2+(2*z))
		kk=rk.Entry(window,textvariable=ff,font=("Arial",10))
		kk.grid(row=13+(3*z),column=9,ipady=1+(2*z))
		list2.append(kk)
		ll=rk.Label(window,text="Passenger age",font=("Algerian",14),bg="light yellow")
		ll.grid(row=14+(3*z),column=8,pady=2+(2*z))
		mm=rk.Entry(window,textvariable=rr,font=("Arial",10))
		mm.grid(row=14+(3*z),column=9,ipady=1+(2*z))
		list2.append(mm)
		pop=rk.Label(window,text="Passenger gender",font=("Algerian",14),bg="light yellow")
		pop.grid(row=15+(3*z),column=8,pady=2+(2*z))
		rr1=rk.Radiobutton(window,text='M',variable=radio1,value=1,command=lambda t='M',v=radio1:insert('Male'))
		rr1.grid(row=15+(3*z),column=9,sticky=rk.W,columnspan=1,pady=10)
		rr2=rk.Radiobutton(window,text='F',variable=radio2,value=2,command=lambda t='F',v=radio2:insert('Female'))
		rr2.grid(row=15+(3*z),column=10,sticky=rk.W,columnspan=1,pady=10)
	fck=rk.Label(window,text="Date",font=("Algeriam",14),bg="light yellow")
	fck.grid(row=16+(3*z),column=8,pady=10)
	e69=ttk.Combobox(window,width=6,textvariable=opk)
	e69["values"]=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
	e69.grid(row=16+(3*z),column=9,pady=10)
	e56=ttk.Combobox(window,width=6,textvariable=opppk)
	e56["values"]=("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")
	e56.grid(row=16+(3*z),column=10,pady=10)
	bb=rk.Button(window,text="Submit",font=("Aharoni",19),bg="coral",command=xx)
	bb.grid(row=18+(3*z),column=9,pady=30)
def ma():
	global lk,s2,mg,ek
	window.configure(bg="white")
	b3.destroy()
	f1.destroy()
	g.destroy()
	lk=rk.IntVar()
	mg=rk.Label(window,text="How many seats to book",font=("Algerian",18),bg="light yellow")
	mg.grid(row=16,column=8,pady=30)
	ek=rk.Entry(window,textvariable=lk,font=("Arial",14))
	s2=rk.Button(window,text="Submit",font=("Aharoni",19),command=gk,bg="coral")
	s2.grid(row=18,column=8,pady=40)
	ek.grid(row=16,column=9,ipady=5)
	e3.destroy()
	e4.destroy()
	me.destroy()
	me2.destroy()
#Searches for Trains available:-    
def ab():
    global fr,to,x1,x2,me,me2,g1
    if g1==1:
        me.destroy()
        me2.destroy()
        fr=(mr.get())
        to=mrk.get()
    sql=("SELECT trainnam,Fare FROM Railways WHERE Place=%s and Reacpla=%s")
    val=(mr.get(),mrk.get())
    curdor.execute(sql,val)
    ok=curdor.fetchone()
    if ok!=None:
            x1=ok[0]
            x2=ok[1]
            p=("Train- '{}'  ,  fare:- {}").format(x1,x2)
            me2=rk.Label(window,text='Trains Available are:-',font=('Algerain',15),bg='light green')
            me2.grid(row=25,column=9,pady=2)
            me=rk.Button(window,text=p,command=ma,font=("Aharoni",13),bg="cyan")
            me.grid(row=26,column=9,pady=10)
            b4.destroy()
            aisahibanaya(x1)
            g1=1
    if ok==None:
	    messagebox.showerror("not avail","No train availbale")
#takes reach and destination from user:-        
def book():
	global mr,mrk,f1,e4,g,e3,b3
	window.configure(bg="light blue")
	b6.destroy()
	b5.destroy()
	mr=rk.StringVar()
	mrk=rk.StringVar()
	f1=rk.Label(window,text="From where",font=("Algerian",17),bg="light yellow")
	f1.grid(row=15,column=8,pady=10)
	e3=ttk.Combobox(window,width=32,textvariable=mr)
	e3['values']=("Allahbad","Agra","Agra cantt","Bareily","Hazrat Nizzamudin",
          "Gorakhpur","kanpur","Kanpur Central","Lucknow","Lucknow NR",
          "Jodhpur","Mathura")
	e3.grid(row=15,column=9,ipady=5)
	e3.current()
	g=rk.Label(window,text="To where",font=("Algerian",17),bg="light yellow")
	g.grid(row=16,column=8,pady=10)
	e4=ttk.Combobox(window,width=32,textvariable=mrk)
	e4['values']=("Allahbad","Ajmer","Bhuj","New Delhi","Raigarh","Chappra",
          "Hyderabad Deccan","Jhansi","Mumbai","Amritsar","Bhopal",
          "Madanmahal","Hawrah")
	e4.grid(row=16,column=9,ipady=5)
	e4.current()
	b4.destroy()   
	b3=rk.Button(window,text="Search",font=("Aharoni",19),command=ab,bg="coral")
	b3.grid(row=18,column=9,pady=40)
#Checks if user data is in records or not:-    
def adddata():
         global username,password,d1,a,b4,b6,b,mk,b5,jmk
         if rooj1==1:
            list100=[ii2,kk2,ll2,mm2,aa2,bb2,dd2]
            for i in list100:
                i.destroy()
         if rooj==1 and rooj1==0:
             window69.destroy()
             window4.destroy()
         if rooj==0:
             username=(A.get())
             password=(B.get())
             sql="(select * from info where username= %s and pass= %s LIMIT 0,1)"
             val=(username,password)
             curdor.execute(sql,val)
             d1=curdor.fetchone()
             jmk=list(username)
         if d1!=None and jmk!=[] or rooj==1 or rooj1==1:
             window.configure(bg="cyan")
             b4=rk.Button(window,text="Book a ticket",font=("Aharoni",19),command=book,bg="coral")
             b4.grid(row=17,column=11,pady=20)
             b5=rk.Button(window,text='Cancel Ticket',font=('Aharoni',19),command=cancel,bg='coral')
             b5.grid(row=18,column=11,pady=20)
             b6=rk.Button(window,text="Know timing of trains",font=("Aharoni",19),bg="coral",command=xxx)
             b6.grid(row=19,column=11,pady=20)
             b1.destroy()
             e1.destroy()
             e2.destroy()
             D.destroy()
             E.destroy()
             a=1
             if rooj==0:    
                 if jmk==[] or d1==None:	         	         	        
	                 messagebox.showerror("Error","No user found")
	                 mk=rk.Button(window,text="Sign in",command=sign,font=("Aharoni",19),bg="coral")
	                 mk.grid(row=17,column=4,pady=40)
	                 b=1
#Inserts user data in records	        	        	       	       
def ap():
	global user,password,jk,b4,a,detail,b6,b5
	user=(r.get())
	password=(m.get())
	sql1="SELECT * FROM info WHERE username=%s"
	u=(user,)
	curdor.execute(sql1,u)
	jk=curdor.fetchone()
	mko=list(user)
	if mko==[]:
		messagebox.showerror("Invalid","Invalid name")
	if jk==None and mko!=[]:
	    window.config(bg="cyan")
	    messagebox.showinfo("Signup","You are sign in sucessfuly")
	    detail.destroy()
	    b5=rk.Button(window,text='Cancel Ticket',font=('Aharoni',19),command=cancel,bg='coral')
	    b5.grid(row=18,column=11,pady=20)
	    b4=rk.Button(window,text="Book a ticket",font=("Aharoni",19),command=book,bg="coral")	
	    b4.grid(row=17,column=11,pady=20) 
	    b6=rk.Button(window,text="Know timing of trains",font=("Aharoni",19),bg="coral",command=xxx)
	    b6.grid(row=19,column=11,pady=20)   
	    d.destroy()
	    e.destroy()
	    s.destroy()
	    f.destroy()
	    b2.destroy() 
	    sql="INSERT INTO info(username,pass) VALUES(%s,%s)"
	    val=(user,password)
	    curdor.execute(sql,val)
	    mycon.commit()
	if mko!=[] and jk!=None:
	    messagebox.showerror("Already exists","User already exist")
	    detail=rk.Button(window,text='Login',command=LOGIN,font=("Aharoni",19),bg="coral")
	    detail.grid(row=16,column=9,pady=40)
	    a=1	
#If new user, Then this allows to enter new data:-        
def sign():
	global r,m,d,e,s,f,b2
	r=rk.StringVar()
	m=rk.StringVar()
	mk.destroy()
	if b==1:
		list3=[b1,e1,e2,D,E]
		for i in list3:
			i.destroy()
	window.configure(bg='sky blue')
	detail.destroy()
	d=rk.Label(window,text="Username",font=("Algerian",16),bg="light yellow")
	d.grid(row=13,column=8,pady=10)
	e=rk.Entry(window,textvariable=r,font=("Arial",14))
	e.grid(row=13,column=9,ipady=10)
	s=rk.Label(window,text="Password",font=("Algerian",16),bg="light yellow")
	s.grid(row=15,column=8,pady=10)
	f=rk.Entry(window,textvariable=m,font=("Arial",14))
	f.grid(row=15,column=9,ipady=10)
	b2=rk.Button(window,text="Submit",command=ap,font=("Aharoni",18),bg="coral")
	b2.grid(row=17,column=9,pady=40)
#If old user, This akkows to login again:-    
def LOGIN():
        global A,B,b1,e1,e2,D,E,rooj
        o=(op.get())
        del(o)
        window.geometry("500x500")
        window.configure(bg="sky blue")
        detail.destroy()
        if a==1:
            list3=[d,e,s,f,b2]
            for i in list3:
                i.destroy()
        mk.destroy()
        A=rk.StringVar()
        B=rk.StringVar()
        D=rk.Label(window,text='Username',font=("Algerian",19),bg="light yellow")
        D.grid(row=13,column=8,pady=10)
        e1=rk.Entry(window,textvariable=A,font=("Arial",14))
        e1.grid(row=13,column=9,ipady=10)
        E=rk.Label(window,text='Password',font=("Algerian",19),bg="light yellow")
        E.grid(row=15,column=8,pady=10)
        e2=rk.Entry(window,textvariable=B,font=("Arial",14))
        e2.grid(row=15,column=9,ipady=10)
        rooj=0
        b1=rk.Button(window,text='Submit',width=10,command=adddata,font=("Aharoni",18),bg="coral")
        b1.grid(row=17,column=9,pady=40)         
detail=rk.Button(window,text='Login',command=LOGIN,font=("Aharoni",19),bg="coral")
mk=rk.Button(window,text="Sign in",command=sign,font=("Aharoni",19),bg="coral")
detail.grid(row=13,column=20,pady=40)
mk.grid(row=13,column=7,pady=40)
window.mainloop()  
Footer
© 2023 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
Pythonprojects/IndianRailways_tkinter.py at main · kashyap-ji/Pythonprojects
