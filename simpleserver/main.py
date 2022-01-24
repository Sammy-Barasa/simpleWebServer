from pathlib import Path
from serverclass import serverthread
import sys, ssl
from set_up import run_setup

# import logging

BASE_DIR= Path(__file__).resolve().parent.parent

print(BASE_DIR)
old_config={}


if __name__ == "__main__":
    # arguments are either main.py start/reload

    try:
        mode = sys.argv[1]

        if mode == "start":
            # run setup
            # validation before starting server
            # start surver
            cfig = run_setup(BASE_DIR)
            print(cfig)
            serverthread.ThreadedServer(config = cfig,set_up_complete=True,base_dir=BASE_DIR).run()
        elif mode =="reload":
            serverthread.ThreadedServer(config = {"port":3000,"host":"","ssl/tls":"True"},set_up_complete=True).run()
        else:
            print("use the below comand and available options.")
            print("sudo python3 main.py [start | reload]")
    
    except ssl.SSLEOFError as sslerr:
        print("Secure HTTPS connection is required")
        print(sslerr)

    except BaseException as B:
        print(type(B))
        print(B)
        raise
    except:
        print("")
        print("Use the below comand and available options.")
        print("sudo python3 main.py start | reload")










        