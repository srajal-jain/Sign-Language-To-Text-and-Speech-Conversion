import matplotlib.pyplot as plt

# Data for the table
classes = ['Class A', 'Class B', 'Class C', 'Class D', 'Class E', 'Class F']
accuracy = [0.95, 0.89, 0.92, 0.93, 0.96, 0.88]
precision = [0.92, 0.86, 0.91, 0.88, 0.94, 0.82]
recall = [0.97, 0.92, 0.94, 0.95, 0.97, 0.91]
f1_score = [0.94, 0.89, 0.92, 0.91, 0.95, 0.86]

# Plotting the metrics
plt.figure(figsize=(10, 6))

plt.plot(classes, accuracy, marker='o', label='Accuracy')
plt.plot(classes, precision, marker='o', label='Precision')
plt.plot(classes, recall, marker='o', label='Recall')
plt.plot(classes, f1_score, marker='o', label='F1 Score')

plt.title('Sign Language Detection Metrics')
plt.xlabel('Classes')
plt.ylabel('Score')
plt.legend()

plt.xticks(rotation=45)
plt.ylim([0, 1])

plt.grid(True)
plt.tight_layout()

plt.show()
