import pandas as pd
import numpy as np

df = pd.read_csv("gestão_funcionarios.csv")

#Mostrar o DataFrame antes das alterações
print(df)

#Aumento de 10% do Salario
df["Salario"] = round((df["Salario"] * 1.1), 2)

#Calcular Salario Anual
df["Salario Anual"] = df["Salario"] * 12

#Guardar Alterações no ficheiro CSV
df.to_csv("gestão_funcionarios.csv", index=False)

#Mostrar Maior Salário
maior_salario = df.loc[df["Salario"].idxmax()] # => Serve para dizer o indice do Salario mais alto ou valor mais alto
print(f"O funcionário com o maior salário é {maior_salario["Nome"]} com {maior_salario["Salario"]}€, e Salário Anual de {maior_salario["Salario Anual"]}€")

#Depois das alterações 
print(df)