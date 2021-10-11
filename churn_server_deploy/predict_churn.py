#!/usr/bin/env python

import pickle

model_file = '/home/brady/environments/model_deploy/model1.bin'
dv_file = '/home/brady/environments/model_deploy/dv.bin'

#customer = {"contract": "two_year", "tenure": 12, "monthlycharges": 19.7}
customer = {"contract": "two_year", "tenure": 1, "monthlycharges": 10}
#customer = {"contract": "two_year", "tenure": 12, "monthlycharges": 10}

with open(model_file, 'rb') as f_model:
    model = pickle.load(f_model)
    
with open(dv_file, 'rb') as f_dv:
    dv = pickle.load(f_dv)


X = dv.transform([customer])  ## apply the one-hot encoding feature to the customer data 
p_hat = model.predict_proba(X)[0, 1]
print(f"Customer properties are: \n {customer} \n \n Probability of churn: {p_hat}")  

