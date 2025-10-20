
# 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

from openai import OpenAI

client = OpenAI(api_key="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")

# 设置你的API密钥
# client.api_key = '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'

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role":"user","content":"请介绍一下第一次出国去华盛顿有什么玩的？"}]
)

print(completion.choices[0].message.content)


# response = client.Completion.create(
#   engine="GPT-4o mini",
#   prompt="中国首都是什么城市？"
# )
#
# print(response.choices[0].text.strip())



