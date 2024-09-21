from pytube import YouTube
import streamlit as st
from tools import is_youtube_url, find_downloads_folder
import os

def Download(link, download_format):
    if not is_youtube_url(link):
        st.toast('Please insert a correct URL', icon="🚨")
        return

    try:
        youtubeObject = YouTube(link)
        st.write("ok")
    except Exception as e:
        st.toast(f"Video could not be found: {e}", icon="🚨")
        return
    
    # Find downloads folder
    downloads_folder = find_downloads_folder()
    st.write("ok2")
    try:
        # Handle MP4 download (video + audio)
        if download_format == 'MP4':
            st.write("ok2.5")
            stream = youtubeObject.streams.filter(file_extension='mp4').first()
            st.write("ok3")
            if stream:
                file_name = stream.default_filename
                stream.download(output_path=downloads_folder, filename=file_name)
                st.success(f"Download completed successfully: {file_name}")
            else:
                st.error("No suitable MP4 stream found.", icon="🚨")

        # Handle MP3 download (audio only)
        elif download_format == 'MP3':
            st.write("ok4")
            st.write(youtubeObject.streams)
            stream = youtubeObject.streams.filter(only_audio=True).first()
            st.write("ok5")
            if stream:
                out_file = stream.download(output_path=downloads_folder)
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'

                # Replace the old .mp3 file if it already exists
                if os.path.exists(new_file):
                    os.remove(new_file)
                os.rename(out_file, new_file)
                
                st.success("MP3 Download completed successfully!")
            else:
                st.error("No suitable MP3 stream found.", icon="🚨")

    except Exception as e:
        st.error(f"An error occurred during download: {e}")
