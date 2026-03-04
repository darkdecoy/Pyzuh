from pyzuh import Agents,authenticate_wazuh
import requests
import json

def run_scan_and_post_to_slack(wazuh_client, slack_webhook_url):
    # Run system scan on all agents
    response = wazuh_client.run_sysscan(pretty=True, wait_for_complete=True)

    # Post response to Slack channel
    slack_message = {
        "text": "Wazuh system scan completed",
        "attachments": [
            {
                "text": json.dumps(response, indent=4)
            }
        ]
    }
    requests.post(slack_webhook_url, json=slack_message)

if __name__ == "__main__":
    api_url = "https://x.x.x.x:55000"
    os.environ["WAZUH_USERNAME"] = "wazuh"
    os.environ["WAZUH_PASSWORD"] = "wazuh"

    # Define your Slack webhook URL
    slack_webhook_url = 'your-slack-webhook-url'

    try:
        # Authenticate with Wazuh API
        token = authenticate_wazuh(api_url)
        print("Authentication successful.")
    except Exception as e:
        print("Authentication failed:", e)

    # Initialize the Wazuh client
    wazuh_client = Agents(api_url=api_url, jwt_token=token)

    # Run system scan and post results to Slack
    run_scan_and_post_to_slack(wazuh_client, slack_webhook_url)
