#!/usr/bin/env python
from __future__ import unicode_literals

# Allow direct execution
import os
import sys
import unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from test.helper import try_rm
from youtube_dl import YoutubeDL
from youtube_dl.utils import DownloadError

def _download_time(url, filename, StartTime, EndTime):
    """ Returns a true value if the file has been downloaded"""

    params = {
        'Start_Time': StartTime,
        'writeinfojson': True,
        'outtmpl': '%(id)s.%(ext)s',
    }

    ydl = YoutubeDL(params)
    ydl.add_default_info_extractors()
    json_filename = os.path.splitext(filename)[0] + '.info.json'
    try_rm(json_filename)
    try:
        ydl.download([url])
    except DownloadError:
        try_rm(json_filename)
    res = os.path.exists(json_filename)
    try_rm(json_filename)
    return res

class TestDownloadDelay(unittest.TestCase):
    def _assert_time(self, url, filename, StartTime):
        self.assertTrue(_download_time(url, filename, StartTime))

    def test_youtube(self):
        self._assert_time('https://www.youtube.com/watch?v=dQw4w9WgXcQ', 1, StartTime = 5)

if __name__ == '__main__':
    unittest.main()