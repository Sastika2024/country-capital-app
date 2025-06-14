from flask import Flask, render_template, request

app = Flask(__name__)

capital_map = {
    'India': 'New Delhi',
    'Australia': 'Canberra',
    'United States': 'Washington, D.C.',
    'France': 'Paris'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    selected_country = None
    capital = None
    if request.method == 'POST':
        selected_country = request.form['country']
        capital = capital_map.get(selected_country, 'Not Found')
    return render_template('index.html', countries=capital_map.keys(),
                           selected_country=selected_country, capital=capital)

if __name__ == '__main__':
    app.run(debug=True, port=5012)
