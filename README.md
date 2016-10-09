# Hello

blubox is a little web app that takes the most recent videos posted on metafilter.com and turns them into a continuous YouTube playlist. It's currently kinda weird on mobile but does work.

**[See the live demo on extrafuture.com](https://extrafuture.com/blubox/)**

# Yes and...

blubox was made by [@philnelson](http://twitter.com/philnelson), and it's two things:

1. A python3-based script that requires the [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), [requests](http://docs.python-requests.org/en/master/), [json](https://docs.python.org/3/library/json.html), urllib, isodate, and datetime python libraries. It pulls [this page from metafilter](https://labs.metafilter.com/recent-youtube-posts) every hour and caches the results as a JSON file.

2. An HTML, javascript, and jquery page that takes said JSON file and uses the [YouTube iframe API](https://developers.google.com/youtube/v3/getting-started) to load the 10 most recent videos as a queue.

It'll probably work, but like, I dunno.
