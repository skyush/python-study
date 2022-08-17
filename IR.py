
salary = float(input("Insira o seu salário: "))
annualSalary = salary * 12
quota = [1713.58, 4257.57, 7633.51, 10432.32]
base = [22847.76, 33919.8, 45012.6, 55976.16]
ir = 0
if (annualSalary <= base[0]):
    ir = 0

if ((annualSalary > base[0]) and (annualSalary <= base[1])):
    ir = quota[0]
    print("Voce está isento do Imposto de Renda")
elif ((annualSalary > base[1]) and (annualSalary <= base[2])):
    ir = quota[1]
    print("O valor devido a receita é de: " "%.2f" % ir)
elif ((annualSalary > base[2]) and (annualSalary <= base[3])):
    ir = quota[2]
    print("O valor devido a receita é de: " "%.2f" % ir)
elif (annualSalary > base[3]):
    ir = quota[3]
    print("O valor devido a receita é de: " "%.2f" % ir)