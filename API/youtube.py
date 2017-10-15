que = 'linkin park'

from apiclient.discovery import build
service = build('youtube', 'v3')

def get_channel(service,que):
    search = service.search()
    res = search.list(q=que,part='snippet').execute()
    items = res['items']

    cid = None

    for it in items:
        if it['id']['kind']=='youtube#channel':
            cid = it['id']['channelId']
            break

    assert cid!=None
    return cid

def get_playlist_id(service,cid):
    channel = service.channels()
    res = channel.list(id=cid,part='contentDetails').execute()
    con = res['items'][0]['contentDetails']
    return con['relatedPlaylists']['favorites']

def get_video_ids(service,pid):
    pl = service.playlistItems()
    r = pl.list(part='contentDetails',maxResults=50,playlistId=pid).execute()
    its = r['items']
    return list(map(lambda x:x['contentDetails']['videoId'],its))

cid = get_channel(service,que)
pid = get_playlist_id(service,cid)
#vids = get_video_ids(service,pid)
























