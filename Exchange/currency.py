from flask import Flask, render_template, request, redirect, url_for
import requests, csv, json
import csv_create

app = Flask(__name__)


with open('rates.csv', 'r') as csvfile:
    for line in csvfile.read().splitlines():
        print(line)

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()[0]
rates = data['rates']
f = open('rates.csv', 'w')
w = csv.writer(f, delimiter=';')
w.writerows([r.values() for r in rates])
f.close()

def calculate(currency, amount):
    amounts = int(amount)
    for i in rates:
        values = [i["currency"], i["code"], i["bid"], i["ask"]]
        if values[1] == currency:
            return (amounts * i["ask"])

@app.route("/", methods=["GET", "POST"])
def currency():
    if request.method == "POST":
        datas = request.form
        currency = datas.get('currency')
        amount = datas.get("quantity")
        ask = calculate(currency, amount)
        return render_template("currency.html", ask=ask)

    return render_template("currency.html")


if __name__ == '__main__':
    app.run(debug=True)
