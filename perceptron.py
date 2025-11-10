# perceptron for 3 input OR/AND/NOR/NAND gate

import numpy as np
from sklearn.metrics import accuracy_score,confusion_matrix ,classification_report

# --- Sigmoid functions ---
def sigmoid_function(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivatives(x):
    return x * (1 - x)

# --- Training data ---
inputs = np.array([
    [0, 0, 0],
    [0, 0, 1],
    [0, 1, 0],
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 1]
])

lst = [
    [0, 1, 1, 1, 1, 1, 1, 1],  # OR
    [0, 0, 0, 0, 0, 0, 0, 1],  # AND
    [1, 0, 0, 0, 0, 0, 0, 0],  # NOR
    [1, 1, 1, 1, 1, 1, 1, 0]   # NAND
]

outputs = np.array(lst)

# --- Choose logic gate ---
choice = input('Enter for which you want to train OR/AND/NOR/NAND: ').upper()
if choice == 'OR':
    r = 0
elif choice == 'AND':
    r = 1
elif choice == 'NOR':
    r = 2
elif choice == 'NAND':
    r = 3
else:
    print('Invalid Choice.')
    exit()

# --- Initialize weights, bias, learning rate ---
weights = np.random.uniform(-1, 1, 3)
bias = np.random.uniform(-1, 1, 1)
learning_rate = 0.5

# --- Training loop ---
epoch = 0
while True:
    total_error = 0
    for i in range(len(inputs)):
        weighted_sum = np.dot(inputs[i], weights) + bias
        sigmoid_output = sigmoid_function(weighted_sum)

        # Calculate error and update
        error = outputs[r][i] - sigmoid_output
        delta = learning_rate * error * sigmoid_derivatives(sigmoid_output)

        weights += inputs[i] * delta
        bias += delta
        total_error += abs(error)

    epoch += 1
    if total_error < 0.01 or epoch > 10000:  # Fast convergence
        break

print("\n--- Training Complete ---")
print(f"Epochs: {epoch}")
print(f"Trained Weights: {weights}")
print(f"Trained Bias: {bias}\n")

result = []
# --- Testing section (no threshold, raw sigmoid) ---
def test_perceptron(test_inputs):
    print(f"Testing {choice} Perceptron (raw sigmoid outputs):\n")
    for x in test_inputs:
        weighted_sum = np.dot(x, weights) + bias
        sigmoid_output = sigmoid_function(weighted_sum)
        x = 1 if sigmoid_output>0.5 else 0
        result.append(x)
        print(f"Input: {x} -> Weighted sum: {weighted_sum[0]:.2f}, Sigmoid: {sigmoid_output[0]:.4f}")

# --- Test data ---
test_inputs = np.array([
    [0, 0, 0],
    [0, 1, 1.5],
    [1, 0.5, 1],
    [1, 1.2, 0],
    [1, 1, 1]
])
test_outputs = np.array([[0,1,1,1,1],[0,0,0,0,1],[1,0,0,0,0],[1,1,1,1,0]])



test_perceptron(test_inputs)
print(result)

accuracy = accuracy_score(test_outputs[r],result)
confutionMatrix = confusion_matrix(test_outputs[r],result)
classificationReport = classification_report(test_outputs[r],result)
print(accuracy)
print(confutionMatrix)
print(classificationReport)
