rules =[
    (["snezzing","runny nose"],"Common Cold"),
    (["fever","body ache","fatigue"],"influenza"),
     (["fever", "cough", "loss of taste or smell"], "covid19"),
    (["cough", "sore throat"], "respiratory_infection")

]


def forward_chaining(symptoms):
    facts = set(symptoms)
    inferred = set()
    change = True
    while change:
        change = False
        for condition,conclution in rules:
            can_fire = True
            for cond in condition:
                if cond not in facts:
                    can_fire=False
                    break
            if can_fire and conclution not in facts:
                facts.add(conclution)
                inferred.add(conclution)
                change = True

    if inferred:
        for f in inferred:
            print(f)
    else:
        print("No disease can be inferred from the symptoms")

def backward_chaining(goal,known_facts):
    if goal in known_facts:
        return True
    for condition ,conclution in rules:
        if conclution==goal:
            can_prove = True
            for x in condition:
                if not backward_chaining(x,known_facts):
                    can_prove=False
                    break
            if can_prove:
                print(f"Goal '{goal}' proven!")
                return True
            
    return False
    

symptoms= []
user_input = input("enter your Symptoms : ").lower()
s = user_input.split(',')
for x in s:
    x = x.strip()
    symptoms.append(x)

print(symptoms)

goal = input("Enter your suspected Diease :")

# forward_chaining(symptoms)
backward_chaining(goal,symptoms)
