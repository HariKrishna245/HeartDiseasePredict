<!-- BANNER -->
<p align="center">
  <img src="https://img.shields.io/badge/Heart%20Disease%20Prediction-Machine%20Learning-red?style=for-the-badge" alt="Heart Disease Prediction Banner" />
</p>

<h1 align="center">❤️ Heart Disease Prediction using Machine Learning</h1>

<p align="center">
  An end-to-end Machine Learning project to predict the likelihood of heart disease using clinical health parameters, complete with a modular ML pipeline and a Tkinter-based GUI.
</p>

---

## 🏷️ Badges

<p align="left">
  <img src="https://img.shields.io/github/languages/top/HariKrishna245/HeartDiseasePredict?style=for-the-badge" alt="Top Language" />
  <img src="https://img.shields.io/github/last-commit/HariKrishna245/HeartDiseasePredict?style=for-the-badge" alt="Last Commit" />
  <img src="https://img.shields.io/github/repo-size/HariKrishna245/HeartDiseasePredict?style=for-the-badge" alt="Repo Size" />
  <img src="https://img.shields.io/github/license/HariKrishna245/HeartDiseasePredict?style=for-the-badge" alt="License" />
</p>

---

## 📌 Overview

**HeartDiseasePredict** is a complete end-to-end Machine Learning project developed to predict the likelihood of heart disease using clinical health parameters.

The project demonstrates a fully structured ML workflow including:

- Data preprocessing  
- Exploratory Data Analysis (EDA)  
- Correlation and feature importance analysis  
- Model training and comparison  
- Final model selection and saving  
- A Tkinter-based GUI for real-time predictions  

Each step is modularized into separate Python scripts (`step1_preprocessing.py` → `step6_save_model.py`) to ensure clarity, scalability, and a professional project structure.

---

## 📁 Project Structure

```plaintext
HeartDiseasePredict/
│
├── src/
│   ├── heart_gui.py                  
│   ├── step1_preprocessing.py       
│   ├── step2_visualization.py       
│   ├── step3_correlation.py         
│   ├── step4_model_comparison.py    
│   ├── step5_final_model.py         
│   └── step6_save_model.py         
│
├── data/                             
│   └── cardio_train.csv
│
├── models/                           
│   ├── model.pkl
│   └── scaler.pkl
│
├── assets/                          
│   ├── gui_screenshot.png
│   └── eda_plot.png
│
├── .gitignore                        
├── README.md                         
├── RUN_INSTRUCTIONS.md               
└── requirements.txt                  


