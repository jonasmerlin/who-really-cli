# This module sets up the arguments and parses the arguments provided

import os
import argparse
import requests

def set_up_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("portrait", help="the portrait you want to classify")

    return parser.parse_args()

args = set_up_arguments()

def classify_portrait(portrait_path):
    url = "http://who-really.herokuapp.com/classification/portrait/upload"
    files = {"file": open(portrait_path, "rb")}
    r = requests.post(url, files=files)
    return r.text

if __name__ == '__main__':
    print(classify_portrait(args.portrait))
