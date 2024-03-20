# Date 3/19/2024
# Author: Quintin Dunn
# Description: This is just a project to hold singular API endpoints for my other projects.

from flask import Flask
from youtube_transcript_api import YouTubeTranscriptApi


app = Flask(__name__)


cache = {}


@app.get("/get-youtube-transcript/<string:youtube_id>")
async def get_youtube_transcript(youtube_id: str):
    transcripts = YouTubeTranscriptApi.list_transcripts(youtube_id)

    transcript_fetched = {}

    if youtube_id in cache:
        return cache.get(youtube_id)

    for transcript in transcripts:
        if transcript.is_generated:
            transcript_fetched = transcript.fetch()
            break
    else:
        if transcripts:
            transcript_fetched = transcripts[0].fetch()

    return transcript_fetched or {}


if __name__ == '__main__':
    app.run(port=8000, debug=True)