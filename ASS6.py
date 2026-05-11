# 1. KNOWLEDGE BASE
# Format: [ [List of Symptoms], "Disease Name", "Advice" ]
knowledge_base = [
    (["fever", "cough", "sneezing"], "Common Cold", "Rest and drink warm fluids"),
    (["fever", "body pain", "headache"], "Flu", "Take paracetamol and rest"),
    (["fever", "joint pain", "rash"], "Dengue", "Visit a hospital immediately"),
    (["fever", "dry cough", "loss of smell"], "COVID-19", "Isolate and get tested"),
    (["stomach pain", "vomiting"], "Infection", "Drink ORS and eat light food")
]

# 2. INFERENCE ENGINE (Logic)
def diagnose(user_symptoms):
    print("\n--- Diagnostic Report ---")
    
    for symptoms, disease, advice in knowledge_base:
        # Check if ALL symptoms of a disease are present in user input
        if all(s in user_symptoms for s in symptoms):
            print(f"Result: {disease}")
            print(f"Advice: {advice}")
            return # Stop after finding the first match

    print("Result: Undetermined")
    print("Advice: Please consult a doctor for a professional checkup.")

# 3. USER INTERFACE
print("Hospital Management Expert System")
print("Enter symptoms separated by commas (e.g. fever, cough, sneezing):")

# Take input and clean it (strip spaces and lowercase)
user_input = [s.strip().lower() for s in input("> ").split(",")]

diagnose(user_input)