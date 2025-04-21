from ytdataApi import YoutubeDataAPI
from fileHandler import FileHandler, VideoIdHandler
from ytTranscriptApi import fetch_transcript_comments
import json

while True:
    break


# I need to merge some methods for less complexity
print("1")
video_ids = YoutubeDataAPI.fetch_video_ids_pl("PL7BImOT2srcFJlt4kdzJLttcd9wRCdnF9")

print("2")
VideoIdHandler.save_video_ids(video_ids=video_ids)

print("3")
tc_comment_dict = fetch_transcript_comments(VideoIdHandler.read_video_ids())

print("4")

print("5")
FileHandler.save_transcript_comments(tc_comment_dict)

# I need to put methods of different files to classes for increased modularity

# Add yt_api_key in ydDataApi to a seperate a seperate txt
class UserInput:
    # Fetches and saves transcript and comments to trancript_comments.json
    def trancript_comments_to_json(vid_pl_id):
        transcript_comments_dict = {}
        # Decide whether input is playlist or not, then get their ids
        if vid_pl_id.str.startswith("PL"):
            # Storing ids in video_ids, store trancript_comments in 
            # transcript_comments_dict and save it to json file
            video_ids = YoutubeDataAPI.fetch_video_ids_pl(vid_pl_id)
            transcript_comments_dict = fetch_transcript_comments(video_ids)
            FileHandler.save_transcript_comments(transcript_comments_dict)
        else:
            # Fetch video's trancript and comments to to dictionary
            transcript_comments_dict = fetch_transcript_comments(vid_pl_id)
            # Save dictionary to json file
            FileHandler.save_transcript_comments(transcript_comments_dict)

    # Reads and returns transcript_comments.json
    def read_transcript_comments():
        transcript_comments = FileHandler.read_transcript_comments()
        return transcript_comments
    
    def get_youtube_api_key():
        return None
    