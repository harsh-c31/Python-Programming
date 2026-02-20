import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import warnings

warnings.filterwarnings('ignore')

# Load Titanic dataset
titanic_data = pd.read_csv('titanic.csv')

# Remove rows where target is missing
titanic_data = titanic_data.dropna(subset=['Survived'])

# Select features & target
X = titanic_data[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']]
Y = titanic_data['Survived']

# Encode categorical data
X['Sex'] = X['Sex'].map({'female': 0, 'male': 1})

# Fill missing ages
X['Age'] = X['Age'].fillna(X['Age'].median())

# Train-test split
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Train Random Forest model
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(x_train, y_train)

# Predictions
y_pred = rf_classifier.predict(x_test)

# Metrics
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy:.2f}")
print("\nClassification Report:\n", report)

# Predict one sample
sample = x_test.iloc[0:1]
predict = rf_classifier.predict(sample)

sample_dict = sample.iloc[0].to_dict()
print(f"\nSample Passenger: {sample_dict}")
print(f"Predicted Survival: {'Survived' if predict[0] == 1 else 'Did Not Survive'}")
