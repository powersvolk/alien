class Settings:

    def __init__(self):

        self.caption_name = "Alien Invasion"
        self.screen_mode = False
        self.screen_width = 700
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        self.ship_limit = 3

        self.bullet_width = 3
        self.bullet_height = 7
        self.bullet_color = (240, 240, 240)
        self.bullets_allowed = 5

        self.star_speed = 1
        self.star_number = 30

        self.fleet_drop_speed = 10

        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 0.3
        self.alien_points = 50

        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale 

        self.alien_points = int(self.alien_points * self.score_scale)  