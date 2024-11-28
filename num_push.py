import pyxel
import random

# 画面の大きさ
WINDOW_HEIGHT = 160
WINDOW_WIDTH = 160

# 表のマスの数
GRID_SIZE = 4
# 各マスの大きさ
CELL_SIZE = 9
# 最大の値
MAX_NUM = GRID_SIZE * GRID_SIZE


# 表の開始位置
START_POS_X = 60
START_POS_Y = 30

class MixedNumberGame:
    def __init__(self):
        pyxel.init(WINDOW_WIDTH, WINDOW_HEIGHT, title="Mixed Number Game")
        self.reset_game()
        self.load_images()
        self.init_sounds()
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def reset_game(self):
        """ゲームの状態をリセット"""
        self.numbers = list(range(1, MAX_NUM + 1))  # 1~16のリスト
        random.shuffle(self.numbers)  # 数字をランダムに並べる
        self.current_number = 1  # プレイヤーが押すべき現在の数字
        self.error_message = ""  # エラーメッセージ

        # 各マスに表示するタイプ（0: 数字, 1: 漢数字）をランダムに決定
        self.display_types = [random.choice([0, 1]) for _ in range(16)]


    def load_images(self):
        """画像を読み込む（Pyxelエディタで事前に設定）"""
        # 画像バンク0に画像を登録している前提
        pyxel.load("number.pyxres")  # 数字のスプライト

    def init_sounds(self):
        """効果音を初期化"""
        pyxel.sound(0).set("c3e3g3", "t", "7", "n", 10)  # 正解音
        pyxel.sound(1).set("g2c2", "t", "7", "n", 20)  # 間違い音

    def update(self):
        """ゲームの状態を更新"""
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            mouse_x = pyxel.mouse_x
            mouse_y = pyxel.mouse_y

            # クリックされたマスを特定
            col = (mouse_x - START_POS_X) // CELL_SIZE
            row = (mouse_y - START_POS_Y) // CELL_SIZE
            if 0 <= col < GRID_SIZE and 0 <= row < GRID_SIZE:
                index = row * GRID_SIZE + col
                clicked_number = self.numbers[index]

                # 数字が正しい場合
                if clicked_number == self.current_number:
                    pyxel.play(0, 0)  # 正解音を再生
                    self.current_number += 1
                    self.error_message = ""
                    if self.current_number > MAX_NUM:
                        self.error_message = "You Win! Press R to Restart"
                
                # 間違えた場合
                elif clicked_number != self.current_number:
                    pyxel.play(1, 1)  # 間違い音を再生
                    self.error_message = "Wrong! Try Again."

        # リセットキー（Rキー）を押した場合
        if pyxel.btnp(pyxel.KEY_R):
            self.reset_game()

    def draw(self):
        """画面を描画"""
        pyxel.cls(0)  # 背景を黒にする

        # グリッドを描画
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                x = col * CELL_SIZE + START_POS_X
                y = row * CELL_SIZE + START_POS_Y
                index = row * GRID_SIZE + col
                number = self.numbers[index]
                display_type = self.display_types[index]

                # 上と左の枠線だけ特定条件で描画
                if col == 0:  # 最左列は左の枠線を描画
                    pyxel.line(x, y, x, y + CELL_SIZE, pyxel.COLOR_ORANGE)
                if row == 0:  # 最上行は上の枠線を描画
                    pyxel.line(x, y, x + CELL_SIZE, y, pyxel.COLOR_ORANGE)
                # 右の枠線を描画
                pyxel.line(x + CELL_SIZE, y, x + CELL_SIZE, y + CELL_SIZE, pyxel.COLOR_ORANGE)
                # 下の枠線を描画
                pyxel.line(x, y + CELL_SIZE, x + CELL_SIZE, y + CELL_SIZE, pyxel.COLOR_ORANGE)

                # 数字または漢数字を描画
                if display_type == 0:
                    # 数字のスプライトを表示
                    tile_x = ((number - 1) % 4) * 8
                    tile_y = ((number - 1) // 4) * 8
                else:
                    # 漢数字のスプライトを表示
                    tile_x = ((number - 1) % 4) * 8
                    tile_y = ((number - 1) // 4) * 8 + 32 
                pyxel.blt(x + 1, y + 1, 0, tile_x, tile_y, 8, 8, pyxel.COLOR_CYAN)

        # 現在の状態を表示
        pyxel.text(START_POS_X - 7, START_POS_Y - 7, f"Next: {self.current_number}", pyxel.COLOR_YELLOW)

        # エラーメッセージの表示
        if self.error_message:
            pyxel.text(10, 80, self.error_message, pyxel.COLOR_RED)


# ゲームの実行
MixedNumberGame()
