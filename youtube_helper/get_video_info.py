###############################################################################################
#################### Extract information of a Youtube video ##################################
###############################################################################################


from pyyoutube import Api
api = Api(api_key='AIzaSyCKfE-e5tPy6XcD_5ArjrxTV8jrMfuGTKs')

def get_videos_by_playlist(playlist_id='', parse_video=True):
    """
    Given a playlist Id, get all videos under this playlist
    :param playlist_id: playlist_id, string type
    :param parse_video: if set to True, get metadata of all videos, including
        id, title, description, tags, viewCount, likeCount, likeCount, dislikeCount
            if set to False, only return id.
    :return:
    """
    videos = api.get_playlist_items(playlist_id=playlist_id, count=None)
    video_ids = []
    for item in videos.items:
        item = item.to_dict()
        video_ids.append(item['contentDetails']['videoId'])
    if parse_video:
        results = []
        for video_id in video_ids:
            results.append(get_video_by_id(video_id))
        return results
    else:
        return video_ids

def get_video_by_id(video_id=''):
    """
    Given a video id, get key metadata of the video, including:
        id, title, description, tags, viewCount, likeCount, likeCount, dislikeCount
    :param video_id: str type, video id
    :return:
    """
    video_info = api.get_video_by_id(video_id=video_id)
    video = video_info.items[0].to_dict()

    return parse_video_response(video)


def parse_video_response(video=dict()):
    """
    Parse video dict to extract key metadata, including:
        id, title, description, tags, viewCount, likeCount, likeCount, dislikeCount
    :param video:
    :return:
    """
    result = dict()
    result['id'] = video['id']
    result['title'] = video['snippet']['title']
    result['description'] = video['snippet']['description']

    result['tags'] = video['snippet']['tags']
    result['viewCount'] = video['statistics']['viewCount']
    result['likeCount'] = video['statistics']['likeCount']
    result['dislikeCount'] = video['statistics']['commentCount']

    return result


if __name__ == '__main__':
    #video = get_video_by_id(video_id='ADGB1ILUINs')
    #print(video)
    parse_video = True
    video_list = get_videos_by_playlist(playlist_id='PLM8deaCFra9fWNLrxoowZTHcXWULb8yYJ',
                                        parse_video=parse_video)
    print(video_list)





