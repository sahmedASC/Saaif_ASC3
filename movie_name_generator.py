from random import randrange
#CREATE MOVIE NAMES

#The Names
first = ["The","Best","Great","Those","Amazing","Fame","Danger","Return","Rise","Death"]
second = ["Jurassic","Trials","From","Scott","Banana","Monkey","Crazy","of","the","Dead"]
last = ["Come","Park","Maze","Man","Satan","The Abyss","Cyclops","Bad Places","Face","Destruction"]

#Generator

def main():
    i=0
    while i<10:   
        random_index = randrange(0,len(first))
        random = randrange(0,len(second))
        third = randrange(0,len(last))
        print(first[random_index],second[random],last[third])
        i=i+1
main()