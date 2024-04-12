def extract_audio_filenames(text_file_path, output_file_path):
  """
  Extracts audio filenames from a text file and saves them to another file.

  Args:
      text_file_path (str): Path to the text file containing audio information.
      output_file_path (str): Path to the output file where audio filenames will be saved.
  """
  with open(text_file_path, 'r', encoding='UTF-8') as text_file, open(output_file_path, 'w', encoding='UTF-8') as output_file:
    for line in text_file:
      # Split the line based on the pipe delimiter '|'
      parts = line.strip().split('|')
      if len(parts) > 0:
        # Assuming the audio filename is the first part before the pipe
        audio_filename = parts[0]
        output_file.write(f"{audio_filename}\n")

if __name__ == "__main__":
  text_file_path = "last_processed.txt"
  output_file_path = "extracted_audio_filenames.txt"
  extract_audio_filenames(text_file_path, output_file_path)
  print(f"Audio filenames extracted and saved to: {output_file_path}")
