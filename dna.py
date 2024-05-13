import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py database sequence")
        sys.exit(1)

    # TODO: Read database file into a dictionary
    datalist = read_db(sys.argv[1])
    database = build_db(datalist)

    # # Print the resulting database
    # print("Database after building:")
    # print(database)

    # TODO: Read DNA sequence file into a string
    with open(sys.argv[2], 'r') as file:
        dna_sequence = file.read()

    # find longest match of eas STR in DNA sequence
    longest_matches = longest_str_match(database, dna_sequence)

    # print("Longest STR Match:")
    # print(longest_matches)

    # check db for profile match
    check_db_matches(database, longest_matches)

    return


def read_db(filename):
    datalist = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            datalist.append(row)
            # if len(datalist) <= 5:
            #     print(row)

    return datalist


def build_db(datalist):
    database = {}
    for row in datalist:
        name = row.pop('name')
        database[name] = {k: int(v) for k, v in row.items() if v.isdigit()}
    return database


# TODO: Find longest match of each STR in DNA sequence


def longest_str_match(database, sequence):
    # Pull STR patterns from first row of db
    str_patterns = list(database[list(database.keys())[0]].keys())
    # Store longest match in dictionary
    longest_str_match = {}
    # iterate over the STR patterns
    for str_pattern in str_patterns:
        # variables for tracking the longest match
        longest_str = 0
        i = 0
        while i < len(sequence):
            if sequence[i:i+len(str_pattern)] == str_pattern:
                current_str = 1
                i += len(str_pattern)
                while i < len(sequence) and sequence[i:i + len(str_pattern)] == str_pattern:
                    current_str += 1
                    i += len(str_pattern)
                longest_str = max(longest_str, current_str)
            else:
                i += 1
        longest_str_match[str_pattern] = longest_str
        # # Debugging print statements
        # print(f"STR pattern: {str_pattern}, Longest STR: {longest_str}")
        longest_str_match[str_pattern] = longest_str

    return longest_str_match

# TODO: Check database for matching profiles


def check_db_matches(database, longest_matches):
    # Iterate over each profile in the database.
    # For each profile, compare the number of times each STR occurs in the profile with the longest match of each STR in the DNA sequence.
    for profile_name, profile_data in database.items():
        match_found = True

        for str_name, str_count in profile_data.items():
            if str_count != longest_matches.get(str_name, 0):
                match_found = False
                break

        # If all STR counts match, you've found a match. Print the name of the individual and return.
        if match_found:
            print(profile_name)
            return
        # If no match is found after checking all profiles, print "No match".
    print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
