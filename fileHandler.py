from googleapiclient.discovery import build
from ytTranscriptApi import fetch_transcript
import pandas as pd
import json
import os

# Class for handling video_ids in the permanent storage
class VideoIdHandler:
    FILE_NAME = "video_ids.txt"

    # Writes video ids line by line for later usage
    @staticmethod
    def save_video_ids(video_ids):
        # Get the directory of *main.py*
        main_dir = os.path.dirname(os.path.abspath(__import__("__main__").__file__))
        save_path = os.path.join(main_dir, VideoIdHandler.FILE_NAME)

        # Checks whether video_ids list or string, if not raises error
        if isinstance(video_ids, list):
            pass
        elif isinstance(video_ids, str):
            video_ids = [video_ids]
        elif not isinstance(video_ids, (list, str)):
            raise TypeError("video_ids should be list or string")
        
        # Opens the file in save_path writes each id into a new line
        with open(save_path, "w", encoding="utf-8") as file:
            file.write("\n".join(video_ids))

    # Read video ids line by line and returns a list of ids
    @staticmethod
    def read_video_ids():
        # Sets base_dir as cwd of executed file and joins it with FILE_NAME
        main_dir = os.path.dirname(os.path.abspath(\
            __import__("__main__").__file__))
        read_path = os.path.join(main_dir, VideoIdHandler.FILE_NAME)

        # Reads read_path(save_path) and assigns each line as list element
        # of video_ids
        with open(read_path, "r", encoding="utf-8") as file:
            video_ids = [line.strip() for line in file]

        # Returns video_ids list
        return video_ids



class FileHandler:
    # Saves transcript_comments to cwd
    def save_transcript_comments(merged_dict):
        base_dir = os.path.dirname(__file__)
        print(base_dir)
        save_path = os.path.join(base_dir, "transcript_comments.json")

        with open(save_path, "w", encoding="utf-8") as file:
            json.dump(merged_dict, file, ensure_ascii=False, indent=4)

    # Reads file transcript_comments and returns dictionary
    def read_transcript_comments():
        base_dir = os.path.dirname(__file__)
        read_path = os.path.join(base_dir, "transcript_comments.json")

        with open(read_path, "r", encoding="utf-8") as file:
            trancript_comments = json.load(file)
        return trancript_comments

    # Appends merged_dict to file rather than overwriting
    def append_transcript_comments(merged_dict):
        base_dir = os.path.dirname(__file__)
        save_path = os.path.join(base_dir, "transcript_comments.json")

        # Load existing content if the file exists
        if os.path.exists(save_path):
            with open(save_path, "r", encoding="utf-8") as file:
                existing_data = json.load(file)
        else:
            existing_data = {}

        # Update with new data (this preserves the existing ones)
        existing_data.update(merged_dict)

        # Save the updated content back to the file
        with open(save_path, "w", encoding="utf-8") as file:
            json.dump(existing_data, file, ensure_ascii=False, indent=4)






