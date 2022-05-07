print('Nos conte um pouco sobre você?')
nome = input('Qual seu nome completo? ')
apelido = input ('Como você gostaria de ser chamado? ')
idade = input('Quantos anos você tem? ')
endereco = input('Onde você mora? ')
print('Vamos agora ao que interessa? ')
peso = input('Qual seu peso? ')
altura = input('Qual sua altura?')
expectativa = input('Quantos Kg quer perder? ')

ficha = {
    "nome": nome,
    "apelido": apelido,
    "idade": idade,
    "endereco": endereco,
    "peso": peso,
    "altura": altura,
    "expectativa": expectativa
}
print(ficha)

