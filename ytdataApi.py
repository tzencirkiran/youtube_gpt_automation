from googleapiclient.discovery import build
import pandas as pd
import os
from dotenv import load_dotenv

class YoutubeDataAPI:

    def __init__(self):
        # reads env variables and opens access from os.getenv
        load_dotenv()
        self.yt_api_key = os.getenv("YT_API_KEY")
        # Creating a youtube object
        self.youtube = build("youtube", "v3", developerKey=self.yt_api_key)

    ## A search method that returns video ids
    def search(self, keyword):
        # Request for search from youtube data api
        request = self.youtube.search().list(
            q=keyword,
            maxResults=10, 
            part="snippet",
            type="video"
        )

        response = request.execute()

        # Find and save video ids
        video_ids = []

        for item in response["items"]:
            try:
                video_ids.append(item["id"]["videoId"])
            except:
                print("Error! Skipping this video's id appension. Error might be "
                "due to a playlist occurence.")
                continue

        return video_ids


    ## A method that pulls comments from given video ids
    def pull_comments(self, video_ids):
        # Checks whether video_ids list or string, if not raises error
        if isinstance(video_ids, list):
            pass
        elif isinstance(video_ids, str):
            video_ids = [video_ids]
        elif not isinstance(video_ids, (list, str)):
            raise TypeError("video_ids should be list or string")

        # Request for comments from youtube data api
        id_comment_dict = {}
        for video_id in video_ids:
            pageToken = None
            comment_list = []
            while True:
                request = self.youtube.commentThreads().list(
                    videoId=video_id,
                    part="snippet",
                    maxResults=100,
                    pageToken=pageToken,
                    textFormat="plainText"
                )

                response = request.execute()

                # Appending each comment to comment_list
                for item in response["items"]:
                    try:
                        comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
                        comment_list.append(comment)
                    except:
                        print("Skipping this comment's appension")
                        continue

                # Assigning nextPageToken to pageToken for next iteration of while loop
                pageToken = response.get("nextPageToken")

                # If no more pages left to iterate in the while loop, break the loop
                if pageToken == None:
                    break

            # From all pages (100 comments per page), comments gathered in comment_list
            # A dictionary that assigns comment_list according to its id
            id_comment_dict[video_id] = comment_list
        
        return id_comment_dict

    # Returns video titles according to their video ids
    def fetch_video_titles(self, video_ids):
        # Checks whether video_ids list or string, if not raises error
        if isinstance(video_ids, list):
            pass
        elif isinstance(video_ids, str):
            video_ids = [video_ids]
        elif not isinstance(video_ids, (list, str)):
            raise TypeError("video_ids should be list or string")
        
        request = self.youtube.videos().list(
                part="snippet",
                id=video_ids
            )
        response = request.execute()

        video_titles = []
        for item in response["items"]:
            video_titles.append(item["snippet"]["title"])

        return video_titles

    # Fetch video ids inside a playlist, returns video_ids as list
    def fetch_video_ids_pl(self, pl_id):
        nextPageToken = None
        video_ids = []
        # Until each page's videos' ids gathered, this loop continues
        while True:
            request = self.youtube.playlistItems().list(
                part="id,contentDetails",
                playlistId=pl_id,
                maxResults=50,
                pageToken=nextPageToken
            )

            response = request.execute()

            # Appends each video's id to video_ids
            for item in response["items"]:
                video_ids.append(item["contentDetails"]["videoId"])

            # Stores nextPageToken for the next while loop iteration
            nextPageToken = response.get("nextPageToken")

            # if no pages left i.e. nextPageToken is None, breaks the while loop
            if nextPageToken == None:
                break

        return video_ids
    