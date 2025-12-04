# 🚀 Heart Disease Prediction using Machine Learning

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

## 📌 Features

### 🔹 End-to-End ML Pipeline
- Data cleaning, encoding, and scaling  
- Visualizations & statistical insights  
- Correlation heatmaps  
- Training multiple ML models  
- Best model selection based on performance  
- Persisting model/scaler using Pickle  

### 🔹 GUI for Predictions
- Tkinter-based user interface  
- Users enter health inputs and get instant predictions  
- No technical knowledge needed  

### 🔹 Clean, Professional Structure
- Separate folders for `src`, `data`, and `models`  
- Easy to navigate and extend  

---

## 📁 Project Structure

```plaintext
HeartDiseasePredict/
│
├── src/
│   ├── heart_gui.py                  # Tkinter GUI for real-time predictions
│   ├── step1_preprocessing.py        # Cleans and preprocesses raw data
│   ├── step2_visualization.py        # Generates EDA plots
│   ├── step3_correlation.py          # Creates correlation heatmaps
│   ├── step4_model_comparison.py     # Trains & compares ML models
│   ├── step5_final_model.py          # Trains the final chosen model
│   └── step6_save_model.py           # Saves model.pkl & scaler.pkl
│
├── data/                              # Contains dataset (ignored in GitHub)
│   └── cardio_train.csv
│
├── models/                            # Saved ML model and scaler (ignored)
│   ├── model.pkl
│   └── scaler.pkl
│
├── .gitignore                         # Excludes unnecessary folders/files
├── README.md                          # Project documentation
└── requirements.txt                   # Python dependencies
