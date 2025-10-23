# 🧠 Sign-Language-Detection-Model


---

## 📝 Overview

This project is a **Real-Time Sign Language Detection System** that recognizes **English alphabet signs (A–Z)** using a webcam.  
It leverages **MediaPipe** for hand landmark detection and a **Machine Learning model** trained with **custom-collected gesture data**.

---

## 🚀 Features

✨ **Real-time gesture recognition** using OpenCV  
✋ **Hand landmark tracking** via MediaPipe Hands  
🧠 **Custom-trained ML model** for A–Z alphabet detection  
⚡ **Lightweight and efficient** — runs smoothly on most systems  
💾 Includes data collection, model training, and prediction scripts  

---

## 🛠️ Tech Stack

| Category | Technologies |
|-----------|---------------|
| **Language** | Python |
| **Libraries** | OpenCV, MediaPipe, NumPy, Scikit-learn, Pickle |
| **Model** | Random Forest Regressor |
| **Environment** | Jupyter / VS Code / PyCharm |

---

## Project Structure

```bash
📁 Sign-Language-Detection-Model/
├── collect_images.py      # Capture and save hand gesture data  
├── create_dataset.py      # Organize and preprocess collected data  
├── train_classifier.py    # Train the Random Forest Regressor model  
├── test_model.p           # Run real-time sign recognition  
└── requirements.txt       # Dependencies and versions  


---

## 🧩 How It Works

1. 🖼️ **Data Collection** – Capture gesture images for each alphabet using `collect_images.py`.  
2. 🧮 **Dataset Creation** – Extract and save hand landmarks with `create_dataset.py`.  
3. 🧠 **Model Training** – Train the Random Forest classifier using `train_classifier.py`.  
4. 🔍 **Real-Time Detection** – Use your webcam to detect and predict signs live.

---

## 🎯 Future Enhancements

🚀 Support for **dynamic gestures** (words or phrases) — with a larger dataset and GPU training  
🧬 Integration with **CNN / Deep Learning** models for better accuracy  
🔊 Add **audio feedback** for recognized signs  
🪄 Build a **user-friendly GUI** for interaction  


