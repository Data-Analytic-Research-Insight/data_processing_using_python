import requests
from bs4 import BeautifulSoup
import re

ratingSum = 0

r = requests.get('https://book.douban.com/subject/1002299/comments/')
soup = BeautifulSoup(r.text, 'lxml')
comments = soup.find_all('p', 'comment-content')
for comment in comments:
	print(comment.string)

rating = re.compile('<span class="user-stars allstar(.*)? rating" title')
p = re.findall(rating, r.text)
for star in p:
	star = int(star)
	ratingSum += star
print(ratingSum)