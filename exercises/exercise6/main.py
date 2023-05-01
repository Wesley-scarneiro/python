from numberGenerator import NumberGenerator

def main() -> None:
    generator = NumberGenerator(100, 2)
    generator = NumberGenerator(100, 3)
    generator = NumberGenerator(100000, 5)

if __name__ == "__main__":
    main()

'''
Tests:
    File '1_100_2' created successfully
    File '2_100_2' created successfully
    File '3_100_2' created successfully
    File '1_100_3' created successfully
    File '2_100_3' created successfully
    File '3_100_3' created successfully
    File '1_100000_5' created successfully
    File '2_100000_5' created successfully
    File '3_100000_5' created successfully
'''