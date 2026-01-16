import pandas as pd
import numpy as np 
from sklearn.linear_model import LogisticRegression 
import joblib   

# Charger les données

data = pd.read_csv('data/train_data.csv')

X = data[['Age','Account_Manager','Years','Num_Sites']]

y = data['Churn']

# Entrainement du modele

model = LogisticRegression(max_iter=1000)

model.fit(X,y)

#Sauvegarder le modèle entrainé sur joblib ()
joblib.dump(model,'data/churn_model_clean.pkl')
print ("Modèle de regression logistique entrainé et sauvegardé sous 'churn_model_clean.pkl' ")
