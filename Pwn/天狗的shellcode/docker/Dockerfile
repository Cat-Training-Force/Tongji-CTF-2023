FROM ubuntu:20.04
LABEL Author "MiaoTony <i@miaotony.xyz>"
RUN sed -i "s/archive.ubuntu.com/mirrors.bfsu.edu.cn/g" /etc/apt/sources.list && \
    sed -i "s/security.ubuntu.com/mirrors.bfsu.edu.cn/g" /etc/apt/sources.list && \
    apt-get update && apt-get install --no-install-recommends -y lib32z1 xinetd build-essential && \
    rm -rf /var/lib/apt/lists/* && \
    useradd -m ctf

# pwn files
COPY xinetd.conf /etc/xinetd.conf
COPY init.sh /init.sh
COPY --chmod=755 pwn /home/ctf/pwn

RUN chmod +x /init.sh && \
    chown -R ctf:ctf /home/ctf && \
    chmod -R 755 /home/ctf && \
    cp -R /lib* /home/ctf && \
    mkdir /home/ctf/usr && \
    cp -R /usr/lib* /home/ctf/usr && \
    mkdir /home/ctf/dev  && \
    mknod /home/ctf/dev/null c 1 3 && \
    mknod /home/ctf/dev/zero c 1 5 && \
    mknod /home/ctf/dev/random c 1 8 && \
    mknod /home/ctf/dev/urandom c 1 9 && \
    chmod 666 /home/ctf/dev/* && \
    mkdir /home/ctf/bin && \
    cp /bin/sh /home/ctf/bin && \
    cp /bin/ls /home/ctf/bin && \
    cp /bin/cat /home/ctf/bin && \
    cp /bin/base64 /home/ctf/bin && \
    cp /usr/bin/timeout /home/ctf/bin 

CMD ["xinetd", "-dontfork"]
