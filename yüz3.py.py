import numpy as np
import cv2

#  yüz tanıma sınıflandırıcısını yükleme
yuz_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Kamera bağlantısını başlatma
vid = cv2.VideoCapture(0)

# Kullanıcı tanımları ve kimlikleri (mister or mrs)
kullanici_dict = {
    1: "mister",
    2: "Mrs",

}

while True:
    ret, frame = vid.read()
    
    # Gri tonlama yapma
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Yüzleri algılama
    yuzler = yuz_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    
    # Algılanan yüzler için işlemler
    for (x, y, w, h) in yuzler:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # Algılanan yüzü kesme
        yuz_roi = gray[y:y+h, x:x+w]
        
        # Yüz tanıma işlemi
        # Burada sadece yüzleri numaralandırıyoruz
        # Gerçek bir tanıma sistemine entegre etmek için daha karmaşık bir model gerekebilir
        kullanici_id = 0
        for id in kullanici_dict:
            kullanici_id += 1
            ad = kullanici_dict[id]
            cv2.putText(frame, f"{ad}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2, cv2.LINE_AA)
        
    # Ekranı gösterme
    cv2.imshow('Yüz Tanıma', frame)
    
    # Çıkış için 'q' tuşuna basılmasını bekler
    if cv2.waitKey(1) & 0xFF == ord('d'):
        break

# Kamera bağlantısını serbest bırakma ve tüm pencereleri kapatma
vid.release()
cv2.destroyAllWindows()
