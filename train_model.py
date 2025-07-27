# train_model.py
# Train a Random Forest Classifier on the Iris dataset and save the model as model.pkl

import pickle
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)


# Save the trained model to model/model.pkl
with open("model/model.pkl", "wb") as f:
    pickle.dump(clf, f)

print("Model trained and saved as model.pkl")
