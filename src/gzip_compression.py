import os
import gzip
import shutil

def gzip_file(input_file_path: str) -> str:
    """
    Compress a CSV file into AWS CUR-style .csv.gz

    - Fixes bad naming like .csv.csv
    - Outputs: filename.csv.gz
    - Keeps file in same directory
    """

    if not os.path.isfile(input_file_path):
        raise FileNotFoundError(f"File not found: {input_file_path}")

    # Get directory and clean filename
    dir_name = os.path.dirname(input_file_path)
    file_name = os.path.basename(input_file_path)

    # Remove duplicate extensions safely
    base_name = file_name.replace(".csv.csv", ".csv")
    base_name = os.path.splitext(base_name)[0]  # remove .csv

    # Final output: .csv.gz
    output_file_path = os.path.join(dir_name, base_name + ".csv.gz")

    print(f"Compressing:\n{input_file_path}\n→ {output_file_path}")

    # Compress file
    with open(input_file_path, "rb") as f_in:
        with gzip.open(output_file_path, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)

    print("✅ Compression complete")
    return output_file_path


def validate_gzip(file_path: str):
    """
    Quick validation to check if gzip file is readable
    """
    print("\nValidating gzip file...")

    with gzip.open(file_path, "rt") as f:
        first_line = f.readline()

    print("✅ Gzip file is valid")
    print(f"Sample content:\n{first_line[:100]}")


if __name__ == "__main__":
    file_path = r"C:\Users\Dilpreet Singh Bedi\OneDrive\Desktop\cloudcatcher-cur-00002.csv.csv"

    gz_file = gzip_file(file_path)

    # Optional: validate content
    validate_gzip(gz_file)