import pickle


def load_model():
    with open("src/classifier.pkl", "rb") as f:
        return pickle.load(f)


model = load_model()


def predict_category(gender: str, age: int, annual_income: float) -> str:
    gender_num = 0 if gender.lower() == "male" else 1
    prediction = model.predict([[gender_num, age, annual_income]])
    return "High" if prediction[0] == 1 else "Low"
