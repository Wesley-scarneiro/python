###########################################
# Alterando o valor de uma variável global#
###########################################

constant = 3.1415
print(constant)

def change(variable, value):
    variable = value
    return variable

def main():
    # permite nova atribuição
    global constant
    constant = change(constant, 3.141592)
    print(constant)

if __name__ == "__main__":
    main()

'''
3.1415
3.141592
'''

############
# nonlocal #
############

def counter(value):
    def inner():
        nonlocal value
        value += 1
        return value
    return inner

counter10 = counter(0)
print(counter10())
print(counter10())
print(counter10())
print(counter10())

'''
3.1415
3.141592
1
2
3
4
'''