import soundfile as sf
from scipy.signal import resample

import os

def downsample_all_wave_files(audio_dir, output_dir, target_sr=22050):
  """
  Downsamples all wave files (*.wav) in a directory and saves them elsewhere.

  Args:
      audio_dir: Directory containing the wave files (string).
      output_dir: Directory to save the downsampled wave files (string).
      target_sr: Target sampling rate (int, default=22050).
  """
  
  # Create output directory if it doesn't exist
  os.makedirs(output_dir, exist_ok=True)

  # Iterate through all files in the audio directory
  for filename in os.listdir(audio_dir):
    # Check if it's a wave file
    if filename.lower().endswith(".wav"):
      audio_path = os.path.join(audio_dir, filename)

      # Read audio data
      try:
        audio, original_sr = sf.read(audio_path)
      except Exception as e:
        print(f"Error reading audio file {audio_path}: {e}")
        continue  # Skip to next file if an error occurs

      # Check if downsampling is necessary
      if original_sr != target_sr:
        num_samples = len(audio)
        downsampled_audio = resample(audio, int(num_samples * target_sr / original_sr))
      else:
        downsampled_audio = audio

      # Generate output path (same filename in output directory)
      output_path = os.path.join(output_dir, filename)

      # Save downsampled audio
      sf.write(output_path, downsampled_audio, target_sr)
      print(f"Downsampled audio saved to: {output_path}")

# Example usage (replace with your actual paths)
audio_dir = "DUMMY"
output_dir = "downsampled_audio"  # Can be a different directory

downsample_all_wave_files(audio_dir, output_dir)
