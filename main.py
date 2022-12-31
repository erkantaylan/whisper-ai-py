import whisper
import sys
import getopt
import json


def convert(medila_file, output):
    model = whisper.load_model('large')
    result = model.transcribe(medila_file)
    file = open(output, 'a')
    file.write(json.dumps(result))
    file.close()


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
    convert(medila_file, output)


if __name__ == '__main__':
    # print('argv:')
    # print(sys.argv)
    main(sys.argv[1:])
    # convert()
