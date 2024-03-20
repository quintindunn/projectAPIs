# Date 3/19/2024
# Author: Quintin Dunn
# Description: This is just a project to hold singular API endpoints for my other projects.

from flask import Flask
from youtube_transcript_api import YouTubeTranscriptApi


app = Flask(__name__)


@app.get("/get-youtube-transcript/<string:youtube_id>")
async def get_youtube_transcript(youtube_id: str):
    print(youtube_id)
    transcripts = YouTubeTranscriptApi.list_transcripts(youtube_id)

    for transcript in transcripts:
        if transcript.is_generated:
            return transcript.fetch()

    if transcripts:
        return transcripts[0].fetch()
    return {}


if __name__ == '__main__':
    app.run(port=8000, debug=True)