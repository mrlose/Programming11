list=["cat","duck","horse"]
print(list)
a=0
while a<1:
    animal=input("Type a animal, type -1 to quit")
    if animal in list:
        list.remove(animal)
        print(list)
    else:
        list.append(animal)
        print(list)
    if animal=="":
        list.remove(animal)
        list.pop(-1)
        print(list)
    if animal=="-1":
        print("Goodbye!")
        a+=1
    if list==[]:
        print("Goodbye!")
        a+=1
