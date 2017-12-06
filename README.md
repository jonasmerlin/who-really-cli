# who-really-cli

CLI for Who Really?! 

Who Really?! requires a working python 3 installation. This guide assumes you want to use the script from the location you'll clone the repo to and that you'll do so using a virtual python environment for portability.

## Setup

After you clone the repo, run 

`python3 -m venv env`

then

`source env/bin/activate`

and then

`pip install -r requirements.txt`

You can also simply run `setup.sh`, which does these 3 things for you.

## Usage

After that, you'll be able to simply call

`python who-really.py path/to/your/portrait`

For testing purposes, you can use the `test-portrait.jpg` that comes with the repo.

or, if you want to classify a URL

`python who-really.py --url <url>`
