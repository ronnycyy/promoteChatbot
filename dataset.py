# -*- coding: utf-8 -*-


def get_qa_corpus(filename):
    """
    get corpus as list

    :param filename:  对话文件，一问一答形式
    :return: 列表中的单个问答对列表
    """
    f = open(filename, 'r', encoding='utf-8-sig')

    text = f.read()
    list_text = text.split('\n')
    # 奇数列表 答句
    odd_list = []
    # 偶数列表 问句
    even_list = []
    for line in list_text:
        if list_text.index(line) % 2 == 0:
            even_list.append(line)
        else:
            odd_list.append(line)
    corpus_list = []
    for l1 in even_list:
        corpus_list.append([l1, odd_list[even_list.index(l1)]])
    # print(corpus_list)

    print("Successful dialogues loaded")
    return corpus_list


def get_simple_corpus(filename):
    """

    :param filename:  单个语境的对话文件
    :return: 对话列表
    """
    f = open(filename, 'r', encoding='utf-8-sig')
    text = f.read()
    text_list = text.split('\n')

    return text_list

