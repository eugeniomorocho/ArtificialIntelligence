"""
Medical Charges Prediction App using Tkinter
Converts the Streamlit app to a desktop application using Tkinter
"""

import tkinter as tk
from tkinter import ttk, messagebox
import joblib
import pandas as pd
import os

class MedicalChargesPredictionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Medical Charges Prediction")
        self.root.geometry("600x700")
        self.root.resizable(False, False)
        
        # Set style
        self.root.configure(bg="#f0f0f0")
        style = ttk.Style()
        style.theme_use('clam')
        
        # Load the model
        try:
            model_path = os.path.join(os.path.dirname(__file__), 'regression_model.pkl')
            self.model = joblib.load(model_path)
        except FileNotFoundError:
            messagebox.showerror("Error", "Model file 'regression_model.pkl' not found!")
            return
        
        # Create UI
        self.create_widgets()
    
    def create_widgets(self):
        # Title
        title_frame = tk.Frame(self.root, bg="#2c3e50", height=80)
        title_frame.pack(fill=tk.X)
        
        title_label = tk.Label(
            title_frame,
            text="Medical Charges Prediction",
            font=("Arial", 20, "bold"),
            bg="#2c3e50",
            fg="white"
        )
        title_label.pack(pady=20)
        
        # Main frame for inputs
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Age
        ttk.Label(main_frame, text="Age:").grid(row=0, column=0, sticky="w", pady=10)
        self.age_var = tk.IntVar(value=30)
        age_spinbox = ttk.Spinbox(main_frame, from_=0, to=120, textvariable=self.age_var, width=20)
        age_spinbox.grid(row=0, column=1, sticky="ew", pady=10)
        
        # Sex
        ttk.Label(main_frame, text="Sex:").grid(row=1, column=0, sticky="w", pady=10)
        self.sex_var = tk.StringVar(value="male")
        sex_combo = ttk.Combobox(main_frame, textvariable=self.sex_var, 
                                 values=["male", "female"], state="readonly", width=18)
        sex_combo.grid(row=1, column=1, sticky="ew", pady=10)
        
        # BMI
        ttk.Label(main_frame, text="BMI:").grid(row=2, column=0, sticky="w", pady=10)
        self.bmi_var = tk.DoubleVar(value=25.0)
        bmi_spinbox = ttk.Spinbox(main_frame, from_=0.0, to=100.0, 
                                  textvariable=self.bmi_var, width=20, increment=0.1)
        bmi_spinbox.grid(row=2, column=1, sticky="ew", pady=10)
        
        # Number of Children
        ttk.Label(main_frame, text="Number of Children:").grid(row=3, column=0, sticky="w", pady=10)
        self.children_var = tk.IntVar(value=0)
        children_spinbox = ttk.Spinbox(main_frame, from_=0, to=10, 
                                       textvariable=self.children_var, width=20)
        children_spinbox.grid(row=3, column=1, sticky="ew", pady=10)
        
        # Smoker
        ttk.Label(main_frame, text="Smoker:").grid(row=4, column=0, sticky="w", pady=10)
        self.smoker_var = tk.StringVar(value="no")
        smoker_combo = ttk.Combobox(main_frame, textvariable=self.smoker_var,
                                    values=["yes", "no"], state="readonly", width=18)
        smoker_combo.grid(row=4, column=1, sticky="ew", pady=10)
        
        # Region
        ttk.Label(main_frame, text="Region:").grid(row=5, column=0, sticky="w", pady=10)
        self.region_var = tk.StringVar(value="northeast")
        region_combo = ttk.Combobox(main_frame, textvariable=self.region_var,
                                    values=["northeast", "northwest", "southeast", "southwest"],
                                    state="readonly", width=18)
        region_combo.grid(row=5, column=1, sticky="ew", pady=10)
        
        # Configure column weight for responsiveness
        main_frame.columnconfigure(1, weight=1)
        
        # Prediction button
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=20)
        
        predict_button = tk.Button(
            button_frame,
            text="Predict Medical Charges",
            command=self.predict,
            bg="#27ae60",
            fg="white",
            font=("Arial", 12, "bold"),
            padx=20,
            pady=10,
            cursor="hand2"
        )
        predict_button.pack()
        
        # Result label
        self.result_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 14, "bold"),
            bg="#f0f0f0",
            fg="#2c3e50"
        )
        self.result_label.pack(pady=10)
    
    def predict(self):
        try:
            # Get input values
            age = self.age_var.get()
            sex = 1 if self.sex_var.get() == "male" else 0
            bmi = self.bmi_var.get()
            children = self.children_var.get()
            smoker = 1 if self.smoker_var.get() == "yes" else 0
            region = self.region_var.get()
            
            # Convert region to dummy variables
            region_northeast = 1 if region == "northeast" else 0
            region_northwest = 1 if region == "northwest" else 0
            region_southeast = 1 if region == "southeast" else 0
            region_southwest = 1 if region == "southwest" else 0
            
            # Create input DataFrame
            input_data = pd.DataFrame({
                "age": [age],
                "sex": [sex],
                "bmi": [bmi],
                "children": [children],
                "smoker": [smoker],
                "region_northeast": [region_northeast],
                "region_northwest": [region_northwest],
                "region_southeast": [region_southeast],
                "region_southwest": [region_southwest]
            })
            
            # Make prediction
            prediction = self.model.predict(input_data)
            predicted_charges = prediction[0]
            
            # Display result
            self.result_label.config(
                text=f"Predicted Medical Charges: ${predicted_charges:,.2f}",
                fg="#27ae60"
            )
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.result_label.config(text="", fg="#2c3e50")


def main():
    root = tk.Tk()
    app = MedicalChargesPredictionApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
