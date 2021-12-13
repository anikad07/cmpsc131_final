fread = open("Booklist.txt", "r")
startNumber = 0
currentNumber = 0
restrict = True
booklist = []

s = fread.readline()
while s != "":
    s = s.rstrip("\n")
    a = s.split("#")
    s = fread.readline()
    if a[2] == "TRUE":
        restrict = True
    else:
        restrict = False

    startNumber = a[1]

    booklist.append([a[0], int(startNumber), int(startNumber), restrict])

fread.close()

readLibLogs = open("LibraryLog.txt", "r")

borrowArray = []

names = []

for trans in readLibLogs:
    goodVal = trans.rstrip("\n")
    goodVal = trans.split("#")
    #if borrow
    if goodVal[0] == 'B':
        print("b val found")
        # see if the person exists already, if not then make a new person array

        k = 0
        personExists = False
        indexOfName = -1
        while k < len(names) and personExists != True:
            if names[k][0] == str(goodVal[2]):
                personExists = True
                indexOfName = k
            k += 1

        indexOfBook = -1
        w = 0
        while w < len(booklist) and indexOfBook == -1:
            if booklist[w][0] == goodVal[3]:
                indexOfBook = w
            w += 1
        if personExists:
            names[indexOfName][1] += 1
        else:
            names.append([goodVal[2],1,0])
        booklist[indexOfBook][2] -= 1

        borrowArrayIndex = -1
        g = 0
        borrowedAlready = False
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

    #else if return
    elif goodVal[0] == 'R':

        dayReturned = goodVal[1][1]
        dayBorrowed = goodVal[0][1] - 1
        totalDays = dayBorrowed + dayReturned
        numberOfDaysLeft =

    #else if add book

    #else if pay fine

    elif goodVal[0] == 'P':
        pass

    #print(goodVal)


fread.close()
#print(LibLogs)
print(booklist)





#print("---------")
#print(booklist)

