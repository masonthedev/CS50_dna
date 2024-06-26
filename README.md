# CS50_dna

**DNA Analysis Tool**
This Python script analyzes DNA sequences to identify individuals based on their Short Tandem Repeats (STRs) profiles. It reads a database of individuals' STR counts and compares them against the STR counts in a given DNA sequence file to determine potential matches.

**Usage**

To use the DNA analysis tool, run the dna.py script with the following command-line arguments:

python dna.py <database_file> <sequence_file>
<database_file>: Path to the CSV file containing the database of individuals' STR counts.
<sequence_file>: Path to the text file containing the DNA sequence to be analyzed.

Examples
Here are some examples of using the DNA analysis tool:

python dna.py databases/database.csv sequences/sequence.txt
This command will analyze the DNA sequence in sequence.txt using the database in database.csv and output any matching individuals.


Results:

Run as python dna.py databases/small.csv sequences/1.txt. Program should output Bob.
Run as python dna.py databases/small.csv sequences/2.txt. Program should output No match.
Run as python dna.py databases/small.csv sequences/3.txt. Program should output No match.
Run as python dna.py databases/small.csv sequences/4.txt. Program should output Alice.
