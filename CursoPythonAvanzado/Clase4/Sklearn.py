#-*-coding:utf-8-*-
########
#Ej sklearn


from sklearn import tree
#Frutas
#Peso   Textura Nombre
# 150	Rugosa	Naranja
# 170	Rugosa	Naranja
# 140	Lisa	Manzana
# 130	Lisa	Manzana

#0  -> Rugosa
#1	-> Lisa

caracteristicas=[[150,0],[170,0],[140,1],[130,1]]
nombres=['Naranja','Naranja','Manzana','Manzana']

#Crear un árbol de decisión

clasificador=tree.DecisionTreeClassifier()

#Entrenar al clasificador, encontrar patrones en los datos

clasificador=clasificador.fit(caracteristicas,nombres)

#Predecir un comportamiento

print(clasificador.predict([120,0]))



















