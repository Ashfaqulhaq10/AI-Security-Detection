import cv2
import pytesseract
import sqlite3
import os

# --- Step 1: Image path ---
image_path = "DEMO.png"
if not os.path.exists(image_path):
    raise FileNotFoundError(f"Image not found: {image_path}")

# --- Step 2: Load image with OpenCV ---
img = cv2.imread(image_path)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Mild contrast enhancement
gray = cv2.convertScaleAbs(gray, alpha=1.2, beta=0)  # slightly increase contrast

# Optional: resize if text is very small
# height, width = gray.shape
# gray = cv2.resize(gray, (width*2, height*2), interpolation=cv2.INTER_CUBIC)

# Optional: skip thresholding if background is uniform

# --- Step 3: OCR with Pytesseract ---
custom_config = r'--oem 3 --psm 6 -l eng'
text = pytesseract.image_to_string(gray, config=custom_config)

# Clean text
text = "\n".join([line.strip() for line in text.splitlines() if line.strip()])

print("Extracted Text:\n")
print(text)
print("-"*50)

# --- Step 4: Save to SQLite ---
db_path = "data.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS extracted_text (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    image_name TEXT,
    extracted_text TEXT
)
""")

cursor.execute(
    "INSERT INTO extracted_text (image_name, extracted_text) VALUES (?, ?)",
    (image_path, text)
)

conn.commit()
conn.close()

print(f"✅ Extracted text saved to '{db_path}'")
