try:    
    with open('frutas', 'r') as file:
        print(file.read(6))
        print(file.read(6))
        print(file.seek(0))
        print(file.read(12))
        
        
except FileNotFoundError as e:
    print(e)