## Stocker

The Stocker application uses a custom container that runs a Python application.
The application queries the Finnhub API for a stock price.

A Kubernetes cronjob runs the container and specifies what stock symbol to query.
The stock symbol, price, and time is stored in a Postgres service running in k8s.

## Container
The small Python application runs in a container I created.

Container repo: https://hub.docker.com/r/mikebarkas/homelab-stocker/tags
