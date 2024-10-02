#1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo
# valor sempre será a soma dos 2 valores anteriores
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
# escreva um programa na linguagem que desejar onde, 
# informado um número, ele calcule a sequência de Fibonacci e
# retorne uma mensagem avisando se o número informado pertence 
# ou não a sequência.

def fibonacci_until_max(max_value):
    seq = [0, 1]  # Começa a sequência com 0 e 1
    
    # Gera a sequência até que o último número seja maior ou igual ao max_value
    while seq[-1] < max_value:
        next_value = seq[-1] + seq[-2]  # Próximo valor é a soma dos dois últimos
        seq.append(next_value)
    
    return seq


n = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
fib_sequence = fibonacci_until_max(n)  # Gera a sequência de Fibonacci até n
print(f"Sequência de Fibonacci gerada: {fib_sequence}")  # Imprime a sequência

# Verifica se n pertence à sequência
if n in fib_sequence:
    print(f"{n} pertence à sequência de Fibonacci.")
else:
    print(f"{n} não pertence à sequência de Fibonacci.")


#2) Escreva um programa que verifique, em uma string,
# a existência da letra ‘a’, seja maiúscula ou minúscula,
# além de informar a quantidade de vezes em que ela ocorre.

def contar_letras_a(string):

    # Conta a ocorrência de letras 'a' e suas variantes
    contagem_minusculas = (string.count('a') + 
                            string.count('á') + 
                            string.count('à') + 
                            string.count('â') + 
                            string.count('ã'))
    
    # Conta a ocorrência de letras 'A' e suas variantes
    contagem_maiusculas = (string.count('A') + 
                           string.count('Á') + 
                           string.count('À') + 
                           string.count('Â') + 
                           string.count('Ã'))
    
    total = contagem_maiusculas + contagem_minusculas

    # Exibe os resultados
    print(f"A letra 'a' minúscula (incluindo acentuadas) aparece {contagem_minusculas} vez(es) na string.")
    print(f"A letra 'A' maiúscula (incluindo acentuadas) aparece {contagem_maiusculas} vez(es) na string.")
    print(f'No total ela aparece {total} vez(es)' )


entrada = input("Digite uma frase: ")
contar_letras_a(entrada)

#3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1;
# enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);
# Ao final do processamento, qual será o valor da variável SOMA?

def sum():
    indice = 12
    int(indice)
    soma = 0
    k = 1
    while k < indice:
        k = k + 1
        soma = soma + k
    print(soma)
sum()
