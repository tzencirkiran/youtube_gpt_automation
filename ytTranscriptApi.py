from youtube_transcript_api import YouTubeTranscriptApi

# Create an object for YouTubeTranscriptApi
ytt_api = YouTubeTranscriptApi()

## A method for fetching transcript of given youtube videos ids
def fetch_transcript(video_ids):
    # Checks whether video_ids list or string, if not raises error
    # If video_ids is string, converts it to a list
    if isinstance(video_ids, list):
        pass
    elif isinstance(video_ids, str):
        video_ids = [video_ids]
    elif not isinstance(video_ids, (list, str)):
        raise TypeError("video_ids should be list or string")
        
    id_transcript_dict = {}
    for video_id in video_ids:
        fetched_transcript = ytt_api.fetch(video_id, languages=["en", "tr"])

        transcript_text_list = []
        for snippet in fetched_transcript:
            transcript_text_list.append(snippet.text)
        
        transcript_text = " ".join(transcript_text_list)
        id_transcript_dict[video_id] = transcript_text
        
    return id_transcript_dict
    
    

