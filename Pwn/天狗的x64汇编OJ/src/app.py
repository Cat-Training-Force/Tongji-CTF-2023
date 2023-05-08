from flask import Flask, render_template, request
import subprocess
import binascii

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # 处理表单提交
        input_text = request.form['input_text']

        with open("main.s","w") as fout:
            fout.write(input_text)

        try:
            ret = subprocess.run(
                ["sh", "runner.sh"],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                timeout = 10,
                shell = False
            )
        except subprocess.TimeoutExpired:
            output_text = 'Timeout'
            # 将输入框的内容上传的操作
            output_text = f"运行结果为：\n{input_text}"
            return render_template('index.html', default_text=input_text,output_text=output_text)

        try:
            output = ret.stdout.decode()
            output_text = output
        except UnicodeDecodeError:
            output_text = 'Can\'t get output, this is the hex : 0x' + binascii.hexlify(ret.stdout).decode()
        
        # 将输入框的内容上传的操作
        output_text = "运行结果为：{}".format(output_text)
        return render_template('index.html', default_text=input_text,output_text=output_text)
    else:
        # 显示表单页面
        default_text = '''.global _start
.intel_syntax noprefix
_start:
// 以下是你的代码，提交时请删除此行
'''
        return render_template('index.html', default_text=default_text)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='2333')
