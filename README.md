# Project Goal
To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

## Features 
- Publish Time shows that the videos are fetched in reverse chronological order of their publishing date-time
![Alt text](search\screenshots\dashboard.png?raw=true "Title")
- Pagination: 6 objects per page
![Alt text](search\screenshots\hover.png?raw=true "Title")
- Hover over the description to see it completely
![Alt text](search\screenshots\pagination.png?raw=true "Title")
- Click over view button to open that video


#### Scalable and Optimized

### Getting API Key
- https://developers.google.com/youtube/v3/getting-started



### How to <i>RUN</i>
 - Install Python 3.x from https://www.python.org/downloads ( if not installed )
 - Open terminal
 - `pip install django`
 - `python manage.py makemigrations`
 - `python manage.py migrate`
 - `python manage.py startserver`
 - Open http://127.0.0.1:8000/
 
 ### View Database
 - Open terminal
 - `python manage.py createsuperuser`
 - Open http://127.0.0.1:8000/admin
 - Open *Videos*
 
### How to <i>Configure</i>
- Line 35 in views.py: add your search query for which it will fetch you recent videos
- Enter your API_KEY to line 124 in settings.py file which you obtained by following steps as mentioned above.
- I'm fetching the latest videos with time interval of 10 seconds. But you can change that at line 9 of scheduler/data_update.py `seconds : <your_interval>`


### Reference: <i>Calling YouTube API</i>
- https://developers.google.com/youtube/v3/docs/search/list