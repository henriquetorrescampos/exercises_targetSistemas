"""
5) Escreva um programa que inverta os caracteres de um string.
IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
"""


def reverse_string(string):
    reverse_string = ""
    for letter in string:
        reverse_string = letter + reverse_string
    return print(f"String invertida é: {reverse_string}")


text = input("Digite uma string para ser invertida: ")

reverse_string(text)

