#! /usr/bin/python
import time
import argparse
from random import choice

def build_parser():
    parser = argparse.ArgumentParser(description='Learn what notes make up different types of chords!')
    parser.add_argument('scale_type', type=str, nargs='?', default='major', help='Declare type of scale')
    parser.add_argument('study_time', type=int, nargs='?', default=20, help='How many questions do you want asked?')
    args = vars(parser.parse_args())
    return args
args = build_parser()

def get_chords():
    major = {'C': 'C E G', 'Db': 'Db F Ab', 'D': 'D F# A', 'Eb': 'Eb G Bb', 'E': 'E G# B', 'F': 'F A C', 'F#': 'F# A# C#', 'G': 'G B D', 'Ab': 'Ab C Eb', 'A': 'A C# E', 'Bb': 'Bb D F', 'B': 'B D# F#'}
    minor = {'C': 'C Eb G', 'Db': 'Db E Ab', 'D': 'D F A', 'Eb': 'Eb Gb Bb', 'E': 'E G B', 'F': 'F G# C', 'F#': 'F# A C#', 'G': 'G Bb D', 'Ab': 'Ab B Eb', 'A': 'A C E', 'Bb': 'Bb Db F', 'B': 'B D F#'}
    all_scales = {'major': major, 'minor': minor}
    return all_scales

def study_magic():
    study_time = args.get('study_time')
    while study_time != 0:
        scale = args.get('scale_type')
        scale = choice(get_chords().keys()) if scale == 'random' else scale
        #print "dog", choice(get_chords().keys()) #if scale == 'random' else scale
        chord_name = choice(get_chords()[scale].keys())
        print chord_name, scale
        time.sleep(2.5)
        print get_chords()[scale][chord_name]
        time.sleep(4.5)
        print 
        study_time -= 1

def main():
    '''Music theory teacher
    $chords.py [scale]
    '''
    study_magic()

if __name__ == '__main__':
    main()
