# módulo estado_imc

def definir_estado_imc(imc):
    estado = ""

    if imc < 18.5:
        estado = "Abaixo do Peso"
    elif imc >= 18.5 and imc < 25:
        estado = "Peso normal!"
    elif imc >= 25 and imc < 30:
        estado = "Sobrepeso"
    elif imc >= 30 and imc < 35:
        estado = "Obesidae grau I"
    elif imc >= 35 and imc < 40:
        estado = "Obesidade grau II"
    else:
        estado = "Obesidade grau III"
    print(f"O IMC do paciente é: {imc: .1f} - {estado}")

def calcular_imc(peso, altura):
    imc = peso / altura ** 2
    definir_estado_imc(imc)



