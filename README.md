# 🧠 Sign-Language-Detection-Model

This project is a Real-Time Sign Language Detection System that recognizes English alphabet signs (A–Z) using a webcam. It leverages MediaPipe for hand landmark detection and a Machine Learning model trained with custom-collected gesture data.

🚀 Features

📸 Real-time hand gesture detection using OpenCV
✋ Hand landmark tracking with MediaPipe Hands
🧩 Custom-trained ML model for A–Z alphabet recognition
🧠 Efficient and lightweight — runs smoothly on most systems
💾 Includes data collection, training, and prediction scripts

🧰 Tech Stack

Python
OpenCV
MediaPipe
NumPy
Scikit-learn
Pickle

📂 Project Structure
│
├── collect_images.py      # Capture and save hand gesture data
├── create_dataset.py      # Making the folders of the collected data
├── train_classifier.py    # Training the Random Forest Regressor model 
├── test_model.p           # Run real-time sign recognition
└── requirements           # The versions of the tech stack required

🧑‍💻 How It Works

Data Collection – Capture images for each alphabet using collect_images.py.
Model Training – Train a classifier using extracted landmarks.
Real-Time Prediction – Detect hand landmarks live and predict corresponding alphabet signs.

🎯 Future Enhancements

Support for dynamic gestures (e.g., words or phrases) (Requiring huge dataset with more advanced GPUs)
Integration with Deep Learning (CNN) models
Add audio feedback for recognized signs
