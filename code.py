import sqlite3
import random
import datetime
import speech_recognition as sr
import qrcode
import image

def fizzbuzz(num):
    for a in range(num):
        if a%3==0 and a%5==0:
            print(str(a)+" - fizzbuzz")
        elif a%3==0:
            print(str(a)+" - fizz")
        elif a%5==0:
            print(str(a)+" - buzz")

def birthdayparadox():
   birthday=[]
   i=0
   while(i<50):
       year=random.randint(1970,2020)
       if year%4==0 and year%100!=0 or year%400==0:
           leap=1
       else:
           leap=0
       month=random.randint(1,12)
       if month==2 and leap==1:
           day=random.randint(1,29)
       elif month==2 and leap==0:
           day=random.randint(1,28)
       elif month==7 or month==8:
           day=random.randint(1,31)
       elif month%2!=0 and month<7:
           day=random.randint(1,31)
       elif month%2==0 and month>7 and month<12:
           day=random.randint(1,30)
       else:
           day=random.randint(1,30)
       dd = datetime.date(year, month, day)
       day_of_year =dd.timetuple().tm_yday
       i=i+1
       birthday.append(day_of_year)
   birthday.sort()
   i=0
   while(i<50):
       print(birthday[i])
       i=i+1

def leapyear():
    year=int(input("enter the year:"))
    if year % 4==0 and year % 100!=0 or year  % 400==0:
        print("given year is a leap year")
    else:
        print("given year is not a leap yeap")

def guessmovie():
    movies=["anand","drishyam","nayak","golmaal","dangal","taare zameen par","aag","one man army","vikram betal"]
    def create_question(movie):
        n=len(movie)
        letter=list(movie)
        temp=[]
        for i in range(n):
            if letter[i]==" ":
                temp.append(" ")
            else:
                temp.append("*")
        qn="".join(str(x) for x in temp)
        return qn

    def is_present(letter,movie):
        c=movie.count(letter)
        if c==0:
            return False
        else:
            return True

    def unlock(qn,movie,letter):
        ref=list(movie)
        qn_list=list(qn)
        temp=[]
        n=len(movie)
        for i in range(n):
            if ref[i]==' ' or ref[i]==letter:
                temp.append(ref[i])
            else:
                if qn_list[i]=="*":
                    temp.append("*")
                else:
                    temp.append(ref[i])
        qn_new="".join(str(x) for x in temp)
        return qn_new
    def play():
        p1name = input("player 1 - please enter your name:")
        p2name = input("player 2 - please enter your name:")
        pp1 = pp2 = 0
        turn = 0
        while (True):
            if turn % 2 == 0:
                print(p1name + " its your chance")
                picked_movie = random.choice(movies)
                qn = create_question(picked_movie)
                print(qn)
                modified_qn = qn
                not_said = True
                while not_said:
                    letter = input("your letter:")
                    if is_present(letter, picked_movie):
                        modified_qn = unlock  (modified_qn, picked_movie, letter)
                        print(modified_qn)
                        d = input("press 1 to guess the movie or 2 to unlock another letter")
                        if d =='1':
                            ans = input("your answer:")
                            if ans == picked_movie:
                                pp1 = pp1 + 1
                                print("correct")
                                not_said=False
                                print(p1name," your score is",pp1)
                            else:
                                print("wrong answer,try again!")


                    else:
                        print(letter + " not found")
                c = input("press 1 to continue or 0 to stop")
                if c == 0:
                    print(p1name, "your score is ", pp1)
                    print(p2name, "your score is ", pp2)
                    break

            else:
                print(p2name + " its your chance")
                picked_movie = random.choice(movies)
                qn = create_question(picked_movie)
                print(qn)
                modified_qn = qn
                not_said = True
                while not_said:
                    letter = input("your letter:")
                    if is_present(letter, picked_movie):
                        modified_qn = unlock(modified_qn, picked_movie, letter)
                        print(modified_qn)
                        d = input("press 1 to guess the movie or 2 to unlock another letter")
                        if d == '1':
                            ans = input("your answer:")
                            if ans == picked_movie:
                                pp1 = pp1 + 1
                                print("correct")
                                not_said = False
                                print(p1name, " your score is", pp1)
                            else:
                                print("wrong answer,try again!")


                    else:
                        print(letter + " not found")
                c = input("press 1 to continue or 0 to stop")
                if c == 0:
                    print(p1name, "your score is ", pp1)
                    print(p2name, "your score is ", pp2)
                    break
            turn = turn + 1
    play()

def speech_to_text():
    audio_file=("sample_lokeshku.wav")
    r=sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio=r.record(source)
    try:
        print("audio file contains: \n "+r.recognize_google(audio))
    except sr.UnknownValueError :
        print("google speech recogniser could not understand audio")
    except sr.RequestError:
        print("couldn't get the result")

def montehall():
    doors=[0]*3
    gotdoors=[0]*2
    swap=0
    dont_swap=0
    j=0
    while j<10:
        x=random.randint(0,2)
        doors[x]='BMW'
        for i in range(0,3):
            if i==x:
                continue
            else:
                doors[i]='GOT IT'
                gotdoors.append(i)
        print("round : ",j+1)
        choice=int(input("enter your choice: "))
        door_open=random.choice(gotdoors)
        while door_open==choice:
            door_open=random.choice(gotdoors)
        ch=input("do you want to swap (y/n) : ")
        if ch=='y':
            if doors[choice]=='GOT IT':
                print("player wins")
                swap=swap+1
            else:
                print("player lost")
        else:
            if doors[choice]=="GOT IT":
                print("player lost")
            else:
                print("player wins")
                dont_swap=dont_swap+1

        print("wins with swap : ",swap)
        print("wins with dont swap : ",dont_swap)
        print("----------------------------------")

        j=j+1

def encr():
    def encrypt(ltr,key):
        l=[]
        for each in list(ltr):
            l.append(chr(ord(each)+1))
        return ("".join(l))
    letter_body="ABCDEFGH"
    d=encrypt(letter_body,4)
    print(d)

def guess(num):
    a=input("guess a number")
    if a==num:
        print("success")
    else:
        guess(num)

def database1():
    conn = sqlite3.connect('emailsdb.sqlite')
    cur = conn.cursor()

    cur.execute('''
    DROP TABLE IF EXISTS Counts''')

    cur.execute('''
    CREATE TABLE Counts (org TEXT, count INTEGER)''')

    fname = input('Enter file name: ')
    if ( len(fname) < 1 ) : fname = 'mbox.txt'
    fh = open(fname)
    for line in fh:
        if not line.startswith('From: ') : continue
        pieces = line.split()
        email = pieces[1]
        parts = email.split('@')
        org = parts[-1]
        cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
        row = cur.fetchone()
        if row is None:
            cur.execute('''INSERT INTO Counts (org, count) 
                    VALUES ( ?, 1 )''', ( org, ) )
        else :
            cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?',
                (org, ))
        conn.commit()

    sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

    print()
    print ("Counts:")
    for row in cur.execute(sqlstr) :
        print (str(row[0]), row[1])

    cur.close()

def qrcode_generator():

    qr = qrcode.QRCode(
        version=1,
        box_size=5,
        border=5

    )
    conn=sqlite3.connect('emaildb.sqlite')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Counts")

    row1 = cur.fetchall("org")
    for ite in row1:
        print(ite)
    for ite in row1:
        qr.add_data(ite)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.save("1.jpg")

speech_to_text()
