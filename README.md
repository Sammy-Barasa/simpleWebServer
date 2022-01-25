# simpleWebServer
## Installation

simpleWebServe requires [Python3](https://python.org/) v3.8+ to run.

Clone the [simpleWebServer](https://github.com/Sammy-Barasa/simpleWebServer.git) repository.
```git clone repo```
change directrory to root of simpleWebServer
```cd repo```
All dependancies are in python standard library so no need for pip installing requirements.txt. 
To run simpleWebServer use the following commands:

change directory into simplserver
```cd simplserver```
start server with two commands
```python3 main.py start```
This runs a set_up function that checks for platform, python version,checks config file, and ssl/tsl .pem certificates. It reports and guides you on set up
```python3 main.py reload```
This runs the server with already completed setup. However, its functionallity has not been implemented in full. I recommend using ```start```

During set up, if no ```config.json``` in the root directory you will be promted to opt in for default confog file setup `config_default.json`. An example of config file is shown below.
``` 
{
    "http":{
        "ssl/tls":"True"},
    "server":{
        "port":16000,
        "host":""
    }
}
```
For future versions you will be able to add proxy options and that option can be added in this form.
``` 
{
    "http":{
        "ssl/tls":"True"},
    "server":{
        "port":16000,
        "host":"",
        "port":{"port":8000,
                "host":"localhost"
        }
    }
}
```
Proxy option in the current version errors with ```sslError```

Default config file is shown below
```
{
    "http":{
        "ssl/tls":"False"
    },
    "server":{
        "port":3000,
        "host":""
    }
}
```
#### Set up Process
After finding the configuration options simpleWebServer, looks for ssl/tls certificate files. These file certificates can be obtained from ssl/tls vendors or you can generate self endorsed certificates using ```OpenSSL```. simpleWebServer has a self endorsed OpenSSL certificates. SSL file certificates have ``.pem`` extention.
By default simpleWebServer has
```cert.pem```
```key.pem```
This are self endorsed OpenSSL certificates and have a downside of being unkown to most ssl/tls sites. If you obtain from a porpular vendor the better, make sure to name the files ```cert.pem``` and ```key.pem``` and place them in the root directory. simpleWebServer looks for these names by default.

When valid ssl/tls files are found, you will be promted to put the `passphrase` of your certificates. Correct passphrase guarantees a `secure transport layer` connection socket formed. Incorrect passphrase results to creating a non-secure transport layer. Hitting enter on the prompt with without pass phrase alsoresults to `non-secure transport`. For simpleWebServer, its passphrase is the name of the repository.

If set up is successful, simpleWebServer will listen on `config.server.port`

#### simpleWebServer architecture
SimpleWebServer is a multithreaded server. It creates new thread for every request and itself runs on a thread itself.
It accepts `GET` and `POST` requests on path `/`

During its running it is subject to wait time on linux environment after executing a request. A trying to reconnect request can cause `OSError: [Errno 9] Bad file descriptor` since simpleWebServer hasnot been optimized yet. In that case hit `ctrl+c` key to stop the server and start again.

#### Other things to note

- OpenSSL comes by default on linux environment. You can use the following command to create one  ``` openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365```
- ONLY TWO environment variables may be required incase.If you name othernamse asside from `cert.pem` and `key.pem` put them in environment variables such as shown below :
    -create environment im root directory
    ```python3 -m venv venv```
    -activate the environment
    ``` source venv/bin/activate```
    -create `.env` file in root directory 
    -use the following constants: `CERT` and `KEY`
    -Environment variable example:
    ```
    "CERT"=server.pem
    "KEY"=server_key.pem
    ```
- Using `ssl/tls:true` requires a `https request`. If the request is not https and the config is set to true, the following ssl error will occur
```ssl.SSLError: [SSL: HTTP_REQUEST] http request (_ssl.c:1131)```
- MOST EXAMPLES ARE USED IN LINUX PLATFORM. You can find what works in your platform

#### Development

Want to contribute? Great!

Install, make changes and send a pull request!

Other improvements are on the way

#### License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Free Software, Hell Yeah!**
