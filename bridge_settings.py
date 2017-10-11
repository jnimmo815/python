class Settings():
    """A class to  store all the bridge bid buddy settings."""
    
    def __init__(self):
        """Initialize the game's static settings."""
        #   Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (40, 255, 70)
        
        #   Card position settings
        self.x_start_pos = 25
        self.y_start_pos = 100
