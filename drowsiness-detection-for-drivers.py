import cv2
import dlib
import pygame
import time 
face_detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor("models/shape_predictor_68_face_landmarks.dat")
camera = cv2.VideoCapture(0)
s = 0  
w = 0

def eyes():
    left_eye = (face_landmarks.part(36).x, face_landmarks.part(36).y)
    right_eye = (face_landmarks.part(45).x, face_landmarks.part(45).y)
    eye_ratio = (abs(face_landmarks.part(37).y - face_landmarks.part(41).y) + abs(face_landmarks.part(38).y - face_landmarks.part(40).y)) / (2 * abs(face_landmarks.part(36).x - face_landmarks.part(39).x))   
    return eye_ratio

def lips():
    upper_lip = face_landmarks.part(62)
    lower_lip = face_landmarks.part(66)
    lip_distance = abs(lower_lip.y - upper_lip.y)
    return lip_distance

def send_alert():
    pygame.mixer.init()
    cv2.putText(frame, "Warning!", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
    alert_sound = pygame.mixer.Sound("models/alarm-82999.wav")
    alert_sound.play()

def finish():
    camera.release()
    cv2.destroyAllWindows()

while camera.isOpened():
    ret, frame = camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector(gray)
    for face in faces:
        face_landmarks = shape_predictor(gray, face)
        if eyes() <= 0.2:
            s += 1
            
            if s<31 and s%10==0:
                w=w+1
                cv2.putText(frame, f"{w}", (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            if s > 40:
                send_alert()
        else:
            s = 0
            w = 0
        if lips() > 32:
            send_alert()
        cv2.imshow("Result", frame)
    if cv2.waitKey(1) == ord("q"):
        print("Camera closed!")
        finish()
        break
