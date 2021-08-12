import csv
import os
import argparse

from Levenshtein import distance


def get_cmd_line_args():
    parser = argparse.ArgumentParser(
        description='Prints all the names with the desired Levenshtein distance from a csv file')

    parser.add_argument('--file', '-f', type=str, required=True,
                        help='Path and name to desired file')

    parser.add_argument('--ld', '-l', type=int, required=True,
                        help='Desired Levenshtein Distance')

    parser.add_argument('--comparing_str', '-c', type=str, required=True,
                        help='The comparing string')

    parser.add_argument('--idx_column', '-i', type=int, required=True,
                        help='index of the column with the desired names')

    parser.add_argument('--header_present', '-hp', action='store_true',
                        help='True if the first line of the file is an header')

    args = parser.parse_args()

    print('Levenshtein Distance: {}'.format(args.ld))
    print('Comparing String: {}'.format(args.comparing_str))
    print('File Name: {}'.format(args.file))
    print('Index of the column: {}'.format(args.idx_column))
    print('Header Present: {}'.format(args.header_present))
    print()
    return args.file, args.ld, args.comparing_str, args.header_present, args.idx_column


def print_ld_matches(file_path_name, desired_ld, comparing_str, header_present, idx_column):
    if not os.path.isfile(file_path_name):
        print('File {} does not exists'.format(file_path_name))
        exit(1)

    matching_set = set()

    try:
        with open(file_path_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            if header_present:
                next(csv_reader)

            for row in csv_reader:
                if row:
                    if distance(comparing_str, row[idx_column]) == desired_ld:
                        matching_set.add(row[idx_column])

        print('Found {} matching names: '.format(len(matching_set)))
        print(', '.join(matching_set))

    except Exception as e:
        print('Exception: {}, please check file {}'.format(e, file_path_name))
        exit(1)


if __name__ == '__main__':
    file, ld, cs, hp, idx = get_cmd_line_args()
    print_ld_matches(file_path_name=file, desired_ld=ld, comparing_str=cs, header_present=hp, idx_column=idx)
