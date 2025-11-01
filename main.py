import customtkinter as ctk
from tkinter import messagebox


class PlaylistGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Playlist Generator")
        self.root.geometry("900x700")
        
        # Set theme and color
        ctk.set_appearance_mode("dark")  # Modes: "dark", "light", "system"
        ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"
        
        # Activity categories
        self.activities = [
            "Gym Workout",
            "Study Session",
            "Running",
            "Party",
            "Chill/Relax",
            "Focus/Work",
            "Sleep",
            "Road Trip"
        ]
        
        # Setup UI
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the main user interface"""
        # Header
        header_frame = ctk.CTkFrame(self.root, corner_radius=10)
        header_frame.pack(fill="x", padx=20, pady=(20, 10))
        
        title_label = ctk.CTkLabel(
            header_frame, 
            text="🎵 Playlist Generator", 
            font=ctk.CTkFont(size=32, weight="bold")
        )
        title_label.pack(pady=15)
        
        subtitle_label = ctk.CTkLabel(
            header_frame,
            text="Select an activity to generate your perfect playlist",
            font=ctk.CTkFont(size=14),
            text_color="gray70"
        )
        subtitle_label.pack(pady=(0, 15))
        
        # Main content area
        content_frame = ctk.CTkFrame(self.root, corner_radius=10)
        content_frame.pack(fill="both", expand=True, padx=20, pady=(10, 20))
        
        # Activity selection
        activity_label = ctk.CTkLabel(
            content_frame, 
            text="Choose Activity:",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        activity_label.grid(row=0, column=0, sticky="w", padx=20, pady=(20, 10))
        
        self.activity_dropdown = ctk.CTkComboBox(
            content_frame,
            values=self.activities,
            width=400,
            height=40,
            font=ctk.CTkFont(size=14),
            dropdown_font=ctk.CTkFont(size=13),
            state="readonly"
        )
        self.activity_dropdown.set("Select an activity")
        self.activity_dropdown.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="ew")
        
        # Generate button
        generate_btn = ctk.CTkButton(
            content_frame, 
            text="Generate Playlist",
            command=self.generate_playlist,
            height=45,
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color="#1DB954",
            hover_color="#1ed760"
        )
        generate_btn.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="ew")
        
        # Playlist display area
        playlist_label = ctk.CTkLabel(
            content_frame, 
            text="Generated Playlist:",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        playlist_label.grid(row=3, column=0, sticky="w", padx=20, pady=(10, 10))
        
        self.playlist_display = ctk.CTkTextbox(
            content_frame, 
            height=350,
            font=ctk.CTkFont(size=14),
            wrap="word"
        )
        self.playlist_display.grid(row=4, column=0, padx=20, pady=(0, 20), sticky="nsew")
        self.playlist_display.insert("1.0", "No playlist generated yet.\n\nSelect an activity and click 'Generate Playlist' to begin.")
        self.playlist_display.configure(state="disabled")
        
        # Configure grid weight for responsive layout
        content_frame.grid_columnconfigure(0, weight=1)
        content_frame.grid_rowconfigure(4, weight=1)
        
    def generate_playlist(self):
        """Generate playlist based on selected activity"""
        selected_activity = self.activity_dropdown.get()
        
        if selected_activity == "Select an activity":
            messagebox.showwarning("No Activity Selected", "Please select an activity first!")
            return
        
        # Enable editing to update content
        self.playlist_display.configure(state="normal")
        self.playlist_display.delete("1.0", "end")
        
        # Display loading message
        self.playlist_display.insert("end", f"Generating {selected_activity} playlist...\n\n")
        self.root.update()
        
        # TODO: Connect to backend API to get actual playlist
        # For now, show placeholder data
        sample_playlist = self.get_sample_playlist(selected_activity)
        
        # Clear and display the playlist
        self.playlist_display.delete("1.0", "end")
        self.playlist_display.insert("end", f"✓ Playlist Generated for: {selected_activity}\n")
        self.playlist_display.insert("end", "=" * 50 + "\n\n")
        
        for i, song in enumerate(sample_playlist, 1):
            self.playlist_display.insert("end", f"{i}. {song['title']} - {song['artist']}\n")
            self.playlist_display.insert("end", f"   Duration: {song['duration']}\n\n")
        
        self.playlist_display.configure(state="disabled")
    
    def get_sample_playlist(self, activity):
        # Placeholder data - this will come from backend in the future
        playlists = {
            "Gym Workout": [
                {"title": "Mascara", "artist": "Deftones", "duration": "3:45"},
                {"title": "Walk", "artist": "Pantera", "duration": "5:15"},
                {"title": "No Face", "artist": "Drake", "duration": "2:17"},
                {"title": "COME N GO", "artist": "Yeat", "duration": "3:19"},
                {"title": "Sing About Me, I'm Dying Of Thirst", "artist": "Kendrick Lamar", "duration": "12:03"}, ]
        }
        
        # Return playlist for activity, or generic one if not found
        return playlists.get(activity, [
            {"title": "Sample Song 1", "artist": "Artist A", "duration": "3:45"},
            {"title": "Sample Song 2", "artist": "Artist B", "duration": "4:12"},
            {"title": "Sample Song 3", "artist": "Artist C", "duration": "3:58"},
            {"title": "Sample Song 4", "artist": "Artist D", "duration": "4:30"},
            {"title": "Sample Song 5", "artist": "Artist E", "duration": "3:22"},
        ])
        
    def connect_to_backend(self, endpoint, data):
        """
        Placeholder for future backend connection
        
        Args:
            endpoint: API endpoint URL
            data: Data to send to backend
        """
        # Implement backend API calls here
        # Example: requests.post(endpoint, json=data)
        pass


def main():
    root = ctk.CTk()
    app = PlaylistGeneratorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
