# Simulating basic cloud storage operation (conceptual demo)

def upload_to_cloud(file_name):
    print(f"Connecting to Google Cloud Storage...")
    print(f"Uploading {file_name} to bucket...")
    print("Upload successful!")

def main():
    file_name = "sample_data.txt"
    upload_to_cloud(file_name)

if __name__ == "__main__":
    main()
