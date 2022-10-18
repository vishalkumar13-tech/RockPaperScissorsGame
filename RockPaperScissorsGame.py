from tkinter import *
from PIL import Image , ImageTk
from tkinter import messagebox
import random 
import time

class gameHome(Tk):
    def __init__(self , master ):
        master.attributes('-fullscreen',True)

        plrname = StringVar()
        def startGame():
            if plrname.get():
                import time
                time.sleep(0.2)
                master = Toplevel()
                img = Image.open("RPSbg.jpg")
                img = img.resize((1600, 800), Image.ANTIALIAS)
                pic = ImageTk.PhotoImage(img)
                imglabel = Label(master, image=pic)
                imglabel.place(x=0, y=0, relheight=1, relwidth=1)
                gamePage(master , plrname.get())
            else:
                messagebox.showwarning("NOTE" ,"Hey anonymous!.....Enter your name")
                messagebox.Message(master)

        def gameInfo():
            messagebox.showinfo("About" , "This is a single player ROCK , PAPER , SCISSORS game. To win against the computer you need to score 5 points before the computer.\n                                                                                          By Atif")

        imgs = Image.open("air.hl.RockPaperScissors-w250.ico")  # imageNO:1
        imgs = imgs.resize((50,30), Image.ANTIALIAS)
        pics = ImageTk.PhotoImage(imgs)

        f = Frame(master)
        topleft = Label(f , image = pics )
        topleft.pack(side = "left")
        head = Label(f , text = "R O C K   P A P E R   S C I S S O R S" , font = "system 10 normal")
        head.pack(side = LEFT , fill = X ,expand = True)
        exitBtn = Button(f , text = "  X   " , command = quit  , font = "times 12 bold"  , bg = "red" ,fg ="white" , anchor = "ne")
        exitBtn.pack()
        f.pack(side = TOP ,fill = X)

        f = Frame(master, bg="red")
        Label(f, text="Enter your name : ", font="times 30 bold ", bg="red", fg="black").pack(side =  "left")
        nameIn = Entry(f, width=35, font="comicsansms 30 italic", bg="black", fg = "green" , textvariable=plrname , insertbackground = "green")
        nameIn.pack(side = "left"  , fill = X , expand = True)
        f.pack(anchor=CENTER , fill = X , ipadx = 30 , ipady = 50)

        
        def enter(event):
            startB.config(bg = "black" ,fg = "green")
        def leave(event):
            startB.config(bg = "green" ,fg = "black")

        def enterA(event):
            aboutB.config(bg="black", fg="green")
        def leaveA(event):
            aboutB.config(bg="green", fg="black")

        def enterC(event):
            quitB.config(bg="black", fg="green")

        def leaveC(event):
            quitB.config(bg="green", fg="black")

        f = Frame(master)
        startB = Button(f ,text="Start Game", width = 11 ,font="cursive 20 italic", bg="green" , fg = "black" , command = startGame ,bd = 5 , relief = RAISED)
        aboutB = Button(f ,text="About Game",width = 11 , font="cursive 20 italic", bg="green" , fg = "black" , command = gameInfo ,bd = 5 , relief = RAISED)
        startB.pack()
        aboutB.pack()
        quitB = Button(f ,text="Quit Game",width = 11 , font="cursive 20 italic", bg="green" , fg = "black" , command = quit ,bd = 5 , relief = RAISED)
        quitB.pack()
        startB.bind('<Enter>',enter)
        startB.bind('<Leave>',leave)
        aboutB.bind('<Enter>', enterA)
        aboutB.bind('<Leave>', leaveA)
        quitB.bind('<Enter>', enterC)
        quitB.bind('<Leave>',leaveC)
        f.pack(side = LEFT , padx = 110)



        img = Image.open("rpsimg.jpg")
        img = img.resize((1200, 500), Image.ANTIALIAS)
        pic = ImageTk.PhotoImage(img)

        w = Canvas(master, width=1000, height=500, bg='green')
        w.pack(pady=80)
        w.create_image(500, 250, image=pic)
        # todo : stone paper scissor images
        # TODO : imageresizing     -->Atif1.jpg  =  f"Atif"{1}png"  ---->  img = img.resize((400,400) , Image.ANTIALIAS
        master.mainloop()

