# 📈 Bitbar Portfolio

This is a simple [bitbar](ttps://github.com/matryer/bitbar) plugin for monitoring a stock portfolio using alpha vantage to power the stock data.

## Installation

- Follow the [usual instructions](https://github.com/matryer/bitbar#installing-plugins) for installing bitbar plugins from their guidelines
- Ensure you pick a reasonable time between runs to avoid hitting rate limits with alpha vantage.
- Install required dependencies - we require 2 for this plugin:
  ```
      pip install alpha_vantage
      pip install load_dotenv
  ```
- Create a .env file in your plugins directory as described below

### Environment variables

As bitbar runs outside your usual terminal we use a .env file in your plugins directory to provide configuration to the plugin.
You currently require two variables to use this plugin :

- ALPHAVANTAGE_API_KEY - use this for your alpha vantage api key, they are free and can be acquired [here](https://www.alphavantage.co/support/#api-key)
- PORTFOLIO_SYMBOLS - use this for a comma separated list of symbols you want to monitor eg. `lgen.l,goog,tsla`
