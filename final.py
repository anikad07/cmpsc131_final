fread = open("Booklist.txt", "r") #opens the book
startNumber = 0 #initilizes how many books they started with
currentNumber = 0 #initilizes how many books the library currently has
restrict = False #sets the default option of being restricted as false
booklist = [] #initializes the booklist array


#the function below reads each line and adds the data into the array
s = fread.readline()
while s != "":
    s = s.rstrip("\n")
    a = s.split("#")
    s = fread.readline()
    if a[2] == "TRUE":
        restrict = True

    startNumber = a[1]

    booklist.append([a[0], int(startNumber), int(startNumber), restrict])
    #the array looks like ["book name", start_number_of_books, current_number_of_books, restricted_or_not]

fread.close()

#function that reads the library logs
readLibLogs = open("LibraryLog.txt", "r")

borrowArray = []

names = []

for trans in readLibLogs:
    goodVal = trans.rstrip("\n")
    goodVal = trans.split("#")
    #if borrow
    if goodVal[0] == 'B':

        # see if the person exists already, if not then make a new person array
        k = 0
        personExists = False
        indexOfName = -1
        while k < len(names) and personExists != True:
            if names[k][0] == str(goodVal[2]):
                personExists = True #if found it sets the condition to true
                indexOfName = k
            k += 1

        #looks for the book in booklist
        indexOfBook = -1
        w = 0
        while w < len(booklist) and indexOfBook == -1:
            if booklist[w][0] == goodVal[3]:
                indexOfBook = w
            w += 1

        dayBorrow = goodVal[2]
        #if the person has already borrowed a book then it adds that they have borrowed one more book
        if personExists:
            names[indexOfName][1] += 1
            names[indexOfName][3].append( [goodVal[3] , dayBorrow] ) #adds the book onto the list of books checked out

        #if they have not borrowed a book yet then it adds them to the name array
        else:
            names.append([goodVal[2],1,0,[[goodVal[3],dayBorrow]]])
        booklist[indexOfBook][2] -= 1 #updates booklist to show that a book has been checked out

        borrowArrayIndex = -1
        g = 0
        borrowedAlready = False
        #this sees if the book has already been checked out
        '''
        while g < len(borrowArray) and borrowedAlready != True:
            if borrowArray[g][0] == str(goodVal[3]):
                borrowedAlready = True
                borrowArrayIndex = g
            g += 1
        
        if borrowedAlready:
            borrowArray[borrowArrayIndex][1] += 1
        else:
            borrowArray.append([booklist[indexOfBook][0],1])

        # if they exist then add a book to their total
        # add book to checked out array and remove from booklist
        '''
    #else if return
    elif goodVal[0] == 'R':

        #find the book in book list and add it back

        #gets the person
        indexOfName = -1
        k = 0
        while k < len(names):
            if names[k][0] == str(goodVal[2]):
                indexOfName = k
            k += 1

        #get index of book checked out in names array

        #



        if booklist[4]: #if its restricted it gets a 7 day borrow
            borrowmax = 7
        else:
            borrowmax = 28 #else its just the regular

        dayreturned = goodVal[1] #gets the day returned
        dayborrowed = goodVal[1] # gets the day borrowed
        totaldays = dayborrowed + dayreturned
        numberofdaysleft = int(borrowmax) - int(totaldays)

        fines = 0
        if numberofdaysleft < 0:
            fineddays = numberofdaysleft * -1
            if borrowmax == 7:
                fines = fineddays * 5
            else:
                fines = fineddays * 1
        names[2] = fines




    #else if add book

    #else if pay fine

    elif goodVal[0] == 'P':
        pass

    #print(goodVal)


fread.close()
#print(LibLogs)
print(booklist)

print("option one: can a student borrow a book")
print("option two: what are the most popular books in the library, how many days were they borrowed")
option= int(input("Please enter an option"))
if option==1:
    if names[2]>0:
        print("no, the student cannot borrow a book")
    else: print("yes the student can borrow a book")
if option==2: 



#print("---------")
#print(booklist)

