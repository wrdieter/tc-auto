#!/usr/bin/env python3
"""Batch transcode MKV files into mp4's"""

import argparse
import glob
import os
import subprocess
import yaml

def main():
    parser = argparse.ArgumentParser(description="Batch transcode MKV files into mp4's")
    args = parser.parse_args()

    incoming = 'incoming'
    for movie_title in os.listdir(incoming):
        print(movie_title)
        for mkv in glob.glob(os.path.join(incoming, movie_title, '*.mkv')):
            print(mkv)
            _, mkv_file = os.path.split(mkv)
            dest_dir = os.path.join('transcoded', movie_title)
            if mkv_file != 'title00.mkv':
                dest_dir = os.path.join(dest_dir, "Behind The Scenes")
                dest_file = os.path.join(dest_dir, mkv_file.replace('.mkv','.mp4'))
            else:
                dest_file = os.path.join(dest_dir, movie_title + '.mp4')
            if not os.path.isdir(dest_dir):
                os.makedirs(dest_dir)
            #print(['HandBrakeCLI', '-Z', 'Super HQ 1080p30 Surround', '-O',
            subprocess.run(['HandBrakeCLI', '-Z', 'Super HQ 1080p30 Surround', '-O',
                           '-i', mkv, '-o', dest_file])


if __name__ == "__main__":
    main()
