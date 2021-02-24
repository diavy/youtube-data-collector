###############################################################################################
#################### Extract information of a Youtube Playlist ################################
###############################################################################################


from pyyoutube import Api
api = Api(api_key='AIzaSyCKfE-e5tPy6XcD_5ArjrxTV8jrMfuGTKs')

def get_playlists_by_channel(channel_id="", count=None):
    """
    Given a channel ID, get all playlists under the channel
    :param channel_id: string type, channel ID
    :param count: number of playlists returned, if count is None, then get ALL playlists
    :return: playlists, including
        id, channelId, channelTitle, title, and description
    """
    playlists = api.get_playlists(channel_id=channel_id, count=count)
    playlists = playlists.items.to_dict()

    results = []
    for pl in playlists:
        results.append(parse_playlist_response(pl))
    return results


def get_playlist_by_id(playlist_id=''):
    """
    Given a playlist_id, get metadata of the playlist
    :param playlist_id:
    :return:
    """
    playlist = api.get_playlist_by_id(playlist_id=playlist_id)
    playlist = playlist.items[0].to_dict()
    return parse_playlist_response(playlist)


def parse_playlist_response(playlist=dict()):
    """
    Parse playlist dict to extract key metadata, including:
        id, title, description, channelId, channelTitle
    :param playlist: dict type of a playlist metadata
    :return:
    """
    result = dict()
    result['id'] = playlist['id']
    result['channelId'] = playlist['snippet']['channelId']
    result['channelTitle'] = playlist['snippet']['channelTitle']
    result['title'] = playlist['snippet']['title']
    result['description'] = playlist['snippet']['description']

    return result

if __name__ == "__main__":
    channel_id = 'UCCerg0895HYBJauluk-vWwA'
    user_name = '猴哥财经'

    # ch_info = get_channel_by_id(channel_id=channel_id)
    playlists_info = get_playlists_by_channel(channel_id=channel_id)
    print(playlists_info)




