import cv2
import mediapipe as mp

# Inisialisasi MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
# Buka kamera
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    # Mirror image supaya natural
    frame = cv2.flip(frame, 1)
    # Konversi BGR ke RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Proses deteksi tangan
    results = hands.process(rgb_frame)
    # Jika tangan terdeteksi
    if results.multi_hand_landmarks and results.multi_handedness:
        for idx, hand in enumerate(results.multi_handedness):
            # klasifikasi
            if hand.classification[0]:

                # Jika index == 1 → tangan kanan
                if hand.classification[0].index == 1:
                    cv2.putText(frame, "KANAN",
                                (200, 50),
                                cv2.FONT_HERSHEY_PLAIN,
                                5,
                                (255, 0, 0),
                                3)

                # Jika index == 0 → tangan kiri
                elif hand.classification[0].index == 0:
                    cv2.putText(frame, "KIRI",
                                (200, 50),
                                cv2.FONT_HERSHEY_PLAIN,
                                5,
                                (0, 0, 255),
                                3)

        # Gambar landmark tangan
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )
    cv2.imshow("Deteksi Tangan Kanan & Kiri", frame)
    if cv2.waitKey(1) & 0xFF == 27:  # tekan ESC untuk keluar
        break
cap.release()
cv2.destroyAllWindows()