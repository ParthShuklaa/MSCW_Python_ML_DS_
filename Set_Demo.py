MyMobiles = {"Nokia","Samsung","Apple","Oneplus"}

def display():
    for mobile in MyMobiles:
        print(mobile)
    print("------------------")

display()
MyMobiles.add("Mi")
display()

MyMobiles.remove("Nokia")
display()

print(MyMobiles.pop())
