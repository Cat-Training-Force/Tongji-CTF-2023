FROM python:3.10.11-slim-bullseye
LABEL Author "MiaoTony <i@miaotony.xyz>"

RUN sed -i "s/archive.ubuntu.com/mirrors.bfsu.edu.cn/g" /etc/apt/sources.list && \
    sed -i "s/security.ubuntu.com/mirrors.bfsu.edu.cn/g" /etc/apt/sources.list && \
    apt-get update && apt-get install --no-install-recommends -y lib32z1 xinetd build-essential && \
    rm -rf /var/lib/apt/lists/* && \
    useradd -m ctf && \
    python -m pip config set global.index-url https://mirror.sjtu.edu.cn/pypi/web/simple && \
    python -m pip install -U pip && python -m pip install --no-cache-dir numpy==1.21.6

COPY xinetd.conf /etc/xinetd.conf
COPY --chmod=755 entrypoint.sh /entrypoint.sh
COPY chall.py /home/ctf/chall.py
COPY opencv_python-4.7.0.6b73d90miaotony-cp310-cp310-linux_x86_64.whl /home/ctf/

RUN cd /home/ctf && chown ctf:ctf /home/ctf && chmod 755 /home/ctf && \
    python -m venv env1 --system-site-packages && \
    python -m venv env2 --system-site-packages && \
    ./env1/bin/python -m pip install --no-cache-dir opencv-contrib-python-headless==4.7.0.72 && \
    ./env2/bin/python -m pip install --no-cache-dir opencv_python-4.7.0.6b73d90miaotony-cp310-cp310-linux_x86_64.whl && \
    ./env1/bin/python -c "import cv2; print(cv2.__version__)" && \
    ./env2/bin/python -c "import cv2; print(cv2.__version__)"

USER ctf
CMD ["xinetd", "-dontfork"]
