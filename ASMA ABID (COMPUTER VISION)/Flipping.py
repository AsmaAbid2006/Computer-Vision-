import cv2
cap = cv2.VideoCapture('Task6/video1.mp4')
while True:
    ret, frame = cap.read()
    if not ret:
        break
    flip_horizontal = cv2.flip(frame, 1)
    flip_vertical = cv2.flip(frame, 0)
    flip_both = cv2.flip(frame, -1)
    cv2.imshow('Flipped Horizontal', flip_horizontal)
    cv2.imshow('Flipped Vertical', flip_vertical)
    cv2.imshow('Flipped Both', flip_both)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()