<p align="center">
  <img src="https://justserpapi.com/logo/whiteBgColor.png" alt="JustSerpAPI Logo" width="200">
</p>

<h1 align="center">JustSerpAPI Python SDK</h1>

<p align="center">
  <a href="https://pypi.org/project/justserpapi/">
    <img src="https://img.shields.io/pypi/v/justserpapi?color=blue&style=flat-square" alt="PyPI version">
  </a>
  <a href="https://pypi.org/project/justserpapi/">
    <img src="https://img.shields.io/pypi/pyversions/justserpapi?style=flat-square" alt="Python Versions">
  </a>
  <a href="https://docs.justserpapi.com">
    <img src="https://img.shields.io/badge/docs-latest-brightgreen?style=flat-square" alt="Documentation">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-orange?style=flat-square" alt="License">
  </a>
</p>

<p align="center">
  <strong>The most reliable and high-performance SERP API for Google Search, Maps, News, Shopping, and more.</strong>
</p>

---

## 🌐 Quick Links

- **Official Website**: [justserpapi.com](https://justserpapi.com)
- **API Documentation**: [docs.justserpapi.com](https://docs.justserpapi.com)
- **User Dashboard**: [user.justserpapi.com](https://user.justserpapi.com)
- **Support**: [support@justserpapi.com](mailto:support@justserpapi.com)

---

## 🚀 Overview

JustSerpAPI provides a comprehensive suite of tools to scrape and parse search engine results in real-time. This Python SDK allows you to integrate Google Search, Maps, Images, News, Shopping, and AI-powered overviews directly into your Python applications with full type safety and high performance.

### Key Features
- **Full Google Coverage**: Search, Maps, News, Shopping, Finance, Images, and Patents.
- **AI-Powered**: Access Google AI Overviews and AI Search modes.
- **Easy Integration**: Built-in authentication, automatic retries, and clean models.
- **Type Safety**: Full PEP 484 type hints support for a great developer experience.

---

## 🛠 Installation

Install the package via `pip`:

```bash
pip install justserpapi
```

---

## 📖 Getting Started

To start using the SDK, you need an **API Key**. You can get one from the [User Dashboard](https://user.justserpapi.com).

### Simple Search Example

```python
import justserpapi
from justserpapi.api.google_api_api import GoogleAPIApi
from pprint import pprint

# Configure the SDK
configuration = justserpapi.Configuration(
    host="https://api.justserpapi.com"
)
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY_HERE'

# Initialize the API client
with justserpapi.ApiClient(configuration) as api_client:
    # Create an instance of the Google API
    api_instance = GoogleAPIApi(api_client)
    
    try:
        # Search for "coffee shops in New York"
        response = api_instance.search(
            query="coffee shops in New York",
            location="New York,NY",
            language="en"
        )
        pprint(response)
    except justserpapi.ApiException as e:
        print(f"Exception when calling API: {e}")
```

---

## 🍱 Supported APIs

| Service | Method | Description |
| :--- | :--- | :--- |
| **Google Search** | `search()` | Core Google search results (Organic, Ads, etc.) |
| **Google Maps** | `maps_search()` | Local business listings and place details |
| **Google AI** | `ai_overview()` | Extract AI-generated summaries from Google |
| **Google Images** | `images_search()` | High-quality image search results |
| **Google News** | `news_search()` | Real-time news results |
| **Google Shopping**| `shopping_search()`| Comprehensive product and price data |

Check out the [Full Documentation](https://docs.justserpapi.com) for a complete list of endpoints and parameters.

---

## 🛡️ Authentication

The API uses an API Key passed in the `X-API-Key` header. In the SDK, this is managed via the `Configuration` object:

```python
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'
```

---

## ⚖️ License

Distributed under the MIT License. See `LICENSE` for more information.

---

<p align="center">
  Proudly maintained by the <a href="https://justserpapi.com">JustSerpAPI Team</a>.
</p>
