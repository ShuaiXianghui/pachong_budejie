import requests
import re

url = 'http://www.budejie.com/text/'
html = requests.get(url)
print(html.status_code)
content = html.text

duanzi = re.findall(r'<div class="j-r-list-c-desc">\s+(.*)\s+</div>', content)


f = open('duan.txt', 'w')
for each in duanzi:
    if '<br />' in each:
        new_each = re.sub(r'<br />', '\n',each)
        print(new_each)
        f.write(new_each)
    else:
        print(each)
        f.write(each)
f.close()
