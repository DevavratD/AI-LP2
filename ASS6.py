# -----------------------------------------
# Medical Expert System
#
# Uses symptoms to predict disease
# based on rule matching.
# -----------------------------------------


class ExpertSystem:

    def __init__(self):

        # Knowledge Base
        self.diseases = {

            "Flu": [
                "fever",
                "cough",
                "cold",
                "body pain"
            ],

            "Malaria": [
                "fever",
                "headache",
                "vomiting",
                "sweating"
            ],

            "Diabetes": [
                "thirst",
                "fatigue",
                "weight loss"
            ],

            "Heart Disease": [
                "chest pain",
                "shortness of breath",
                "fatigue"
            ]
        }

    # Inference Engine
    def diagnose(self, symptoms):

        bestMatch = None
        maxScore = 0

        # Check every disease
        for disease, diseaseSymptoms in self.diseases.items():

            score = 0

            # Count matching symptoms
            for symptom in symptoms:

                if symptom in diseaseSymptoms:
                    score += 1

            # Find highest match
            if score > maxScore:

                maxScore = score
                bestMatch = disease

        # Result
        if bestMatch:

            return bestMatch, maxScore

        return None, 0


# Create Expert System
system = ExpertSystem()

print("Enter Symptoms Separated by Comma\n")

# User Input
userInput = input("Symptoms: ").lower()

# Convert to List
symptoms = userInput.split(",")

# Remove Spaces
symptoms = [s.strip() for s in symptoms]

# Diagnosis
disease, score = system.diagnose(symptoms)

# Output
print("\nExpert System Result:\n")

if disease:

    print("Possible Disease:", disease)

    print("Matching Symptoms:", score)

else:

    print("Disease Not Found")