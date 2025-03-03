import os
import pandas as pd

# Define emotion labels based on filename structure
emotion_dict = {
    "01": "Neutral",
    "02": "Calm",
    "03": "Happy",
    "04": "Sad",
    "05": "Angry",
    "06": "Fearful",
    "07": "Disgusted",
    "08": "Surprised"
}

# Folder where RAVDESS dataset is stored
dataset_path = r"C:\Users\LENOVO\OneDrive\Desktop\مهنة\PROJECT SER\datasets"  # Change this to your actual path

# List to store data
data = []

# Loop through all files
for folder in os.listdir(dataset_path):
    folder_path = os.path.join(dataset_path, folder)
    
    if os.path.isdir(folder_path):
        for file in os.listdir(folder_path):
            if file.endswith(".wav"):
                file_path = os.path.join(dataset_path, folder, file)

                
                # Extract emotion from filename (3rd element in filename)
                emotion_code = file.split("-")[2]
                emotion = emotion_dict.get(emotion_code, "Unknown")

                # Append to data list
                data.append([file_path, emotion])

# Create DataFrame
df = pd.DataFrame(data, columns=["file_path", "emotion"])

# Save to CSV
df.to_csv("ravdess_data.csv", index=False)

print("✅ Dataset saved as ravdess_data.csv")
