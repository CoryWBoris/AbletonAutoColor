import Live
from ableton.v2.control_surface import ControlSurface

# Dictionary of track names and their corresponding color indices, you can change these to your liking, any Ableton valid character and any number 0 - 69 inclusive
track_colors = {
    "drums": 1,
    "bass": 2,
    "guitar": 3,
    "vocals": 4,
    "synth": 5
}

def assign_track_color(track):
    """Assigns a color to a track based on its name"""
    track_name = track.name
    temp_name = track_name.lower()
    if temp_name in track_colors:
        color_index = track_colors[temp_name]
        track.color_index = color_index

class ColorChanger(ControlSurface):
    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        app = Live.Application.get_application()
        self.doc = app.get_document()
        # Register the listener functions
        self.doc.add_tracks_listener(self.track_added_listener)

        for track in self.doc.tracks:
            track.add_name_listener(self.track_name_changed_listener(track))


    def track_added_listener(self):
        """Listener function called when a new track is added"""
        self.schedule_message(0, self.handle_track_added)

    def handle_track_added(self):
        for track in self.doc.tracks:
            assign_track_color(track)

    def track_name_changed_listener(self, track):
        """Listener function called when a track's name is changed"""
        assign_track_color(track)
