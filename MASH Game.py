from random import*
from random import randrange
import re
import sys
import time
place = ["Mansion", "Apartment", "Shack", "House"]
money = [10,101,0,210,20,3040,5,5,436,25,723,146,7,46,45,713,73,157,24,57,35,5856736257,34646871,9,01,1346135]
marry = ["Bob","Bobert","John","Oscar","Ashim","Ashim's Girl", "John's Girl","Oscar's Apparently Indian Girl"]
residence = ["California","The Abyss","NY","NJ","Weeb City","Abreuboom's House", "GitHub repository","infinite loop","syntax error","index.html file","a program with an error you can never solve"]

i=0
while i<2:
    user0 = input("What color are your blue jeans?")
    if user0 == "blue":
        i=i+2
    elif user0 == "Blue":
        i=i+2
    else:
        i=i+0
    user1 = input("Where do you see yourself in one second?")
    user2 = input("How does one dab?")
    user3 = input("Where is the place you want to live in?")
    user4 = input("What are the chances of you getting a girlfriend within 24 hours?")
    user5 = input("Money is cool?")
    if user5 == "Yes":
        print("Man aren't you greedy.")
        time.sleep(6)
        sys.exit()
    user6 = input("How much money per year?")
    user7 = input("What do you want to live in")


random_index = randrange(0,len(place))
random = randrange(0,len(money))
third = randrange(0,len(marry))
new = randrange(0,len(residence))
    
print ("You will have a(n)",place[random_index], "in",residence[new],".")
print ("You will marry", marry[third], "and make this much per year:", money[random])



