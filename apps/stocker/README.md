## Stocker

The Stocker application uses a custom container that runs a Python application.
The application queries the Finnhub API for a stock price.

A Kubernetes cronjob runs the container and specifies what stock symbol to query.
The stock symbol, price, and time is stored in a Postgres service running in k8s.

## Container

The small Python application runs in a container I created.

Container repo: https://hub.docker.com/r/mikebarkas/homelab-stocker/tags

## Sync to Supabase

For the data to be public available to the dashboard, the k8s postgres data is synced to
Supabase with a cronjob.

The `stocker-sync` CronJob copies new rows from the `stock` table to Supabase for the
stocker dashboard. It runs at :40 past each hour, 10:40-16:40 ET, after the collectors.

- Code and image: https://github.com/mikebarkas/stocker-dashboard (`sync/`)
- `cron-sync.yaml`: the CronJob, image `ghcr.io/mikebarkas/stocker-sync`
- `secret-sync.yaml`: template for the `stocker-sync-env` secret (fill in locally, never commit values)
- `configmap-supabase-ca.yaml`: Supabase's public CA certificate, used to verify the TLS connection

The sync reads homelab Postgres as the read-only role `stocker_sync`, not `postgres`.
