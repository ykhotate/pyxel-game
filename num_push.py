import pyxel
import random

START_POS_X = 60
START_POS_Y = 30

class MixedNumberGame:
    def __init__(self):
        pyxel.init(160, 160, title="Mixed Number Game")
        self.grid_size = 4  # マスの数（4x4）
        self.cell_size = 9  # 各マスのサイズ
        self.reset_game()
        self.load_images()
        self.init_sounds()
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def reset_game(self):
        """ゲームの状態をリセット"""
        self.numbers = list(range(1, 17))  # 1~16のリスト
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
            col = (mouse_x - START_POS_X) // self.cell_size
            row = (mouse_y - START_POS_Y) // self.cell_size
            if 0 <= col < self.grid_size and 0 <= row < self.grid_size:
                index = row * self.grid_size + col
                clicked_number = self.numbers[index]

                # 数字が正しい場合
                if clicked_number == self.current_number:
                    pyxel.play(0, 0)  # 正解音を再生
                    self.current_number += 1
                    self.error_message = ""
                    if self.current_number > 16:
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
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                x = col * self.cell_size + START_POS_X
                y = row * self.cell_size + START_POS_Y
                index = row * self.grid_size + col
                number = self.numbers[index]
                display_type = self.display_types[index]

                # 上と左の枠線だけ描画
                if col == 0:  # 最左列は左の枠線を描画
                    pyxel.line(x, y, x, y + self.cell_size, pyxel.COLOR_ORANGE)
                if row == 0:  # 最上行は上の枠線を描画
                    pyxel.line(x, y, x + self.cell_size, y, pyxel.COLOR_ORANGE)
                # 右の枠線を描画
                pyxel.line(x + self.cell_size, y, x + self.cell_size, y + self.cell_size, pyxel.COLOR_ORANGE)
                # 下の枠線を描画
                pyxel.line(x, y + self.cell_size, x + self.cell_size, y + self.cell_size, pyxel.COLOR_ORANGE)

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
