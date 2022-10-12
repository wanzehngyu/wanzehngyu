#! -*- coding:utf-8 -*-
# 三元组抽取任务，基于“半指针-半标注”结构
from paddlenlp import Taskflow

def extract_spoes(text):
    """
    function:模型抽取函数
    param: 读入的文书文本
    return: 返回值为UIE模型抽取的关键信息
    """
    #设置需抽取的关键信息类别
    schema = ['被告', '原告','上诉人', '被上诉人','案件名称']
    #设置UIE模型参数
    ie = Taskflow('information_extraction', schema=schema,task_path='./checkpoint/model_best',device_id=0)
    ie.set_schema(schema)
    extract_re=ie(text)[0]
    #将抽取结果转化为想要的格式存入redic变量中
    redic={}
    for key,value in extract_re.items():
        content=[]
        for i in range(0,len(value)):
            content.append(value[i].get('text'))
        bvalue='，'.join(content)
        redic[key]=bvalue
    return redic



def extract_spoes_format(text):
    """
    function:模型抽取函数主函数
    param: 读入的文书文本
    return: 返回值为模型抽取的关键信息结果redic
    """
    result = extract_spoes(text)
    return result


if __name__ == '__main__':
    text = '民事起诉状原告：上海银建出租汽车有限公司，住所地上海市虹口区场中路531号。法定代表人：刘春利，董事长。委托诉讼代理人：孔嵘，公司员工。被告：王庆学，男，1968年7月11日出生，汉族，住安徽省阜阳市阜南县。被告：中国人民财产保险股份有限公司厦门市分公司，住所地福建省厦门市思明区湖滨北路68号。负责人：罗健，总经理。委托诉讼代理人：余天云，上海恒量律师事务所律师。原告上海银建出租汽车有限公司（以下简称银建公司）与被告王庆学、中国人民财产保险股份有限公司厦门市分公司（以下简称保险公司）机动车交通事故责任纠纷一案'
    print(extract_spoes_format(text))


