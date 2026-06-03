import pandas as pd
import numpy as np

#df => DataFrame
df = pd.read_csv("alunos.csv")

#Mostrar o DataFrame
print(df)

#Media dos alunos
media = np.mean(df["Nota"])

print(f"A media dos alunos é de {round(media, 1)} valores")

#Maior nota entre os alunos
maior_nota = max(df["Nota"])

print(f"A maior nota entre os alunos é de {maior_nota} valores")

#Mostrar alunos que passaram
print(df[df["Nota"] >= 10])

#Passou de Modulo 
df["Passou Módulo"] = np.where(df["Nota"] >= 10, "Sim", "Não") #np.where(condição, valor se verdadeiro, valor se falso)

df.to_csv("alunos.csv", index=False) # index=False => para não mostrar o indice no ficheiro CSV
