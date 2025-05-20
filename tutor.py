import json
import random
from concept_explainer import explain_concept
from progress_tracker import update_progress, get_score
from nvidia_chat import nvidia_chat


with open("data/questions.json") as f:
    questions = json.load(f)

def ask_question(q, q_id):
    print("\n---")
    print(f"Q{q_id + 1}: {q['question']}")
    for opt in q["options"]:
        print(opt)

    user_ans = input("Your Answer (A/B/C/D): ").strip().upper()
    correct = q["answer"].strip().upper().endswith(user_ans)
    print("✅ Correct!" if correct else f"❌ Incorrect! Correct Answer: {q['answer']}")
    
    print("\nExplanation:")
    print(q["explanation"])
    
    print("\nAI Explanation:")
    print(nvidia_chat(q['question'], q['answer'], q['explanation']))

    show_concept = input("\nDo you want the concept explained? (y/n): ").strip().lower()
    if show_concept == 'y':
        print("\n📘 Concept:")
        print(explain_concept(q["topic"]))

    update_progress(q_id, correct)

def main():
    print("📚 AI Aptitude Tutor CLI")
    print("------------------------")

    while True:
        print("\nMenu:")
        print("1. Practice Questions")
        print("2. View Score")
        print("3. Exit")

        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            random.shuffle(questions)
            for i, q in enumerate(questions):
                ask_question(q, i)
                cont = input("\nNext? (y/n): ")
                if cont.lower() != 'y':
                    break
        elif choice == "2":
            correct, total = get_score()
            print(f"\n🧾 Your Score: {correct}/{total} ({(correct/total)*100:.1f}%)")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
