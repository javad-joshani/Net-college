dict = {}
while True:
    
    print("// c // for crate")
    print("// u // for update")
    print("// r // for remove")
    print("// q // for quite")
    print("// s // for show list")

    choise = input("Enter value:")
    if choise == "c":
        name = input("name:")
        famil = input("famil:")
        age = input("age:")

        person_id = len(dict)+1
    
        dict[person_id] ={ "name" : name,"famil" : famil,"age" : age }
        print(f"{name} {famil} is completed!!")
        print(dict)
        

    if choise == "r":
        person_id = int(input("chose id:"))
        del dict[person_id]
        print(f"{name} {famil} is removed!!!!")

    if choise == "u":
        person_id = int(input("choise index for update:"))
        name = input("name:")
        famil = input("famil:")
        age = input("age:")
        dict[person_id]={"name" : name,"famil" : famil,"age" : age}
        print("the preson is updated!!")

    if choise == "s":
        print(dict)

    if choise == "q":
        print("finish")
        break
             