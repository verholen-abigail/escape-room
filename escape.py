from escaperoom.setup import start
import argparse
from escaperoom.transcript import Transcript

parser = argparse.ArgumentParser()
parser.add_argument("--start", default="intro")
parser.add_argument("--transcript", default="run.txt")

args = parser.parse_args()

if __name__ == "__main__":
    transcript = Transcript(args.transcript)
    start(args.start, transcript)