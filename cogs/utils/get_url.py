from youtubesearchpython import VideosSearch


def get_url(videoname):

    videosSearch = VideosSearch(videoname, limit=1)

    res = videosSearch.result()['result'][0]['link']
    return res
