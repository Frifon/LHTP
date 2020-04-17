import requests
from datetime import datetime
from bs4 import BeautifulSoup
from webapp.model import db, News


def get_html(url):
	try:
		result = requests.get(url)
		result.raise_for_status()
		return result.text

	except(requests.RequestExeption, ValueError):
		print('оу где сеть ?')
		return False

def get_python_news():
	html = get_html('https://www.python.org/blogs/')
	if html:
	    soup = BeautifulSoup(html, 'html.parser')
	    # news_list = soup.find('ul', class_='list-recent-posts')
	    recent_news = soup.find('ul', class_='list-recent-posts')
	    # print(recent_news)
	    recent_news = recent_news.find_all('li')
	    result_news = []
	    for news in recent_news:
	        title = news.find('a').text #берет то, что между тегами а
	        url = news.find('a')['href'] #берет ссылку в теге href
	        on_website = news.find('time').text
	        try:
	        	on_website = datetime.strptime(on_website, '%Y-%m-%d')
	        except ValueError:
	        	on_website = datetime.now()
	        	save_news(title, url, on_website)
	#         result_news.append({
	#             'title': title,
	#             'url': url,
	#             'on_website': on_website
	#         })
	#     return result_news
	# return False


def save_news(title, url, on_website):
	news_exists = News.query.filter(News.url == url).count()
	print(news_exists)
	if not news_exists:
	    news_news = News(title=title, url=url, on_website=on_website)
	    db.session.add(news_news)
	    db.session.commit()


# if __name__ == '__main__':
# 	html = get_html('https://www.python.org/blogs/')
# 	if html:
# 		with open('python.org.html', 'w', encoding = 'utf8') as f:
# 			f.write(html)
# 	print(get_python_news())
