# Real-Time Voter Authentication System

Real-Time Voter Authentication System: An advanced voting solution using barcode scanning and facial recognition to ensure secure and accurate voter verification. The system scans barcodes from IDs and verifies identities through real-time facial recognition, enhancing election security and streamlining the voting process.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Setup](#setup)
  - [1. Clone the repository](#1-clone-the-repository)
  - [2. Install the required Python libraries](#2-install-the-required-python-libraries)
  - [3. Generate Encryption Key](#3-generate-encryption-key)
  - [4. Create and Populate the Database](#4-create-and-populate-the-database)
  - [5. Run the Voter Verification System](#5-run-the-voter-verification-system)
- [How It Works](#how-it-works)
- [License](#license)
- [Contact](#contact)
- [Disclaimer](#disclaimer)

## Introduction

The Real-Time Voter Authentication System is a Python-based application designed to improve the security and efficiency of the voting process. By combining barcode scanning and facial recognition technology, this system ensures that each voter is accurately identified, preventing fraud and enhancing the integrity of elections.

## Features

- **Barcode Scanning**: Utilizes a webcam to scan voter ID barcodes.
- **Facial Recognition**: Matches the face of the voter with the stored image in the database.
- **Database Management**: Securely stores voter information, including encrypted barcodes and face images.
- **Encryption**: Ensures that sensitive voter information is encrypted and protected.

## Project Structure

The project contains the following main files:

- `Voter_verification.py`: Handles barcode scanning, face recognition, and verification.
- `Database_creation.py`: Creates the SQLite database and adds voter data.
- `Key_generation.py`: Generates an encryption key used for securing data.
- `encryption_key.key`: The generated encryption key (not included in the repository for security reasons).
- `voters.db`: The SQLite database containing voter information (generated during runtime).

## Installation

### Prerequisites

Ensure that you have the following installed on your system:

- Python 3.x
- pip (Python package installer)
- OpenCV
- face_recognition
- cryptography
- numpy
- pyzbar

### Libraries Required

Install the required Python libraries using the following command:

    pip install opencv-python pyzbar sqlite3 cryptography face_recognition numpy 

## Setup

### 1. Clone the repository:

      git clone https://github.com/yourusername/Real-Time-Voter-Authentication-System.git
      cd Real-Time-Voter-Authentication-System

### 2. Install the required Python libraries:
  
        pip install -r requirements.txt

### 3. Generate Encryption Key

  - Before you can create and populate the database, you need to generate an encryption key.
  - Run the Key_generation.py script to create the encryption_key.key file:

        python Key_generation.py

  This will generate a file named encryption_key.key, which will be used to encrypt sensitive data in the database.

### 4. Create and Populate the Database

  - Once the encryption key is generated, you can create and populate the database with voter information.

  - Open the Database_creation.py file.

  - Modify the add_voter function call at the end of the script to include actual voter information. Example:

        add_voter('John Doe', 'XYZ1234567', 'path_to_image_of_voter.jpg')
  
    Replace 'path_of_the_image_of_voter_card' in Database_creation.py with the actual path of the voter's image.

  - Run the script to create the voters.db SQLite database and add the voter(s):

        python Database_creation.py

### 5. Run the Voter Verification System

  Now that the database is set up, you can run the voter verification system.

  - Run the Voter_verification.py script:

        python Voter_verification.py

  - The system will activate the webcam and start scanning for barcodes.

  - Once a barcode is detected, it will retrieve the corresponding voter information from the database.

  - The system will then attempt to match the face of the voter with the stored image.

  - If the face matches, the voter is authenticated; otherwise, the system will indicate a failed authentication.


## How It Works
- Barcode Scanning: The system uses the cv2 and pyzbar libraries to capture and decode barcodes from voter IDs.
- Face Recognition: The face_recognition library compares the real-time image captured by the webcam with the stored image in the database.
- Database Management: SQLite3 is used to store and manage voter information securely.
- Encryption: Sensitive data, such as barcodes, are encrypted using the cryptography.fernet module before being stored in the database.

  ## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

If you have any questions or issues with this project, please contact Faiz-3112 .

## Disclaimer

This project is protected under copyright law. No part of this project may be reproduced, distributed, or transmitted in any form or by any means, including photocopying, recording, or other electronic or mechanical methods, without the prior written permission of the author, except in the case of brief quotations embodied in critical reviews and certain other noncommercial uses permitted by copyright law.

Unauthorized use, reproduction, or distribution of this material is prohibited and may result in severe civil and criminal penalties.
