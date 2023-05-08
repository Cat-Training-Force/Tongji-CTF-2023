FROM python:3.7-alpine

ENV PYTHONUNBUFFERED=0

RUN echo "http://mirrors.ustc.edu.cn/alpine/v3.5/main" > /etc/apk/repositories
RUN echo "http://mirrors.ustc.edu.cn/alpine/v3.5/community" >> /etc/apk/repositories

RUN apk add gcc
COPY src/requirements.txt /tmp
RUN pip install --no-cache-dir -r /tmp/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# Creating working directory
RUN mkdir /app
COPY src/ /app

RUN adduser -S appuser
RUN chmod -R 755 /app/
RUN chmod +x /app/start.sh
RUN chmod 777 /app/main.s
RUN chmod 777 /app/main
RUN chmod 777 /app/flag
USER appuser

WORKDIR /app
CMD ["sh","/app/start.sh"]
