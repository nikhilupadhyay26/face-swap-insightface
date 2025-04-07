# face-swap-insightface

1. App Intro
This is a simple but powerful face swapping tool built using InsightFace. It detects faces in an image, swaps in a face from another image, and sharpens the final result for better quality.

It uses a lightweight config file, requires no GPU, and works well on Windows with Python 3.10+.

---

## 🔧 Features

- Detects faces using `insightface` face analysis models
- Swaps a source face into all detected faces in the target image
- Saves both the original swapped and sharpened versions
- Runs on CPU (no GPU required)
- Works via a simple `config.json` file

---

## 🚀 Setup Instructions

### 1. Clone this repository

```bash
git clone https://github.com/your-username/face-swap-insightface.git
cd face-swap-insightface

2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate     # Windows
# source venv/bin/activate  # Mac/Linux


3. Install all required packages
pip install -r requirements.txt


📁 Project Structure
├── face_swap_pipeline.py       # Main script for face swapping and sharpening
├── config.json                 # Configuration file for image paths
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── samay.png                   # Example source face image
├── stud.jpeg                   # Example target image
├── face_swap_result.jpg        # Output: face-swapped result
├── sharpened_output.jpg        # Output: sharpened result



▶️ How to Run
python face_swap_pipeline.py
