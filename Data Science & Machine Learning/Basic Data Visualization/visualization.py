import pandas as pd

df = pd.read_csv("iris.csv")

print(df.Species.unique()) #species feature'undan kaç çeşit çiçek olduğunu bulduk

print(df.info()) #df ile ilgili bilgileri getirir

print(df.describe()) #string olmayan numeric bilgileri getirir(ortalama, min, ma vs)

setosa = df[df.Species == "Iris-setosa"] #sadece setosaların olduğu df
versicolor = df[df.Species == "Iris-versicolor"] #sadece versicolor'un olduğu df

print(setosa.describe())
print(versicolor.describe())

# %%

import matplotlib.pyplot as plt

df1 = df.drop(["Id"], axis = 1)

df1.plot()
plt.show() #df'deki verileri görselleştirdik

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.plot(setosa.Id ,setosa.PetalLengthCm, color = "red", label = "setosa ")
plt.plot(versicolor.Id ,versicolor.PetalLengthCm, color = "green", label = "setosa ")
plt.plot(virginica.Id ,virginica.PetalLengthCm, color = "blue", label = "setosa ")

plt.xlabel("ıd") # x eksenine "ıd" metnini etiket olarak ekler
plt.ylabel("PetalLengthCm") # y eksenine "PetalLengthCm" metnini etiket olarak ekler
plt.legend() # grafiğe daha önce plt.plot() fonksiyonu ile eklenen etiketin görünmesini sağlar
plt.show() #oluşturulan tüm grafik öğelerini (çizgi grafiği, eksen etiketleri, legend vb.) bir grafik penceresinde gösterir

df1.plot(grid = True) # grafiği ızgara biçiminde böler
plt.show()

#%% scatter plot

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.scatter(setosa.PetalLengthCm, setosa.PetalWidthCm, color = "red", label = "setosa")
plt.scatter(versicolor.PetalLengthCm, versicolor.PetalWidthCm, color = "green", label = "versicolor")
plt.scatter(virginica.PetalLengthCm, virginica.PetalWidthCm, color = "blue", label = "virginica")

plt.legend()
plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")
plt.title("scatter plot")
plt.show()

# %% histogram

plt.hist(setosa.SepalLengthCm, bins = 30) #bins bar sayısıdır
plt.xlabel("SepalLengthCm values")
plt.ylabel("frekans")
plt.title("histogram")
plt.show()

# %% bar plot

import numpy as np

x = np.array([1,2,3,4,5,6,7])
y = x*2+5

plt.bar(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("bar plot")
plt.show()

# %% subplots

df1.plot(grid = True, alpha = 0.9, subplots = True)
plt.show()

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.subplot(2,1,1)
plt.plot(setosa.Id ,setosa.PetalLengthCm, color = "red", label = "setosa ")
plt.ylabel("setosa - PetalLengthCm")

plt.subplot(2,1,2)
plt.plot(versicolor.Id ,versicolor.PetalLengthCm, color = "green", label = "setosa ")
plt.ylabel("versicolor - PetalLengthCm")
plt.show()















