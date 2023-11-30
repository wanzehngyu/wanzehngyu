import json
from gevent import pywsgi
from main import main_call,logger
import os
from flask import Flask, request
from flask_cors import CORS, cross_origin
import platform
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/entity_extraction', methods=['POST'])
@cross_origin()
def gen_ans():
    # 上传文档
    data = {"sucess": 0}
    file = request.files.get("filename")
    # 表示没有发送文件
    if file is None:
        logger.info('文件上传失败！')
        return {'message': "文件上传失败"}
    # 判断文件格式
    elif file.filename.endswith(('.pdf','.doc','.docx')):
        # 保存文件
        root_dir = os.getcwd()
        logger.info('---------------------------当前根目录：{}'.format(root_dir))
        file_name = file.filename.replace(" ", "")
        # windows和linux下目录调用方式不同
        if platform.system() == "Windows":
            file.save(root_dir + '/upload/' + file_name)
        elif platform.system() == "Linux":
            file.save(root_dir + '/upload/' + file_name)
        # 开始抽取
        table_result, end_result = main_call(file_name)
        data["table_result"] = table_result
        data["end_result"] = end_result
        data["sucess"] = 1
        output = json.dumps(data, ensure_ascii=False)
        logger.info('本次接口调用结束！\n')
        return output # 返回json格式的数据到客户端
    else:
        logger.info('上传文件格式不支持！')
        logger.info('本次接口调用结束！\n')
        return {'message': "上传文件格式不支持！"}

#123
if __name__ == '__main__':
    server = pywsgi.WSGIServer(("0.0.0.0",5001), app) #
    server.serve_forever()
