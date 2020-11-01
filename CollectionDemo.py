#WAP to implement Collection

BookList = ["Wings of Fire","The monk who sold his Ferari","Hamlet"]

print(BookList)
def Display():
    for book in BookList:
        print(book)


#Displaying elements of list
for book in BookList:
    print(book)

#Adding more books
BookList.append("You can Win")
BookList.append("White Tiger")


print("---------------before poping Book---------------")
Display()
#implemeting PoP
print(BookList.pop())
print("---------------After poping Book---------------")

Display()


print("Enter 10 books you want in your list")
for i in range(10):
    name = input("Enter Book name")
    BookList.append(name)

Display()









for book in BookList:
    print(book)

#delete a book
BookList.remove("Hamlet")
print("-----------------------------------------")
for book in BookList:
    print(book)
print("Book at first location")
print(BookList[0])

print("Counting Elements of List ")
print(BookList.count("White Tiger"))
Display()
