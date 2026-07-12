import time
import socket
import sys

def system_seconds_since_1900():
    seconds_delta = 2208988800
    seconds_since_unix_epoch = int(time.time())
    seconds_since_1990_epoch = seconds_since_unix_epoch + seconds_delta

    return seconds_since_1990_epoch

domain = "time.nist.gov"
port = 37



while(1):
    s = socket.socket()
    target = (domain,port)
    s.connect(target)
    d = s.recv(4096)
    t = int.from_bytes(d, "big")
    print(f"NIST time : {t}")
    t_1900 = system_seconds_since_1900()
    print(f"System time : {t_1900}")
    if len(d) == 0:
        break