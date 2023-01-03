import sys
import getopt
from http.server import HTTPServer

from whisper_helper import WhisperHelper
import WhisperServer


def main(argv):
    opts, args = getopt.getopt(argv, "i:o:", ["ifile=", "ofile="])
    medila_file = ""
    output = ""
    for opt, arg in opts:
        if opt in ("-i", "--ifile"):
            medila_file = arg
        elif opt in ("-o", "--ofile"):
            output = arg
        else:
            print("error: " + argv)
            sys.exit()
    helper = WhisperHelper()
    helper.save_to_file(medila_file, output)


def start():
    webServer = HTTPServer(("localhost", 8000), WhisperServer.WhisperServer)
    print("Server started http://%s:%s" % ("localhost", 8000))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")


if __name__ == '__main__':
    # print('argv:')
    # print(sys.argv)
    # main(sys.argv[1:])
    # convert()
    start()
