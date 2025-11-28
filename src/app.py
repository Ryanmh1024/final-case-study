from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__, template_folder="../templates")

# Load CSV
df = pd.read_csv("assets/graduates.csv")

# Normalize column names (optional but helpful)
df.columns = df.columns.str.strip()

@app.route("/")
def index():
    majors = sorted(df["Education.Major"].unique())
    return render_template("index.html",majors=majors)

@app.route("/data")
def data():
    major = request.args.get("major")

    if not major:
        return jsonify({"years": [], "salaries": []})

    # Filter for selected major
    filtered = df[df["Education.Major"] == major]

    # Remove rows where salaries are zero (no data)
    filtered = filtered[filtered["Salaries.Mean"] > 0]

    years = filtered["Year"].astype(int).tolist()
    salaries = filtered["Salaries.Mean"].astype(float).tolist()

    return jsonify({"years": years, "salaries": salaries})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)