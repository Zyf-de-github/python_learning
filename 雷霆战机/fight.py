import sys
import pygame
from setting import Settings
from ship import Ship
from bullet import Bullet
from enemy import Enemy
from explode import Explosion
from button import Button
import random

class Fight:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0),pygame.RESIZABLE)
        self.settings.screen_width=self.screen.get_width()
        self.settings.screen_height=self.screen.get_height()
        pygame.display.set_caption('Fight')
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.game_state=False
        self.play_button = Button(self, 'Play')
        self.AUTO_FIRE_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.AUTO_FIRE_EVENT, int(self.settings.bullets_speed * 1000))  # 每 500 毫秒触发一次事件


    def run_game(self):
        while True:
                self.check_events()
                if self.game_state:
                    self.ship.update()
                    self.bullets.update()
                    self.enemies_coming()
                    self.enemies.update()
                self.update_screen()
                self.clean_up()
                self.check_collisions()
                self.explosions.update()
                self.losing_game()


    def losing_game(self):
        if pygame.sprite.spritecollideany(self.ship, self.enemies):
            self.ship.life_times -= 1
            # print('Game Over')
            for enemy in self.enemies:
                # 在敌人位置创建爆炸
                explosion = Explosion(enemy.rect.center, self)
                self.explosions.add(explosion)
            explosion = Explosion(self.ship.rect.center, self)
            self.explosions.add(explosion)
            self.enemies.empty()
            self.ship.__init__(self)
            if self.ship.life_times < 0:
                self.game_state=False
                pygame.mouse.set_visible(True)



    def clean_up(self):
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            for enemy in self.enemies.copy():
                if enemy.rect.bottom >= self.settings.screen_height:
                    self.enemies.remove(enemy)
            print('子弹数量:'+str(len(self.bullets))+' 敌机数量:'+str(len(self.enemies)))

    def check_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)

        # 为每个被击中的敌人创建爆炸效果
        for bullet, hit_enemies in collisions.items():
            for enemy in hit_enemies:
                # 在敌人位置创建爆炸
                explosion = Explosion(enemy.rect.center, self)
                self.explosions.add(explosion)

    def check_events(self):
        for event in pygame.event.get():
            # 退出游戏
            if event.type == pygame.QUIT:
                sys.exit()

            # 鼠标点击开始按钮
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.play_button.rect.collidepoint(mouse_pos):
                    pygame.mouse.set_visible(False)
                    self.game_state = True

            # 按键松开 0 退出
            elif event.type == pygame.KEYUP and event.key == pygame.K_0:
                sys.exit()

            # 游戏进行中才响应键盘事件
            if self.game_state:
                # 按键按下
                if event.type == self.AUTO_FIRE_EVENT:
                    self.fire_bullet()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                    elif event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                    elif event.key == pygame.K_UP:
                        self.ship.moving_up = True
                    elif event.key == pygame.K_DOWN:
                        self.ship.moving_down = True

                # 按键抬起
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.ship.moving_left = False
                    elif event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    elif event.key == pygame.K_UP:
                        self.ship.moving_up = False
                    elif event.key == pygame.K_DOWN:
                        self.ship.moving_down = False

    def enemies_coming(self):
        temp = random.randint(1, 30000)
        if temp < 100:
            new_enemy = Enemy(self)
            self.enemies.add(new_enemy)


    def fire_bullet(self):
        new_bullet = Bullet(self,0,0)
        new_bullet_left = Bullet(self, -20,20)  # 向左偏移20像素
        new_bullet_right = Bullet(self, 20,20)  # 向右偏移20像素
        self.bullets.add(new_bullet, new_bullet_left, new_bullet_right)

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        if not self.game_state:
            self.play_button.draw_button()
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for enemy in self.enemies.sprites():
            enemy.draw_enemy()
        for explosion in self.explosions.sprites():
            explosion.draw(self.screen)  # 使用自定义的draw方法
        pygame.display.flip()



if __name__ == '__main__':
    fight = Fight()
    fight.run_game()