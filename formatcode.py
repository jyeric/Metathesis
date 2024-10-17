import os
import jsbeautifier

# 格式化public目录下的所有js文件
def format_js_files(directory):
    # 初始化jsbeautifier的选项
    opts = jsbeautifier.default_options()
    opts.indent_size = 2  # 设置缩进为2个空格

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".js"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    js_code = f.read()
                
                # 使用jsbeautifier格式化JS代码
                beautified_js = jsbeautifier.beautify(js_code, opts)

                # 将格式化后的内容写回文件
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(beautified_js)
                print(f"Formatted: {file_path}")

# 对根目录下的file.info文件按照字典序排序
def sort_file_info(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # 去除每行的换行符并按字典序排序
        sorted_lines = sorted([line.strip() for line in lines])
        
        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            for line in sorted_lines:
                f.write(line + '\n')
        print(f"Sorted: {file_path}")
    else:
        print(f"File not found: {file_path}")

if __name__ == "__main__":
    # 格式化public目录下的所有js文件
    format_js_files("public")
    
    # 对根目录下的file.info文件进行排序
    sort_file_info("file.info")
