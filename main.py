# -*- coding: utf-8 -*-

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

from dataset import get_qa_corpus, get_simple_corpus

chatbot = ChatBot(
    'WuKong',    # 机器人的名字
    read_only=True,   # 关闭输入学习，只读训练语料
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'threshold': 0.65,
            'default_response': '不好意思哦，刚没听清，您可以再说一遍吗？'  # 默认回答
        }
    ]
)

# Create a new trainer for the chatbot
trainer = ListTrainer(chatbot)

# 获取问答对（全局语境）
qa_corpus = get_qa_corpus('ai_dias.txt')
# 获取单个语境
simple_corpus = get_simple_corpus('simple.txt')

# Train the chatbot based on the dialogues corpus
for dialogue in qa_corpus:
    trainer.train(dialogue)

print("question and answer training completed")

trainer.train(simple_corpus)
print("single context training completed")
print()
print("========================== 进入Task-oriented chatbot交互 ==============================")


# Keyboard interaction
# use 'ctrl + d' to quit
print("您好，这里是XX银行信用卡合作商，来电是想邀请您办理XX银行信用卡！")
while True:
    try:
        query = input(">>>")
        response = chatbot.get_response(query)
        print(response)
    except EOFError:
        break
