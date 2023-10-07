#!/bin/bash

redis-cli SET Statistic:suppliers "{\"name\": \"suppliers\", \"value\": 484961, \"history\": [482152, 482630, 483057, 483453, 483897, 484354, 484961]}"

echo "Значение для ключа Statistic:suppliers установлено в Redis"
