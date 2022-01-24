import platform,os
import string
from utils import get_config, check_ssl_cert


def run_setup(base_dir):

    conf_to_use={}
    # old_config
    print("\n")
    print("simpleWebServer Setup\n")
    # check python version
    pyv = platform.python_version()
        # report on version
    print(f"Found python {pyv} \n")
        # act on version
    # check for config file
    old_config = get_config(base_dir,"config.json")
    conf_to_use = old_config  # to be verified on ssl/tls

    # check platform; accept only linux 
    plt = platform.system() # repor on platform
        # act on platform
    print(f"\nFound platform {plt}")
    
    # check for ssl/tls http status from http
    sthttp = old_config['http']['ssl/tls']
    
    if sthttp:
        
        # find key.pem, cert.pem from root directory
        print(os.getenv("CERT"))
        print(sthttp)
        certs = check_ssl_cert(base_dir,os.environ.get("CERT"),os.environ.get("KEY"),plt)
        if certs:
            # accept only linux  for ssl/tls for easy setup
            conf_to_use["http"]=old_config["http"]
            return
        # ensure ssl/tls fase if no cert.pem,key.pem files
        conf_to_use["http"]={"ssl/tls":"False"}
        return
    
        
    # set server states: alive, restarting, reloading, failed
        # start  -- initial starting, set_up_complete state; con_fig_has_changed
            #    -- store current value of config in memory
            #    -- alive state true,started  at LINK
        # reload -- close connection and start it again without set up, can_reload state, reloading state
            #    -- can reload only if setup was successfull and not changed; report config change status

    # return(config{}, set_up_complete,con_fig_has_changed)
    return conf_to_use



# ##################################### todo1 #################################### # done
        # show server setup process on the terminal
        # report on python version, if not above 3.6 recomend re install and stop
        # report on platform, if not linux ssl false
        # found config file, not found quit/use default config prompt
        # if default skip pem, 
        # if config and linux and ssl: find pem; 
            # if non recommend with quiting and run pem instruction on root dir
            # if found;validate pem;?assert ssl/tls valid: ssl/false