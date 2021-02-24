###############################################################################################
#################### Extract information of a Youtube Channel #################################
###############################################################################################


from pyyoutube import Api
api = Api(api_key='AIzaSyCKfE-e5tPy6XcD_5ArjrxTV8jrMfuGTKs')

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

def get_channel_by_username(user=''):
    """
    Given a Youtube user ID, extract important metadata about this channel, including:
    id, title, description, viewCount, videoCount, subscriberCount
    :param user: a user_id of a Youtube channel
    :return:
    """
    channel_info = api.get_channel_info(channel_name=user)
    res = channel_info.items[0].to_dict()
    if not res:
        return None
    return parse_channal_response(res)

def parse_channal_response(channel=dict()):
    """
    Parse channel dict to extract key metadata, including:
    id, title, description, viewCount, videoCount, subscriberCount
    :param channel: a dictionary containing all metadata of a channel
    :return:
    """

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


if __name__ == '__main__':
    channel_id = 'UCCerg0895HYBJauluk-vWwA'
    user_name = 'padnag1'

    #ch_info = get_channel_by_id(channel_id=channel_id)
    ch_info = get_channel_by_username(user_name)
    print(ch_info)

