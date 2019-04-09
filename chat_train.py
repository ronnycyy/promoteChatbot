# -*- coding: utf-8 -*-

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

from dataset import get_qa_corpus


def get_chatbot():
    chatbot = ChatBot(
        'WuKong',    # 机器人的名字
        read_only=True,   # 关闭输入学习，只读训练语料
        logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch',  # 最佳匹配适配器
                'threshold': 0.65,   # 置信度
                'default_response': '不好意思哦，刚没听清，您可以再说一遍吗？'  # 默认回答
            }
        ]
    )

    # Create a new trainer for the chatbot
    trainer = ListTrainer(chatbot)

    # 获取问答对（全局语境）
    qa_corpus = get_qa_corpus('ai_dias.txt')

    # Train the chatbot based on the dialogues corpus
    for dialogue in qa_corpus:
        trainer.train(dialogue)

    return chatbot
