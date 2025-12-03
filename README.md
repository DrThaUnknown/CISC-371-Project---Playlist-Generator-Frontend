# CISC 371 Project - Playlist Generator Frontend

Playlist generator application. Users can select an activity (Gym, Study, Running, etc.) and view a generated playlist.

Built with CustomTkinter.

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

- `main.py` - Main application file with GUI template
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
- **Backend Ready**: Placeholder method ready for backend API integration

### Theme Customization

Change appearance mode in `main.py`:
```python
ctk.set_appearance_mode("dark")  # "dark", "light", or "system"
ctk.set_default_color_theme("blue")  # "blue", "green", or "dark-blue"
```

### Future Backend Connection

When ready to connect to backend, install requests:
```bash
pip install requests
```

Then implement the `connect_to_backend()` method in `main.py`.

## Resources

- [CustomTkinter Documentation](https://customtkinter.tomschimansky.com/)
- [CustomTkinter GitHub](https://github.com/TomSchimansky/CustomTkinter)
- [CustomTkinter Examples](https://github.com/TomSchimansky/CustomTkinter/wiki/Examples)
