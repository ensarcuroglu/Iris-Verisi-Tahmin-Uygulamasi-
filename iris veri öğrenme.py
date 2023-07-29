from sklearn.datasets import load_iris
iris_dataset = load_iris()
print(iris_dataset)

from sklearn.model_selection import train_test_split
X_ogren, X_test, y_ogren, y_test = train_test_split(iris_dataset['data'],iris_dataset['target'])
print(X_ogren.shape)
print(X_test.shape)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 1)
print(knn)

knn.fit(X_ogren, y_ogren)

X_yeni = [[3.5,2.1,3.4,1.2]]
tahmin = knn.predict(X_yeni)
print(tahmin)

dogruluk = knn.predict(X_test)
print(dogruluk)

import numpy as np
print(np.mean(dogruluk == y_test) * 100)




