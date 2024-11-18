import pyxel
import random

# ゲームの定数
SCREEN_WIDTH = 160
SCREEN_HEIGHT = 120
TOWER_COST = 10
ENEMY_SPEED = 0.5
ENEMY_SPAWN_RATE = 60  # フレームごとの敵の生成頻度

class TowerDefenseGame:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="Tower Defense Game")
        self.reset_game()
        pyxel.run(self.update, self.draw)

    def reset_game(self):
        self.towers = []  # タワーのリスト
        self.enemies = []  # 敵のリスト
        self.coins = 20  # 初期コイン数
        self.score = 0  # スコア
        self.frame_count = 0  # フレームカウント

    def spawn_enemy(self):
        """敵をランダムな位置に生成"""
        self.enemies.append({"x": 0, "y": random.randint(0, SCREEN_HEIGHT - 8), "hp": 3})

    def update(self):
        self.frame_count += 1

        # 敵を一定間隔で生成
        if self.frame_count % ENEMY_SPAWN_RATE == 0:
            self.spawn_enemy()

        # プレイヤーがタワーを設置
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and self.coins >= TOWER_COST:
            self.towers.append({"x": pyxel.mouse_x, "y": pyxel.mouse_y})
            self.coins -= TOWER_COST

        # 敵の移動
        for enemy in self.enemies:
            enemy["x"] += ENEMY_SPEED

        # タワーの攻撃
        for tower in self.towers:
            for enemy in self.enemies:
                if abs(tower["x"] - enemy["x"]) < 20 and abs(tower["y"] - enemy["y"]) < 20:
                    enemy["hp"] -= 1
                    if enemy["hp"] <= 0:
                        self.enemies.remove(enemy)
                        self.score += 1
                        self.coins += 5  # コインを獲得

        # 敵がゴールに到達
        self.enemies = [enemy for enemy in self.enemies if enemy["x"] < SCREEN_WIDTH]

    def draw(self):
        pyxel.cls(0)

        # タワーの描画
        for tower in self.towers:
            pyxel.circ(tower["x"], tower["y"], 5, pyxel.COLOR_GREEN)

        # 敵の描画
        for enemy in self.enemies:
            pyxel.rect(enemy["x"], enemy["y"], 8, 8, pyxel.COLOR_RED)

        # スコアとコインの表示
        pyxel.text(5, 5, f"Score: {self.score}", pyxel.COLOR_WHITE)
        pyxel.text(5, 15, f"Coins: {self.coins}", pyxel.COLOR_YELLOW)

        # プレイヤーが設置可能なタワーの範囲表示
        if self.coins >= TOWER_COST:
            pyxel.circ(pyxel.mouse_x, pyxel.mouse_y, 5, pyxel.COLOR_CYAN)

# ゲームを実行
TowerDefenseGame()
