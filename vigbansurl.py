import time
import ngrok

# 1. Make sure Vigilant Bans is running on PC (http://localhost:3000/?backend=ws://localhost:8999)
# 2. Get an authtoken from https://dashboard.ngrok.com
# 3. Replace authtoken string with generated authtoken
# 4. Run Python file

authtoken = "[INSERT AUTH TOKEN HERE]"

ngrok.set_auth_token(authtoken)
frontend = ngrok.forward(3000)
backend = ngrok.forward(8999)


print(
    f"Vigilant Bans Remote URL:\n\n{frontend.url()}/?backend=wss://{backend.url().split("//")[1]}:443\n\n"
)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Goodbye!")
