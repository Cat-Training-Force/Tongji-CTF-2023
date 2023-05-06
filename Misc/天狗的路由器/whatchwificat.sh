#!/bin/bash

FLAGSSID='tjctf{this_is_hidden_flag}'
PWD=tac233333.

while [ 1 ]
do
    sleep 3
    date
    # script for macOS only
    airport -I | grep "SSID: ${FLAGSSID}"
    if [ $? -ne 0 ]; then
        networksetup -setairportnetwork en0 "${FLAGSSID}" $PWD
        echo "Reconnecting..."
    else
        sleep 10
    fi
done