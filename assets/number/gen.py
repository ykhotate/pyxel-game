import os

def generate_files(directory, start, end):
    # フォルダが存在しない場合は作成
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    for i in range(start, end + 1):
        file_name = f"{i}.txt"
        file_path = os.path.join(directory, file_name)
        # ファイルを作成し、任意の内容を書き込む
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(f"これはファイル {i} の内容です。\n")
        print(f"{file_name} を生成しました。")

# 使用例
output_directory = "num"  # ファイルを生成するフォルダ
start_number = 1  # 開始番号
end_number = 16  # 終了番号

generate_files(output_directory, start_number, end_number)
