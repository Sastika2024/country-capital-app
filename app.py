from flask import Flask, render_template, request

app = Flask(__name__)

# ✅ Country to capital map
capital_map = {
    "India": "New Delhi",
    "Australia": "Canberra",
    "United States": "Washington, D.C.",
    "France":"Paris" # Newly added on 14-06-25
}

@app.route("/", methods=["GET", "POST"])
def index():
    capital = ""
    selected_country = ""

    if request.method == "POST":
        selected_country = request.form.get("country")
        capital = capital_map.get(selected_country, "Unknown")

    return render_template("index.html", capital=capital, countries=capital_map.keys(), selected=selected_country)

if __name__ == "__main__":
    app.run(port=5012, debug=True)
