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

class TestDownloadDelay(unittest.TestCase):
    test_video_url = "https://youtu.be/dQw4w9WgXcQ?si=_KXToD_sq153eIcm"

    def setUp(self):
        print("Write here")

    def test_downloadtime(self, url, filename, StartTime):
        print("Write Here")


if __name__ == '__main__':
    unittest.main()