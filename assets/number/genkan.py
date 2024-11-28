import os

def generate_japanese_number_files(directory, start, end):
    # 日本語の数字リスト
    japanese_numbers = [
        "一", "二", "三", "四", "五", "六", "七", "八", "九", "十",
        "十一", "十二", "十三", "十四", "十五", "十六"
    ]
    
    # フォルダが存在しない場合は作成
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    for i in range(start, end + 1):
        # 日本語の番号を取得
        if i <= len(japanese_numbers):
            file_name = f"{japanese_numbers[i - 1]}.txt"
            file_path = os.path.join(directory, file_name)
            # ファイルを作成し、任意の内容を書き込む
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(f"これはファイル「{japanese_numbers[i - 1]}」の内容です。\n")
            print(f"{file_name} を生成しました。")
        else:
            print(f"エラー: {i} の日本語名が見つかりませんでした。")

# 使用例
output_directory = "num"  # ファイルを生成するフォルダ
start_number = 1  # 開始番号
end_number = 16  # 終了番号

generate_japanese_number_files(output_directory, start_number, end_number)
