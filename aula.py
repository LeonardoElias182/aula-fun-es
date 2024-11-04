# def calcular_area (altura: float, largura: float):
#     area = altura * largura
#     return area

# area_1 = calcular_area (5, 10)
# print (area_1)



# def dividir (a: float, b: float):
#     divisao = a / b
#     return divisao

# a = 10
# b = 5
# divisao = dividir (a, b)
# print (divisao)



# def eh_positivo (numero: float):
#     ele_eh_positivo = None
#     if numero >= 0:
#        ele_eh_positivo = True
#     else: 
#         ele_eh_positivo = False
#     return ele_eh_positivo

# print (eh_positivo (2))

# def quadrado (numero: float):
#     numero_quadrado = numero * numero
#     return numero_quadrado
    
# numero_ao_quadrado = quadrado (7)
# print (numero_ao_quadrado)

# def string_vazia (texto: str):
#     texto_vazio = None
#     if texto == '':
#         texto_vazio = False
#     else:
#         texto_vazio = True
#     return texto_vazio

# text = input ('Digite aqui uma mensagem, ou não: ')

# print (string_vazia (text))    


# def celcius_para_fahrenheit (celcius: float):
#     temp_fahrenheit = (celcius *9/5) + 32
#     return temp_fahrenheit

# temperatura = celcius_para_fahrenheit (0)
# print (temperatura)


def tabuada (numero: int):
    for i in range (1, 11):
        multiplicacao = (f'{numero} x {i} = {numero*i}')
        exibir = print(multiplicacao)
    return exibir

   
resultado = tabuada (3)


        
      
    






