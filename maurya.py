import requests
import json
from urllib.parse import quote

class VirusTotalChecker:
    def __init__(self):
        # Initialize with actual API endpoint
        self.base_url = "https://www.virustotal.com/vtapi/v2/domain/report"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def check_domain(self):
        api_key = input("Enter your VirusTotal API key: ").strip()
        domain = input("Enter domain to check: ").strip()
        
        params = {
            'apikey': api_key,
            'domain': domain
        }

        try:
            response = requests.get(
                self.base_url,
                params=params,
                headers=self.headers,
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                
                # Sample expected response format for businesses.uber.com
                expected_data = {
                    "BitDefender domain info": "This URL domain/host was seen to host badware at some point in time",
                    "detected_communicating_samples": [
                        {
                            "date": "2023-09-21 07:42:22",
                            "positives": 1,
                            "sha256": "1776b4685faadbd9ff2ac08eb1c26a09fafb1621f050733ca916b1db9bf0b953",
                            "total": 74
                        }
                    ],
                    "detected_downloaded_samples": [],
                    "detected_referrer_samples": [
                        {
                            "date": "2023-09-21 07:42:22",
                            "positives": 1,
                            "sha256": "1776b4685faadbd9ff2ac08eb1c26a09fafb1621f050733ca916b1db9bf0b953",
                            "total": 74
                        }
                    ],
                    "response_code": 1,
                    "verbose_msg": "Domain found in dataset"
                }

                # Print formatted response
                print("\n=== Domain Analysis Results ===")
                print(json.dumps(data, indent=2, sort_keys=False))

                # Additional information display
                if data.get("BitDefender domain info"):
                    print("\n=== BitDefender Analysis ===")
                    print(data["BitDefender domain info"])

                if data.get("detected_communicating_samples"):
                    print("\n=== Detected Communicating Samples ===")
                    for sample in data["detected_communicating_samples"]:
                        print(f"Date: {sample['date']}")
                        print(f"Positives/Total: {sample['positives']}/{sample['total']}")
                        print(f"SHA256: {sample['sha256']}")
                        print("---")

            else:
                print(f"Error: Status Code {response.status_code}")
                print(response.text)

        except requests.exceptions.RequestException as e:
            print(f"Network Error: {str(e)}")
        except json.JSONDecodeError:
            print("Error: Invalid JSON response")
        except Exception as e:
            print(f"Unexpected Error: {str(e)}")

if __name__ == "__main__":
    checker = VirusTotalChecker()
    checker.check_domain()
