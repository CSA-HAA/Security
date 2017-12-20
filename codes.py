#Hamzah Ahmed
#v1.0
#Research in IT

import random

count = 100

#Generates 100 codes
#Run only when wanting to replace all existing codes

with open("availablecodes.txt","w") as file:
    while count!=0:
        count-=1
        securitycode=random.randrange(1111,9998)
        file.write(str(securitycode)+'\n')