from person_teacher import Person, Teacher

def main():
    p1 = Person("Wesley", 27, "male", "122354658")
    p1.add_interests("Python", "AI", "Software Engenieering", "Philosofy")
    p1.greeting()

    p2 = Person("Maria", 23, "female", "155666958")
    p2.greeting()

    f1 = Teacher("Filomena Augusta", 42, "female", 12548756522, "University of São Paulo", 12)
    f1.greeting()
    f1.professional_greeting()
    f1.add_disciplines("Database", "Computer Organization and Architecture")
    f1.professional_greeting()

    Person.getTotalPeople1()
    Person.getTotalPeople2()


if __name__ == "__main__":
    main()