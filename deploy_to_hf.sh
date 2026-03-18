#!/bin/bash
set -e

export PATH="$HOME/.local/bin:$PATH"

SPACE_NAME="ai-document-assistant"

# Check if logged in
AUTH_STATUS=$(hf auth whoami 2>&1)
if [ "$AUTH_STATUS" = "Not logged in" ]; then
    echo "Not logged in to Hugging Face."
    echo ""
    echo "Option 1: Login with token"
    echo "  hf auth login --token YOUR_HF_TOKEN"
    echo ""
    echo "Option 2: Pass token as argument to this script"
    echo "  ./deploy_to_hf.sh YOUR_HF_TOKEN"
    echo ""

    if [ -n "$1" ]; then
        echo "Logging in with provided token..."
        hf auth login --token "$1"
    else
        echo "Get your token from: https://huggingface.co/settings/tokens"
        exit 1
    fi
fi

HF_USERNAME=$(hf auth whoami 2>&1 | head -1)
echo "Logged in as: $HF_USERNAME"

python3 << PYEOF
from huggingface_hub import HfApi

api = HfApi()
user_info = api.whoami()
username = user_info["name"]
space_id = f"{username}/$SPACE_NAME"

print(f"Creating/updating Space: {space_id}")

try:
    api.create_repo(
        repo_id=space_id,
        repo_type="space",
        space_sdk="docker",
        private=False,
        exist_ok=True,
    )
    print(f"Space ready: https://huggingface.co/spaces/{space_id}")
except Exception as e:
    print(f"Note: {e}")
    print("Continuing with upload...")

print("Uploading files...")
api.upload_folder(
    folder_path="/home/vedant-naidu/Desktop/capstone_project",
    repo_id=space_id,
    repo_type="space",
    ignore_patterns=[
        ".git/*",
        "__pycache__/*",
        "*.pyc",
        "venv/*",
        "data/vector_db/*",
        "data/uploads/*.pdf",
        ".env",
        "deploy_to_hf.sh",
    ],
)
print("")
print("=" * 60)
print("DEPLOYMENT SUCCESSFUL!")
print("=" * 60)
print(f"")
print(f"IMPORTANT: Set the GROQ_API_KEY secret in your Space:")
print(f"  https://huggingface.co/spaces/{space_id}/settings")
print(f"  Add secret: GROQ_API_KEY = <your groq api key>")
print(f"")
print(f"Your Space URL:")
print(f"  https://huggingface.co/spaces/{space_id}")
print(f"")
print(f"API endpoints:")
print(f"  https://{username}-{space_id.split('/')[-1]}.hf.space/")
print(f"  https://{username}-{space_id.split('/')[-1]}.hf.space/chat")
print(f"  https://{username}-{space_id.split('/')[-1]}.hf.space/documents")
PYEOF