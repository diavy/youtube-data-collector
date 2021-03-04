

class YTvideo:

    def _init_(self, API_KEY, channel_id):
        self.API_KEY = API_KEY
        self.channel_id = channel_id
        self.channel_stats = None

    def get_channel_stats(Self):
        url = f"//www.googleapis.com/youtube/v3/channel?part=statistics&id={self.channel_id}&key={self.api_key}"

    print(url)


    def get_channel_by_id(channel_id=''):
    """
    Given a Youtube channel ID, extract important metadata about this channel, including:
    id, title, description, viewCount, videoCount, subscriberCount

    :param channel_id: channel id of Youtube
    :return:
    """
    channel_info = api.get_channel_info(channel_id=channel_id)
    res = channel_info.items[0].to_dict()
    return parse_channal_response(res)
   
   
   
   
   
   def get_channel_response(self):

         channel_videos = self._get_channel_videos(limit = none)
         print(len(channel)videos))

         result = {"snippet", "description","publishAt ", "viewCount", "video count",  }
        for video_id in channel_videos:
            for result in results:






def parse_channal_response(channel=dict()):
    

    result = {}

    result['id'] = channel['id']
    result['title'] = channel['snippet']['title']
    result['description'] = channel['snippet']['description']
    result['publishedAt'] = channel['snippet']['publishedAt']

    result['viewCount'] = channel['statistics']['viewCount']
    result['videoCount'] = channel['statistics']['videoCount']
    result['subscriberCount'] = channel['statistics']['subscriberCount']

    result['keywords'] = channel['brandingSettings']['channel']['keywords']
    result['country'] = channel['brandingSettings']['channel']['country']
    return result

    
    
    
    



        
