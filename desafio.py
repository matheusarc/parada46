#desafio utilizando um metodo de lista append (adicionar algo a lista)
funcionarios = ['Ronaldo', 'Roberta', 'Carla', 'Moura']

funcionarios.append('Cristiano')
print(funcionarios)


#fazendo um desafio com função
def n_par():
    n = int(input("Digite seu número: "))
    if n%2 == 0:
        print(f"O número {n} é par!")
    elif n%2 == 1:
        print(f"O número {n} é ímpar!")

n_par()