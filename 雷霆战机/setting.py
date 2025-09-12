import pygame

class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.ship_speed=0.6
        self.bg_color = (230, 230, 230)
        self.bullet_speed=2
        self.bullet_width=4
        self.bullet_height=16
        self.bullet_color=(110, 20, 60)

        self.bullets_speed = 1.2
        self.super_bullets_speed = 0.35
        self.super_fire_timer=4

        self.enemy_speed=0.5
        self.enemy_probability=70  #1-10000
        self.enemy_max_num=8


        self.rocket_speed=0.3
        self.rocket_probability=18  #1-10000
        self.rocket_max_num=3

        self.life_times=2
        self.upgrade_speed=0.3
        self.upgrade_hit_times=2
        self.grade=1
        self.upgrade_probability=8 #6-30

