import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh

# Webカメラから入力
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
cap = cv2.VideoCapture(0)

# 貼り付ける画像を読み込み
overlay_image = cv2.imread("icon.png", cv2.IMREAD_UNCHANGED)

with mp_face_mesh.FaceMesh(
    max_num_faces=5,  # 複数の顔に対応するために変更
    refine_landmarks=True,
    min_detection_confidence=0.3,
    min_tracking_confidence=0.3,
) as face_mesh:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(image)

        # 検出された顔のメッシュをカメラ画像の上に描画
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                # 顔の輪郭の座標を取得
                landmarks = []
                for point in face_landmarks.landmark:
                    h, w, c = image.shape
                    x, y = int(point.x * w), int(point.y * h)
                    landmarks.append((x, y))

                # 顔の高さと幅を計算
                face_width = landmarks[454][0] - landmarks[234][0]  # 右端 - 左端
                face_height = landmarks[152][1] - landmarks[10][1]  # 下端 - 上端

                # 画像をリサイズして顔の大きさに合わせる
                resized_overlay = cv2.resize(
                    overlay_image,
                    (face_width, face_height),
                    interpolation=cv2.INTER_AREA,
                )

                # 画像をオーバーレイ
                overlayed_image = image.copy()
                for i in range(face_height):
                    for j in range(face_width):
                        alpha = resized_overlay[i, j, 3] / 255.0
                        overlayed_image[
                            landmarks[10][1] + i, landmarks[234][0] + j, :
                        ] = (1 - alpha) * overlayed_image[
                            landmarks[10][1] + i, landmarks[234][0] + j, :
                        ] + alpha * resized_overlay[
                            i, j, 0:3
                        ]

                image = overlayed_image

        cv2.imshow("MediaPipe Face Mesh", cv2.flip(image, 1))
        if cv2.waitKey(5) & 0xFF == 27:
            break
cap.release()
