from __future__ import absolute_import, unicode_literals
import subprocess
import json

from find_it.ffmpeg import convert_to_mp3
from task_queue.celery_app import c_app

dir = '/home/pghimire/examples/pysound/media/download/%(title)s-acodec:%(acodec)s-abr:%(abr)s.%(ext)s'
d = '/home/pghimire/examples/pysound/media/download/file.json'

@c_app.task
def download(url):
    try:
        check_process = subprocess.Popen(['youtube-dl', '-j', '-o', dir, url], stdin=subprocess.PIPE,
                                         stdout=subprocess.PIPE)
    except subprocess.CalledProcessError as err:
        print(err)
    else:
        for line in check_process.stdout.readlines():
            json_data = json.loads(line.decode('utf-8'))
            filesize = int(json_data['requested_formats'][0]['filesize']) + int(json_data['requested_formats'][0]['filesize'])
            title = json_data['fulltitle']
            duration = json_data['duration']
            acodec = json_data['acodec']
            bitrate = json_data['abr']
            ext = json_data['ext']
        # if int(filesize) > 1*10**6:
        #     raise Exception('Video size too large')

        try:
            # process = subprocess.Popen(['youtube-dl', '--max-filesize', '25k', '-R' '5', '-o', base_dir, url],
            #                            stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            process = subprocess.Popen(['youtube-dl', '-o', dir, url],
                                       stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        except subprocess.CalledProcessError as err:
            print(err)
        else:
            print('Success')


url = "https://www.youtube.com/watch?v=S2ILybG36-E"
u = "https://www.youtube.com/watch?v=9tjdswqGGVg"
s= "https://www.youtube.com/watch?v=668nUCeBHyY"

# download(s)
download.delay(s)
print('running')
