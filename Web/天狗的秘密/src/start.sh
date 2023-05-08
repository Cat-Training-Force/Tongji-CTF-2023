#!/bin/bash
echo $GZCTF_FLAG > /app/static/flag
GZCTF_FLAG=""
flask run --host='0.0.0.0' --port=5000