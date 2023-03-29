
"""
Egzersiz: (Konu: Algoritmalar, Veri Yapıları)
"""

"""
Soru 1 (25 Puan)
Bu soruda merge adında bir fonksiyon yazmanız beklenmektedir. 
Bu fonksiyon parametre olarak içinde küçükten büyüğe sıralanlanmış 2 liste alacaktır. 
Yazdığınız fonksiyon bu iki listeyi tek bir liste haline getirmeli, ama oluşan liste yine
küçükten büyüğe sıralı olmalıdır. 
örnek:
merge([1,3,5,19], [2, 6, 20])
üstteki fonksiyon [1, 2, 3, 5, 6, 19, 20] listesi return etmelidir.
"""


"""
Soru 2: (10 Puan)
    Bir string'i [::-1] ya da reverse metodlarını KULLANMADAN ters çeviren bir fonksiyon yazınız.
Eğer Python'da var olan metodlardan birini kullanırsanız çözümünüz kabul edilmeyecektir. 
reverse("Armut") -> "tumrA" return etmelidir. 
"""


"""
Soru 3: (20 Puan)
    a) bubbleSort adında bir fonksiyon yazın. Bu fonksiyon listenizi bubble sort algoritması ile
sıralamalıdır. (fonksiyon bir şey return etmeyecek, listeyi in-place sıralayacak.) Sıraladıktan sonra
Fonskiyon sıralanmış listeyi ve toplam kaç yer değiştirme yapıldığını yazdırmalıdır.

    b) a şıkkının aynısını bu sefer selection sort algoritması için yapın.
"""


"""
Soru 4: (45 Puan)
Ön bilgi: Stack veri yapısı
    Türkçede 'Yığın' olarak geçer. Pek çok algoritma ya da temel bilgisayar yazılımları stack
yapısını sıklıkla kullanır, oldukça önemli bir veri yapısıdır. Kısaca Stack, ekleme ve çıkarma işlemlerinin
sadece listenin sonundan yapıldığı bir veri yapısıdır. ekleme ve çıkarmak için genelde push(x) ve pop() terimleri
kullanılır. 

Temel olarak bir stack'te 4 adet operasyon yapılır. Bunların adları ve işlevleri şöyledir.

1:  push(x): x elemanını stack'in sonuna ekler. Örnek
stack = []
stack.push(1) -> [1]
stack.push(4) -> [1, 4]
stack.push(7) -> [1, 4, 7]

2:  pop(): stack'in son elemanını kaldırır ve patlattığı elemanı return eder. 
Eğer stack boş ile ve patlatılabilecek data fazla eleman yoksa -1 return eder.
Örnek:

İlk durum: stack = [3, 4, 6, 9, 11]
stack.pop() -> [3, 4, 6, 9] #returns 11
stack.pop() -> [3, 4, 6] #returns 9
stack.pop() -> [3, 4] #returns 6
stack.pop() -> [3]  #returns 4
stack.pop() -> [] #returns 3
stack.pop() -> [] #returns -1, no element to pop

3: top(): Bu fonksiyon stack'in son elemanını KALDIRMADAN sadece return eder. 
İlk durum:  stack = [1, 2, 7, 11]
stack.top() #returns 11, do not change any element in the stack.

4: clear(): stack'in içindeki bütün elemanları siler. 
İlk durum: stack = [9, 6, 2, 7]
stack.clear()
print(stack) -> prints []

Bu soruda sizden istenen kendi veri yapınızı tasarlamanızdır. 
Stack class'ını ve basedilen 4 metodu tanımlayın. 
Stack class'ından oluşturulan bir obje print edildiğinde aşadığıdaki şekilde print edilsin:
Stack:[5,6,7]

İpucu: Python'daki list veri yapısını class'in attrribute'u olarak kullanabilirsiniz.
"""