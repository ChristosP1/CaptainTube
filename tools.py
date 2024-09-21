import re
from pathlib import Path

def is_youtube_url(url):
    # Regular expression pattern to match various YouTube URL formats
    youtube_regex = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')

    # Compile the regex
    youtube_pattern = re.compile(youtube_regex)

    # Check if the URL matches the pattern
    match = youtube_pattern.match(url)

    if match:
        return True
    else:
        return False
    
    
def find_downloads_folder():
    downloads_path = str(Path.home() / "Downloads")
    return downloads_path