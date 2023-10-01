import pandas
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Importing the dataset and splitting the dataset
dataset = pandas.read_csv('breast_cancer_.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.75, random_state=1)

# Training the model and Predicting
classifier = SVC(C=0.5667, kernel='linear', random_state=0)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
linear_svm_accu = accuracy_score(y_test, y_pred)