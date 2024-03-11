import argparse
import glob
import os
import sys
import re
from assignment1.main import censor_phone_numbers, censor_dates, censor_names, censor_emails, censor_addresses
from pathlib import Path

def process_text(text, options):
    if options['names']:
        text = censor_names(text)
    if options['dates']:
        text = censor_dates(text)
    if options['phones']:
        text = censor_phone_numbers(text)
    #if options['emails']:
        #text = censor_emails(text)
    if options['address']:
        text = censor_addresses(text)
    return text

def process_files(input_pattern, output_dir, options, stats_flag):
    stats = {'files_processed': 0, 'characters_censored': 0, 'errors': 0}
    output_dir_path = Path(output_dir) / "gradescopetestsout"
    output_dir_path.mkdir(parents=True, exist_ok=True)

    for file_path in glob.glob(input_pattern, recursive=True):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            censored_content = process_text(content, options)
            censored_character_count = censored_content.count('#')
            stats['characters_censored'] += censored_character_count

            output_file_path = output_dir_path / (Path(file_path).name + '.censored')
            with open(output_file_path, 'w', encoding='utf-8') as file:
                file.write(censored_content)
            stats['files_processed'] += 1
        except Exception as e:
            print(f"Error processing file {file_path}: {e}", file=sys.stderr if stats_flag == 'stderr' else sys.stdout)
            stats['errors'] += 1

    stats_message = (f"Files processed: {stats['files_processed']}\n"
                     f"Characters censored: {stats['characters_censored']}\n"
                     f"Errors: {stats['errors']}")
    if stats_flag == 'stderr':
        sys.stderr.write(stats_message + '\n')
    elif stats_flag == 'stdout':
        sys.stdout.write(stats_message + '\n')


def main():
    parser = argparse.ArgumentParser(description='Censor sensitive information from text files')
    parser.add_argument('--input', type=str, required=True, help='Glob pattern for input files')
    parser.add_argument('--output', type=str, required=True, help='Output directory')
    parser.add_argument('--stats', choices=['stdout', 'stderr'], required=True, help='Where to write stats')
    parser.add_argument('--names', action='store_true', help='Censor names')
    parser.add_argument('--dates', action='store_true', help='Censor dates')
    parser.add_argument('--phones', action='store_true', help='Censor phone numbers')
    #parser.add_argument('--emails', action='store_true', help='Censor emails')
    parser.add_argument('--address', action='store_true', help='Censor addresses')

    args = parser.parse_args()
    os.makedirs(args.output, exist_ok=True)
    options = {
        'names': args.names,
        'dates': args.dates,
        'phones': args.phones,
        #'emails': args.emails,
        'address': args.address
    }
    process_files(args.input, args.output, options, args.stats)

if __name__ == '__main__':
    main()