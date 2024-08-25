# Convert live-video id to live-chat id
# fetch live chats continuously, and stop when it finds a particular sender
# return sender message

import googleapiclient.discovery


# YouTube API setup
API_KEY = "AIzaSyAAEKBGXDqd0kLw6xRIv5Xp-wfc6tryoQA"  # Replace with your actual YouTube API key
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

    # Request to get live broadcast details
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

    

    # message = []
    # while message == "null" or message['items'][0]['authorDetails']['displayName'] != 'Nightbot':

        # response = request.execute()
        # message = response
    
    # return messages['items'][1]

# ----
    # response = request.execute()
    # print(response.keys())
# ----

    # messages = []
    # # count = 0
    # for i in range(3):
    #     response = request.execute()

    #     for mssg in response:
    #         # if mssg['authorDetails']['displayName'] == 'Nightbot':
    #         messages.append(mssg)
        
    #     nextPageToken = response.get("nextPageToken")
    #     # count+=1

    #     if nextPageToken == None:
    #         return 'No more messages available'
    
    # return messages
    # # return str(count)

#----

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
            # print(f"One comment scraped by : {response['items'][0]['authorDetails']['displayName']}")
            nextPageToken = response.get("nextPageToken")
            if not nextPageToken:
                return 'No responses now'



def mainMssg(video_id):

    livechatid = get_live_chat_id(video_id)

    if livechatid:
        messages = get_live_chat_messages(livechatid)
        
        # print(messages)
        # print(messages.type)
        # print(messages['items'][1])
        # print(messages['items'][0].keys())
        # print(messages['items'][0]['authorDetails']['displayName'])
        # print(messages['items'][1]['snippet'].keys())
        
        return messages

    else:
        return "No live chat found in this video"


score = mainMssg('paXOFTp3Hx0')
print(score)
# score = score.split('|')[2]
# score = score.split(' ')
print(score)