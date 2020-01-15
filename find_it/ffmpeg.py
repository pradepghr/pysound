import os
import time
import subprocess
from find_it import app


def convert_to_mp3(source=None, codec='libmp3lame', bitrate='192k', new_name='audio'):
    """
    Convert the source audio to new format
    :param source:
    :param codec:
    :param bitrate:
    :param new_name:
    :return:
    """
    # Example: ffmpeg - i <source> - acodec libmp3lame - ab 192k <new_name>.mp3
    # -i audio.wav : source file
    # -acodec mp3 : "mp3" audio codec to create the target file.
    # -ab 192k : audio bitrate
    # audio.mp3 : Dump the encoded audio data into a file called audio.mp3.
    filename = app.config['BASE_DIR'] + '/media/audio.mp3'
    try:
        return_code = subprocess.check_call(['ffmpeg', '-i', '../media/audio.mp3'])
    except subprocess.CalledProcessError as error:
        print('Failed\n---------')
        print(error)
    else:
        print('Success')


src = app.config['BASE_DIR'] + '/media/' + 'yatri.mp3'
convert_to_mp3(src)
