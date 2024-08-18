import cv2
from pyzbar import pyzbar
import sqlite3
from cryptography.fernet import Fernet
import face_recognition
import numpy as np
import time

# Load the encryption key
with open('encryption_key.key', 'rb') as key_file:
    key = key_file.read()

cipher = Fernet(key)

# Connect to the database
conn = sqlite3.connect('voters.db')
cursor = conn.cursor()

def get_voter_by_barcode(barcode):
    cursor.execute('SELECT id, name, face_image FROM voters WHERE original_barcode = ?', (barcode,))
    return cursor.fetchone()

def verify_face(known_face_image, real_time_image):
    known_face_encodings = face_recognition.face_encodings(known_face_image)
    real_time_face_encodings = face_recognition.face_encodings(real_time_image)

    if not known_face_encodings:
        print("Error: No face detected in known face image.")
        return False
    if not real_time_face_encodings:
        print("Error: No face detected in real-time image.")
        return False

    known_face_encoding = known_face_encodings[0]
    real_time_face_encoding = real_time_face_encodings[0]
    
    results = face_recognition.compare_faces([known_face_encoding], real_time_face_encoding)
    return results[0]

def scan_barcode():
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open video capture.")
        return None
    
    barcode_data = None

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame from video capture.")
            break
        
        # Detect barcodes in the frame
        barcodes = pyzbar.decode(frame)
        if barcodes:
            for barcode in barcodes:
                barcode_data = barcode.data.decode('utf-8')
                (x, y, w, h) = barcode.rect
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                barcode_text = f"{barcode_data} ({barcode.type})"
                cv2.putText(frame, barcode_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                print(f"Scanned Barcode: {barcode_data}")
                voter = get_voter_by_barcode(barcode_data)
                
                if voter:
                    print("Matching barcode found in the database.")
                    id, name, face_image_blob = voter
                    known_face_image = cv2.imdecode(np.frombuffer(face_image_blob, np.uint8), cv2.IMREAD_COLOR)
                    cap.release()
                    cv2.destroyAllWindows()
                    return known_face_image
                else:
                    print("No matching barcode found in the database. Invalid barcode.")
        else:
            pass
            #print("No barcode detected.")
        
        cv2.imshow('Barcode Scanner', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    return None

def verify_face_with_camera(known_face_image):
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open video capture.")
        return False
    
    print("Please position your face in front of the camera for verification.")
    time.sleep(10)  # Wait for 10 seconds for the user to position their face
    
    ret, real_time_frame = cap.read()
    if not ret:
        print("Error: Could not read frame from video capture.")
        cap.release()
        return False
    
    # Convert the captured frame to RGB (required for face_recognition)
    real_time_image_rgb = cv2.cvtColor(real_time_frame, cv2.COLOR_BGR2RGB)
    
    # Display the real-time image for verification
    cv2.imshow('Real-Time Image', real_time_frame)
    cv2.waitKey(1)  # Display the frame for 1 millisecond
    
    is_face_match = verify_face(known_face_image, real_time_image_rgb)
    
    cap.release()
    cv2.destroyAllWindows()
    return is_face_match

def main():
    known_face_image = scan_barcode()
    
    if known_face_image is not None:
        is_face_match = verify_face_with_camera(known_face_image)
        
        if is_face_match:
            print("Face match successful. Voter is authenticated.")
        else:
            print("Face match failed. Voter is not authenticated.")
    else:
        print("Barcode scanning failed or barcode not found in database.")

if __name__ == "__main__":
    main()