# title: Pyxel Survive
# author: yk hotate
# desc: A Pyxel Survival Game
# version: 1.0

import pyxel
import random

# ゲーム定数
SCREEN_WIDTH = 160
SCREEN_HEIGHT = 120
PLAYER_SPEED = 2
ENEMY_SPEED = 1

class SurvivalGame:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="2D Survival Game")
        self.reset_game()
        pyxel.run(self.update, self.draw)

    def reset_game(self):
        self.player_x = SCREEN_WIDTH // 2
        self.player_y = SCREEN_HEIGHT // 2
        self.food_x = random.randint(0, SCREEN_WIDTH - 8)
        self.food_y = random.randint(0, SCREEN_HEIGHT - 8)
        self.enemies = [
            [random.randint(0, SCREEN_WIDTH - 8), random.randint(0, SCREEN_HEIGHT - 8)]
            for _ in range(3)
        ]
        self.score = 0
        self.game_over = False

    def update(self):
        if self.game_over:
            if pyxel.btnp(pyxel.KEY_R):
                self.reset_game()
            return

        # プレイヤーの移動
        if pyxel.btn(pyxel.KEY_W):
            self.player_y = max(0, self.player_y - PLAYER_SPEED)
        if pyxel.btn(pyxel.KEY_S):
            self.player_y = min(SCREEN_HEIGHT - 8, self.player_y + PLAYER_SPEED)
        if pyxel.btn(pyxel.KEY_A):
            self.player_x = max(0, self.player_x - PLAYER_SPEED)
        if pyxel.btn(pyxel.KEY_D):
            self.player_x = min(SCREEN_WIDTH - 8, self.player_x + PLAYER_SPEED)

        # 食べ物を取ったらスコア加算
        if abs(self.player_x - self.food_x) < 8 and abs(self.player_y - self.food_y) < 8:
            self.score += 1
            self.food_x = random.randint(0, SCREEN_WIDTH - 8)
            self.food_y = random.randint(0, SCREEN_HEIGHT - 8)

        # 敵の移動
        for enemy in self.enemies:
            if enemy[0] < self.player_x:
                enemy[0] += ENEMY_SPEED
            elif enemy[0] > self.player_x:
                enemy[0] -= ENEMY_SPEED

            if enemy[1] < self.player_y:
                enemy[1] += ENEMY_SPEED
            elif enemy[1] > self.player_y:
                enemy[1] -= ENEMY_SPEED

            # 敵との接触判定
            if abs(self.player_x - enemy[0]) < 8 and abs(self.player_y - enemy[1]) < 8:
                self.game_over = True

    def draw(self):
        pyxel.cls(0)

        if self.game_over:
            pyxel.text(SCREEN_WIDTH // 2 - 40, SCREEN_HEIGHT // 2, "GAME OVER", pyxel.COLOR_RED)
            pyxel.text(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 10, f"Score: {self.score}", pyxel.COLOR_WHITE)
            pyxel.text(SCREEN_WIDTH // 2 - 60, SCREEN_HEIGHT // 2 + 20, "Press R to Restart", pyxel.COLOR_WHITE)
            return

        # プレイヤーの描画
        pyxel.rect(self.player_x, self.player_y, 8, 8, pyxel.COLOR_CYAN)

        # 食べ物の描画
        pyxel.rect(self.food_x, self.food_y, 8, 8, pyxel.COLOR_YELLOW)

        # 敵の描画
        for enemy in self.enemies:
            pyxel.rect(enemy[0], enemy[1], 8, 8, pyxel.COLOR_RED)

        # スコアの描画
        pyxel.text(5, 5, f"Score: {self.score}", pyxel.COLOR_WHITE)

# ゲームの実行
SurvivalGame()
