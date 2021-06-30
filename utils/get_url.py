# from youtubesearchpython import VideosSearch
# def get_url(videoname):
#     videosSearch = VideosSearch(videoname, limit = 1)
#     videosResult = videosSearch.next()
#     print(videosResult)
    
# get_url("Computer man song")

from youtubesearchpython import VideosSearch
def get_url(videoname):

    videosSearch = VideosSearch(videoname, limit = 1)

    res = videosSearch.result()['result'][0]['link']
    return res
print(get_url("hello world"))