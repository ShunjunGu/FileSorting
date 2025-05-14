# FileSorting

这是一个简单的Python脚本，可以按文件后缀整理目录下的所有文件。

## 功能

- 自动创建对应后缀名的文件夹（如 .txt → txt_files）
- 无后缀文件归类到 no_extension 文件夹
- 跳过已存在的目标文件夹

## 使用方法

1. 克隆仓库：`git clone https://github.com/ShunjunGu/FileSorting.git`
2. 运行脚本：`python organizeBySuffixName.py`
3. 输入需要整理的目录路径，脚本会自动将文件按后缀分类到同名文件夹中。

## 注意事项

- 需要Python 3.x环境
- 目录路径请使用绝对路径或有效的相对路径
