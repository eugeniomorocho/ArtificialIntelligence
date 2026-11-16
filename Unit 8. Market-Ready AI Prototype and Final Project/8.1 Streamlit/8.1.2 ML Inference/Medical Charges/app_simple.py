"""
Medical Charges Prediction App - Simple Tkinter Version
Local desktop application - No Streamlit needed
"""

import tkinter as tk
from tkinter import ttk, messagebox
import joblib
import pandas as pd
import os
from pathlib import Path

class MedicalChargesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Medical Charges Prediction")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        
        # Load model
        model_path = Path(__file__).parent / 'regression_model.pkl'
        if not model_path.exists():
            messagebox.showerror("Error", f"Model not found: {model_path}")
            root.destroy()
            return
        
        self.model = joblib.load(model_path)
        
        # Create interface
        self.setup_ui()
    
    def setup_ui(self):
        # Title
        tk.Label(self.root, text="Medical Charges Predictor", 
                font=("Arial", 16, "bold"), pady=10).pack()
        
        # Frame for inputs
        frame = ttk.Frame(self.root, padding=20)
        frame.pack(fill="both", expand=True)
        
        # Age
        ttk.Label(frame, text="Age:").grid(row=0, column=0, sticky="w", pady=5)
        self.age = ttk.Spinbox(frame, from_=0, to=120, width=25)
        self.age.set(30)
        self.age.grid(row=0, column=1)
        
        # Sex
        ttk.Label(frame, text="Sex:").grid(row=1, column=0, sticky="w", pady=5)
        self.sex = ttk.Combobox(frame, values=["male", "female"], state="readonly", width=23)
        self.sex.set("male")
        self.sex.grid(row=1, column=1)
        
        # BMI
        ttk.Label(frame, text="BMI:").grid(row=2, column=0, sticky="w", pady=5)
        self.bmi = ttk.Spinbox(frame, from_=0, to=100, increment=0.1, width=25)
        self.bmi.set(25)
        self.bmi.grid(row=2, column=1)
        
        # Children
        ttk.Label(frame, text="Children:").grid(row=3, column=0, sticky="w", pady=5)
        self.children = ttk.Spinbox(frame, from_=0, to=10, width=25)
        self.children.set(0)
        self.children.grid(row=3, column=1)
        
        # Smoker
        ttk.Label(frame, text="Smoker:").grid(row=4, column=0, sticky="w", pady=5)
        self.smoker = ttk.Combobox(frame, values=["no", "yes"], state="readonly", width=23)
        self.smoker.set("no")
        self.smoker.grid(row=4, column=1)
        
        # Region
        ttk.Label(frame, text="Region:").grid(row=5, column=0, sticky="w", pady=5)
        self.region = ttk.Combobox(frame, 
                                   values=["northeast", "northwest", "southeast", "southwest"],
                                   state="readonly", width=23)
        self.region.set("northeast")
        self.region.grid(row=5, column=1)
        
        # Button
        ttk.Button(frame, text="Predict", command=self.predict).grid(row=6, column=0, 
                                                                      columnspan=2, pady=20)
        
        # Result
        self.result = tk.Label(self.root, text="", font=("Arial", 12, "bold"), fg="green")
        self.result.pack(pady=10)
    
    def predict(self):
        try:
            data = pd.DataFrame({
                "age": [int(self.age.get())],
                "sex": [1 if self.sex.get() == "male" else 0],
                "bmi": [float(self.bmi.get())],
                "children": [int(self.children.get())],
                "smoker": [1 if self.smoker.get() == "yes" else 0],
                "region_northeast": [1 if self.region.get() == "northeast" else 0],
                "region_northwest": [1 if self.region.get() == "northwest" else 0],
                "region_southeast": [1 if self.region.get() == "southeast" else 0],
                "region_southwest": [1 if self.region.get() == "southwest" else 0]
            })
            
            pred = self.model.predict(data)[0]
            self.result.config(text=f"Predicted: ${pred:,.2f}", fg="green")
        except Exception as e:
            self.result.config(text=f"Error: {str(e)}", fg="red")


if __name__ == "__main__":
    root = tk.Tk()
    app = MedicalChargesApp(root)
    root.mainloop()
