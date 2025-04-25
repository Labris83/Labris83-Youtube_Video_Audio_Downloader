import yt_dlp
import sys

#The best already merged combination of video and audio will be downloaded
def download_video(vid_url, output_path):
    try:
        ydl_opts = {
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Save location + title
            'format': 'best'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([vid_url])
        print("\nDownload complete\n")
    except Exception as e:
        print(e)

#Best video and best audio are downloaded separately and merged into a video with the best overall quality
def download_best_video(vid_url, output_path):
    print('Warning!This is going to work only for systems that have ffmpeg installed')
    try:
        ydl_opts = {
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'format': 'bestvideo+bestaudio/best'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([vid_url])

        print("\nDownload complete\n")
    except Exception as e:
        print(e)

#The best available audio file will be downloaded(default format)
def download_audio(vid_url, output_path):
    try:
        ydl_opts = {
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'format': 'bestaudio/best',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([vid_url])
        print("\nDownload complete\n")
    except Exception as e:
        print(e)

#The best available audio file will be converted to the preferable audio format
def download_audio_format(vid_url, output_path, a_format):
    print('Warning!This is going to work only for systems that have ffmpeg installed')
    try:
        ydl_opts = {
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': a_format,
                'preferredquality': '192',
            }],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([vid_url])
        print("\nDownload complete\n")
    except Exception as e:
        print(e)


#Used as "Main Menu"
def get_option():
    while True:
        print('1.Download YouTube video')
        print('2.Download Youtube audio(best default format available)')
        print('3.Download Youtube video with the best quality(ffmpeg has to be installed)')
        print('4.Download Youtube audio with preferable format(ffmpeg has to be installed)')
        print('5.Quit\n')
        choice = input('Please enter the number left to your desired option: ').strip()

        if not choice:
            print('Empty input. Please try again\n')
        elif choice not in ['1', '2', '3', '4', '5']:
            print('Invalid input. Please try again\n')
        else:
            break
    return choice




while True:
    print('Warning!For best results install ffmpeg from the official website\n')
    user_choice = get_option()
    #In case user want's to quit, it's checked first
    if user_choice == '5':
        sys.exit()

    #The user has to input an url and a save path for any situation
    while True:
        video_url = input('Please enter the video\'s url: ').strip()
        if not video_url:
            print('Empty input. Please try again\n')
        else:
            while True:
                save_path = input('Please enter save path: ').strip()
                if not save_path:
                    print('Empty input. Please try again\n')
                else:
                    break
            break

    #User's choice calls the corresponding function
    if user_choice == '1':
        download_video(video_url, save_path)
    elif user_choice == '2':
        download_audio(video_url, save_path)
    elif user_choice == '3':
        download_best_video(video_url, save_path)
    elif user_choice == '4':
        #The preferable audio format is being selected
        while True:
            print('1.mp3(recommended)')
            print('2.wav')
            print('3.m4a')
            print('4.webm')
            audio_format = input(
                '\nWhich format of audio would you like(enter the number left to your option): ').strip()

            if not audio_format:
                print('Empty input. Please try again\n')
            elif audio_format not in ['1', '2', '3', '4']:
                print('Invalid input. Please try again\n')
            else:
                break


        audio_formats = {
            '1': 'mp3',
            '2': 'wav',
            '3': 'm4a',
            '4': 'webm',
        }
        #Based on user's input the selected audio format is passed through the audio_formats dictionary
        download_audio_format(video_url, save_path, audio_formats[audio_format])


