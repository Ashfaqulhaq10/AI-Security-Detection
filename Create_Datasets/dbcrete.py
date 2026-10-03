
import sqlite3
import csv
import os

CSV_FILE = "V12_datasets.csv"      # your CSV input file
DB_FILE = "V12_datasets.db"          # output DB file
TABLE = "unsafe_prompts"             # FTS5 table name

# Delete old DB if present (optional)
if os.path.exists(DB_FILE):
    os.remove(DB_FILE)

# Create SQLite connection
conn = sqlite3.connect(DB_FILE)
cur = conn.cursor()

# Enable FTS5 (ships with modern Python SQLite)
cur.execute(f"""
CREATE VIRTUAL TABLE {TABLE}
USING fts5(prompt_id, prompt_text, tokenize='porter');
""")

# Insert CSV rows
with open(CSV_FILE, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        pid = row.get("prompt_id", "")
        text = row.get("prompt_text", "")
        cur.execute(
            f"INSERT INTO {TABLE} (prompt_id, prompt_text) VALUES (?, ?)",
            (pid, text)
        )

conn.commit()
conn.close()
print(f"✅ Created {DB_FILE} with FTS5 table '{TABLE}' successfully.")
