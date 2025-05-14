import os
import shutil
from pathlib import Path


def organize_files(target_dir: str):
    """
    按文件后缀整理目录下的所有文件
    - 自动创建对应后缀名的文件夹（如 .txt → txt_files）
    - 无后缀文件归类到 no_extension 文件夹
    - 跳过已存在的目标文件夹
    """
    target_dir = os.path.abspath(target_dir)  # 转换为绝对路径

    # 验证目录有效性
    if not os.path.isdir(target_dir):
        print(f"错误：目录 {target_dir} 不存在")
        return

    # 遍历所有文件
    for entry in os.scandir(target_dir):
        if entry.is_file():  # 只处理文件
            file_path = Path(entry.path)
            ext = file_path.suffix.lower()

            # 处理无后缀文件
            if not ext:
                category = "no_extension"
            else:
                category = ext[1:]  # 移除点号，如 .txt → txt

            # 创建目标目录
            dest_dir = Path(target_dir) / f"{category}_files"
            dest_dir.mkdir(exist_ok=True)

            # 避免递归处理已整理的文件夹
            if dest_dir in file_path.parents:
                continue

            # 移动文件（保留原名）
            try:
                shutil.move(str(file_path), dest_dir / file_path.name)
                print(f"已移动：{file_path.name} → {category}_files")
            except Exception as e:
                print(f"移动失败 {file_path.name}：{str(e)}")


if __name__ == "__main__":
    target_path = input("请输入需要整理的目录路径：").strip()
    organize_files(target_path)
    print("\n整理完成！所有文件已按后缀分类到同名文件夹中")
