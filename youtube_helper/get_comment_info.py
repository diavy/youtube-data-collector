##############################################################################################
#################### Extract comments of Youtube video ##################################
###############################################################################################
from pyyoutube import Api
api = Api(api_key='AIzaSyCKfE-e5tPy6XcD_5ArjrxTV8jrMfuGTKs')

def get_comments_by_video(video_id='', count=None, include_replies=False):
    """
    Given a video id, get all comments of the video, including:
        id, videoId, authorName, authorChannelUrl, text, likeCount, viewCount, repliesCount
    :param video_id: string type of video ID
    :param count: # of comments returned. if set to None, get ALL comments
    :param include_replies: also include replies of each comments.
    :return: a list comments
    """
    comments = api.get_comment_threads(video_id=video_id, count=count)

    comments_info = []
    for comment in comments.to_dict()['items']:
        comments_info.append(parse_comment_response(comment, parse_replies=include_replies))

    return comments_info


def get_comments_by_channel(channel_id='', count=None, include_replies=False):
    """
    Given a channel id, get all comments of the channel, including:
        id, videoId, authorName, authorChannelUrl, text, likeCount, viewCount, repliesCount
    :param video_id: string type of video ID
    :param count: # of comments returned. if set to None, get ALL comments
    :param include_replies: also include replies of each comments.
    :return: a list of comments
    """

    comments = api.get_comment_threads(all_to_channel_id=channel_id, count=count)

    comments_info = []
    for comment in comments.to_dict()['items']:
        comments_info.append(parse_comment_response(comment, parse_replies=include_replies))

    return comments_info


def parse_comment_response(comment=dict(), parse_replies=False):
    """
    Parse comment dict to extract key metadata, including:
        id, videoId, authorName, authorChannelUrl, text, likeCount, viewCount, repliesCount
    :param comment: comment response, dict type
    :param parse_replies: whether to include replies
    :return: metadata of a comment
    """
    result = dict()

    result['id'] = comment['id']
    result['videoId'] = comment['snippet']['videoId']

    comment_snippet = comment['snippet']['topLevelComment']['snippet']
    result['authorName'] = comment_snippet['authorDisplayName']
    result['authorChannelUrl'] = comment_snippet['authorChannelUrl']
    result['text'] = comment_snippet['textDisplay']
    result['likeCount'] = comment_snippet['likeCount']
    result['publishedAt'] = comment_snippet['publishedAt']
    result['replyCount'] = comment['snippet']['totalReplyCount']
    if parse_replies and comment['replies']:
        result['replies'] = []
        for reply in result['replies']:
            result['replies'].append(parse_reply_response(reply))
    return result

def get_comment_replies_by_id(comment_id=''):
    """
    Given a comment id, get all its replies
    :param comment_id:
    :return: a list of replies
    """
    replies_info = []
    replies = api.get_comments(parent_id=comment_id)
    for reply in replies.items:
        replies_info.append(parse_reply_response(reply.to_dict()))
    return replies_info

def parse_reply_response(reply=dict()):
    """
    Parse reply dict to extract metadata
    :param reply: dict type of a reply object
    :return: key metadata of a reply, including:
        id, videoId, authorName, authorChannelUrl, text, likeCount, viewCount, repliesCount
    """
    result = dict()
    result['id'] = reply['id']
    snippet = reply['snippet']
    result['authorName'] = snippet['authorDisplayName']
    result['authorChannelUrl'] = snippet['authorChannelUrl']
    result['text'] = snippet['textDisplay']
    result['likeCount'] = snippet['likeCount']
    result['publishedAt'] = snippet['publishedAt']

    return result


if __name__ == '__main__':
    video_id = 'ADGB1ILUINs'
    comment_id = 'Ugx3mQ7C3NzAgjbGoDx4AaABAg'
    channel_id = 'UCCerg0895HYBJauluk-vWwA'
    include_replies = True

    print("get comments from video:")
    res = get_comments_by_video(video_id=video_id, include_replies=include_replies)
    print(len(res))
    print(res[-1])

    print("get all replies of a comment thread")
    replies = get_comment_replies_by_id(comment_id=comment_id)
    for r in replies:
        print(r)

    print('get all comments of a channel')
    all_comments = get_comments_by_channel(channel_id=channel_id, include_replies=include_replies)
    for comment in all_comments[:10]:
        print(comment)




