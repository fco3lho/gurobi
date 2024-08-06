import gurobipy as gp
from gurobipy import GRB

def gurobi(n, m, b, w, p):
    # Criar o modelo
    model = gp.Model()
    model.setParam(GRB.Param.LogToConsole, 0)

    # Criação das variáveis de decisão
    x = model.addVars(n, m, vtype=GRB.BINARY, name="x")

    # Definição da função objetivo
    model.setObjective(gp.quicksum(p[i] * x[i, j] for i in range(n) for j in range(m)), GRB.MAXIMIZE)

    ##### Restrições

    # Cada item pode estar somente em uma mochila
    for i in range(n):
        expr = gp.LinExpr()
        for j in range(m):
            expr = expr + x[i, j]
        model.addConstr(expr <= 1, name=f"item_{i}")

    # Soma dos itens na mochila não pode exceder a capacidade da mochila
    for j in range(m):
        expr = gp.LinExpr()
        for i in range(n):
            expr = expr + w[i] * x[i, j]
        model.addConstr(expr <= b[j], name=f"mochila_{j}")

    ##### 

    # Otimizar o modelo
    model.optimize()

    # Verificar e exibir os resultados
    if model.status == GRB.OPTIMAL:
        print("\n---------------------------------------------------")
        print("Solução ótima")
        print("---------------------------------------------------")
        print(f"Valor da função objetivo: {model.objVal}\n")

        for j in range(m):
            items = []
            for i in range(n):
                if x[i, j].x == 1:
                    items.append(i+1)
            print(f"Mochila {j+1}: {items}")
    else:
        print("Não foi encontrada nenhuma solução ótima")