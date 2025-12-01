from flask import Flask, render_template, request
import requests
import random

app = Flask(__name__)

# --- CONFIGURATION ---
# This is your actual Last.fm API Key
API_KEY = "af2a4028ec8fa7d52bcf4d46e5b3c198"
USER_AGENT = "CISC 371 App"

def get_songs_from_api(activity):
    """
    Fetches top songs for a specific activity from Last.fm
    """
    # 1. Map user input to Last.fm tags
    # (Last.fm uses specific tags like 'workout', 'study', 'chill')
    tag_map = {
        "gym": "workout",
        "workout": "workout",
        "lifting": "workout",
        "cardio": "running",
        "studying": "study",
        "study": "study",
        "focus": "focus",
        "relaxing": "chill",
        "sleep": "sleep",
        "party": "party",
        "commuting": "road trip"
    }
    
    # Use the mapped tag, or default to what the user typed
    search_tag = tag_map.get(activity.lower(), activity)

    # 2. Last.fm API URL
    url = "http://ws.audioscrobbler.com/2.0/"
    params = {
        'method': 'tag.gettoptracks',
        'tag': search_tag,
        'api_key': API_KEY,
        'format': 'json',
        'limit': 50  # Fetch top 50 so we can shuffle them
    }
    headers = {'user-agent': USER_AGENT}

    try:
        response = requests.get(url, params=params, headers=headers)
        data = response.json()

        results = []
        if 'tracks' in data and 'track' in data['tracks']:
            for track in data['tracks']['track']:
                # Format: "Song Name - Artist"
                song_str = f"{track['name']} - {track['artist']['name']}"
                results.append(song_str)
        
        # 3. Return 5 random songs from the top 50 (so it feels fresh every time)
        if results:
            return random.sample(results, k=min(5, len(results)))
        return []

    except Exception as e:
        print(f"API Error: {e}")
        return []

@app.route('/', methods=['GET', 'POST'])
def home():
    playlist = []
    activity = ""
    error = None
    
    if request.method == 'POST':
        activity = request.form.get('activity')
        
        # CALL THE API instead of reading the JSON file
        playlist = get_songs_from_api(activity)
        
        if not playlist:
            error = "No songs found for that activity. Try 'gym', 'study', or 'party'."

    return render_template('index.html', playlist=playlist, activity=activity, error=error)

if __name__ == '__main__':
    app.run(debug=True)