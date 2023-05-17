import subprocess

args = ["python3", "test.py"]
process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(000000000000)

try:
    # 等待命令执行完成或超时
    stdout, stderr = process.communicate(timeout=5)
except subprocess.TimeoutExpired:
    # 超时异常，终止子进程
    process.kill()
    stdout, stderr = process.communicate()

# 输出标准输出和错误
print(stdout.decode())
print(stderr.decode())