import fitz
import json
import os

TOPIC_KEYWORDS = {
    "Percentages": ["percent", "%", "percentage"],
    "Time and Work": ["men", "work", "days", "hours", "together", "alone", "complete"],
    "Profit and Loss": ["profit", "loss", "cost price", "selling price", "gain"],
    "Ratios and Proportions": ["ratio", "proportion", "divided", "share"],
    "Averages": ["average", "mean"],
    "Simple Interest": ["simple interest", "principal", "rate", "interest"],
    "Compound Interest": ["compound interest", "amount", "compounded"],
    "Time and Distance": ["speed", "distance", "train", "km/hr"],
    "Boats and Streams": ["boat", "stream", "current", "upstream", "downstream"],
    "Mixtures and Alligations": ["mixture", "milk", "solution", "water"],
    "Pipes and Cisterns": ["pipe", "cistern", "tank", "filled", "emptied"],
    "Problems on Ages": ["age", "years ago", "older", "younger"]
}

def detect_topic(text):
    text = text.lower()
    for topic, keywords in TOPIC_KEYWORDS.items():
        if any(k in text for k in keywords):
            return topic
    return "General"

def extract_questions(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()

    # Split questions using blank lines as separator
    raw_questions = full_text.strip().split("\n\n")

    structured_questions = []

    for block in raw_questions:
        lines = [line.strip() for line in block.strip().split("\n") if line.strip()]
        if not lines:
            continue

        question_text = ""
        options = []
        answer = ""
        explanation = ""
        found_explanation = False

        for i, line in enumerate(lines):
            lower_line = line.lower()

            if lower_line.startswith("answer"):
                answer = line.split("–")[-1].strip()

            elif lower_line.startswith("explanation"):
                # Get all lines after 'Explanation:'
                explanation_lines = lines[i + 1:]
                explanation = " ".join(explanation_lines).strip()
                found_explanation = True
                break  # Done parsing

            elif line[:2].upper() in {"A.", "B.", "C.", "D."}:
                options.append(line.strip())

            else:
                question_text += line + " "

        if question_text and options and answer:
            structured_questions.append({
                "question": question_text.strip(),
                "options": options,
                "answer": answer,
                "explanation": explanation
            })

    return structured_questions

def save_questions(questions, out_path="data/questions.json"):
    os.makedirs("data", exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(questions, f, indent=2)

if __name__ == "__main__":
    path = r".\Placement-Aptitude-Preparation\Aptitude Questions\Accenture\Accenture-Aptitude-Questions-and-Answers (1).pdf"
    questions = extract_questions(path)
    save_questions(questions)
    print(f"Parsed {len(questions)} questions successfully.")
