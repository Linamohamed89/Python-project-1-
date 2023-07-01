'''
     -start: welcome message , games options
     -enter game number
     -option : option to exit
     -start play game
     -finish game : play again
     -yes : play again - no : exit 
'''


class Game:
    def __init__(self):
        while True:
            print('''welcome in our Game , Enter game number
            1:Fillter By Length
            2:Even odd range
            3:to Exit...''')
            user_choice=int(input('Enter Game number:'))
            if user_choice==3 :
                break

            elif user_choice==1:
                self:fillter_by_length()

            elif user_choice==2:
                self.even_odd_range()


            play_again=input('Press any key to play again,n to exit ')
            if play_again == 'n':
                break


    def fillter_by_length(self):
        names=input('Enter Names:')
        names_list=names.split(',')
        length=int(input('Enter Length:'))

        for n in  names_list:
            if len(n) >= length:
                print(n)


    def even_odd_range(self):
        start=int(input('Enter Start:'))
        end=int(input('Enter Start:'))
        even=[]
        odd=[]

        for x in range(start,end+1):
            if x%2==0:
                even.append(x)
            else:
                odd.append(x)
        print(even)
        print(odd)

g1=Game()

#game :names seperated , length ---> names < length

def fillter_by_length():
    names=input('Enter Names:')
    print(names)


fillter_by_length()


#########################

def fillter_by_length():
    names=input('Enter Names:')
    names_list=names.split(',')
    print(names_list)
    length=int(input('Enter Length:'))
   
fillter_by_length()
    


#########################

def fillter_by_length():
    names=input('Enter Names:')
    names_list=names.split(',')
    length=int(input('Enter Length:'))

    for n in  names_list:
        if len(n) >= length:
            print(n)
   
fillter_by_length()

    
##########################

def even_odd_range():
    start=int(input('Enter Start:'))
    end=int(input('Enter Start:'))
    even=[]
    odd=[]

    for x in range(start,end+1):
        if x%2==0:
            even.append(x)


        else:
            odd.append(x)
    print(even)
    print(odd)

'''
Enter Start:0
Enter Start:100
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
'''

even_odd_range()



    
