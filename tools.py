import httpx


def wikipedia(q):
    response = httpx.get("https://en.wikipedia.org/w/api.php", params={
        "action": "query",
        "list": "search",
        "srsearch": q,
        "format": "json"
    })
    return response.json()["query"]["search"][0]["snippet"]

# print(wikipedia('cat'))

def calculate(what):
    return eval(what)

# print(calculate('2+2*3'))

known_actions = {
    "wikipedia": wikipedia,
    "calculate": calculate,
}