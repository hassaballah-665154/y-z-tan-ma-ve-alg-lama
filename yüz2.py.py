import cv2


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Kamera veya video dosyası tanımlama
cap = cv2.VideoCapture(0)  # 0 varsayılan kamerayı seçer, farklı bir video dosyası için yol verilebilir

while True:

    ret, frame = cap.read()
    
    # Gri tonlamalıya dönüştür
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Yüzleri algıla
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Algılanan yüzleri etiketle
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, 'Face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
    
    # Pencereye kameradan gelen görüntüyü göster
    cv2.imshow('Face Detection', frame)
    
    # 'q' tuşuna basarak çıkış yap
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Çıkış temizleme
cap.release()
cv2.destroyAllWindows()
