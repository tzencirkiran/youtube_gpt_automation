from userInput import UserInput
from ytTranscriptApi import YoutubeDataAPI

while True:
    # Gets user input for their command
    user_input = input("Command: ").strip()

    # cmd: break
    if user_input == "break":
        break
    # cmd: fetch youtube data
    elif user_input.startswith("fetch youtube data"):
        vid_pl_id = user_input.split(" ")[-1]
        UserInput.trancript_comments_to_json(vid_pl_id)
        print("youtube data fetched and saved")
    # cmd: read youtube data
    elif user_input == "read youtube data":
        print(UserInput.read_transcript_comments())
    # cmd: set youtube api key
    elif user_input.startswith("set youtube api key"):
        api_key = user_input.split(" ")[-1]
        UserInput.set_youtube_api_key(api_key)

