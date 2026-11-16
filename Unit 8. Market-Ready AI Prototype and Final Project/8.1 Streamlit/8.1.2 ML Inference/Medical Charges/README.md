# Medical Charges Prediction App

Predict medical insurance charges based on patient characteristics using a trained machine learning model.

---

## 🚀 Quick Start

```bash
python3 app_simple.py
```

The app opens instantly. No installation needed if you have Python 3.7+.

---

## 📋 What You Need

### Minimum
- Python 3.7+
- Dependencies: `pip3 install -r requirements.txt`

### Or use launcher
- **Mac:** Double-click `run.command`
- **Windows:** Double-click `run.bat`

---

## 📖 Guides

| Document | Purpose |
|----------|---------|
| **QUICK_START_GUIDE.md** | Get running in 30 seconds |
| **BUILD_EXECUTABLE_PYINSTALLER.md** | Create standalone executable |

---

## 🎯 How to Use

1. Launch the app
2. Enter patient information:
   - Age (0-120)
   - Sex (Male/Female)
   - BMI (Body Mass Index)
   - Number of children
   - Smoker status (Yes/No)
   - Region (NE/NW/SE/SW)

3. Click **"Predict"**
4. View result: `Predicted: $XXXX.XX`

---

## 📁 Files

```
Medical Charges/
├── app_simple.py                        ← Main application
├── regression_model.pkl                 ← ML model
├── requirements.txt                     ← Dependencies
├── run.command                          ← Mac launcher
├── run.bat                              ← Windows launcher
├── README.md                            ← This file
├── QUICK_START_GUIDE.md                 ← Getting started
└── BUILD_EXECUTABLE_PYINSTALLER.md      ← Build executable
```

---

## 🔧 Installation

```bash
# Install dependencies
pip3 install -r requirements.txt

# Or manually
pip3 install joblib pandas scikit-learn
```

---

## 💻 Build Standalone Executable

Create an app that works without Python installed:

```bash
python -m pip install pyinstaller
pyinstaller --onefile --windowed app_simple.py
```

Details: See `BUILD_EXECUTABLE_PYINSTALLER.md`

---

## ⚡ Features

✅ Simple GUI (Tkinter)  
✅ Fast predictions  
✅ Professional formatting  
✅ Cross-platform (Mac/Windows/Linux)  
✅ Error handling  
✅ No internet required  

---

## 🛠️ Troubleshooting

**"Python not found"**
→ Use `python3` instead of `python`

**"Module not found"**
→ Run `pip3 install -r requirements.txt`

**"Model not found"**
→ Ensure `regression_model.pkl` is in the same folder

**More help:**
→ See `BUILD_EXECUTABLE_PYINSTALLER.md`

---

## 📊 Model Information

- **Algorithm:** Linear Regression
- **Training Data:** Medical charges dataset
- **Features:** Age, Sex, BMI, Children, Smoker, Region
- **Accuracy:** Model validation performance embedded

---

## 📦 Distribution

After building executable:

```bash
# Copy entire dist folder
cp -r dist/ ~/Desktop/MedicalCharges_App
```

Share `dist/app_simple` with others. Works on any Mac without Python.

---

## 📝 License

This project is provided as-is for educational purposes.

---

**Start now:** Run `python3 app_simple.py` or see `QUICK_START_GUIDE.md` 🎉
