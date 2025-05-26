import cv2
cap = cv2.VideoCapture('Task6/video1.mp4')
while True:
    ret, frame = cap.read()
    if not ret:
        break
    and_result = cv2.bitwise_and(frame, frame, mask=None)
    or_result = cv2.bitwise_or(frame, frame, mask=None)
    xor_result = cv2.bitwise_xor(frame, frame, mask=None)
    not_result = cv2.bitwise_not(frame)
    cv2.imshow('Bitwise AND', and_result)
    cv2.imshow('Bitwise OR', or_result)
    cv2.imshow('Bitwise XOR', xor_result)
    cv2.imshow('Bitwise NOT', not_result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
