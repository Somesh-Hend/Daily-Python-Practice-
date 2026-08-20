print("------------------------------------------------------------")
print("Wellcome to SKBC".center(60))
print("------------------------------------------------------------")
tuple=(1000,2000,5000,10000,20000,50000,100000,400000,800000,1000000)
def answer_checka( ):
    global answer
    if answer=="a":
        print("you are correct")
    else:
        print("sorry you are out of kbc")
        exit( )
def answer_checkb():
    global answer
    if answer=="b":
        print("you are correct")
    else:
        print("sorry you are out of kbc")
        exit( )
def answer_checkc( ):
    global answer
    if answer=="c":
        print("you are correct")
    else:
        print("sorry you are out of kbc")
        exit( )
def answer_checkd( ):
    global answer
    if answer=="d":
        print("you are correct")
    else:
        print("sorry you are out of kbc")
        exit( )
def list_maker( ):
    global lis
    print("a)",lis[0])
    print("b)",lis[1])
    print("c)",lis[2])
    print("d)",lis[3])
enter=input("click Enter for your first question")
print("------------------------------------------------------------")
print("Question no. 1st".center(60))
print("kontya deshane sarvat aadhi kagdi mudra vaprnyat suruvat keli hoti?")
lis=["India","chaina","america","britane"]
list_maker( )
answer=input("Enter your Answer:")
answer_checkb()
print("You win",tuple[0],".rs")
print("------------------------------------------------------------")
print("Question no.2".center(60))
print("India la kontya varshi swatantra milal hote?")
lis=[1949,1950,1947,1948]
list_maker( )
answer=input("Enter your Answer:")
answer_checkc( )
print("You win",tuple[1],".rs")
print("------------------------------------------------------------")
print("Question no.3".center(60))
print("Chatrapati Shivaji Maharajacha jalm kontya varshi zala hota?")
lis=[1630,1632,1633,1631]
list_maker( )
answer=input("Enter your Answer:")
answer_checka( )
print("You win",tuple[2],".rs")
print("------------------------------------------------------------")
print("Question no.4".center(60))
print("Mumbai maharastra chya aadhi kontya state la denyachi tayari chalu hoti?")
lis=["Gova","Andrapradesh","Madyapradesh","Gujrat"]
list_maker( )
answer=input("Enter your answer:")
answer_checkd( )
print("You win",tuple[3],".rs")
print("------------------------------------------------------------")
print("Question no.5".center(60))
print("Which state is having 100% litresy rate?")
lis=["Maharastra","Gova","Kerla","Karnataka"]
list_maker( )
answer=input("Enter your answer:")
answer_checkc( )
print("You win",tuple[4],".rs")
print("------------------------------------------------------------")
print("Question no.6".center(60))
print("Konti country che lok Sarvat aadhi kalash parvatavar pohochle?")
lis=["Nepal","India","Chiana","Konich nahi pohochu sakle"]
list_maker( )
answer=input("Enter your answer:")
answer_checkd( )
print("You win",tuple[5],".rs")
print("------------------------------------------------------------")