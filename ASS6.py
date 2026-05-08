# ----------------------------------------
# Medical Expert System
#
# Symptoms are used to identify disease
# based on predefined rules.
# ----------------------------------------


class ExpertSystem:

    def diagnose(self, symptoms):

        # Rule Base

        if "fever" in symptoms and "cough" in symptoms:

            return "Possible Disease: Flu"

        elif "fever" in symptoms and "headache" in symptoms:

            return "Possible Disease: Malaria"

        elif "chest pain" in symptoms and "shortness of breath" in symptoms:

            return "Possible Disease: Heart Disease"

        elif "thirst" in symptoms and "fatigue" in symptoms:

            return "Possible Disease: Diabetes"

        else:

            return "Disease Not Found"


# Create Expert System
system = ExpertSystem()

# User Input
print("Enter Symptoms Separated by Comma\n")

userSymptoms = input("Symptoms: ").lower()

# Convert input into list
symptoms = userSymptoms.split(",")

# Remove extra spaces
symptoms = [s.strip() for s in symptoms]

# Diagnosis
result = system.diagnose(symptoms)

print("\nExpert System Result:")
print(result)