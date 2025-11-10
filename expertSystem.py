symptopms ={
    "john" : ["snezzing","runny nose"],
    "marry": ["fever","body ache","fatigue"],
    "sam" : ["cough","sore throat"]
}

def has_flu(person_symptoms):
    if "fever" in person_symptoms and "body_ache":
        return True

def has_cold(person_symptoms):
    if "snezzing" in person_symptoms and "runny nose" in person_symptoms:
        return True

def diagonosis(person):
    if person not in symptopms:
        print(f'{person} is not Found')
        return
    
    person_symptoms = symptopms[person]

    if has_cold(person_symptoms):
        print(f'{person} might have cold')
    elif has_flu(person_symptoms):
        print(f'{person} might have flu')
    else:
        print(f'{person} has nothing')
diagonosis('john')
diagonosis("marry")




# class MedicalDiagnosisSystem:
#     def __init__(self):
#         self.symptoms_db = {
#             "john": ["sneezing", "runny nose"],
#             "marry": ["fever", "body ache", "fatigue"],
#             "sam": ["cough", "sore throat"],
#             "alice": ["fever", "cough", "runny nose"]
#         }
        
#         self.rules = {
#             'cold': ["sneezing", "runny nose"],
#             'flu': ["fever", "body ache"],
#             'throat infection': ["cough", "sore throat"],
#             'common cold': ["sneezing", "runny nose", "cough"]
#         }
    
#     def forward_chaining(self, person):
#         """Forward chaining: Symptoms → Diagnosis"""
#         if person not in self.symptoms_db:
#             return f"{person} not found"
        
#         symptoms = self.symptoms_db[person]
#         diagnoses = []
        
#         for disease, required_symptoms in self.rules.items():
#             if all(symptom in symptoms for symptom in required_symptoms):
#                 diagnoses.append(disease)
        
#         return diagnoses
    
#     def backward_chaining(self, person, target_disease):
#         """Backward chaining: Diagnosis → Symptoms verification"""
#         if person not in self.symptoms_db:
#             return f"{person} not found"
        
#         if target_disease not in self.rules:
#             return f"Unknown disease: {target_disease}"
        
#         symptoms = self.symptoms_db[person]
#         required_symptoms = self.rules[target_disease]
#         missing_symptoms = [symptom for symptom in required_symptoms if symptom not in symptoms]
        
#         if not missing_symptoms:
#             return f"✓ {person} likely has {target_disease}"
#         else:
#             return f"✗ {person} does not have {target_disease}. Missing: {', '.join(missing_symptoms)}"
    
#     def comprehensive_diagnosis(self, person):
#         """Combined approach"""
#         print(f"\n=== DIAGNOSIS FOR {person.upper()} ===")
        
#         if person not in self.symptoms_db:
#             print("Patient not found")
#             return
        
#         symptoms = self.symptoms_db[person]
#         print(f"Symptoms: {', '.join(symptoms)}")
        
#         # Forward Chaining
#         print("\nForward Chaining Results:")
#         fc_results = self.forward_chaining(person)
#         if fc_results:
#             for disease in fc_results:
#                 print(f"  - Might have: {disease}")
#         else:
#             print("  - No specific diagnosis found")
        
#         # Backward Chaining for common diseases
#         print("\nBackward Chaining Verification:")
#         common_diseases = ['cold', 'flu', 'throat infection', 'common cold']
#         for disease in common_diseases:
#             result = self.backward_chaining(person, disease)
#             if "likely" in result:
#                 print(f"  {result}")

# # Run comprehensive diagnosis
# print("=== COMPREHENSIVE MEDICAL DIAGNOSIS SYSTEM ===")
# mds = MedicalDiagnosisSystem()

# for person in ["john", "marry", "sam", "alice"]:
#     mds.comprehensive_diagnosis(person)