class gamePage(Tk):
    def __init__(self , master , pName):

        master.geometry("900x400")
        master.configure(bg="orange")
        master.attributes('-fullscreen', True)
        rps = [ 'Paper','Rock' , 'Scissors']
        d = {'Paper': 0, 'Rock': 1, 'Scissors': 2}
        global gameOver
        gameOver = 0
        global pcounter
        pcounter = 0
        global ccounter
        ccounter = 0
        name = StringVar()
        name.set(pName)
        myTurn = StringVar()
        myTurn.set("Choose One ")
        winbtn = StringVar()
        winbtn.set("")
        cbtn = StringVar()
        cbtn.set("")
        pPts = IntVar()
        pPts.set(pcounter)
        cPts = IntVar(ccounter)
        cPts.set(0)

        def game(event):
            userTurn.config(bg = "black")
            userTurn.update()
            cbtn.set("Computer's turn ....")
            global gameOver
            global pcounter
            global ccounter
            pch = d[event.widget.cget("text")]  # 0/1/2
            cch = int(100*random.random())%3   # 0/1/2
            cbtn.set("Computer's turn .")
            lbl.update()
            time.sleep(0.4)
            cbtn.set("Computer's turn ..")
            lbl.update()
            time.sleep(0.3)
            cbtn.set("Computer's turn ....")
            lbl.update()
            time.sleep(0.2)
            cbtn.set(f"{name.get()} : {rps[pch]}       |       Computer : {rps[cch]}")
            winbtn.set(".........")
            b4.update()
            time.sleep(0.1)
            winbtn.set('.................')
            b4.update()
            time.sleep(0.1)
            winbtn.set('.............................')
            b4.update()
            time.sleep(0.1)
            winbtn.set('..........................................')
            b4.update()
            time.sleep(0.1)
            winbtn.set('....................................................')
            b4.update()
            time.sleep(0.1)
            winbtn.set('......................................................... ...')

            b4.update()
            time.sleep(0.2)
            if pch == cch:
                b4.config(bg = "white")

                winbtn.set("its a TIE !")
            elif cch - pch == 1 or cch - pch == -2:
                b4.config(bg = "green")
                winbtn.set(f"{name.get()} +1 ")
                pcounter += 1
                pPts.set(pcounter)
                print(f"{rps[cch]} won")
            else:
                b4.config(bg="red")
                winbtn.set("Computer +1")
                ccounter += 1
                cPts.set(ccounter)
                print(f"{rps[cch]} lost")

            if pcounter == 5:
                winbtn.set(f"You won by {pcounter - ccounter} points")
                b4.update()
                time.sleep(2)
                gameOver=1

            elif ccounter == 5:
                winbtn.set(f"Better luck next time :(")
                b4.update()
                time.sleep(2)
                gameOver=1

            elif ccounter == pcounter == 5:
                winbtn.set("TIE final score = 10")
                b4.update()
                time.sleep(2)
                gameOver=1
            if gameOver == 1:
                master.destroy()
            userTurn.config(bg="green")
            userTurn.update()

        imgs = Image.open("air.hl.RockPaperScissors-w250.ico")  # imageNO:1
        imgs = imgs.resize((50, 30), Image.ANTIALIAS)
        pics = ImageTk.PhotoImage(imgs)

        f = Frame(master)
        topleft = Label(f, image=pics)
        topleft.pack(side="left")
        head = Label(f, text="R O C K   P A P E R   S C I S S O R S", font="system 10 normal")
        head.pack(side=LEFT, fill=X, expand=True)
        exitBtn = Button(f, text="  X   ", command=quit, font="times 12 bold", bg="red", fg="white", anchor="ne")
        exitBtn.pack()
        f.pack(side=TOP, fill=X)

        f = Frame(master)  #points table
        Label(f, textvariable = name , font = "comicsansms 30 normal" ,anchor = "nw" , bg = "black" , fg ="green").pack( side = "left" , fill = BOTH , expand = True)
        Label(f, text = "Computer" , font = "comicsansms 30 normal", bg = "black" , fg ="green").pack(side = "left"  , fill = BOTH)
        f.pack(side = "top" , fill = BOTH)

        f = Frame(master)  #points table
        Label(f, textvariable = pPts , font = "comicsansms 30 normal" , bg = "black" , fg ="green" , anchor = "nw").pack(side = "left" ,fill = X ,expand = True)
        Label(f, textvariable = cPts , font = "comicsansms 30 normal", bg = "black" , fg ="green" ).pack(side = "right")
        f.pack(side = "top" , fill = BOTH)

        f = Frame(master , bg = "black") #player turn
        userTurn = Label(f , textvariable = myTurn ,font = "comicsansms 20 normal" , bg = "green" ,fg = "black")
        userTurn.pack(side = "left"  , ipadx = 20 , ipady = 20 ,padx = 100)
        b1 = Button(f , text="Rock", font="comicsansms 30 normal", bg="pink",bd = 10 )
        b1.pack(side = "left" , ipadx = 40 , padx = 30)
        b2 = Button(f , text="Paper", font="comicsansms 30 normal", bg="pink" , bd =10)
        b2.pack(side = "left" ,ipadx =30 , padx = 30 )
        b3 = Button(f , text="Scissors", font="comicsansms 30 normal", bg="pink" ,bd =10)
        b3.pack(side="left" ,padx =30)
        b1.bind('<Button-1>',game)
        b2.bind('<Button-1>',game)
        b3.bind('<Button-1>',game)
        f.pack(side = "top" ,pady = 10 , fill = BOTH)

        lbl = Label(master, textvariable = cbtn, bg="pink" ,font="comicsansms 30 normal"  , bd = 10 , relief = SUNKEN)
        lbl.pack( side = "top" , fill = "x" ,ipady = 30, padx = 30 , pady = 70)

        b4 = Label(master, textvariable = winbtn, bg="pink" ,font="comicsansms 30 normal" )
        b4.pack(side = "top" , fill = "x" ,ipady = 30, padx = 30 , pady = 70)

        master.mainloop()

master = Tk()
img = Image.open("RPSbg.jpg")   #imageNO:1
img = img.resize((1600,800) , Image.ANTIALIAS)
pic = ImageTk.PhotoImage(img)
imglabel = Label(master ,image=pic)
imglabel.place(x=0, y=0, relheight=1, relwidth=1)
gameHome(master)
master.mainloop()
