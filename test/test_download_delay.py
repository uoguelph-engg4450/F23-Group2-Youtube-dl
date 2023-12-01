#!/usr/bin/env python
from __future__ import unicode_literals

# Allow direct execution
import os
import sys
import unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from youtube_dl.download_delay import DownloadDelay
from datetime import datetime, timedelta
from test.helper import try_rm
from youtube_dl import YoutubeDL
from youtube_dl.utils import DownloadError

class TestDownloadDelay(unittest.TestCase):
    test_video_url = "https://youtu.be/dQw4w9WgXcQ?si=_KXToD_sq153eIcm"

    def setUp(self):
        print("Write here")

    def test_downloadtime(self, url, filename, StartTime):
        print("Write Here")
    
    #Test to see if the current time and delay time are differe
    def schedule_delay_different_time(self):
        current_time = datetime.strptime('2:30', '%H:%M')
        download_time = datetime.strptime('5:55', '%H:%M')
        download_time = DownloadDelay(current_time, target_time)

        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            download_delay.schedule_delay()

        output = mock_stdout.getvalue()
        expected_output = "Time is different than current time, so delay will start at 5:55"
        delf.assertEqual(output, expected_output)

    #Test to see is the current time and delay time are the same
    def schedule_delay_same_time(self):
        current_time = datetime.strptime('2:30', '%H:%M')
        download_time = datetime.strptime('2:30', '%H:%M')
        download_time = DownloadDelay(current_time, target_time)

        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            download_delay.schedule_delay()

        output = mock_stdout.getvalue()
        expected_output = "Time is same as different time, delay will no be applied"
        delf.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()