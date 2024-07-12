import random
from songs import *
import os
import sqlite3
from time import sleep

#EQUATION = y=1000000-\left(d\cdot10000-\left(v^{3}\cdot15+20000\right)\right) just put it in desmos 
#D = difficulty
# v = volforce
def equation(DIFF,VF):
    answer = 1000000 - (DIFF * 10000 - (VF ** 3 * 15 + 20000))
    return answer 

'''
if diff == 17:
            diff = "seventeen"
        elif diff == 18:
            diff = "eighteen"
        elif diff == 19:
            diff = "nineteen"
        elif diff == 20:
            diff = "twenty"
'''

class challenges():

    def __init__ (self,vf,user,CHECK_FOR_VF_IN_DB=False) -> None:

        if CHECK_FOR_VF_IN_DB == True:
            conn = sqlite3.connect(r"D:\usc\maps.db")
            cursor = conn.cursor()
            sql = f"SELECT VF FROM User WHERE Name LIKE '{user}'"
            cursor.execute(sql)
            vf = cursor.fetchone()
            
        self.vf = vf
        self.usr = user

    def make_id(self,diff) -> str:
        
        randomchart = random.randint(0,len(getsongslist(19)))
        # I think I want it formatted like this: RANDOMCHART-DIFF-GOALSCORE
        goalscore = equation(diff,self.vf)
        goalscore += random.randint(-10000,10000) #gotta add a bit of randomness :3
        if goalscore > 1000000:
            goalscore = 995000

        goalscore = (str(goalscore)+"0") #I'm so fucking stupid I thought the best score was 1 million not ten million :skull: I've been playing for 2 years 
        id = f"{randomchart}-{diff}-{goalscore}"
        self.id = id.split("-")
        return id
    
    def translate_id(self,ID):
        self.id = ID.split("-")

    def get_challenge(self):
        hold = self.id
        if hold[1] == '17':
            temp = getsongslist(17)
            answer = f"Get {hold[2]} or more on {temp[int(hold[0])]} {hold[1]}"
            return answer
        if hold[1] == '18':
            temp = getsongslist(18)
            answer = f"Get {hold[2]} or more on {temp[hold[0]]} {hold[1]}"
            return answer
        if hold[1] == '19':
            temp = getsongslist(19)
            answer = f"Get {hold[2]} or more on {temp[hold[0]]} {hold[1]}"
            return answer
        if hold[1] == '20':
            temp = getsongslist(20)
            answer = f"Get {hold[2]} or more on {temp[int(hold[0])]} {hold[1]}"
            return answer
        
    def checkdbforscore(self):
        conn = sqlite3.connect(r"D:\usc\maps.db")
        cursor = conn.cursor()
        sql = """SELECT score,chart_hash FROM Scores ORDER BY timestamp DESC LIMIT 5"""
        cursor.execute(sql)
        returned = list(cursor.fetchall())
        #print(returned)
        conn.close()
        hold = self.id
        temp = getsongslist(int(hold[1]))
        hold1 = hold[1]
        checkforme = songhash[hold1][temp[int(hold[0])]]
        #print(checkforme)
        #VOLPOINTS CALCULATION y=d^2*v/2

        for i in returned:
            if i[0] >= int(hold[2]):
                if i[1] == checkforme:
                    print ("congrats on the clear")
                    conn = sqlite3.connect("sdvxtools.db")
                    cursor = conn.cursor()
                    sql = f"SELECT * FROM User WHERE Name LIKE '{self.usr}'"
                    cursor.execute(sql)
                    returned = list(cursor.fetchall())
                    update1 = returned[0][1]+(int(hold[1]) ** 2 * (int(self.vf)/2))
                    update2 = returned[0][2]+1
                    sql = f"UPDATE User SET Volpoints={update1},Challenges_Completed={update2} WHERE Name='{self.usr}'"
                    cursor.execute(sql)
                    conn.commit()
                    conn.close()
                    return ["CLEAR",update1]
            return ":3"
                    
def MAKEuser(NAME,VF) -> None:
    conn = sqlite3.connect(r"sdvxtools.db") 
    cursor = conn.cursor()
    sql = f"INSERT INTO User(Name,Volpoints,Challenges_Completed,VF) Values(?,?,?,?)"
    commitinfo = (NAME,0,0,VF)
    cursor.execute(sql,commitinfo)
    conn.commit()
    conn.close()
                    
def GETallusers() -> list:
    conn = sqlite3.connect("sdvxtools.db")
    cursor = conn.cursor()
    sql = "SELECT Name FROM User"
    cursor.execute(sql)
    answer = list(cursor.fetchall())
    conn.close()
    return answer

def UPDATEuserinto(NAME,value) -> None:
    conn = sqlite3.connect("sdvxtools.db")
    cursor = conn.cursor()
    sql = f"UPDATE User SET VF='{value}' WHERE Name='{NAME}'"
    cursor.execute(sql)
    conn.commit()
    conn.close()

def GETuserVF(NAME) -> str:
    conn = sqlite3.connect("sdvxtools.db")
    cursor = conn.cursor()
    sql = f"SELECT VF FROM User WHERE Name='{NAME}'"
    cursor.execute(sql)
    answer = cursor.fetchone()
    conn.close()
    return answer



if __name__ == "__main__":
    #hold = os.listdir("C:\\Users\\diyaj\\Documents\\GitHub\\biggpiu.github.io\\sdvxtools\\picker\\charts\\20")
    #doingyourmom = []
    #for i in hold:
    #    i = i.replace(".jpg","")
    #    doingyourmom.append(i)
    #print (str(doingyourmom))
    hold = challenges(17,"GUEST")
    print(hold.make_id(17))
    print(hold.get_challenge())

    temp = hold.checkdbforscore()

    while temp != "CLEAR":
        temp = hold.checkdbforscore