#!/usr/bin/env python3
"""Batch transcode MKV files into mp4's"""

import argparse
import glob
import os
import shutil
import subprocess
import yaml

def main():
    parser = argparse.ArgumentParser(description="""\
Batch transcode MKV files into mp4's suitable for import to Plex

Search all directories in input-dir for directories of MKV files, and then
transcode the contents of those directories, giving the largest file the
same name as the directory and storing the remaining files in a subdirectory
called "Behind The Scenes".  The resulting directory is copied to output-dir,
and the original input directory is copied to archive-dir.

Wthe main title, and the remaining tracks will appear as "Behind the
Scenes" extras.hen the directories in input-dir are in the form "Title
(Year)" and output-dir is a directory that Plex searches for movies, the
largest video will appear in Plex as the main title, and the remaining
tracks will appear as "Behind the Scenes" extras.
""")
    parser.add_argument('--input-dir', default='incoming',
                        help='Directory containing mkv files to be
                        transcoded')
    parser.add_argument('--output-dir', default='Movies',
                        help='Directory in which to write transcoded
                        files')
    parser.add_argument('--archive-dir', default='loaded',
                        help='Directory in which to place source of '
                             'sucessfully transcoded files')
    args = parser.parse_args()

    transcode_tmp = '/tmp/transcode'
    for movie_title in os.listdir(args.input_dir):
        print(movie_title)
        titles = glob.glob(os.path.join(args.input_dir, movie_title, '*.mkv'))
        if len(titles) == 0:
            continue
        titles = sorted(titles, key=os.path.getsize, reverse=True)
        # ASSUME: biggest .mkv file is the main feature, and others are extras
        main_mkv = titles.pop(0)
        dest_dir = os.path.join(transcode_tmp, movie_title)
        dest_file = os.path.join(dest_dir, movie_title + '.mp4')
        if not os.path.isdir(dest_dir):
            os.makedirs(dest_dir)
        transcode(main_mkv, dest_file)

        # Put all the extras into "Behind The Scenes" and sort them out later
        dest_dir = os.path.join(dest_dir, "Behind The Scenes")
        if not os.path.isdir(dest_dir):
            os.makedirs(dest_dir)
        for mkv in titles:
            _, mkv_file = os.path.split(mkv)
            dest_file = os.path.join(dest_dir, mkv_file.replace('.mkv','.mp4'))
            transcode(mkv, dest_file)
        # Move completed movies to the done area and archive input
        shutil.move(os.path.join(transcode_tmp, movie_title), args.output_dir)
        shutil.move(os.path.join(args.input_dir, movie_title), args.archive_dir)


def transcode(in_path, out_path):
    """Transcode the movie"""
    #print(['HandBrakeCLI', '-Z', 'Super HQ 1080p30 Surround', '-O',
    subprocess.run(['HandBrakeCLI', '-Z', 'Super HQ 1080p30 Surround', '-O',
                   '-i', in_path, '-o', out_path])


if __name__ == "__main__":
    main()
