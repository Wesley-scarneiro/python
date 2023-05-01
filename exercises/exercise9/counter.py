from collections import Counter

def main():
    
    numbers = [1,1,1,1,2,3,2,3,2,5,5,5,6,6,9,8,8,7,7,7,12,12,12,15,141,141,141]
    print("Numbers --> ", numbers)
    numbers_frequency = dict(Counter(numbers))
    print("Numbers frequency --> ", numbers_frequency)

if __name__ == "__main__":
    main()