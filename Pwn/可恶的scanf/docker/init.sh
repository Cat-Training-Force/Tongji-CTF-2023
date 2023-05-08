#!/bin/sh

echo $GZCTF_FLAG > /home/ctf/flag
chown -R ctf:ctf /home/ctf/flag
unset GZCTF_FLAG
GZCTF_FLAG=""

/usr/sbin/chroot --userspec=ctf:ctf /home/ctf timeout 50 /pwn
