import requests

def count_words(subreddit, word_list, instances=None, after=None, count=0):
    if instances is None:
        instances = {}  # Initialize instances dictionary

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    try:
        response.raise_for_status()  # Check for request errors
        results = response.json().get("data")
    except (requests.exceptions.HTTPError, ValueError):
        print("")  # Print nothing if request failed
        return

    after = results.get("after")
    count += results.get("dist")

    for c in results.get("children"):
        title = c.get("data").get("title").lower().split()
        for word in word_list:
            word = word.lower()  # Convert word to lowercase
            # Check for complete word matches only
            if any(t == word for t in title):
                if word not in instances:
                    instances[word] = 1
                else:
                    instances[word] += 1

    if after is None:
        if len(instances) == 0:
            print("")
            return

        # Sort instances by count (descending) and word (ascending)
        sorted_instances = sorted(instances.items(), key=lambda item: (-item[1], item[0]))
        for word, count in sorted_instances:
            print(f"{word}: {count}")
    else:
        count_words(subreddit, word_list, instances, after, count)

# Example usage
count_words("programming", ["python", "javascript", "java"])

