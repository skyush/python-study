
salary = float(input("Insira o seu salário: "))
annualSalary = salary * 12
base = [22847.76, 33919.80, 45012.60, 55976.16 ]
aliquot = [0.075,0.15,0.225,0.275]
ir = 0
if annualSalary <= base[0]:
    ir = 0
    print("Voce está isento do Imposto de Renda")
elif ((annualSalary >base[0]) and (annualSalary <=base[1])):

    ir = (annualSalary - base[0]) * aliquot[0]
    print("O valor devido ao Fisco é de R$", "%.2f" % ir)

elif ((annualSalary >base[1]) and (annualSalary <=base[2])):

    ir = (annualSalary - base[0]) * aliquot[0]
    print("O valor devido ao Fisco é de R$", "%.2f" % ir)

elif ((annualSalary >base[2]) and (annualSalary <=base[3])):

    ir = (annualSalary - base[0]) * aliquot[0]
    print("O valor devido ao Fisco é de R$", "%.2f" % ir)
    
elif ((annualSalary >base[3])):

    ir = (annualSalary - base[0]) * aliquot[0]
    print("O valor devido ao Fisco é de R$", "%.2f" % ir)
