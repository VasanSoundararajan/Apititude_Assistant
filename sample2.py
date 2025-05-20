import fitz  # PyMuPDF
import json
import os
import re

PDF_PATH = r".\Placement-Aptitude-Preparation\Aptitude Questions\Accenture\Accenture-Aptitude-Questions-and-Answers (1).pdf"
OUTPUT_PATH = "data/questions.json"
import fitz  # PyMuPDF

def extract_structured_questions(pdf_path):
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


print(extract_structured_questions(PDF_PATH))