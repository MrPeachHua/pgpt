# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai


def gpt_content(input):
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      # {"role": "system", "content": "You are a helpful assistant."},
      # {"role": "user", "content": "Who won the world series in 2020?"},
      # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
      {
        "role": "user",
        "content": input
      }
    ])
  # print(response)
  print(response["choices"][0]["message"]["content"])
  return response["choices"][0]["message"]["content"]


# a = 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;
# gpt_content("你好世界")
