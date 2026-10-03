import sqlite3

DB_FILE = "V12_datasets.db"
TABLE = "unsafe_prompts"

conn = sqlite3.connect(DB_FILE)
cur = conn.cursor()

query = "reveal system prompt"  # test phrase
for row in cur.execute(f"SELECT prompt_id, prompt_text FROM {TABLE} WHERE prompt_text MATCH ?", (query,)):
    print(row)
conn.close()
