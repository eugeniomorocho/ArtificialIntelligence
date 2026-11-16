# 🚀 Build Standalone Executable with PyInstaller

Create a standalone executable that works on any Mac without Python installed.

---

## Prerequisites

- Python 3.7+
- Virtual environment activated
- Required dependencies installed

---

## Step-by-Step Guide

### Step 1: Install PyInstaller

Open Terminal and run:

```bash
python -m pip install pyinstaller
```

### Step 2: Navigate to Medical Charges folder

```bash
cd /Users/eugenio/Documents/ArtificialIntelligence/"Unit 8. Market-Ready AI Prototype and Final Project"/"8.1 Streamlit"/"8.1.2 ML Inference"/"Medical Charges"
```

### Step 3: Build the executable

```bash
pyinstaller --onefile --windowed app_simple.py
```

---

## Result

Your executable will be created in: **`dist/app_simple`**

### Executable properties:
- ✅ Standalone (no Python required)
- ✅ Works on any Mac
- ✅ Double-click to run
- ✅ File size: ~100-150 MB
- ⏱️ Build time: 1-3 minutes

---

## How to Run

### Option 1: Direct double-click
1. Open Finder → `dist/` folder
2. Double-click `app_simple`
3. App opens immediately

### Option 2: From Terminal
```bash
./dist/app_simple
```

### Option 3: Copy to Desktop
1. Copy `dist/app_simple` to your Desktop
2. Double-click whenever you want to use it

---

## First Time Security Warning (Mac)

If you see a security warning:

1. **Right-click** on the executable
2. Click **"Open"**
3. Confirm in the dialog
4. Now you can use double-click normally

---

## Troubleshooting

### Issue: "pyinstaller: command not found"
**Solution:** Use full path:
```bash
python -m pip install pyinstaller
pyinstaller --onefile --windowed app_simple.py
```

### Issue: "externally-managed-environment"
**Solution:** Activate virtual environment:
```bash
source /Users/eugenio/Documents/ArtificialIntelligence/.venv/bin/activate
python -m pip install pyinstaller
```

### Issue: Model not found
**Solution:** Make sure `regression_model.pkl` is in the same folder as `app_simple.py`

---

## What Gets Built

```
dist/
├── app_simple          ← Your executable (double-click to run)
└── _internal/          ← Libraries and dependencies (auto-managed)
```

---

## Distribution

After building:
- ✅ Share the entire `dist/` folder or just `dist/app_simple`
- ✅ Works on any Mac with the same OS version or newer
- ✅ No Python installation needed on recipient's Mac

---

## Optional: Create an .app bundle (Mac)

For a more native Mac experience:

```bash
pyinstaller --onefile --windowed --osx-bundle-identifier=com.medicalcharges.app app_simple.py
```

This creates `dist/app_simple.app` that looks like a regular Mac application.

---

## Notes

- Build time: First build takes 1-3 minutes, rebuilds are faster
- File size: ~100-150 MB (includes Python runtime and all dependencies)
- Platform-specific: Built on Mac = Mac executable only
- For Windows/Linux: Build on those platforms or use CI/CD

---

**Ready to build? Run Step 1-3 above!** 🎉
