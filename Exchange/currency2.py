from flask import Flask, render_template, request, redirect, url_for
import requests, csv, json
from create_csv import rates, create_csv

app = Flask(__name__)


def calculate(currency, amount):
    create_csv(rates)
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
