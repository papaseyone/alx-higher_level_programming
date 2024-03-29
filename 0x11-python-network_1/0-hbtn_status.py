import urllib.request

# Define the URL to fetch
url = "https://alx-intranet.hbtn.io/status"

# Use urllib to send a request and fetch the response
with urllib.request.urlopen(url) as response:
    # Read the content of the response and decode it to UTF-8
    body = response.read().decode('utf-8')

# Display the body of the response with some information
print("\t- Body response:")
print("\t\t- type: {}".format(type(body)))
print("\t\t- content: {}".format(body))
