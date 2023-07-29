# Iris-Verisi-Tahmin-Uygulamas--
Bu proje, Python programlama dili ve Spyders IDE'si ile scikit-learn kütüphanesini kullanarak "Iris" veri setini yükleyerek, k-En Yakın Komşu (k-Nearest Neighbors - k-NN) algoritmasıyla iris çiçeklerinin sınıflandırılmasını gerçekleştiren bir makine öğrenimi uygulamasını içermektedir.

Veri Yüklemesi ve Hazırlığı:

- sklearn.datasets.load_iris() fonksiyonu kullanılarak Iris veri seti yüklenir.

- Veri seti, çiçeklerin özelliklerini (uzunluk ve genişlik gibi) ve hedef sınıf etiketlerini içeren bir yapıdadır.


Veri Seti Açıklaması:

- Iris veri seti, üç farklı iris çiçeği türüne (setosa, versicolor ve virginica) ait 150 örnek içermektedir.

- Her bir çiçek örneği için dört özellik (uzunluk ve genişlik) ölçümü bulunmaktadır: sepal length, sepal width, petal length ve petal width.

- Her bir çiçek türü, veri setinde eşit sayıda örnekle temsil edilir.

Veri Seti Bölme:

- train_test_split() fonksiyonu kullanılarak veri seti, öğrenme ve test veri kümelerine ayrılır.

-Öğrenme veri kümesi (X_ogren ve y_ogren), modelin eğitiminde kullanılırken, test veri kümesi (X_test ve y_test), modelin performansını değerlendirmek için kullanılır.

k-En Yakın Komşu (k-NN) Algoritması:

- KNeighborsClassifier sınıfı, k-NN algoritmasını uygulamak için kullanılır.

- n_neighbors = 1 parametresiyle, algoritmanın bir komşuyu temel alarak sınıflandırma yapacağı belirtilir.

- knn.fit(X_ogren, y_ogren) kod satırı, modelin eğitim verileri üzerinde eğitilmesini sağlar.

Tahmin ve Sonuçlar:

- Yeni bir çiçek örneği olan X_yeni verisi, eğitilen k-NN modeliyle sınıflandırılır ve tahmin edilen sınıf etiketi tahmin olarak elde edilir.

- Modelin performansı, test veri kümesi üzerinde tahmin yaparak dogruluk olarak hesaplanır.

- Son olarak, elde edilen doğruluk değeri yüzde cinsinden ifade edilerek ekrana yazdırılır.


Bu proje, temel makine öğrenimi kavramlarını anlamak, veri setlerinin yüklenmesi ve işlenmesi, k-NN algoritmasının kullanımı, model eğitimi ve performans değerlendirmesi gibi adımların pratiğini yapmak amacıyla hazırlanmıştır. Aynı zamanda, iris çiçeklerinin türlerinin özelliklere göre sınıflandırılması gibi gerçek dünya uygulamalarına giriş niteliği taşır.

Bu proje üzerinde yaptığınız çalışmaları paylaşarak, diğer geliştiricilerle işbirliği yapabilir ve deneyimlerinizi artırabilirsiniz. Aynı zamanda, projeyi farklı veri setleri veya farklı makine öğrenimi algoritmalarıyla genişleterek daha kapsamlı bir çalışma haline getirebilirsiniz.

Keyifli çalışmalar dilerim!
