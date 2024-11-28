import os
import sys

def convert_to_array(file_path):
    try:
        # ファイルを読み込み
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
        # 結果リストを作成
        result = []
        for line in lines:
            row = []
            for char in line.strip():
                if char == "■":
                    row.append("f")
                elif char == "．" or char == " ":
                    row.append(0)
            result.append(row)
        return result
    except FileNotFoundError:
        print(f"エラー: ファイル '{file_path}' が見つかりませんでした。")
        sys.exit(1)

def save_to_file(data, original_file_path, output_dir):
    # 元ファイル名を取得
    base_name = os.path.basename(original_file_path)
    # 新しいファイルパスを生成（num-c フォルダ内に保存）
    output_file_path = os.path.join(output_dir, base_name)
    # 結果をファイルに書き込む
    with open(output_file_path, "w", encoding="utf-8") as file:
        for row in data:
            file.write(f"{row}\n")
    print(f"変換結果を保存しました: {output_file_path}")

def main():
    # 入力フォルダと出力フォルダ
    input_dir = "num"
    output_dir = "num-c"
    
    # 出力フォルダが存在しない場合は作成
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 入力フォルダ内のすべてのテキストファイルを取得
    text_files = [f for f in os.listdir(input_dir) if f.endswith(".txt")]
    if not text_files:
        print(f"エラー: フォルダ '{input_dir}' にテキストファイルが見つかりませんでした。")
        sys.exit(1)

    # 各テキストファイルを処理
    for text_file in text_files:
        input_file_path = os.path.join(input_dir, text_file)
        converted_array = convert_to_array(input_file_path)
        save_to_file(converted_array, input_file_path, output_dir)

if __name__ == "__main__":
    main()
