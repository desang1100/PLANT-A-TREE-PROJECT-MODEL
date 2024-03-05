import csv

text_filename = "dataset.txt"
csv_filename = "data.csv"
delimiter = ";"  # Specify the delimiter used in the text file

with open(text_filename, "r") as text_file:
    # Read the text file using the specified delimiter
    data = [line.strip().split(delimiter) for line in text_file]

with open(csv_filename, "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(data)

print(f"Text file '{text_filename}' converted to CSV file '{csv_filename}'")
