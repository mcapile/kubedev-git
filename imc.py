import os
print("kubedev GIT")
altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em Kg: "))

imc = peso / altura**2

print("Seu IMC: %.4f" % imc)

if imc < 16:
        print("Magreza grave")
elif imc < 17:
        print("Magreza moderada")
elif imc < 18.5:
        print("Magreza leve")
elif imc < 25:
        print("Saudavel")
elif imc < 30:
        print("Sobrepeso")
elif imc < 35:
        print("Obesidade Grau I")
elif imc < 40:
        print("Obesidade Grau II (severa)")
else:
        print("Obesidade Grau III (morbida)")

os.system("pause")

