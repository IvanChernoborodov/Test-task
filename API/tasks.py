from celery import shared_task
import requests
from bs4 import BeautifulSoup
from .models import Post
from celery.task import task
import logging
import time




logger = logging.getLogger(__name__)
main_url = 'https://news.ycombinator.com/'




def get_html(url):
	"""
	get html of main_url
	"""
	try:
		r = requests.get(url)
		return r.text
	except ConnectionError:
		logger.error('Сonnection trouble')



def find_info_and_save(html):
	"""
	find title and href of posts and save it to db
	"""
	soup = BeautifulSoup(html, 'lxml')
	try:
		page = soup.find_all('a', class_='storylink', href=True)

		for post in page:
			if not Post.objects.filter(title=str(post.getText())).exists():
				Post.objects.create(title=str(post.getText()), url=post['href'])
				print('saved')
				logger.info('saved')
			else:
				logger.info('instance exists')
				print('exist')


	except Exception as e:
		print(e)


@task
def main_parse():
	html = get_html(main_url)
	find_info_and_save(html)




