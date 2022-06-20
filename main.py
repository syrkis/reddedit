# main.py
#    runs reddit experiment
# by: Noah Syrkis

from src import utils, run_daily
import pandas as pd
import sys


# main function
def main():
    path   = sys.argv[1]
    client = utils.get_client()
    data   = utils.setup(path)
    data   = run_daily(client, data)
    data.to_csv(path)

if __name__ == "__main__":
    main()

