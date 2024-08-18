
import sqlite3
from cryptography.fernet import Fernet
import cv2

# Load the encryption key
with open('encryption_key.key', 'rb') as key_file:
    key = key_file.read()

cipher = Fernet(key)

# Connect to the database
conn = sqlite3.connect('voters.db')
cursor = conn.cursor()

# Drop the voters table if it exists and create it again
cursor.execute('DROP TABLE IF EXISTS voters')
cursor.execute('''
    CREATE TABLE voters (
        id TEXT PRIMARY KEY,
        name TEXT,
        original_barcode TEXT,
        encrypted_barcode TEXT,
        face_image BLOB
    )
''')

# Function to add a voter
def add_voter(name, original_barcode, image_path):
    encrypted_barcode = cipher.encrypt(original_barcode.encode())
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not read image from {image_path}")
        return
    
    _, buffer = cv2.imencode('.jpg', image)
    face_image = buffer.tobytes()
    
    cursor.execute('''
        INSERT OR REPLACE INTO voters (id, name, original_barcode, encrypted_barcode, face_image)
        VALUES (?, ?, ?, ?, ?)
    ''', (original_barcode, name, original_barcode, encrypted_barcode, face_image))
    conn.commit()

# Add sample voter
add_voter('John Cena', 'XYZ1234567', 'sample_image_path.jpg')


# Close the connection
conn.close()
