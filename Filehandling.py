def Read():
    myFile = open("MyDetails.txt",'r')
    print(myFile.readline())
    print(myFile.readlines())
    myFile.close()

Read()

myFile = open("MyDetails.txt",'a')
details = input("Enter More details about you....\n")
myFile.writelines("\n"+details+"\n" )
myFile.write("\n")

myFile.close()

Read()