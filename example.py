import gurobipy as gp
from gurobipy import GRB

# Cria modelo
model = gp.Model()

# Desativa exibição do log
model.setParam(GRB.Param.LogToConsole, 0)

# Cria as variáveis
x1 = model.addVar(lb=0, ub=GRB.INFINITY, vtype=GRB.CONTINUOUS)
x2 = model.addVar(lb=0, ub=GRB.INFINITY, vtype=GRB.CONTINUOUS)
x3 = model.addVar(lb=0, ub=GRB.INFINITY, vtype=GRB.CONTINUOUS)

# Define a função objetivo
model.setObjective(2*x1 + 5*x2 + x3, sense=GRB.MAXIMIZE)

# Define as restrições
model.addConstr(x1 + x2 <= 6)
model.addConstr(x2 - x3 >= 4)
model.addConstr(4*x1 + 2*x2 + x3 <= 15)

# Resolve o problema
model.optimize()

print(f'Valor da função objetivo: {model.objVal}')
print(f'Valor das variáveis: x1={x1.X}, x2={x2.X} x3={x3.X}')