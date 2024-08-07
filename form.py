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

# ---------------------------------- NEXT -----------------------------------------

    from tkinter import messagebox
dict = {}
def crate(people):
    name = input("name:")
    famil = input("famil:")
    age = input("age:")

    person_id = len(people) + 1
    people[person_id] ={
        "name" : name,
        "famil" : famil,
        "age" : age
    }
    messagebox.showinfo("see mee",f"{name} {famil} age: {age} crated.")
    

def remove(people):
    person_id = int(input("remove id :"))
    if person_id in people:
        del people[person_id]
        print("removed !!!")
    else:
        print("not founded person")

def update(people):
    person_id = int(input("update id :"))

    if person_id in people:
        name = input("name:")
        famil = input("famil:")
        age = input("age:")

        people[person_id] = {
            "name" : name,
            "famil" : famil,
            "age" : age
        }
        print("person updated !!!")
    else:
        print("person not fonded !!!")

while True:
    print("// c // for crate")
    print("// u // for update")
    print("// r // for remove")
    print("// q // for quite")

    choise = input("what do you want??")
    if choise == "c":
        crate(dict)
    elif choise == "u":
        update(dict)
    elif choise == "r":
        remove(dict)
    elif choise == "q":
        print("out")
        break

    if choise == "q":
        print("finish")
        break
             
