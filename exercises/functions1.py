def person(name, age=None, gender=None):
    if age and gender:
        print(f"Name: {name}")
        print(f"Age: {age}")
        print(f"Gender: {gender}")
    elif age:
        print(f"Name: {name}")
        print(f"Age: {age}")
    elif gender:
        print(f"Name: {name}")
        print(f"Gender: {gender}")
    else:
        print(f"Name: {name}")

person("Wesley")
person("Wesley", 27, "male")
person("Wesley", 27)
person("Wesley", gender="male")