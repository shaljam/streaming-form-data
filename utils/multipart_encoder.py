from argparse import ArgumentParser
import mimetypes

from requests_toolbelt import MultipartEncoder


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('-f', '--filename', help='Data file')
    parser.add_argument('-d', '--decode', help='Decode output before printing',
                        action='store_true')
    return parser.parse_args()


def main():
    args = parse_args()

    with open(args.filename, 'rb') as file_:
        content_type = mimetypes.guess_type(args.filename)[0]

        fields = {
            'name': 'random name',
            'age': '10',
            'file': (args.filename, file_, content_type)
        }

        encoder = MultipartEncoder(fields=fields)

        if args.decode:
            print(encoder.to_string().decode('utf-8'))
        else:
            print(encoder.to_string())


if __name__ == '__main__':
    main()