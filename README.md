# ping-check
Sends a series of pings to destination servers and submits the results to graphite.

```
usage: ping_check.py [-h] [-s SERVER [SERVER ...]] [-n] [-d GRAPHITE_SERVER]
                     [-p GRAPHITE_PORT] [-x GRAPHITE_PREFIX]

optional arguments:
  -h, --help            show this help message and exit
  -s SERVER [SERVER ...], --server SERVER [SERVER ...]
                        Servers to ping
  -n, --dry-run         Dry Run. (Send no metrics to Graphite)
  -d GRAPHITE_SERVER, --graphite-server GRAPHITE_SERVER
                        Graphite Server
  -p GRAPHITE_PORT, --graphite-port GRAPHITE_PORT
                        Graphite Port
  -x GRAPHITE_PREFIX, --graphite-prefix GRAPHITE_PREFIX
                        Graphite Metric Prefix
```
