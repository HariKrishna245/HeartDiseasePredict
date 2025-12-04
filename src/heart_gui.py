import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import pickle

# Load model and scaler
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Root setup
root = tk.Tk()
root.title("❤️ Cardiovascular Disease Predictor")
root.state('zoomed')  # Make fullscreen
root.configure(bg="#ecf0f1")

# ========== Header ==========
header = tk.Label(root, text="Cardiovascular Disease Prediction System", font=("Helvetica", 26, "bold"), bg="#3498db",
                  fg="white", pady=20)
header.pack(fill=tk.X)

# ========== Main Frame ==========
main_frame = tk.Frame(root, bg="#ecf0f1", padx=50, pady=30)
main_frame.pack(fill=tk.BOTH, expand=True)

fields = [
    ("Age (years)", "entry"),
    ("Gender", "dropdown", ["1 - Male", "2 - Female"]),
    ("Height (cm)", "entry"),
    ("Weight (kg)", "entry"),
    ("Systolic BP", "entry"),
    ("Diastolic BP", "entry"),
    ("Cholesterol", "dropdown", ["1 - Normal", "2 - Above Normal", "3 - Well Above"]),
    ("Glucose", "dropdown", ["1 - Normal", "2 - Above Normal", "3 - Well Above"]),
    ("Smoke", "dropdown", ["0 - No", "1 - Yes"]),
    ("Alcohol", "dropdown", ["0 - No", "1 - Yes"]),
    ("Physical Activity", "dropdown", ["0 - No", "1 - Yes"]),
]

entries = {}

# ========== Layout Fields ==========
for i, (label_text, input_type, *dropdown_values) in enumerate(fields):
    row = i // 2
    col = (i % 2) * 2

    tk.Label(main_frame, text=label_text, font=("Arial", 14), bg="#ecf0f1").grid(row=row, column=col, sticky="w",
                                                                                 padx=(0, 10), pady=15)

    if input_type == "entry":
        entry = tk.Entry(main_frame, font=("Arial", 14), width=25)
        entry.grid(row=row, column=col + 1, padx=(0, 40), pady=10)
        entries[label_text] = entry
    else:
        combo = ttk.Combobox(main_frame, values=dropdown_values[0], state="readonly", font=("Arial", 14), width=23)
        combo.grid(row=row, column=col + 1, padx=(0, 40), pady=10)
        combo.current(0)
        entries[label_text] = combo


# ========== Predict Button ==========
def predict():
    try:
        age = int(entries["Age (years)"].get())
        height = float(entries["Height (cm)"].get())
        weight = float(entries["Weight (kg)"].get())
        sbp = float(entries["Systolic BP"].get())
        dbp = float(entries["Diastolic BP"].get())

        gender = int(entries["Gender"].get().split(" - ")[0])
        chol = int(entries["Cholesterol"].get().split(" - ")[0])
        gluc = int(entries["Glucose"].get().split(" - ")[0])
        smoke = int(entries["Smoke"].get().split(" - ")[0])
        alco = int(entries["Alcohol"].get().split(" - ")[0])
        active = int(entries["Physical Activity"].get().split(" - ")[0])

        values = [age, gender, height, weight, sbp, dbp, chol, gluc, smoke, alco, active]
        scaled = scaler.transform([values])
        result = model.predict(scaled)[0]

        if result == 1:
            result_label.config(text="⚠️ High Risk of Heart Disease", fg="red")
        else:
            result_label.config(text="✅ Low Risk of Heart Disease", fg="green")

    except Exception as e:
        messagebox.showerror("Error", f"Please check inputs.\n\n{e}")


# ========== Reset Form ==========
def reset():
    for widget in entries.values():
        if isinstance(widget, tk.Entry):
            widget.delete(0, tk.END)
        else:
            widget.current(0)
    result_label.config(text="", fg="black")


# ========== Button Frame ==========
btn_frame = tk.Frame(root, bg="#ecf0f1")
btn_frame.pack(pady=30)

tk.Button(btn_frame, text="Predict", font=("Arial", 16), bg="#27ae60", fg="white", width=15, command=predict).grid(
    row=0, column=0, padx=20)
tk.Button(btn_frame, text="Reset", font=("Arial", 16), bg="#c0392b", fg="white", width=15, command=reset).grid(row=0,
                                                                                                               column=1,
                                                                                                               padx=20)

# ========== Result Label ==========
result_label = tk.Label(root, text="", font=("Arial", 20, "bold"), bg="#ecf0f1")
result_label.pack(pady=10)

root.mainloop()
