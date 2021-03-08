from googleapiclient.discovery import build
from pprint import pprint

key = 'AIzaSyCP1bYByevm4G5dE5dlqiACYXDY7Clo2yY'
video_url = "https://www.youtube.com/watch?v="

def results(song):
    if song == "":
        return []
    youtube = build('youtube', 'v3',developerKey = key)
    request = youtube.search().list(
        part = "snippet",
        maxResults = 2,
        q = song,
        type = "video"
    )
    response = request.execute()
    results = []
    for item in response['items']:
        pprint(item)
        idconcact=video_url+item['id']['videoId']
        results.append(idconcact)
    #if(request)
    print("results")
    print (results)
    return results


if __name__ == "__main__":
    #t = results("my dearest")
    #pprint(t)

    op={}
    op['op1']=[]
    op['ed1'] =[]
    #print(op['op1'])
    op['op1'].append("asdfasdasdfa")
    op['op1'].append("asdffa")
    op['ed1'].append("ed1")
    #print(op['op1'][1])
        