from PIL import Image, ImageDraw, ImageFont

def render_text_to_matrix(text, font_path="arial.ttf", font_size=8):
    font = ImageFont.truetype(font_path, font_size)
    # 文字列を描画
    img = Image.new("1", (len(text) * font_size, font_size), color=0)
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), text, font=font, fill=1)

    # ドットパターン取得
    pixels = img.load()
    matrix = []
    for y in range(img.height):
        row = ""
        for x in range(img.width):
            row += "X" if pixels[x, y] else " "
        matrix.append(row)

    return "\n".join(matrix)

# サンプル実行
print(render_text_to_matrix("AB", font_size=8))