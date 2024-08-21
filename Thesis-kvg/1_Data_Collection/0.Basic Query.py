import requests

# The URL of the Snapshot Hub GraphQL API endpoint
url = "https://hub.snapshot.org/graphql"

# GraphQL query
query = """
{
  proposals {
    id
    title
    body
    start
    end
    state
    author
  }
}
"""

response = requests.post(url, json={'query': query})

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Failed to fetch data:", response.status_code)