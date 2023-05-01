class Person:

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    
    # O próprio objeto agora pode ser chamado como um método/função
    def __call__(self, *args):
        self.interests = args
        return self

def main():
    jose = Person("Jose", 30)
    print(f"{jose.name}\n{jose.gender}")
    jose("Python", "AI", "Science")
    print(f"{jose.interests}")

if __name__ == "__main__":
    main()