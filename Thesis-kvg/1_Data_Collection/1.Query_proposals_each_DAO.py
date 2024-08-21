import requests
from datetime import datetime

# The URL of the Snapshot Hub GraphQL API endpoint
url = "https://hub.snapshot.org/graphql"

# GraphQL query
query = """
query Proposals {
  proposals(
    first: 700,
    skip: 0,
    where: {
      space_in: ["ferrum-network.eth"],
      state: "closed"
    }
  ) {
    id
    title
    body
    choices
    start
    end
    snapshot
    state
    author
    scores
    votes
    scores_total
    strategies {
      network
      params
    }
  }
}
"""

headers = {
    "Content-Type": "application/json",
}

response = requests.post(url, json={'query': query}, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Failed to fetch data:", response.status_code)
    print(response.text) 

# export the data into an xlsx

import pandas as pd

proposals = data['data']['proposals']

df = pd.DataFrame(proposals)

# Select which columns to export
columns_to_export = ['id', 'title', 'body', 'choices', 'start', 'end', 'snapshot', 'state', 'author', 'scores', 'votes', 'scores_total', 'strategies']
df_export = df[columns_to_export]

filename = "/Users/Karsten/Desktop/ferrum-network.eth.xlsx"
df_export.to_excel(filename, index=False)

print(f"File saved as {filename}")
