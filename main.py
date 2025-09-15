import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

# 1. Get prompt from command line
if len(sys.argv) < 2:
    print("Error: Please provide a prompt as a command line argument.")
    sys.exit(1)
    

# Check for --verbose flag
verbose = False
args = sys.argv[1:]
if "--verbose" in args:
    verbose = True
    args.remove("--verbose")


user_prompt = " ".join(args)

# 2. Load API key
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Check your .env file.")

# 3. Create the Gemini client
client = genai.Client(api_key=api_key)

# --- Conversation history ---
conversation = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)])
]

# --- Call model ---
response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=conversation
)
# --- Print results ---
if verbose:
    print(f'User prompt: "{user_prompt}"')

print(response.text)

# --- Print token usage if available ---
if hasattr(response, "usage_metadata"):
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count
    if verbose:
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")
else:
    if verbose:
        print("Token usage metadata not available.")







