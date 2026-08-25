import sys
import datetime as dt

def logger(msg, no_return=False, flush=False, primer='', exit = 0):
    date_time = dt.datetime.now()
    print(f"{primer}[{date_time.strftime('%X')}] {msg}", end="" if no_return else "\n", flush=flush)
    if exit:
        sys.exit()
