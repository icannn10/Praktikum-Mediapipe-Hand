import cv2
import mediapipe
capture = cv2.VideoCapture(0) #video capture pada device kamera nomer 0

mediapipehand = mediapipe.solutions.hands
#inisialisasi deteksi tangan

tangan = mediapipehand.Hands()
#variable tangan untuk menyimpan konfigurasi deteksi tangan

while True:
    success, img = capture.read() #menyimpan citra tangkapan kamera img ke RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #merubah warna img ke RGB
    results = tangan.process(imgRGB) #melakukan proses dari imgRGB
    if results.multi_hand_landmarks:
        print("tangan")
    else:
        print("tidak ada")
    cv2.imshow("webcam" ,img)
    cv2.waitKey(10)
    if cv2.waitKey(10) & 0xff == ord('q'):
            break
capture.release()
cv2.destroyAllWindows()
