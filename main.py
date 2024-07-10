from time import sleep
from mainbackend import *
user = None

def main(clear=True):
    if clear == True:
        clearscreen()
    print ("SDVXTOOLS CHALLENGES")
    print ("1. Input Challenge Code")
    print ("2. Create User")
    print ("3. Update User VF")
    print ("4. List Users")
    print ("type 'userset-NAME' to set your user")
    print ("")
    usrinput = input(">>>")
    if usrinput == "1":
        clearscreen()
        print("Paste Your Challenge code")
        usrinput = input(">>>")
        challengecode(usrinput)
    if usrinput == "2":
        createaccount()
    if usrinput == "3":
        updateuser()
    if usrinput == "4":
        listallusers()
    if "userset" in usrinput:
        setuser(usrinput)

def createaccount():
    clearscreen()
    print("Enter Username")
    print ("")
    usrinput = input(">>>")
    hold = usrinput
    print("Enter your volforce")
    print("NOTE dont enter your division (eg. dandelion,crimson,imperial) but rather enter your volforce numbers")
    print ("")
    usrinput = input(">>>")
    hold2 = usrinput
    MAKEuser(hold,hold2)
    main()

def updateuser():
    clearscreen()
    display = GETallusers()
    for i in range(len(display)):
        print (f"{i}. {display[i][0]}")
    
    print ("select which user to update")
    hold1 = input (">>>")
    print ("Input your new VF")
    hold2 = input (">>>")
    UPDATEuserinto(clean(display[int(hold1)][0]),int(hold2))
    main()

def listallusers():
    display = GETallusers()
    for i in range(len(display)):
        print (f"{i}. {display[i][0]}")
    main(False)

def setuser(COMMAND):
    user = COMMAND.replace("userset-","")
    print(f"\n Set user {user} \n")
    main(False)


def challengecode(INPUT):
    if user != None:
            hold = GETuserVF(user)
            challenge = challenges(hold,user)
            challenge.translate_id(INPUT)
            yourchallenge = challenge.get_challenge()
            print (yourchallenge)
            hold2 = challenge.checkdbforscore()
            while "CLEAR" not in hold2:
                sleep(5)
                hold2 = challenge.checkdbforscore()

            print (f"You have gained {hold2[1]} volpoints!")
            main()
    else:
        hold = GETuserVF("GUEST")
        challenge = challenges(hold,"GUEST")
        challenge.translate_id(INPUT)
        yourchallenge = challenge.get_challenge()
        print (yourchallenge)
        hold2 = challenge.checkdbforscore()
        while "CLEAR" not in hold2:
            sleep(5)
            hold2 = challenge.checkdbforscore()

        print (f"You have gained {hold2[1]} volpoints!")
        main()

def clean(string) -> str:
    string = string.replace("'","")
    string = string.replace(",","")
    return string

def clearscreen():
    for i in range(500):
            print("\n")
    

if __name__ == "__main__":
    main()