import random
from songs import *
import os

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

    def __init__ (self,vf) -> None:
        self.vf = vf

    def get_id(self,diff) -> str:
        
        randomchart = random.randint(0,len(getsongslist(19)))
        # I think I want it formatted like this: RANDOMCHART-DIFF-GOALSCORE
        goalscore = equation(diff,self.vf)
        goalscore += random.randint(-10000,10000) #gotta add a bit of randomness :3

        id = f"{randomchart}-{diff}-{goalscore}"
        self.id = id.split("-")
        return id
    
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


def checkdbforscore():
    pass

if __name__ == "__main__":
    #hold = os.listdir("C:\\Users\\diyaj\\Documents\\GitHub\\biggpiu.github.io\\sdvxtools\\picker\\charts\\20")
    #doingyourmom = []
    #for i in hold:
    #    i = i.replace(".jpg","")
    #    doingyourmom.append(i)
    #print (str(doingyourmom))
    hold = challenges(17)
    print(hold.get_id(17))
    print(hold.get_challenge())