# This module sets up the arguments and parses the arguments provided

import os
import argparse
import requests

def set_up_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("portrait", help="the portrait you want to classify")
    parser.add_argument("-u", "--url", help="is the path a url?", action="store_true")

    return parser.parse_args()

args = set_up_arguments()

def classify_portrait(portrait_path):
    if args.url:
        url = "http://who-really.herokuapp.com/classification/portrait/url"
        data = {"url": portrait_path}
        r = requests.post(url, data=data)
    else:
        url = "http://who-really.herokuapp.com/classification/portrait/upload"
        files = {"file": open(portrait_path, "rb")}
        r = requests.post(url, files=files)
    return r.text

if __name__ == '__main__':
    print(classify_portrait(args.portrait))
