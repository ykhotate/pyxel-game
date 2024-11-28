from PIL import Image, ImageDraw, ImageFont

def render_text_to_matrix(text, font_path="YuGothM.ttc", font_size=8):
    font = ImageFont.truetype(font_path, font_size)
    # 文字列を描画
    img = Image.new("1", (len(text) * font_size, font_size), color=0)
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), text, font=font, fill=1)

    # ドットパターン取得
    pixels = img.load()
    matrix = []
    for y in range(img.height):
        row = []
        for x in range(img.width):
            row.append("f" if pixels[x, y] else "0")
            # 行の形式を調整: 先頭に '[', 末尾に ']', 文字の間に ','
        formatted_row = f"[{','.join(row)}],"
        matrix.append(formatted_row)

    return "\n".join(matrix)

def save_to_file(matrix, file_path="output.txt"):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(matrix)
# サンプル実行
matrix = render_text_to_matrix("九十閂仁仁泗伍鮫", font_size=32)
save_to_file(matrix, "output.txt")
print("結果を 'output.txt' に書き出しました。")