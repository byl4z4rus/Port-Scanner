import port_scanner
import argparse

def main():

    parser = argparse.ArgumentParser(description="""Tool's Function: Scanning port status Usage: python main.py --port 1-100 --IPadd 127.0.0.1""")
    parser.add_argument("--port", dest="port" ,type=str,help="Target port range")
    parser.add_argument('--IPadd', dest="host" ,type=str,help="Target IP address")

    args=parser.parse_args()
    host, port_range= args.host, args.port
    port_range=str(port_range)

    scanner_object = port_scanner.Scanning()
    scanner_object.set(host, port_range)
    scanner_object.scan_port()

if __name__ == '__main__':
    main()
    






