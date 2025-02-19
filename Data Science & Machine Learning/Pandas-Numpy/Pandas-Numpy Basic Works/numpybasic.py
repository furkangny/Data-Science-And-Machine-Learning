# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpybasic as np

array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(array.shape) #arrayin matris boyutlarını değiştirdik

a = array.reshape(3,5)
print(a.shape)

array.ndim # tek boyutlu
a.ndim # 2 boyutlu (çünkü değiştirdik)

print(a.dtype.name) #array içindeki value'lerin türü
print(a.size) # size'ını verir
print(type(a)) #a'nın türünü verir -> array

array1 = np.array([[1,2,3,4], [5,6,7,8], [9,8,7,5]]) #array1.shape ile (3,4)'lük matris oluşumunu görebiliriz

zeros = np.zeros((3,4)) #(3,4)'lük içi sıfırlarla dolu bir matris oluşturur
""" array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])
"""
zeros[0,0] = 5 #(0,0)'ını 5 değeri ile günceller
print(zeros)
""" [[5. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]"""

ones = np.ones((3,4)) #zeros'un aynısı 0 yerine 1 yapar
blabla = np.empty((2,3)) #içi boş array oluşturur ama değerler yerine garbage değer atar ama aslında boştur

a = np.arange(10,50,5) # 10-50 arasını 5'er 5'er yazdırır 50'yi dahil etmez (10,15,20..45)

a = np.linspace(10,50,20) #


"""*********************************************************************************************"""

#basic operations

import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.sin(a)) # a arrayinin sinüsünü alır

a = np.array([[1,2,3], [4,5,6]])
b = np.array([[1,2,3], [4,5,6]])
print(a*b)

a = np.random.random((5,5)) # 5'e 5'lik 0-1 arası random array
a.sum() # içindeki değerleri toplar
a.max() # içindeki max değer min için a.min yap

print(a.sum(axis=0)) # a arrayinin sütunlarını toplar
print(a.sum(axis=1)) # a arrayinin satırlarını toplar

print(np.sqrt(a)) # a arrayinin kare kökü
print(np.sqare(a)) # a arrayinin karesi

"""*********************************************************************************************"""

#indexing and flexing

import numpy as np

array = np.array([1,2,3,4,5,6,7])

array[0:4] # 4. indexi dahil etmez
array[::-1] # arrayi ters çevirir

array1= np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(array1[1,1])
print(array1[:,1]) # satırların hepsini sütunların 1. indexini alır ---->ÇIKTI -> [2 7]
print(array1[1, 1:4]) # 1. satırın 1'den 4'e kadar olan değerlerini verir
print(array1[-1,:]) # son satırıın hepsini alır
print(array1[:,-1]) # son sütunun hepsini alır

"""*********************************************************************************************"""

#shape manuplated


import numpy as np

array = np.array([[1,2,3], [4,5,6], [7,8,9]])

a = array.ravel() # arrayi tek boyutlu yapar -> array([1, 2, 3, 4, 5, 6, 7, 8, 9])
b = a.reshape(3,3) # tekrar 3'e 3 yapar

arrayT = b.T # b arrayinin transpozunu alır

array3 = np.array([[1,2], [3,4], [5,6]])

array3.resize(2,3) #reshape ile aynı görevi görür resize diretk arrayi günceller reshape farklı bi değişkede tutulur

"""*********************************************************************************************"""

#stacking arrays

import numpy as np

array1 = np.array([[1,2], [4,5]])
array2 = np.array([[-1,-2], [-4,-5]])

arrayvertical = np.vstack((array1,array2)) # arrayleri dikey düzlemde birleştirir

"""array([[ 1,  2],
       [ 4,  5],
       [-1, -2],
       [-4, -5]])"""

arrayhor = np.hstack((array1,array2))  # arrayleri yatay düzlemde birleştirir

"""array([[ 1,  2, -1, -2],
       [ 4,  5, -4, -5]])"""

"""*********************************************************************************************"""

#array convert

import numpy as np

liste = [1,2,3,4]
array = np.array(liste)

liste2 = list(array) # arrayi listeye çevirir type ile bak

a = np.array([1,2,3])
b = a
c = a

"""a b c aynı alanda tutulduğu için eğer b'nin bi depeerini değişirsek diğerleri de değişir"""

#çözüm

d = np.array([1,2,3])
e = d.copy()
f = d.copy()

"""artık farklı bellek bölgelerinde tutulduğu için biri değişirse diğerleri etkilenmez"""
