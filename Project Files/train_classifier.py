import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
data_dict = pickle.load(open('./data.pickle', 'rb'))
data = np.asarray(data_dict['data'])
labels = np.asarray(data_dict['labels'])

# Split data
x_train, x_test, y_train, y_test = train_test_split(
    data, labels, test_size=0.2, shuffle=True, stratify=labels
)

# Train model
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(x_train, y_train)

# Evaluate
y_pred = model.predict(x_test)
score = accuracy_score(y_pred, y_test)
print(f"Model accuracy: {score * 100:.2f}%")

# Save model
with open('model.p', 'wb') as f:
    pickle.dump({'model': model}, f)

print("Model saved as model.p")
