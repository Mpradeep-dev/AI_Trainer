import cv2 as cv
import numpy as np
import pose_module as pm

vid = cv.VideoCapture("res/gym1.mp4")
dec = pm.detector()
count = 0
dir = 0

while vid.isOpened():
    isTrue, img = vid.read()
    if not isTrue:
        break

    img = cv.resize(img, (img.shape[1] * 2, img.shape[0] * 2))
    height = img.shape[0]  # y-axis (resized)
    width = img.shape[1]   # x-axis (resized)

    img = dec.find_pose(img, False)
    lmlist = dec.get_conn(img, False)

    top_margin = int(height * 0.1)    # 10% from top
    bottom_margin = int(height * 0.05)  # 5% from bottom

    if lmlist is not None and len(lmlist) > 0:
        angle = dec.find_angle(12, 14, 16, img, True)

        per = np.interp(angle, (210, 330), (0, 100))

        if per == 100:
            if dir == 1:
                count += 0.5
                dir = 0
        if per == 0:
            if dir == 0:
                count += 0.5
                dir = 1

        # Rep progress bar (right side) — shows current rep completion
        bar_y = int(np.interp(per, [0, 100], [height - bottom_margin, top_margin]))

        # Draw outer bar
        cv.rectangle(img, (width - 80, top_margin), (width - 30, height - bottom_margin),
                     (255, 0, 255), 3)

        # Draw filled bar
        cv.rectangle(img, (width - 80, bar_y), (width - 30, height - bottom_margin),
                     (255, 0, 255), cv.FILLED)

        # Show rep percentage text
        cv.putText(img, f"{int(per)}%", (width - 120, top_margin - 10),
                   cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        # Curl count panel (bottom-left)
        cv.rectangle(img, (0, height - 200), (250, height), (0, 255, 0), cv.FILLED)
        cv.putText(img, "Curls", (50, height - 130),
                   cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv.putText(img, str(int(count)), (60, height - 50),
                   cv.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 5)

    cv.imshow("AI Gym Trainer", img)
    if cv.waitKey(10) & 0xFF == 27:
        break

vid.release()
cv.destroyAllWindows()