choice = input("choisis entre JavaScript, python, java : ")

def langage(choice):
    if choice == "JavaScript":
        return "tu es un développeur web"
    elif choice == "python":
        return "tu es un développeur IA"
    elif choice == "java":
        return "tu es un développeur logiciel"
    else:
        return "Choix invalide"

result = langage(choice)
print(result)
