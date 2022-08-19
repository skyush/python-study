salary = [1500, 2800, 3600, 5500, 8000, 10000, 15300]
salaryList =[]
aliquot = [0.075, 0.15, 0.225, 0.275]
deduction = [1713.58, 4257.57, 7633.51, 10432.32]
base = [22847.76, 33919.8, 45012.6, 55976.16]
ir = 0
for x in salary:
    salaryList.append(float(x))
annualSalary = 12 * salaryList[0]

print(annualSalary)
for x in salaryList:
    if (annualSalary <= base[0]):
        ir = 0
        print("Voce está isento do Imposto de Renda")

    if ((annualSalary > base[0]) and (annualSalary <= base[1])):
        ir = annualSalary * aliquot[0] - deduction[0]
        print("O valor devido a receita é de: " "%.2f" % ir)

    elif ((annualSalary > base[1]) and (annualSalary <= base[2])):
        ir = annualSalary * aliquot[1] - deduction[1]
        print("O valor devido a receita é de: " "%.2f" % ir)

        ir = annualSalary * aliquot[2] -deduction[2]
        print("O valor devido a receita é de: " "%.2f" % ir)
        
    elif (annualSalary > base[3]):
        ir = annualSalary * aliquot[3] - deduction[3]
        print("O valor devido a receita é de: " "%.2f" % ir)