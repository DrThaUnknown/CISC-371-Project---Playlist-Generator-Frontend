# CISC 371 Project - Playlist Generator Frontend

Playlist generator application. Users can enter an activity (Gym, Study, Running, etc.) and view a generated playlist powered by the Last.fm API.

Built with Flask, HTML, CSS, and JavaScript.

## Setup

Install dependencies:
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install customtkinter
```

## Running the Application

```bash
flask run
```

## Project Structure

- `app.py` - Main application file with the flask backend
- `app.js` - JS code for better Web-App animations and flow
- `style.css` - Custom CSS code
- `index.html` - Main page of the Web-App
- `about.html` - An about page about the project
- `README.md` - This file

## Features

- **Activity Selection**: Choose from 8 different activities:
  - Gym Workout
  - Study Session
  - Running
  - Party
  - Chill/Relax
  - Focus/Work
  - Sleep
  - Road Trip

- **Playlist Generation**: Click "Generate Playlist" to create a playlist for your selected activity
- **Playlist Display**: View generated songs with title, artist, and duration
- **Modern UI**: Dark theme with smooth animations and rounded corners
- **Backend Ready**: backend API integrated



## Resources

- [CustomTkinter Documentation](https://customtkinter.tomschimansky.com/)
- [CustomTkinter GitHub](https://github.com/TomSchimansky/CustomTkinter)
- [CustomTkinter Examples](https://github.com/TomSchimansky/CustomTkinter/wiki/Examples)
