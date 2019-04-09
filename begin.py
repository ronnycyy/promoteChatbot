"""
Beginning of the dialogue system

@author: ronny
create_time: 2019-04-09
"""

from chat_train import get_chatbot
from end_points import get_end_points

# 获取机器人
chatbot = get_chatbot()

# 获取结束对话列表
end_list = get_end_points()


print("========================== 进入Task-oriented chatbot交互 ==============================")

# Keyboard interaction
# use 'ctrl + d' to quit
print("您好，这里是XX银行信用卡合作商，来电是想邀请您办理XX银行信用卡！")
while True:
    try:
        query = input(">>>")
        response = chatbot.get_response(query)
        print(response)
        response = str(response)
        if response in end_list:
            print("===推销结束，是否继续？Y/N===")
            intend = input()
            if intend == 'Y':
                print("===聊天继续===")
            else:
                print("===退出系统===")
                break
    except EOFError:
        break
