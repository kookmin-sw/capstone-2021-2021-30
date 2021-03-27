"""
need to install pytube(https://python-pytube.readthedocs.io/en/latest/index.html)
  !pip install pytube
"""

from pytube import YouTube

YouTube('https://youtu.be/2lAe1cqCOXo').streams.first().download()
