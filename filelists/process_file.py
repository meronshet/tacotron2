import argparse


def process_line(line):
  """
  Processes a line by removing the audio duration, separating the filename and text,
  and adding a prefix.

  Args:
      line: The line to process (string).

  Returns:
      The processed line (string).
  """
  parts = line.split('|')  # Split the line using pipe (|) delimiter
  filename, text = parts[0], parts[2]  # Extract filename and text
  return f"DUMMY/{filename}|{text}\n"  # Add prefix and join with pipe


def process_file(input_file, output_file):
  """
  Processes lines from a file, applies the processing function, and saves the results.

  Args:
      input_file: Path to the file to process (string).
      output_file: Path to save the processed content (string).
  """
  processed_lines = []
  with open(input_file, 'r', encoding='UTF-8') as f:
    for line in f:
      processed_lines.append(process_line(line.strip()))

  with open(output_file, 'w', encoding='UTF-8') as f:
    f.writelines(processed_lines  + ['\n'])


def main():

  process_file("shet_dataset_text_train.txt", "last_processed.txt")
  print(f"Processed lines saved to: last_processed.txt")


if __name__ == "__main__":
  main()
