from flask import Flask, render_template, request

def convert_currency(amount, rate=1.1):
    return round(amount * rate, 2)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    error = None

    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
            from_currency = request.form['from_currency']
            to_currency = request.form['to_currency']

            # Simple static exchange rates
            rates = {
                ('EUR', 'USD'): 1.1,
                ('USD', 'EUR'): 0.91,
                ('EUR', 'GBP'): 0.86,
                ('GBP', 'EUR'): 1.16,
                ('USD', 'GBP'): 0.78,
                ('GBP', 'USD'): 1.28
            }

            if from_currency == to_currency:
                result = f"{amount} {to_currency}"
            else:
                rate = rates.get((from_currency, to_currency))
                if rate:
                    converted = convert_currency(amount, rate)
                    result = f"{converted} {to_currency}"
                else:
                    error = "Conversión no disponible."

        except ValueError:
            error = "Introduce una cantidad válida."

    return render_template('index.html', result=result, error=error)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
