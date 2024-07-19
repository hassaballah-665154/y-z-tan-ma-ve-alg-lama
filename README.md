# yüz tanıma ve etkileme projesi

Bu proje, OpenCV kütüphanesini kullanarak gerçek zamanlı yüz tanıma ve etiketleme işlemi yapmayı amaçlamaktadır. Kamera aracılığıyla algılanan yüzler, önceden tanımlanmış kullanıcı isimleri ile etiketlenir.

## Proje Özellikler

** Yüz Algılama  OpenCV kullanılarak yüzlerin algılanması.
** Etiketleme Algılanan yüzlerin kullanıcı isimleri ile etiketlenmesi.
** Gerçek Zamanlı İşleme Kamera aracılığıyla gerçek zamanlı görüntü işleme.

# kullanlan kütüphaneler
openCv
numpy

# Nasıl Çalışır?
Proje, Haarcascades kullanarak yüzleri algılar. Algılama işlemi gerçek zamanlı olarak gerçekleştirilir ve sonuçlar anında ekranda gösterilir.

# Kullanıcı Tanımları ve Kimlikleri
kullanici_dict = {
    1: "mister",
    2: "Mrs",
}
