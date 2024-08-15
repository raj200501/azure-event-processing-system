import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load and preprocess the data
data = pd.read_csv('events.csv')
X = data.drop('event_type', axis=1)
y = data['event_type']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForest model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Save the model to a file
joblib.dump(model, 'event_classifier.pkl')

print("Model training completed and saved.")
