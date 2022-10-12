from flask import Flask, request
import json
from gevent import pywsgi
from UIE_model import extract_spoes_format

app = Flask(__name__)


@app.route('/model_app', methods=['GET','POST'])
def gen_ans():
    data = {"sucess": 0}
    text = request.form.get('text')
    result = extract_spoes_format(text)
    data["data"] = result
    data["sucess"] = 1
    output = json.dumps(data, ensure_ascii=False)

    return output # 返回json格式的数据到客户端

# python3 -m flask run
if __name__ == '__main__':
    server = pywsgi.WSGIServer(("0.0.0.0",5000), app) #
    server.serve_forever()




