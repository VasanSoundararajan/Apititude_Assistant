import os

def explain_concept(topic):
    topic_file = f"concepts/{topic.lower().replace(' ', '_')}.txt"
    if os.path.exists(topic_file):
        with open(topic_file) as f:
            return f.read()
    return "No concept explanation available for this topic."
