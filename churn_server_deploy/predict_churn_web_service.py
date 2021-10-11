from flask import Flask
from flask import request
from flask import jsonify
import pickle

#customer = {"contract": "two_year", "tenure": 1, "monthlycharges": 10}

model_file = 'model2.bin'
dv_file = 'dv.bin'

with open(model_file, 'rb') as f_model:
    model = pickle.load(f_model)

with open(dv_file, 'rb') as f_dv:
    dv = pickle.load(f_dv)

app = Flask('churn')

@app.route('/churn' , methods=['POST'])
def churn():
    customer = request.get_json()
    X = dv.transform([customer])
    p_hat = model.predict_proba(X)[0, 1]
    y_hat = p_hat >= 0.5

    result = {'churn_probbility' : float(p_hat) , 'churn_prediction' : bool(y_hat)}

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
