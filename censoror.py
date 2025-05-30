import argparse
import glob
import os
import sys
import re
from assignment1.main import censor_phone_numbers, censor_dates, censor_names,  censor_addresses
from pathlib import Path

def process_text(text, flags):
    original_text = text
    censor_stats = {'names': 0, 'dates': 0, 'phones': 0, 'emails': 0, 'address': 0}

    if flags['names']:
        text_before = text
        text,count = censor_names(text)
        censor_stats['names'] = count

    if flags['dates']:
        text_before = text
        text,count = censor_dates(text)
        censor_stats['dates'] = count

    if flags['phones']:
        text_before = text
        text,count = censor_phone_numbers(text)
        censor_stats['phones'] = count
    #if flags['emails']:
        #text = censor_emails(text)
    if flags['address']:
        text_before = text
        text,count = censor_addresses(text)
        censor_stats['address'] = count

    return text, censor_stats


def process_files(input_pattern, output_dir, flags, stats_flag):
    stats = {'files_processed': 0, 'characters_censored': 0, 'errors': 0}
    detailed_stats = []
    # output_dir_path = Path(output_dir) / ""
    # output_dir_path.mkdir(parents=True, exist_ok=True)

    for file_path in glob.glob(input_pattern, recursive=True):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            censored_content, file_censor_stats = process_text(content, flags)
            censored_character_count = censored_content.count('\u2588')
            stats['characters_censored'] += censored_character_count
            detailed_stats.append((file_path, file_censor_stats))

            file_base_name = os.path.basename(file_path)
            output_file_path = os.path.join(output_dir, file_base_name + '.censored')

            with open(output_file_path, 'w', encoding='utf-8') as file:
                file.write(censored_content)
            stats['files_processed'] += 1
        except Exception as e:
            print(f"Error processing file {file_path}: {e}", file=sys.stderr if stats_flag == 'stderr' else sys.stdout)
            stats['errors'] += 1

    for file_path, file_stats in detailed_stats:
        stats_message = f"{file_path}: Names censored: {file_stats['names']}, Dates censored: {file_stats['dates']}, Phones censored: {file_stats['phones']}, Addresses censored: {file_stats['address']}"
        if stats_flag == 'stderr':
            sys.stderr.write(stats_message + '\n')
        elif stats_flag == 'stdout':
            sys.stdout.write(stats_message + '\n')
        else:
            with open(stats_flag, 'a') as stats_file:  # Ensure stats are appended
                stats_file.write(stats_message + '\n')

    summary_stats_message = (f"Files processed: {stats['files_processed']}\n"
                             f"Characters censored: {stats['characters_censored']}\n"
                             f"Errors: {stats['errors']}")
    if stats_flag == 'stderr':
        sys.stderr.write(summary_stats_message + '\n')
    elif stats_flag == 'stdout':
        sys.stdout.write(summary_stats_message + '\n')
    else:
        with open(stats_flag, 'a') as stats_file:
            stats_file.write(summary_stats_message + '\n')

def main():
    parser = argparse.ArgumentParser(description='Censor sensitive information from text files')
    parser.add_argument('--input', type=str, required=True, help='Glob pattern for input files')
    parser.add_argument('--output', type=str, required=True, help='Output directory')
    parser.add_argument('--stats', required=True, help='Where to write stats')
    parser.add_argument('--names', action='store_true', help='Censor names')
    parser.add_argument('--dates', action='store_true', help='Censor dates')
    parser.add_argument('--phones', action='store_true', help='Censor phone numbers')
    #parser.add_argument('--emails', action='store_true', help='Censor emails')
    parser.add_argument('--address', action='store_true', help='Censor addresses')

    args = parser.parse_args()
    os.makedirs(args.output, exist_ok=True)
    flags = {
        'names': args.names,
        'dates': args.dates,
        'phones': args.phones,
        #'emails': args.emails,
        'address': args.address
    }
    process_files(args.input, args.output, flags, args.stats)

if __name__ == '__main__':
    main()