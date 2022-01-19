from pathlib import Path
from serverclass import serverthread


BASE_DIR= Path(__file__).resolve().parent.parent

print(BASE_DIR)


if __name__ == "__main__":
    serverthread.ThreadedServer(config = {"port":8000,"host":""}).run()