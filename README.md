# VoxScene MVP

## AI-Powered Offline Scene Understanding Prototype

VoxScene MVP is an AI-based assistive prototype designed to help visually impaired users understand their surroundings through voice interaction.

The system uses a laptop camera to capture an image, processes it using an offline computer vision model, generates a simple scene description, and provides voice feedback to the user.

The main goal of this MVP is to validate that lightweight AI vision can run locally without depending on cloud services.

---

# Project Objective

The objective of VoxScene MVP is to build an offline-first AI assistant that can:

- Capture surroundings through a camera
- Understand basic objects using computer vision
- Generate human-readable descriptions
- Provide spoken feedback using text-to-speech

---

# Core Workflow


User Voice Command

    ↓

Speech Recognition

    ↓

Camera Capture

    ↓

AI Vision Model

    ↓

Object Detection

    ↓

Scene Description

    ↓

Text To Speech

    ↓

Voice Output


---

# Features

## Voice Interaction

Users can activate the system using voice commands.

Example:

"What is in front of me?"

---

## Image Capture

The system captures images using the laptop webcam.

Technology:

- OpenCV

---

## AI Vision Understanding

The captured image is analyzed using a lightweight object detection model.

Technology:

- YOLOv8 Nano

Output example:


laptop
chair
cup


---

## Scene Description

Detected objects are converted into simple human-friendly descriptions.

Example:

Input:


laptop, chair


Output:


I can see a laptop and chair around you.


---

## Voice Output

The generated description is converted into speech.

Technology:

- pyttsx3 Text To Speech

---

# Technology Stack

## Programming Language

Python 3.11


## Computer Vision

OpenCV


## AI Model

YOLOv8 Nano


## AI Framework

Ultralytics


## Speech Recognition

SpeechRecognition


## Text To Speech

pyttsx3


---

# Project Structure


VoxScene_Prototype

│
├── src
│ ├── main.py
│ ├── camera.py
│ ├── ai_model.py
│ ├── description.py
│ ├── speech.py
│ ├── voice.py
│ ├── config.py
│ └── logger.py
│
├── assets
│ └── captured_images
│
├── models
│
├── tests
│
├── logs
│
├── requirements.txt
│
└── README.md


---

# Installation

Clone the repository:


git clone <repository-url>


Move into project folder:


cd VoxScene_Prototype


Create virtual environment:


python -m venv venv


Activate environment:

Windows:


venv\Scripts\activate


Install dependencies:


pip install -r requirements.txt


---

# Run Project

Start VoxScene:


python -m src.main


Then speak:


What is in front of me?


The system will capture an image, analyze it, and provide a voice response.

---

# Current MVP Capabilities

✅ Offline AI vision pipeline  
✅ Voice command activation  
✅ Webcam image capture  
✅ Object detection  
✅ Scene description generation  
✅ Voice feedback  


---

# Current Limitations

This MVP does not include:

- Real-time continuous vision
- Navigation assistance
- Traffic detection
- Emergency guidance
- Advanced scene reasoning

---

# Future Improvements

Possible future improvements:

- Better vision-language models
- More natural scene descriptions
- Object searching
- Multi-language support
- Mobile application version
- Real-time assistance

---

# Development Approach

The project follows an incremental MVP development approach:

Build → Test → Improve

Each module was developed and tested independently before full system integration.

---

# Project Status

Current Status:

**Prototype Completed**

The MVP successfully demonstrates an offline AI vision assistant pipeline running locally on a laptop.
