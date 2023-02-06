# Solução

import pandas as pd

df = pd.read_csv(r'C:\Users\joaov\Downloads\alunos3.csv', sep = ';', decimal = ',', usecols= [0,3,4,5,6])

df['Media'] = df.apply(lambda row:
    row[1:5].mean(),
    axis = 1
)


# Solução alternativa

# df['Media'] = df.iloc[:,[1, 2, 3, 4]].mean(axis = 1)


# Solução alternativa

# df['Media'] = df[['Prova_1', 'Prova_2', 'Prova_3', 'Prova_4']].mean(axis = 1)


# continuação do ecercício

print(df)

# df[["RA","Media"]].to_excel(r'C:\Users\joaov\Downloads\medias.xlsx', sheet_name= 'Medias')

df[["RA","Media"]].to_excel(r'C:\Users\joaov\Downloads\medias_2.xlsx', index = False)