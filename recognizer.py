import joblib
from sklearn.feature_extraction.text import TfidfVectorizer


def check_gender(name: str) -> str:
    print(name)

    vectorizer = joblib.load("names_vectorizer.joblib")
    model_to_predict = joblib.load('names_gender.joblib')

    prediction = model_to_predict.predict(vectorizer.transform([name]).toarray())
    if prediction is not None:
        return prediction[0]
