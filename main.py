import streamlit as st
from pytube import YouTube
from downloader import Download
import os


def interface():
    # ----------------------------- CaptainTube logo ----------------------------- #
    col1, col2, col3 = st.columns([2, 1, 2])

    with col2:
        st.image("logo/captain_tube_logo.png", width=120)
    
    
    # Radio button to choose between MP3 and MP4
    st.markdown("***")
    download_option = st.radio("Choose the format to download:",("MP3", "MP4"), horizontal = True)

    # Textbox for the YouTube link
    youtube_link = st.text_input("Enter the YouTube URL:")

    # Display user's selection and YouTube link
    if youtube_link:
        if download_option == 'MP3':
            if st.button("Download MP3"):
                Download(youtube_link, download_option)
        elif download_option == 'MP4':
            if st.button("Download MP4"):
                Download(youtube_link, download_option)
        
    




if __name__ == '__main__': 
    interface()