import json,os,sys

def get_config(base_directory,file):
    """check for config file from root of directory"""
    path_file = os.path.join(base_directory,file)
    print(f"constructed path is: {path_file}")
    try:
        with open(path_file,'r') as f:
            conf = json.load(f)
            print(conf)
            return conf
    except json.decoder.JSONDecodeError as err:
        print(err)
        print("\nENSURE YOUR JSON_FILE IS IN CORRECT JSON FORMAT FOR PYTHON3!!!")
        # raise
        return False

    except FileNotFoundError:
        print(f"\nNo config file found in {path_file}")
        print("Ensure your config file is named config.json at root directory of the server")
        print("\n To use default config select below")
        print("\t1. yes")
        print("\t2. no")
        res = int(input(" "))
        if res == 1:
            deflt=get_config(base_directory,"config_default.json")
            print(" Using default config")
            return deflt
        print("quiting setup>>>>")
        sys.exit(1)
        return False
        
    except BaseException as e:
        print(type(e))
        print(e)
        # raise
        return False


def check_ssl_cert(basedirectory,file1,file2,plat):
    """check for ssl certificates .pem from root of directory"""

    path_file1 = os.path.join(basedirectory,file1)
    path_file2 = os.path.join(basedirectory,file2)
    print(f"constructed path 1 is: {path_file1}")
    print(f"constructed path 2 is: {path_file2}")
    try:
        with open(path_file1,'r'):
            pass
        with open(path_file2,'r'):
            return True

    except FileNotFoundError:
        print(f"\nNo .pem file found in {path_file1}")
        print(f"\nNo .pem file found in {path_file2}")
        if plat =="Linux":
            print(f"For {plat} platform, you can generate self endorsing ssl certificates. Use the below command on your terminal")
            print("\nopenssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365")
            return False
        print("\tYou can generate .pem ssl certificates and place them on your root directory. SET file names on .env with CERT and KEY strings")
        return False
        
    except BaseException as e:
        print(type(e))
        print(e)
        # raise
        return False