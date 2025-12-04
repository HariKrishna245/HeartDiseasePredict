
## 1️⃣ Clone the Project
git clone https://github.com/HariKrishna245/HeartDiseasePredict.git
cd HeartDiseasePredict

## 2️⃣ (Optional) Create a Virtual Environment
# Windows:
python -m venv venv
venv\Scripts\activate

# macOS / Linux:
python3 -m venv venv
source venv/bin/activate

## 3️⃣ Install Required Python Packages
pip install -r requirements.txt

## 4️⃣ (Optional) Run Each Machine Learning Pipeline Step
# Step 1 – Data Preprocessing
python src/step1_preprocessing.py

# Step 2 – Exploratory Data Analysis (EDA)
python src/step2_visualization.py

# Step 3 – Correlation Analysis
python src/step3_correlation.py

# Step 4 – Model Comparison
python src/step4_model_comparison.py

## 5️⃣ Train the Final Machine Learning Model
python src/step5_final_model.py

## 6️⃣ Save the Model
python src/step6_save_model.py

## 7️⃣ Run the Tkinter GUI Application
python src/heart_gui.py

# GUI will open → Enter patient details → Click Predict
