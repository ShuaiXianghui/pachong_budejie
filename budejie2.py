import requests
import re

pattern = re.compile(r'<div class="j-r-list-c-desc">\s+(.*)\s+</div>')

# open html
def open_url(url):
	html = requests.get(url)
	content = html.text
	return content

# get content
def get_content(num):
	text_list = []
	for page in range(1, int(num)):
		address = 'http://www.budejie.com/text/'+str(page)
		content = open_url(address)
		result = re.findall(pattern, content)
		for each in result:
			text_list.append(each)
	return text_list

# write content into file
def save(num):
        f = open('duanzi.txt', 'w')
        for each in get_content(num):
                if '<br />' in each:
                        new_each = re.sub(r'<br />', '\n',each)
                        f.write(new_each)
                else:
                        f.write(str(each) + '\n')
                f.write('\n')
        f.close()

if __name__ == '__main__':
	print('exit by pressing q or Q')
	number = int(input('how many pages do you want to read：'))
	save(number + 1)
	content = get_content(number + 1)
	for each in content:
		if '<br />' in each:
			new_each = re.sub(r'<br />', '\n',each)
			print(new_each)
		else:
			print(each)
		user_input = input()
		if user_input == 'q' or user_input == 'Q':
			break
	
