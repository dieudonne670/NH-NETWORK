import requests

# Example provider endpoints
PROVIDER_APIS = {
    "MTN": "https://api.mtn.cm/feedback/upload/",
    "Orange": "https://api.orange.cm/feedback/upload/",
    "Camtel": "https://api.camtel.cm/feedback/upload/",
    "Nexttel": "https://api.nexttel.cm/feedback/upload/"
}

def send_csv(provider, file_path):
    url = PROVIDER_APIS[provider]
    files = {"file": open(file_path, "rb")}
    response = requests.post(url, files=files)

    if response.status_code == 200:
        print(f"✅ {provider} CSV sent successfully")
    else:
        print(f"❌ Failed to send {provider} CSV: {response.status_code} {response.text}")


if __name__ == "__main__":
    send_csv("MTN", "mtn_feedback.csv")
    send_csv("Orange", "orange_feedback.csv")
    send_csv("Camtel", "camtel_feedback.csv")
    send_csv("Nexttel", "nexttel_feedback.csv")
