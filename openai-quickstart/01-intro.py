from openai import OpenAI
from dotenv import load_dotenv,find_dotenv
from openai.types.chat import ChatCompletionUserMessageParam

load_dotenv(find_dotenv())

# client是后续编程的入口
client = OpenAI()


def test01():
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user",
             "content": "请介绍一下第一次出国去华盛顿有什么玩的？"}
        ]
    )
    print(completion.choices[0].message.content)



def test02():
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[ChatCompletionUserMessageParam(role="user", content="请以李白的风格，写一首描述中国长城的诗")],
        stream=True
    )
    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")



if __name__ == '__main__':
    test02()




