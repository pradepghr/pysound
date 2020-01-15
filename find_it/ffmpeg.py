import subprocess
import celery

from find_it import app


def convert_to_mp3(source=None, acodec='libmp3lame', bitrate='192k'):
    """
    Convert the source audio to new format
    :param acodec:
    :param acodec:
    :param source:
    :param bitrate:
    :param new_name:
    :return: String:

    # Example: ffmpeg - i <source> - acodec libmp3lame - ab 192k <new_name>.mp3
    # -i audio.wav : source file
    # -acodec mp3 : "mp3" audio codec to create the target file.
    # -ab 192k : audio bitrate
    # audio.mp3 : Dump the encoded audio data into a file called audio.mp3.
    """
    filename = app.config['BASE_DIR'] + '/media/output.mp3'
    try:
        return_code = subprocess.check_call(['ffmpeg', '-i', source, '-acodec', acodec, '-ab', bitrate, filename])
    except subprocess.CalledProcessError as error:
        print('Failed\n---------')
        print(error)
    else:
        print('Success')


def slice_and_convert_mp3(**kwargs):
    """
    Slice and Convert the source audio to new format
    :param source:
    :param codec:
    :param bitrate:
    :param new_name:
    :return:

    Example: ffmpeg -i yatri.mp3 -acodec libmp3lame -ab 192k -ss 00:10:00 -t 00:6:00 audio.mp3
     -ss 00:10:00 or -ss:600 : starts after 10 min into or 600 sec
     -t 00:06:00 or -t 300: for 5 min or 300 sec
    """
    source = kwargs['source']
    acodec = kwargs.get('acodec', 'libmp3lame')
    bitrate = kwargs.get('bitrate', '292k')
    output = kwargs['output']
    start_time = kwargs['start_time']
    duration = kwargs['duration']

    try:
        # return_code = subprocess.check_call(['ffmpeg', '-i', source, '-acodec', acodec, '-ab', bitrate,
        #                                      '-ss', start_time, '-t', duration, output])
        process = subprocess.Popen(['ffmpeg', '-i', source, '-acodec', acodec, '-ab', bitrate, '-ss', start_time,
                                  '-t', duration, output], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        process.communicate(input=b"y")
    except subprocess.CalledProcessError as error:
        print('Failed\n---------')
        print(error)
    else:
        print('Success')


# base_dir = '/home/pghimire/examples/pysound/media/'

# slice_and_convert_mp3(source=base_dir + 'yatri.mp3', acodec='libmp3lame', bitrate='192k',
#                       start_time='00:12:26', duration='00:01:00', output=base_dir + 'output.mp3')
# slice_and_convert_mp3(source=base_dir + 'yatri.mp3', start_time='00:12:26', duration='00:01:00',
#                       output=base_dir + 'output.mp3')
