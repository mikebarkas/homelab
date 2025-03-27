## Stocker

The Stocker application uses a custom container that runs a Python application.
The application queries the Finnhub API for a stock price.

A Kubernetes cron runs the container and specifies what stock symbol to query.
The stock symbol, price, and time is stored in a Postgres service running in k8s.

