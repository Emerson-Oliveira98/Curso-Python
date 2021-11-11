import cv2


webcam = cv2.VideoCapture(0)

if webcam.isOpned():
    print("Conectou")
    print(webcam.read())
    validacao, frame = webcam.read()


    while validacao:
        validacao, frame = webcam.read()
        cv2.imshow("Video da Webcam", frame)
        key = cv2.waitKey(5) #esperando milisegundos e pegando jey do teclado
        if key == 27: #ESC
            break

    cv2.imwrite("FOTOLIRA.png", frame)


webcam.release()
cv2.destroyAllWindows()