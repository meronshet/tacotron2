import librosa
import soundfile as sf

def get_sampling_rate(audio_path):
  """
  Reads the audio file header using soundfile and returns the sampling rate.

  Args:
      audio_path: Path to the audio file (string).

  Returns:
      The sampling rate of the audio file (int), or None if an error occurs.
  """
  try:
    info = sf.info(audio_path)
    return info.samplerate
  except Exception as e:
    print(f"Error getting info from audio file {audio_path}: {e}")
    return None


if __name__ == '__main__':
    
    print(get_sampling_rate("./ab_dfeat-01.wav"))