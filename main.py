
# FUNÇÕES

# pega s:string, l:index inicio(0), r:index fim(len(s)-1), res-lista de permutações finais
def permute(s, l, r, res):
    # se início for igual ao fim - adiciona a permutação a lista
    if l == r:
        res.append(s)
    else:
        # loop para tree de permutações
        for i in range(l, r+1):
            # troca para subbranch
            s = swap(s, l, i)
            # recursão de branch, l+1 - caracter depois do fixado
            permute(s, l+1, r, res)
            # desfazer a troca para ir para outra branch
            s = swap(s, l, i)


# troca realizada na função permute
def swap(s, i, j):
    # transformar a string em lista
    s = list(s)
    # troca
    s[i], s[j] = s[j], s[i]
    # retorna uma nova string
    return ''.join(s)


# função contadora de inversões, sigma = permutação em string ex: '1234'
def inversion_number(sigma):
    # Caso base: a permutação é de tamanho 1, não há inversões.
    if len(sigma) == 1:
        return 0, sigma
    else:
        # Dividir a permutação em duas metades.
        mid = len(sigma) // 2
        left = sigma[:mid]
        right = sigma[mid:]
        # Chamar a função recursivamente para contar as inversões em cada metade.
        left_inv, left_sorted = inversion_number(left)
        right_inv, right_sorted = inversion_number(right)

        # Juntar as duas metades e contar as inversões entre elas.
        merged = []
        i = j = 0
        inversions = left_inv + right_inv
        while i < len(left_sorted) and j < len(right_sorted):
            if left_sorted[i] <= right_sorted[j]:
                merged.append(left_sorted[i])
                i += 1
            else:
                merged.append(right_sorted[j])
                j += 1
                inversions += len(left_sorted) - i
                
        # Adicionar quaisquer elementos restantes da metade esquerda ou direita.
        merged += left_sorted[i:]
        merged += right_sorted[j:]
        
        # Retornar o número total de inversões e a permutação ordenada. 
        # merged não será utilizado no restante do código (poderia excluir, mas não vou)
        return inversions, merged

def get_matrix(n):
    matrix = []
    for k in range(1,n+1):
        col = []
        for i in range (1, n+1):
            v = int(input(f"Digite o valor do elemento a({k},{i}) da matriz: "))
            col.append(v)
        matrix.append(col)
    return matrix

def print_matrix(matrix):
    print("\n=== Matriz digitada ===")
    for k in matrix:
        line = "[ "
        for i in k:
            line += f"{i}, "
        line = line[:-2] + " ]\n"
        print(line)



# CÓDIGO MAIN
# if __name__ == '__main__':

n = int(input("Digite a dimensão da matriz: "))
matrix = get_matrix(n)
print_matrix(matrix)

# string '1234'
n_string = ''.join([str(i) for i in range(1, n+1)])

# permutações
s_n = []
permute(n_string, 0, len(n_string)-1, s_n)

# print(s_n)

# loop - permutação -> (permutação, inversão)
perm_inv = [(p, inversion_number(p)[0]) for p in s_n]

#print(perm_inv)

# Permutação e sinais
signals = []

for k in perm_inv:
    # se o número de inversões for par sinal +1, se impar sinal -1
    signal = (-1) ** k[1]
    signals.append((k[0], signal))

#print(signals)

# valor da determinante
soma_final = 0
for k in signals:
    produto = 1
    for e in range(0, n):
        chars = list(k[0])
        produto *= matrix[e][int(chars[e])-1]
    if k[1] < 0:
        soma_final += (produto * -1)
    else:
        soma_final += (produto * +1)
print("O valor da determinante dessa matriz é:", soma_final)