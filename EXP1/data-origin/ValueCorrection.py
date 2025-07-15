# 処理：上記ヘッダの値を-50する

import os
import glob
import csv

target_dir = "xx"  # 任意のディレクトリに変更可

csv_files = glob.glob(os.path.join(target_dir, "*.csv"))

# 各CSVファイルを処理
for csv_path in csv_files:
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = list(csv.reader(f))

    # ヘッダ行を取得
    header = reader[0]

    # Q2, Q4, Q5のインデックスを取得
    q2_index = header.index("Q_2")
    q4_index = header.index("Q_4")
    q5_index = header.index("Q_5")

    # データ行を修正
    for row in reader[1:]:
        for idx in [q2_index, q4_index, q5_index]:
            try:
                # 数値として処理し、-50する
                row[idx] = str(float(row[idx]) - 50)
                row[idx] = str(round(float(row[idx]), 5))  # 小数点以下5桁
            except Exception:
                pass

    # 修正後のデータを新しいCSVファイルに書き込む
    base = os.path.basename(csv_path)
    corrected_path = f"{target_dir}/corrected/{base}"
    os.makedirs(f"{target_dir}/corrected", exist_ok=True)
    with open(corrected_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(reader)