import os
from pydub import AudioSegment
from tqdm import tqdm
import glob



# Get a list of all the mp3 files in the current working directory
mp3_files = glob.glob(os.path.join('songs', "*.mp3"))

# Create a new AudioSegment object to store the combined audio
combined_audio = AudioSegment.empty()

# Iterate over the mp3 files and add them to the combined audio object
for mp3_file in tqdm(mp3_files):
    combined_audio += AudioSegment.from_mp3(mp3_file)

# Export the combined audio object to a new mp3 file
combined_audio.export("combined.mp3", format="mp3")