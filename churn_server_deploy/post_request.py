import requests

customer = {"contract": "two_year", "tenure": 12, "monthlycharges": 10}

url = 'http://localhost:9696/churn'

response = requests.post(url, json=customer).json()


if response['churn_prediction'] == True:
    print(f'Churn score: {response["churn_probbility"]} /nSend promo email to: {customer}')
else:
    print(f'Churn score: {response["churn_probbility"]} /nNo need to send promo')



