# ------------------------------------------------------------
# 1️⃣ CLONE THE PROJECT

git clone https://github.com/HariKrishna245/HeartDiseasePredict.git
cd HeartDiseasePredict

# ------------------------------------------------------------
# 2️⃣ (OPTIONAL BUT RECOMMENDED) CREATE A VIRTUAL ENVIRONMENT


# Windows:
python -m venv venv
venv\Scripts\activate

# macOS / Linux:
python3 -m venv venv
source venv/bin/activate

# ------------------------------------------------------------
# 3️⃣ INSTALL ALL REQUIRED PYTHON PACKAGES

pip install -r requirements.txt

# ------------------------------------------------------------
# 4️⃣ (OPTIONAL) RUN EACH MACHINE LEARNING PIPELINE STEP


# Step 1: Data preprocessing
python src/step1_preprocessing.py

# Step 2: Data visualization (EDA)
python src/step2_visualization.py

# Step 3: Correlation analysis
python src/step3_correlation.py

# Step 4: Model comparison (multiple ML models)
python src/step4_model_comparison.py

# ------------------------------------------------------------
# 5️⃣ TRAIN THE FINAL MACHINE LEARNING MODEL

python src/step5_final_model.py

# This generates:
#  → models/model.pkl
#  → models/scaler.pkl

# ------------------------------------------------------------
# 6️⃣ SAVE THE MODEL 

python src/step6_save_model.py

# ------------------------------------------------------------
# 7️⃣ RUN THE TKINTER GUI APPLICATION

python src/heart_gui.py

# GUI will open → Enter patient details → Click Predict
