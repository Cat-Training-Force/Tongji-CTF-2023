FROM ubuntu:20.04 AS builder

COPY src/getflag.c /getflag.c
RUN sed -i "s/archive.ubuntu.com/mirrors.bfsu.edu.cn/g" /etc/apt/sources.list && \
    sed -i "s/security.ubuntu.com/mirrors.bfsu.edu.cn/g" /etc/apt/sources.list && \
    apt-get update && \
    apt-get --no-install-recommends install -y gcc gcc-multilib && \
    gcc -o /getflag /getflag.c -static


FROM ubuntu:20.04
LABEL Author "MiaoTony <i@miaotony.xyz>"
RUN sed -i "s/archive.ubuntu.com/mirrors.bfsu.edu.cn/g" /etc/apt/sources.list && \
    sed -i "s/security.ubuntu.com/mirrors.bfsu.edu.cn/g" /etc/apt/sources.list && \
    apt-get update && apt-get install --no-install-recommends -y lib32z1 xinetd build-essential && \
    rm -rf /var/lib/apt/lists/* && \
    useradd -m ctf

# pwn files
COPY xinetd.conf /etc/xinetd.conf
# COPY --from=builder /lib/x86_64-linux-gnu/ld-linux-x86-64.so.2 /home/ctf/lib64/
# COPY --from=builder /lib/x86_64-linux-gnu/libc.so.6 /home/ctf/lib/x86_64-linux-gnu/
# COPY --from=builder --chown=ctf:ctf --chmod=500 /getflag /home/ctf/
COPY --from=builder --chmod=755 /getflag /getflag

CMD ["xinetd", "-dontfork"]
