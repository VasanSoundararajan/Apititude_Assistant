import json
import os

PROGRESS_FILE = "data/progress.json"

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE) as f:
            return json.load(f)
    return {}

def save_progress(progress):
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=2)

def update_progress(q_id, correct):
    progress = load_progress()
    progress[str(q_id)] = {"correct": correct}
    save_progress(progress)

def get_score():
    progress = load_progress()
    total = len(progress)
    correct = sum(1 for p in progress.values() if p["correct"])
    return correct, total
