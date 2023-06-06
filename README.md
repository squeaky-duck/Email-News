# What is this project?
This app accesses news about a particular topic and sends them by email.
* Gathers news on `topic` as specified at the top of `main.py` via [newsapi](https://newsapi.org)
* Sends the news to email using `smtplib`
> Requires:
> * an app password generated on the GMail account one wishes to receive Email to/from
> * API key from [newsapi](https://newsapi.org)
> * Email address, Gmail App password and news API key should be available as environment variables: `EMAILAPPUSERNAME`, `EMAILNEWSPASSWORD` and `NEWS_API_KEY` respectively.
