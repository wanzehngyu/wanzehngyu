import pandas as pd


def csv_to_dict(file_path):
    # 读取CSV文件
    df = pd.read_csv(file_path)
    result = []

    # 遍历每个单元格
    for row_idx in range(df.shape[0]):  # 遍历行
        for col_idx in range(df.shape[1]):  # 遍历列
            cell_value = df.iat[row_idx, col_idx]
            if pd.notna(cell_value):
                cell_data = {
                    'cell_values': df.iat[row_idx, col_idx],
                    'cell_raw_column': [(row_idx + 1, col_idx + 1)]
                }
                result.append(cell_data)

    return result


# 示例用法
file_path = 'test_csv.csv'  # 替换为你的CSV文件路径
cell_data_list = csv_to_dict(file_path)

# 输出每个单元格的字典
for cell_data in cell_data_list:
    print(cell_data)
