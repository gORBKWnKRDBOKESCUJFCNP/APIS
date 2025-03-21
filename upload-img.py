import requests

# Ask for domain URL (e.g., http://yourdomain.com)
domain = input("Enter your elFinder domain (e.g., http://yourdomain.com): ").strip()

# Construct the elFinder connector URL
ELFINDER_URL = f"{domain}/hris/elfinder/connector.minimal.php"

# Ask for the target folder hash (you should get it from cmd=open if unknown)
target_hash = input("Enter the target folder hash (e.g., m1_MQ for CSAP): ").strip()

# Ask for the file path to upload
file_path = input("Enter the full path of the image to upload: ").strip()

# Ensure inputs are not empty
if not domain or not target_hash or not file_path:
    print("Error: All fields are required.")
    exit()

try:
    # Prepare the upload request
    upload_url = f"{ELFINDER_URL}?cmd=upload&target={target_hash}"
    files = {'upload[]': open(file_path, 'rb')}

    # Send the upload request
    response = requests.post(upload_url, files=files)

    # Print response
    print("Response:", response.json())  # Check response for success or errors

except Exception as e:
    print(f"Upload failed: {e}")
