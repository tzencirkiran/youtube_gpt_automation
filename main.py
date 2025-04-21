from ytdataApi import YoutubeDataAPI
from fileHandler import FileHandler, VideoIdHandler
from ytTranscriptApi import fetch_transcript_comments
import json



# I need to merge some methods for less complexity
print("1")
video_ids = YoutubeDataAPI.fetch_video_ids_pl("PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU")

print("2")
VideoIdHandler.save_video_ids(video_ids=video_ids)

print("3")
tc_comment_dict = fetch_transcript_comments(VideoIdHandler.read_video_ids())

print("4")

print("5")
FileHandler.save_transcript_comments(tc_comment_dict)

# I need to put methods of different files to classes for increased modularity

# Add yt_api_key in ydDataApi to a seperate a seperate txt
