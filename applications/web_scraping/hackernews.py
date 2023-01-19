# Get all news above 100 points
import requests
from bs4 import BeautifulSoup
import pprint

# Grab stories
base_url = "https://news.ycombinator.com/news"
num_pages = 3
links = []
subtext = []

for page in range(1, num_pages + 1):
    res = requests.get(f"{base_url}?p={page}")
    soup = BeautifulSoup(res.text, 'html.parser')
    links += soup.select('.titleline > a')
    subtext += soup.select('.subtext')


def sort_stories_by_points(hackernews):
    """Sorts stories by points"""
    return sorted(hackernews, key=lambda k: k['points'], reverse=True)


def create_custom_hackernews(links, subtext):
    """Create customized hacker news list"""
    hackernews = []
    
    for index, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[index].select('.score', None)
        if not vote: continue
        points = int(vote[0].getText().split(" ")[0])
        if points < 100: continue
        hackernews.append(dict(title=title, href=href, points=points))
    
    return sort_stories_by_points(hackernews)

pprint.pprint(create_custom_hackernews(links, subtext))
