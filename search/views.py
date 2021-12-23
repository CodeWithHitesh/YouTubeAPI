import requests
from datetime import datetime
from isodate import parse_duration
import pytz
from django.utils import timezone
from django.conf import settings
from django.shortcuts import render

from .models import Video
from django.core.paginator import Paginator


# This renders the data to index.html
def renderdata(request):

    getdata()

    videos = Video.objects.all().order_by('id')
    # 6 objects per page
    paginator = Paginator(object_list=videos, per_page=6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'search/index.html', {'page_obj': page_obj})


# This function fetches the data
def getdata():

    search_url = 'https://www.googleapis.com/youtube/v3/search'
    video_url = 'https://www.googleapis.com/youtube/v3/videos'

    search_params = {
        'part': 'snippet',
        'q': 'cricket',
        'key': settings.YOUTUBE_DATA_API_KEY,
        'maxResults': 21,
        'order': 'date',
        'type': 'video'
    }

    r = requests.get(search_url, params=search_params)

    results = r.json()['items']

    video_ids = []
    for result in results:
        video_ids.append(result['id']['videoId'])

    video_params = {
        'key': settings.YOUTUBE_DATA_API_KEY,
        'part': 'snippet,contentDetails',
        'id': ','.join(video_ids),
        'maxResults': 21
    }

    r = requests.get(video_url, params=video_params)

    results = r.json()['items']

    count = Video.objects.count()

    # If no object exists in the table, then create objects from the data fetched above in results
    if count == 0:

        for result in results:

            video_data = {
                'title': result['snippet']['title'],
                'description': result['snippet']['description'],
                'publishedAt': datetime.strptime(result['snippet']['publishedAt'], '%Y-%m-%dT%H:%M:%SZ'),
                'video_id': result['id'],
                'url': f'https://www.youtube.com/watch?v={ result["id"] }',
                'duration': int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
                'thumbnail': result['snippet']['thumbnails']['high']['url']
            }

            # Conversion of 'UTC' to 'Asia/Kolkata'

            # Convert naive datetime to datetime aware
            dt = pytz.utc.localize(video_data['publishedAt'])
            local_dt = timezone.localtime(
                dt, pytz.timezone('Asia/Kolkata'))
            # print(local_dt)
            video = Video.objects.create(title=video_data['title'],
                                         description=video_data['description'], publishedAt=local_dt,
                                         video_id=video_data['video_id'], url=video_data['url'], duration=video_data['duration'],
                                         thumbnail=video_data['thumbnail'])  # create a User object
            video.save()

    #  If objects already exist in the table, then update those objects with latest data.
    else:

        i = 1

        for result in results:

            video_data = {
                'title': result['snippet']['title'],
                'description': result['snippet']['description'],
                'publishedAt': datetime.strptime(result['snippet']['publishedAt'], '%Y-%m-%dT%H:%M:%SZ'),
                'video_id': result['id'],
                'url': f'https://www.youtube.com/watch?v={ result["id"] }',
                'duration': int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
                'thumbnail': result['snippet']['thumbnails']['high']['url']
            }

            dt = pytz.utc.localize(video_data['publishedAt'])
            local_dt = timezone.localtime(
                dt, pytz.timezone('Asia/Kolkata'))
            # id is the primary key of 'Video' table
            Video.objects.filter(id=i).update(title=video_data['title'],
                                              description=video_data['description'], publishedAt=local_dt,
                                              video_id=video_data['video_id'], url=video_data['url'], duration=video_data['duration'],
                                              thumbnail=video_data['thumbnail'])
            i = i + 1
