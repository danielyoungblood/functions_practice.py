def hello():
    print ("nothing")
    return

def pack(apple, orange, pear):
    return [apple, orange, pear]

def eat_lunch(list):
    if len(list) == 0:
        print ("My lunchbox is empty!")
    else: 
        for i in list:
           if list.index(i)==0:
                print('First i eat ' + str(i))
           else:
                print('Next i eat ' + str(i))
    print(' ')
    return 

hello()
print(pack(1,2,3))

#calling a function name eat_lunch with a value of a empty list
#the value between the open and closed paren() is called parameter
#[] open closed bracket means empty list
eat_lunch([]) 

eat_lunch([1])

eat_lunch([1,2]) 