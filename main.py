# main.py
#    runs reddit experiment
# by: Noah Syrkis

from src import utils
from src import run_daily
import pandas as pd


# main function
def main():
    client = utils.get_client()
    data   = utils.setup()
    data   = run_daily(client, data)
    data.to_csv("data.csv", index=False)

if __name__ == "__main__":
    main()

