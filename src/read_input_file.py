# p: Valor de benefício do item
# w: Peso do item
# b: Capacidade da mochila
# n: Número de itens
# m: Número de mochilas

def read_file(file):
    with open(file, 'r') as file:
        # Ler número de itens e mochilas
        n, m = map(int, file.readline().strip().split())
        
        # Inicializar listas para capacidades, pesos e valores
        b = [0.0] * m
        w = [0.0] * n
        p = [0.0] * n

        # Ler capacidades das mochilas
        temp = file.readline().strip().split()
        for i in range(m):
            b[i] = float(temp[i])

        # Ler pesos e valores dos itens
        for i in range(n):
            line = file.readline().strip().split()
            p[i] = float(line[0])
            w[i] = float(line[1])

    return n, m, b, w, p