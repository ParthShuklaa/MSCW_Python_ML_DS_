MyDreamCar = {"name":"Tesla",
              "Color":"Black",
              "Model":"Cyber Truck",
              "Engine Type" : "6 Cylinder Fully Automatic"
              }

def display ():
    for mycar  in MyDreamCar:
        print(mycar)

display()

print(MyDreamCar["Model"])
MyDreamCar["Model"] = "Roadster"
print("--------------------------")
print(MyDreamCar["Model"])


#Displaying values of Dictionary
for value in MyDreamCar:
    print(MyDreamCar[value])