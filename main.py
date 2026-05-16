import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data=pd.read_csv("dataset/loan_prediction_dataset.csv")

data=data.drop(columns=['Employment_Status'])

x=data.drop(columns=['Loan_Approved'])

y=data['Loan_Approved']

model=LogisticRegression()

model.fit(x,y)

prediction=model.predict(x)

print(
    "accuracy:",
    accuracy_score(y,prediction)
)