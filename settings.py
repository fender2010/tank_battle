class Settings():
    """A class to store all for Tank Battle!."""

    def __init__(self):
        """Initialize the game's settings."""
        
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        
        # Tank settings
        self.tank_speed_factor = .5
        
        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
