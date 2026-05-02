import requests

def search(query):

    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": "5879101ce47465d74efa7b9e87f20ed252ee5e80",
        "Content-Type": "application/json"
    }
    payload = {"q": query}

    try:
        response = requests.post(url, headers=headers, json=payload)
        data = response.json()

        results = ""
        for item in data.get("organic", [])[:3]:
            results += f"{item['title']}\n{item['snippet']}\n\n"

        return results if results else "No results found."

    except Exception as e:
        print("SEARCH ERROR:", e)
        return "Search failed."