import argparse
import random


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
  return f"DUMMY/{filename}|{text}"  # Add prefix and join with pipe


def process_and_split_file(input_file, output_dir):
  """
  Processes lines from a file, applies processing function, splits into training,
  validation, and test sets, and saves them as separate files.

  Args:
      input_file: Path to the file to process (string).
      output_dir: Directory to save the split files (string).
  """
  processed_lines = []
  with open(input_file, 'r', encoding='UTF-8') as f:
    for line in f:
      processed_lines.append(process_line(line.strip()))

  # Randomly shuffle lines
  random.shuffle(processed_lines)

  # Calculate split sizes based on percentages
  num_lines = len(processed_lines)
  train_size = int(0.96 * num_lines)
  val_size = int(0.01 * num_lines)
  test_size = num_lines - train_size - val_size
  print(test_size)
  # Split data into training, validation, and test sets
  training_data = processed_lines[:train_size]
  validation_data = processed_lines[train_size:train_size + val_size]
  test_data = processed_lines[train_size + val_size:]

  # Save split data to separate files with prefixes
  with open(f"{output_dir}/shet_dataset_text_train.txt", 'w', encoding='UTF-8') as f:
    f.writelines([line + "\n" for line in training_data])
  with open(f"{output_dir}/shet_dataset_text_val.txt", 'w', encoding='UTF-8') as f:
    f.writelines([line + "\n" for line in validation_data])
  with open(f"{output_dir}/shet_dataset_text_test.txt", 'w', encoding='UTF-8') as f:
    f.writelines([line + "\n" for line in test_data])

  print(f"Data split and saved to {output_dir}")


def main():
  """
  Parses command-line arguments, validates them (optional), and calls the processing and splitting function.
  """
  # Basic validation (optional)
  

  process_and_split_file('last_processed.txt', ".")


if __name__ == "__main__":
  main()
