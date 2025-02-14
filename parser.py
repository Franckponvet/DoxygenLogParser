import sys
import csv

def parse_doxygen_log(log_file, output_csv):
    try:
        with open(log_file, "r", encoding="utf-8") as log, open(output_csv, "w", newline="", encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["Line", "File", "Message"])  # CSV headers
            
            for line in log:
                if ":" in line and "warning:" in line:
                    parts = line.strip().split(":", maxsplit=2)
                    if len(parts) == 3:
                        csv_writer.writerow(parts)
                    else:
                        print(f"Skipping malformed line: {line.strip()}")
            
        print(f" Parsed warnings saved to {output_csv}")

    except Exception as e:
        print(f" Error parsing log file: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python parser.py <log_file>")
        sys.exit(1)

    parse_doxygen_log(sys.argv[1], "warnings.csv")
