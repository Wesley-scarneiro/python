while True:
    salary = float(input("Inform the salary: "))
    tax = input("Informe the tax: ")

    if tax == "":
        tax = 27.0
    else:
        tax = float(tax)

    salaryLiquid = salary - (salary * (tax/100))
    print("\tSalary liquid = R$ {}\n\tTax = {}%".format(salaryLiquid, tax))
    end = input("Exit(yes/no)? ")
    if end == "yes":
        break

print("end")