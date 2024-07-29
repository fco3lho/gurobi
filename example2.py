import gurobipy as gp
from gurobipy import GRB


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

  # print(n)
  # print(m)
  # print(b)
  # print(w)
  # print(p)

  model = gp.Model()
  model.setParam(GRB.Param.LogToConsole, 0)

  x = [[model.addVar(lb=0, ub=1, vtype=GRB.BINARY) for i in range(n)]for j in range(m)]

  obj = gp.LinExpr()

  for i in range(m):
    for j in range(n):
      obj = obj + w[j] * x[i][j]

  model.setObjective(obj, sense=GRB.MAXIMIZE)

  expr = [gp.LinExpr() for i in range(m)]

  for i in range(m):
    for j in range(n):
      expr[i] = expr[i] + p[j] * x[i][j]

  for i in range(m):
    model.addConstr(expr[i] <= b[i])
  
  for i in range(m):
    for j in range(n):
      model.addConstr(x[i][j] <= 1)

  model.optimize()

  print(f'Objetivo: {round(model.objVal)}')

  for i in range(m):
    for j in range(n):
      print(f'x[{i+1}] = {round(x[i][j].X, 1)}')