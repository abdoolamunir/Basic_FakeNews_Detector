# Basic Fake News Detector Using ChatGPT

This project, **Basic Fake News Detector Using ChatGPT**, leverages OpenAI's GPT-3.5 Turbo to analyze and determine the reliability of news articles by comparing them with related news content fetched from the web. It aims to provide users with an automated way to assess the credibility of news, utilizing advanced NLP techniques to summarize and cross-reference news articles.

## Project Description

The **Basic Fake News Detector** is designed to help users identify potential fake news articles by analyzing the content of an article against related articles sourced from the internet. This is achieved by summarizing the articles using OpenAI's GPT-3.5 Turbo model and then searching for related articles via Google's Custom Search JSON API. The system evaluates the consistency of information across these articles to assess the credibility of the original piece.

## Features

- **Article Fetching**: Extracts the text from news articles.
- **Text Summarization**: Uses OpenAI's GPT-3.5 Turbo to generate concise summaries.
- **Google Search**: Automates the process of searching for related articles based on summaries.
- **Reliability Analysis**: Compares the original article with related articles to assess credibility.

## Built With

- Python 3.8+
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - For parsing HTML and extracting the necessary data.
- [Requests](https://docs.python-requests.org/en/master/) - For making HTTP requests to fetch web pages.
- [OpenAI's GPT-3.5 Turbo](https://beta.openai.com/docs/) - For generating summaries and processing natural language.

## Getting Started

### Prerequisites

This project requires Python 3.8+ and pip. You can install the necessary libraries with pip:

```bash
pip install beautifulsoup4 requests
```

### Installation

1. Clone the repo:
 ```bash
   git clone https://github.com/abdoolamunir/Basic_FakeNews_Detector.git
   ```

2. Navigate to the project directory:
```bash
  cd main
```

3. install the required packages:
```bash
pip install -r requirements.txt
```

### Configuration
Set up your environment variables for aPI keys:
```bash
export OPENAI_API_KEY='Your-OpenAI-API-Key'
export GOOGLE_CUSTOM_SEARCH_API_KEY='Your-Google-API-Key'
export GOOGLE_CUSTOM_SEARCH_ENGINE_ID='Your-Custom-Search-Engine-ID'
```

### Usage
Run the main script from the command line:
```bash
python Fake_News_Detector.py
```
Follow the prompts to enter the URL of the news article you wish to analyze (change it in the Url_list var)

###Contributing
We welcome contributions from the community. Please follow the steps below:

Fork the repository.
Create a new branch (git checkout -b feature/YourFeature).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature/YourFeature).
Open a pull request.

