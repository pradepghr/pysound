import urllib
from urllib.request import Request, urlopen
from urllib.parse import urlparse, parse_qs, unquote
import pprint

def download(url):
    try:
        video_id = parse_qs(urlparse(url).query)['v'][0]
        url_data = urlopen('https://www.youtube.com/get_video_info?&video_id=' + video_id).read()
        url_info = parse_qs(unquote(url_data.decode('utf-8')))
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(url_info)
        # token_value = url_info['token'][0]
        # download_url = "https://www.youtube.com/get_video?video_id={0}&t={1}&fmt=18".format(video_id, token_value)
        video_title = url_info['title'][0] if 'title' in url_info else ''
        print(video_title)
        filename = video_title.encode('ascii', 'ignore').decode('ascii').replace("/", "-") + '.mp4'
        try:
            pass
            # content = urlopen(download_url).read()
            # stream = open(filename, 'wb')
            # stream.write(url_info)
            # stream.close()
        except Exception as e:
            print(e)
    except urllib.request.HTTPError as err:
        print(err)
    return filename


url = "https://www.youtube.com/watch?v=S2ILybG36-E"
download(url)
# print(result)
