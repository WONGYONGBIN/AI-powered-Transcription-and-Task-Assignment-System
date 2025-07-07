import ffmpeg
import os

def process_audio(input_path, output_path):
    """
    Process an audio file using FFmpeg.

    Args:
        input_path (str): Path to the input audio file.
        output_path (str): Path to save the processed audio file.

    Returns:
        bool: True if processing is successful, False otherwise.
    """
    try:
        # Ensure the output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Use FFmpeg to convert and normalize the audio
        (
            ffmpeg
            .input(input_path)
            .output(output_path, format='wav', acodec='pcm_s16le', ar='16000')
            .run()
        )
        return True
    except ffmpeg.Error as e:
        print(f"Error processing audio: {e}")
        return False

# Example usage
if __name__ == "__main__":
    input_audio = "example_input.mp3"
    output_audio = "processed_audio/output.wav"
    success = process_audio(input_audio, output_audio)
    if success:
        print("Audio processing completed successfully.")
    else:
        print("Audio processing failed.")
