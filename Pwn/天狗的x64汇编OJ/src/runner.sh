#!/bin/bash
echo "" > main
gcc -nostdlib -static main.s -o main
./main