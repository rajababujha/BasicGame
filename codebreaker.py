import random
chance = 0
d = [random.randint(0,9),random.randint(0,9),random.randint(0,9)]
print(d)
            
z =14

def guessing(g,c):
    count1 = 0
    count2 = 0
    count3 = 0
    for ele in g:
        
        i = int(ele)
        if i in c :
            if g.index(ele) == c.index(i):
                count1 += 1
            
            elif g.index(ele) != c.index(i):
                count2 += 1
            
        if i not in c:
            count3 += 1
            
    checking(count1,count2,count3)



def checking(c1,c2,c3):
    if c1 == 3:
        chance = 14
        print("\rCode Breaked")
        print('\rCode was ',d)
        print("\r<<===============Game Over====================>>")
        print("\rTHanKS!")
        print("\r*"*30)
        print("\n")
        
        
        
    if c1 == 2:
        print("\rTwo digits are matched and indexed correctly.\r")
    if c1 == 1:
        print("\rOne digit is matched and indexed correctly.\r ")
    if c2 == 3:
        print("\rThree digits are matched but wrong indexed. \r")
    if c2 == 2:
        print("\rTwo digits are matched but wrong indexed. \r")
    if c2 == 1:
        print("\rOne digit is matched but wrong indexed. \r")
    if c3 == 1:
        print("\rOne digit is wrong.\r")
    if c3 == 2:
        print("\rTwo digits are wrong.\r")
    if c3 == 3:
        print("\rThree digits are wrong.\r")
    

while True:
    if chance == 14:
        print('The code was {}',format(d))
        print("*****************YOU LOST!****************\n")
        break
    
    if chance < 14:
        
        g =input("\rEnter your guess ? ")
        g = list(g)
        if len(g) == 3:
            guessing(g,d)
        elif len(g) > 3:
            print("\rYour Code is Longer than 3 Digits. \r")
        else:
            print("Your Code is Shorter than 3 Digits. \r")
    
        
        chance += 1
        print("\nRemaining chance is {}".format(z-chance))
        
    
    
