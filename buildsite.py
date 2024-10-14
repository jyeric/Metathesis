import git
import os
import shutil

# 当前仓库路径
repo_path = '.'
publish_base_path = 'publish'

# 打开 Git 仓库
repo = git.Repo(repo_path)

# 获取所有 tags
tags = repo.tags

# 确保发布目录存在
os.makedirs(publish_base_path, exist_ok=True)

DEFAULT_HTML = """<html>
<head>
<title>Metathesis历史页面检索页</title>
</head>
<body>
<h1> Metathesis 历史版本检索页 </h1>
"""
# 遍历每个 tag 并复制 public 文件夹
for tag in tags:
    tag_name = tag.name
    print(f'Processing tag: {tag_name}')
    
    # 检出到 tag 版本
    repo.git.checkout(tag_name)

    # 源 public 目录
    source_public_dir = os.path.join(repo_path, 'public')

    # 目标目录
    target_publish_dir = os.path.join(publish_base_path, tag_name)

    # 确保目标目录存在
    os.makedirs(target_publish_dir, exist_ok=True)

    # 复制 public 目录到目标目录
    if os.path.exists(source_public_dir):
        shutil.copytree(source_public_dir, target_publish_dir, dirs_exist_ok=True)
        print(f'Copied {source_public_dir} to {target_publish_dir}')
    else:
        print(f'Public directory not found for tag: {tag_name}')

    DEFAULT_HTML = DEFAULT_HTML + f"<p> {tag} 版本 <a href=\"https://jyeric.github.io/Metathesis/{tag}\">https://jyeric.github.io/Metathesis/{tag}</a>\n"

DEFAULT_HTML = DEFAULT_HTML + """<p>本历史记录站仅记录了20240528开始的更新，先前更新并未计入</p>
</body>
<html>"""

print(DEFAULT_HTML)

with open('publish/index.html', mode='w') as f:
	f.write(DEFAULT_HTML)

# 返回到主分支
repo.git.checkout('main')

print('Task completed!')
