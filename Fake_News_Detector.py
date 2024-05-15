import requests
from bs4 import BeautifulSoup

def fetch_article_content(url):
    """Fetches article content from a specified URL and returns plain text of the article."""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    content_container = soup.find('div', class_='article__content-container')
    if content_container:
        paragraphs = content_container.find_all('p')
        text = ' '.join(p.get_text() for p in paragraphs)
        return text
    return None

def summarize_text(text, model_name="gpt-3.5-turbo", max_tokens=150):
    """ Summarizes the provided text using OpenAI's GPT-3.5 Turbo with a focus on concise but complete summaries. """
    openai_api_key = "add your OPENAI API KEY here"
    headers = {
        "Authorization": f"Bearer {openai_api_key}"
    }
    data = {
        "model": model_name,
        "messages": [{"role": "system", "content": "Please summarize the following text in one line:"},
                     {"role": "user", "content": text}],
        "max_tokens": max_tokens
    }
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
    if response.status_code == 200:
        responses = response.json().get("choices", [])
        if responses:
            return responses[0].get("message", {}).get("content", "").strip()
    return "Failed to generate summary."

def google_search(search_text, api_key, cse_id):
    """Searches Google using the provided text and returns the top 5 related URLs."""
    search_text = search_text.replace('"', '').strip()
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'q': search_text,
        'key': api_key,
        'cx': cse_id,
        'num': 5
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        results = response.json()
        urls = [item['link'] for item in results.get('items', [])]
        return urls
    return []

def analyze_news_reliability(original_url, related_urls):
    """Analyzes the reliability of the news based on additional sources fetched from related URLs."""
    original_text = fetch_article_content(original_url)
    original_summary = summarize_text(original_text)
    
    if not related_urls:
        return "No related articles found for further analysis."

    related_summaries = [summarize_text(fetch_article_content(url)) for url in related_urls]
    related_text = ' '.join(filter(None, related_summaries))  # Join non-empty summaries

    if original_summary in related_text:
        return "Original article seems credible based on related articles."
    return "Original article may not be credible; discrepancies found."

def find_related_articles_and_analyze(url_list):
    api_key = 'Add your Google Search API Here' 
    cse_id = 'Add your Custom Search Engine ID Here'
    for url in url_list:
        text = fetch_article_content(url)
        summary = summarize_text(text)
        if summary != "Failed to generate summary.":
            related_urls = google_search(summary, api_key, cse_id)
            if related_urls:
                verdict = analyze_news_reliability(url, related_urls)
                print("Original Summary:", summary)
                print("Related URLs:", related_urls)
                print("Analysis Result:", verdict)
            else:
                print("No related URLs found for further analysis.")
        else:
            print("Failed to generate a valid summary for URL:", url)

# Example usage, you may change to any other news article URL
url_list = ["Paste your URL Here"]
find_related_articles_and_analyze(url_list)
