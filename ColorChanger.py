import Live
from ableton.v2.control_surface import ControlSurface

# Dictionary of track names and their corresponding color indices. You can add as many as you like here, highest number is 69, and you can use any string that you would be allowed to type in Ableton.  
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
        self.previous_track_ids = set(track._live_ptr for track in self.doc.tracks)
        # Register the listener functions
        self.doc.add_tracks_listener(self.tracks_changed_listener)

        for track in self.doc.tracks:
            track.add_name_listener(lambda: self.track_name_changed_listener(track))

    def tracks_changed_listener(self):
        """Listener function called when a track is added or deleted"""
        current_track_ids = set(track._live_ptr for track in self.doc.tracks)
        self.schedule_message(0, lambda: self.handle_track_change(current_track_ids))

    def handle_track_change(self, current_track_ids):
        new_track_id = current_track_ids - self.previous_track_ids
        deleted_track_id = self.previous_track_ids - current_track_ids

        if new_track_id:
            new_track_id = new_track_id.pop()
            new_track = None
            for track in self.doc.tracks:
                if track._live_ptr == new_track_id:
                    new_track = track
                    break
            if new_track is not None:
                assign_track_color(new_track)
                # Attach the event listener to the new track
                new_track.add_name_listener(lambda: self.track_name_changed_listener(new_track))

        self.previous_track_ids = current_track_ids

    def track_name_changed_listener(self, track):
        """Listener function called when a track's name is changed"""
        self.schedule_message(0, lambda: assign_track_color(track))
