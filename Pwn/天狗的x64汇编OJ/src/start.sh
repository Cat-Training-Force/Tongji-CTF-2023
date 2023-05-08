#!/bin/bash
echo $GZCTF_FLAG > /app/flag
GZCTF_FLAG=""
flask run --host='0.0.0.0' --port=5000