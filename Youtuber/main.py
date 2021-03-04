from pyyoutube import YTvideo


API_KEY = "AIzaSyCU9_SMdvum5jizunx5gPJcikb1fO0mavc"

channel_id = "UC3mjMoJuFnjYRBLon_6njbQ"

yt = YTvideo(API_KEY, Channel_id)

yt.get_channel_stats()