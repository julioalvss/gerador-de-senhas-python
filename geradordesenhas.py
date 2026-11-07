import random
import string

print("-=-"*20)
print("Bem-vindo ao Gerador de Senhas!")
print("-=-"*20)
tamanho = int(input("Digite o tamanho desejado para a senha: "))
print("-=-"*20)

minusculas = string.ascii_lowercase
maiusculas = string.ascii_uppercase
numeros = string.digits
simbolos = string.punctuation

qtd_minusculas = int(tamanho * 0.50)
qtd_maiusculas = int(tamanho * 0.15)
qtd_numeros = int(tamanho * 0.25)
qtd_simbolos = tamanho - qtd_minusculas - qtd_maiusculas - qtd_numeros

senha = (
    random.choices(minusculas, k=qtd_minusculas) +
    random.choices(maiusculas, k=qtd_maiusculas) +
    random.choices(numeros, k=qtd_numeros) +
    random.choices(simbolos, k=qtd_simbolos)
)
senha = ''.join(senha)
print("Sua senha é: \n{}".format(senha))
print("-=-"*20)