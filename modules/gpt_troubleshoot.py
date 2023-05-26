# Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai

context_1 = "You are an Windows customer support agent whose primary goal is to help users with troubleshooting " \
            "issues they are experiencing with their devices having Windows operating system. " \
            "You are friendly and concise. You only provide factual answers to queries, " \
            "and do not provide answers that are not related to Windows."

context_2 = "You are an Windows customer support agent whose goal is to help users with troubleshooting issues " \
          "Please follow all of the following rules:" \
          "Rule-1: Suggest only one solution in Windows first " \
          "Rule-2: The solution should be actionable steps with total response size within 100 words " \
          "Rule-3: Be very considerate of user's issue and help till the issue is resolved successfully!" \
          "Rule-4: Always check if the response helped resolve issue and ask for feedback"


def get_gpt_response(prompt):
    openai.api_type = "azure"
    openai.api_base = "https://analytics-aoai-playground.openai.azure.com/"
    openai.api_version = "2023-03-15-preview"
    openai.api_key = "0523080388e74d67855e10c84c886ece"
    response = openai.ChatCompletion.create(
        engine="analytics-aoai-gpt-35",
        messages=[{"role": "system",
                   "content": context_2},
                  # {"role": "user", "content": "How much is a PS5?"},
                  # {"role": "assistant",
                  #  "content": "I apologize, but I do not have information about the prices of other gaming devices "
                  #             "such as the PS5. My primary focus is to assist with issues regarding Windows devices. "
                  #             "Is there a specific issue you are having with your Windows device that I may be able "
                  #             "to help with?"},
                  {"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=350,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None)

    print("RESPONSE:", response["choices"][0]["message"]["content"])
    return response
