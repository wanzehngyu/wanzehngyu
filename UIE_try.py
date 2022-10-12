#coding=utf-8
import re
import pdfplumber
import requests,json
import os
import docx
from functools import reduce
import re
import shutil
import pandas as pd
def extract_interface(text):
    """
    function: 调用抽取模型接口
    param: 需要模型抽取的一段文字
    return: 抽取结果，json格式
    """
    url = 'http://127.0.0.1:5000/model_app'
    raw_data = {'text': text}
    res = requests.post(url, raw_data)
    result = res.json()
    return result.get('data')



if __name__ == '__main__':
    text = '民事起诉状原告：上海银建出租汽车有限公司，住所地上海市虹口区场中路531号。法定代表人：刘春利，董事长。委托诉讼代理人：孔嵘，公司员工。被告：王庆学，男，1968年7月11日出生，汉族，住安徽省阜阳市阜南县。被告：中国人民财产保险股份有限公司厦门市分公司，住所地福建省厦门市思明区湖滨北路68号。负责人：罗健，总经理。委托诉讼代理人：余天云，上海恒量律师事务所律师。原告上海银建出租汽车有限公司（以下简称银建公司）与被告王庆学、中国人民财产保险股份有限公司厦门市分公司（以下简称保险公司）机动车交通事故责任纠纷一案'
    print(extract_interface(text))