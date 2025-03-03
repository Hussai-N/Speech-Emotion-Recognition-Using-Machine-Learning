import librosa
import pandas as pd
import numpy as np

# Load the dataset with file paths
df = pd.read_csv("ravdess_data.csv")

# List to store extracted features
features = []

for index, row in df.iterrows():
    file_path = row["file_path"]
    emotion = row["emotion"]

    try:
        # Load audio file
        y, sr = librosa.load(file_path, duration=3, offset=0.5)

        # Extract 13 MFCC features
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        mfccs_mean = np.mean(mfccs, axis=1)  # Take the mean of each MFCC

        # Append features with emotion label
        features.append([file_path] + list(mfccs_mean) + [emotion])

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# Create a new dataframe with features
columns = ["file_path"] + [f"mfcc_{i+1}" for i in range(13)] + ["emotion"]
features_df = pd.DataFrame(features, columns=columns)

# Save to CSV
features_df.to_csv("features.csv", index=False)

print("Feature extraction completed and saved to 'features.csv' ✅")


