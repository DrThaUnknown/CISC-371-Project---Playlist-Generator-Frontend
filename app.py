from flask import Flask, render_template, request
import json
import random

app = Flask(__name__)

# --- DATABASE CONNECTION ---
def load_songs():
    try:
        with open('songs.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# --- ROUTE: The Home Page ---
@app.route('/', methods=['GET', 'POST'])
def home():
    playlist = []
    activity = ""
    
    if request.method == 'POST':
        activity = request.form.get('activity')
        data = load_songs()
        
        # Logic to find songs
        key = activity.lower()
        if key in data:
            playlist = random.sample(data[key], k=min(3, len(data[key])))
        else:
            playlist = ["No songs found for that activity."]

    return render_template('index.html', playlist=playlist, activity=activity)

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)