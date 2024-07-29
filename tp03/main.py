import gurobipy as gp
from gurobipy import GRB

# p: Valor de benefício do item
# w: Peso do item
# b: Capacidade da mochila
# n: Número de itens
# m: Número de mochilas

def read_file():
  with open ('data.txt', 'r') as file:
    n, m = map(int, file.readline().strip().split())
    b = [None for i in range(m)]
    w = [None for i in range(n)]
    p = [None for i in range(n)]

    temp = file.readline().strip().split(' ')

    for i in range(m):
      b[i] = float(temp[i])

    for i in range(n):
      line = file.readline().split(' ')
      w[i] = float(line[0])
      p[i] = float(line[1])

  return n, m, b, w, p

def gurobi(n, m, b, w, p):
  model = gp.Model("mochila_multipla")

  # Criação das variáveis de decisão
  x = model.addVars(n, m, vtype=GRB.BINARY, name="x")

  # Definição da função objetivo
  model.setObjective(gp.quicksum(p[i] * x[i, j] for i in range(n) for j in range(m)), GRB.MAXIMIZE)

  ##### Retrições

  # Cada item pode estar somente em uma mochila
  for i in range(n):
    model.addConstr(gp.quicksum(x[i, j] for j in range(m)) <= 1)

  # Soma dos itens na mochila não pode exceder a capacidade da mochila
  for j in range(m):
    model.addConstr(gp.quicksum(w[i] * x[i, j] for i in range(n)) <= b[j])

  ##### 

  model.optimize()

  if model.status == GRB.OPTIMAL:
    print("Solução ótima encontrada:")
    for j in range(m):
        print(f"Mochila {j+1}:")
        for i in range(n):
            if x[i, j].x > 0.5:  # Se a variável binária é 1
                print(f" - Item {i+1} (Valor: {p[i]}, Peso: {w[i]})")
    print(f"Valor total: {model.objVal}")
  else:
      print("Não foi encontrada uma solução ótima.")

n, m, b, w, p = read_file()
gurobi(n, m, b, w, p)