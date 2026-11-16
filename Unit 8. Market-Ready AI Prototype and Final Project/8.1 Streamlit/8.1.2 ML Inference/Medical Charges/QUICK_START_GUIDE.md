# Quick Start Guide - Medical Charges Predictor

Get started in seconds. Choose your option below.

---

## Option 1: Run with Python (Fastest)

No compilation needed. Just run:

```bash
python3 app_simple.py
```

The app opens immediately.

---

## Option 2: Run with Shell Script (Mac)

Double-click: `run.command`

The app opens automatically.

---

## Option 3: Run with Batch File (Windows)

Double-click: `run.bat`

The app opens automatically.

---

## Option 4: Build Standalone Executable

See: `BUILD_EXECUTABLE_PYINSTALLER.md`

This creates an executable that works without Python installed.

---

## Installation Requirements

Install dependencies once:

```bash
pip3 install -r requirements.txt
```

Or individually:

```bash
pip3 install joblib pandas scikit-learn
```

---

## App Features

✅ Simple desktop interface  
✅ Input fields for all parameters:
   - Age
   - Sex (Male/Female)
   - BMI
   - Number of Children
   - Smoker Status (Yes/No)
   - Region

✅ Instant prediction results  
✅ Formatted currency output ($)

---

## Troubleshooting

### Python not found
Use: `python3` instead of `python`

### Module not found (joblib, pandas, etc.)
Run: `pip3 install -r requirements.txt`

### Model file not found
Make sure `regression_model.pkl` is in the same folder as `app_simple.py`

---

## Files Included

| File | Purpose |
|------|---------|
| `app_simple.py` | Main application |
| `regression_model.pkl` | Trained ML model |
| `run.command` | Mac launcher |
| `run.bat` | Windows launcher |
| `requirements.txt` | Python dependencies |
| `README.md` | Basic info |
| `QUICK_START_GUIDE.md` | This file |
| `BUILD_EXECUTABLE_PYINSTALLER.md` | Build guide |

---

## Next Steps

1. **Try it:** Run `python3 app_simple.py`
2. **Build it:** Follow `BUILD_EXECUTABLE_PYINSTALLER.md`
3. **Share it:** Copy `dist/app_simple` to others

---

**Questions? Check `BUILD_EXECUTABLE_PYINSTALLER.md` for detailed troubleshooting.** 🎉
