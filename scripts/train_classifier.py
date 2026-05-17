import os
import joblib
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Load data
df = pd.read_csv("data/training_data.csv")
print(f"Training on {len(df)} samples")

# Embed
embedder = SentenceTransformer("all-MiniLM-L6-v2")
X = embedder.encode(df["query"].tolist(), show_progress_bar=True)
y = df["label"].tolist()

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
# Train
clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, y_train)

# Evaluate
y_pred = clf.predict(X_test)
print("\n--- Classifier Performance ---")
print(classification_report(y_test, y_pred))

# Save
os.makedirs("models", exist_ok=True)
joblib.dump(clf, "models/router_classifier.pkl")
#joblib.dump(embedder, "models/embedder.pkl")
print("Model saved to models/")