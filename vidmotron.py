import requests
import json
import isodate
import datetime
from bs4 import BeautifulSoup

# This is the URL that we're pulling the video list from.
VIDEO_PAGE = "https://labs.metafilter.com/recent-youtube-posts"

# Set your Youtube API key here. Get one: https://developers.google.com/youtube/v3/getting-started
YT_CREDS = None

if YT_CREDS is None:
    raise ValueError('Enter your YouTube API credential into the script first.')

# Set our custom header so people know who wuz here
headers = {
    'User-Agent': 'blubox 0.1 alpha extreme turbo',
}

print("Fetching {}...".format(VIDEO_PAGE))

# Try and get the page
r = requests.get(VIDEO_PAGE, headers=headers)

if r.status_code == 200:

    # What time is it anyway?
    last_updated = datetime.datetime.isoformat(datetime.datetime.utcnow())
    
    # Create the dict that holds our file data
    file_data = {'updated_at': last_updated, 'videos': []}
    
    print(last_updated)

    print("Loaded the URL.")

    html_doc = r.text

    print("Souping it up.")

    soup = BeautifulSoup(html_doc, 'html.parser')

    # print(soup)

    for link in soup.find_all("div", class_="copy"):

        try:
            print("Found link {} {}".format(
                link.a.get('title'), link.a.get('href')))
            video_id = link.a.get('href')[31:]
            searchUrl = "https://www.googleapis.com/youtube/v3/videos?id=" + \
                video_id + "&key=" + YT_CREDS + "&part=contentDetails"
            video_detail_request = requests.get(searchUrl)
            if video_detail_request.status_code == 200:
                video_detail = video_detail_request.json()
                all_data = video_detail['items']
                contentDetails = all_data[0]['contentDetails']
                duration = isodate.parse_duration(contentDetails['duration'])
                
                print(duration.total_seconds())

                new_video = {'title': link.a.get(
                    'title'), 'duration': duration.total_seconds(), 'id': video_id}
                file_data['videos'].append(new_video)
            else:
                pass
        except Exception as e:
            print(e)

    print("Writing out file...")
    with open("videos.json", "wt") as out_file:
        out_file.write(json.dumps(file_data))

    print("Wrote the file.")

else:
    print("Status Code: {}".format(r.status_code))
    print("*sad beep*")

print("*satisfied beep*")
