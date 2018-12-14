#!/bin/sh

## Do whatever you need with env vars here ...
service cron start
# cron &
# Hand off to the CMD
exec "$@"
