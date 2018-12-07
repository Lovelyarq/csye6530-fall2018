'''
Created on 2018年12月4日

@author: jrq
'''
from labs.module07 import CoapClientConnector

import getopt
import socket
import sys

from coapthon.client.helperclient import HelperClient
from coapthon.utils import parse_uri


client = None


def usage():  # pragma: no cover
    print("Command:\tcoapclient.py -o -p [-P]")
    print("Options:")
    print("\t-o, --operation=\tGET|PUT|POST|DELETE|DISCOVER|OBSERVE")
    print("\t-p, --path=\t\t\tPath of the request")
    print("\t-P, --payload=\t\tPayload of the request")
    print("\t-f, --payload-file=\t\tFile with payload of the request")


def client_callback(response):
    print("Callback")


def client_callback_observe(response):  # pragma: no cover
    global client
    print("Callback_observe")
    check = True
    while check:
        chosen = eval(input("Stop observing? [y/N]: "))
        if chosen != "" and not (chosen == "n" or chosen == "N" or chosen == "y" or chosen == "Y"):
            print("Unrecognized choose.")
            continue
        elif chosen == "y" or chosen == "Y":
            while True:
                rst = eval(input("Send RST message? [Y/n]: "))
                if rst != "" and not (rst == "n" or rst == "N" or rst == "y" or rst == "Y"):
                    print("Unrecognized choose.")
                    continue
                elif rst == "" or rst == "y" or rst == "Y":
                    client.cancel_observing(response, True)
                else:
                    client.cancel_observing(response, False)
                check = False
                break
        else:
            break


def main():  # pragma: no cover
    global client
    op = "GET"
    path = "coap://localhost:5683"
    payload = "haha"
    
    host = "localhost"
    port = 5683

    client = HelperClient(server=(host, port))
    
    
    
    if op == "GET":
        if path is None:
            print("Path cannot be empty for a GET request")
            usage()
            sys.exit(2)
        response = client.get(path)
        print((response.pretty_print()))
        client.stop()
    elif op == "DELETE":
        if path is None:
            print("Path cannot be empty for a DELETE request")
            usage()
            sys.exit(2)
        response = client.delete(path)
        print((response.pretty_print()))
        client.stop()
    elif op == "POST":
        if path is None:
            print("Path cannot be empty for a POST request")
            usage()
            sys.exit(2)
        if payload is None:
            print("Payload cannot be empty for a POST request")
            usage()
            sys.exit(2)
        response = client.post(path, payload)
        print((response.pretty_print()))
        client.stop()
    elif op == "PUT":
        if path is None:
            print("Path cannot be empty for a PUT request")
            usage()
            sys.exit(2)
        if payload is None:
            print("Payload cannot be empty for a PUT request")
            usage()
            sys.exit(2)
        response = client.put(path, payload)
        print((response.pretty_print()))
        client.stop()
    else:
        print("Operation not recognized")
        usage()
        sys.exit(2)


if __name__ == '__main__':  # pragma: no cover
    main()