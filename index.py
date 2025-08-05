import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, urldefrag
import hashlib
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def save_content(url, content, base_path):
    """保存网页内容到本地文件系统"""
    parsed_url = urlparse(url)
    path = parsed_url.path
    if path.endswith('/') or path == '':
        path += 'index.html'
    filepath = os.path.join(base_path, path.lstrip('/'))
    
    if os.path.exists(filepath):
        print(f'File already exists: {filepath}')
        return
    
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'wb') as f:
        f.write(content)

def get_content(url):
    """获取网页内容"""
    response = requests.get(url, verify=False)
    response.raise_for_status()
    return response.content

def parse_links(base_url, content):
    """解析出页面中的所有链接"""
    soup = BeautifulSoup(content, 'html.parser')
    links = set()
    
    for tag in soup.find_all(['a', 'link', 'script', 'img']):
        href = tag.get('href') or tag.get('src')
        if href:
            full_url = urljoin(base_url, href)
            links.add(urldefrag(full_url).url)
    
    return links

def is_media_file(url):
    """判断是否为媒体文件"""
    media_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico', '.css', '.js')
    return url.lower().endswith(media_extensions)

visited = set()
def crawl(url, base_path):
    """深度优先搜索爬取网页"""
    global visited
    stack = [url]

    while stack:
        current_url = stack.pop()
        if current_url in visited:
            print("visited: File already exists: ", current_url)
            continue

        print(f'Crawling: {current_url}')
        try:
            content = get_content(current_url)
            save_content(current_url, content, base_path)
            visited.add(current_url)

            if not is_media_file(current_url):
                for link in parse_links(current_url, content):
                    if link not in visited:
                        stack.append(link)
        except requests.RequestException as e:
            print(f'Failed to fetch {current_url}: {e}')
            
def calculate_sha256(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(65536)  # 64 KB chunks
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()

sha256_content=""
def traverse_and_calculate_sha256(folder_path):
    global sha256_content
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            sha256_hash = calculate_sha256(file_path)
            sha256_content=sha256_content + f"{file_path}: {sha256_hash}\n"

if __name__ == '__main__':
    start_url = 'http://www.evvh-yyq-m.top/'
    base_path = 'public'
    crawl(start_url, base_path)
    start_url = 'http://www.evvh-yyq-m.top/undefined.html'
    base_path = 'public'
    crawl(start_url, base_path) 
    start_url = 'http://www.evvh-yyq-m.top/error.html'
    base_path = 'public'
    crawl(start_url, base_path)
    start_url = 'http://www.evvh-yyq-m.top/trap.html'
    base_path = 'public'
    crawl(start_url, base_path)
    start_url = 'http://www.evvh-yyq-m.top/signin.html'
    base_path = 'public'
    crawl(start_url, base_path)
    start_url = 'http://www.evvh-yyq-m.top/fst.html'
    base_path = 'public'
    crawl(start_url, base_path)
    start_url = 'http://www.evvh-yyq-m.top/itdc.html'
    base_path = 'public'
    crawl(start_url, base_path)
    start_url = 'http://www.evvh-yyq-m.top/rls.html'
    base_path = 'public'
    crawl(start_url, base_path)
    start_url = 'http://www.evvh-yyq-m.top/mypage.html'
    base_path = 'public'
    crawl(start_url, base_path)
    start_url = 'http://www.evvh-yyq-m.top/mng.html'
    base_path = 'public'
    crawl(start_url, base_path)
    start_url = 'http://www.evvh-yyq-m.top/prj.html'
    base_path = 'public'
    crawl(start_url, base_path)
    start_url = 'http://www.evvh-yyq-m.top/images/fst/u496_selected.svg'
    base_path = 'public'
    crawl(start_url, base_path)
    start_url = 'http://www.evvh-yyq-m.top/images/fst/u499_selected.svg'
    base_path = 'public'
    crawl(start_url, base_path)
    start_url = 'http://www.evvh-yyq-m.top/images/fst/u508_selected.svg'
    base_path = 'public'
    crawl(start_url, base_path)
    start_url = 'http://www.evvh-yyq-m.top/images/fst/u511_selected.svg'
    base_path = 'public'
    crawl(start_url, base_path)
    start_url = 'http://www.evvh-yyq-m.top/images/fst/u505_selected.svg'
    base_path = 'public'
    crawl(start_url, base_path)
    start_url = 'http://www.evvh-yyq-m.top/resources/reload.html'
    base_path = 'public'
    crawl(start_url, base_path)
    """
    20250805新增，应对202410页面更新
    """
    start_url = 'https://www.evvh-yyq-m.top/dairy-2122.html'
    base_path = 'public'
    crawl(start_url, base_path)
    start_url = 'https://www.evvh-yyq-m.top/dairy-2324.html'
    base_path = 'public'
    crawl(start_url, base_path)
    """
    20250805新增，应对202410页面二次更新
    """
    start_url = 'https://www.evvh-yyq-m.top/catholics.html'
    base_path = 'public'
    crawl(start_url, base_path)
    start_url = 'https://www.evvh-yyq-m.top/catholics-1.html'
    base_path = 'public'
    crawl(start_url, base_path)
    start_url = 'https://www.evvh-yyq-m.top/catholics-2.html'
    base_path = 'public'
    crawl(start_url, base_path)
    start_url = 'https://www.evvh-yyq-m.top/catholics-3.html'
    base_path = 'public'
    crawl(start_url, base_path)
    start_url = 'https://www.evvh-yyq-m.top/error-1.html'
    base_path = 'public'
    crawl(start_url, base_path)
    start_url = 'https://www.evvh-yyq-m.top/1.MP3'
    base_path = 'public'
    crawl(start_url, base_path)
    start_url = 'https://www.evvh-yyq-m.top/2.MP3'
    base_path = 'public'
    crawl(start_url, base_path)
    """
    20250805更新，应对202503页面小更新
    """
    start_url = 'https://www.evvh-yyq-m.top/dairy-2526.html'
    base_path = 'public'
    crawl(start_url, base_path)


    
    folder_path = 'public'
    traverse_and_calculate_sha256(folder_path)
    with open('file.info','w') as f:
        f.write(sha256_content)