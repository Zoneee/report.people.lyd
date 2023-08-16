import openai


class GPT:
    def __init__():
        pass

    # 设置您的OpenAI API密钥
    openai.api_key = "YOUR_API_KEY"

    # 调用ChatGPT API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # 使用适当的模型
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"},
            {"role": "assistant",
                "content": "The Los Angeles Dodgers won the World Series in 2020."},
            {"role": "user", "content": "Where was it played?"}
        ]
    )

    # 提取助手的回复
    assistant_reply = response['choices'][0]['message']['content']

    # 打印助手的回复
    print(assistant_reply)
