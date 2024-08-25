# Convert live-video id to live-chat id
# fetch live chats continuously, and stop when it finds a particular sender
# return sender message

import googleapiclient.discovery

API_KEY = "AIzaSyAAEKBGXDdqd0kLw6xRIv5Xp-wfcs6tryoQaA"  # Replace with YOUR youtube API key (I've added random characters in here, so copying mine wont work)
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def get_live_chat_id(video_id):
    """
    Fetches the liveChatId for a given video ID.
    
    :param video_id: The ID of the YouTube video/livestream.
    :return: The liveChatId if found, None otherwise.
    """
    youtube = googleapiclient.discovery.build(
        YOUTUBE_API_SERVICE_NAME,
        YOUTUBE_API_VERSION,
        developerKey=API_KEY
    )
    
    request = youtube.videos().list(
        part="liveStreamingDetails",
        id=video_id
    )
    response = request.execute()

    if "items" in response and len(response["items"]) > 0:
        live_stream_details = response["items"][0].get("liveStreamingDetails", {})
        return live_stream_details.get("activeLiveChatId")
    
    return None




def get_live_chat_messages(livechatid):

    youtube = googleapiclient.discovery.build(
        YOUTUBE_API_SERVICE_NAME,
        YOUTUBE_API_VERSION,
        developerKey=API_KEY
    )

    nextPageToken = None

    while True:

        request = youtube.liveChatMessages().list(
        liveChatId = livechatid,
        part='snippet,authorDetails',
        pageToken=nextPageToken,
        maxResults = 1
    )
        response = request.execute()

        if response['items'][0]['authorDetails']['displayName'] == 'Nightbot' and 'VALORANT Champions Seoul - Grand Final' in response['items'][0]['snippet']['displayMessage'].split('|')[0]:
            return response['items'][0]['snippet']['displayMessage']
        else:
            nextPageToken = response.get("nextPageToken")
            if not nextPageToken:
                return 'No responses now'



def mainMssg(video_id):

    livechatid = get_live_chat_id(video_id)

    if livechatid:
        messages = get_live_chat_messages(livechatid)
        return messages

    else:
        return "No live chat found in this video"

# video_id = official yt livestream link
