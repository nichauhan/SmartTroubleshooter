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

context_3 = "You are an Windows customer support expert whose primary goal is to help users with troubleshooting " \
            "issues they are experiencing with their devices having Windows operating system. You should be very " \
            "considerate of user's issue. You should provide various methods which could help fix the issue for the " \
            "customer, beginning with the simplest one. You should only provide factual answers to queries related to " \
            "Windows. If you do not know the answer to the query, reply by saying 'Sorry, I do not have any solution " \
            "to your problem as yet. You may be able to find your answer at windows.support.com.'."

# question_1 = "Windows cannot access the specified device, path, or file. You may not have the appropriate permission " \
#              "to access the item."
#
# answer_1 = "Please follow the steps in the methods below starting with method 1, if that method does not resolve " \
#            "the issue continue to the next method.\n\nMethod 1: Check the permission of the file or folder\nNote Make sure you are an Administrator or you are part of the Domain Admins group if you are in a domain.\nPermissions are rules associated with files that determine if you can access the file and what you can do with it. To check the permission of the file or folder, follow these steps:\na.Right-click the file or folder, and then select Properties.\nb.Select the Security tab.\nc.Under Group or User names, click your name to see the permissions you have.\nd.Select Edit, and then select to check the check boxes for the permissions that you need, and then select OK.\nFor more information on permissions, see http://windows.microsoft.com/windows7/what-are-permissions\n\nMethod 2: Check the file location\nYou might get this error if the shortcut or installation is attempting to access a location that is not currently available such as a networked or a removable drive. Check the path of the file that Windows cannot access and make sure that the location is accessible.\n\nMethod 3: Make sure that the file has not been moved or deleted\nYou can also receive this error if the file has been moved or deleted. Browse to the location of the file and make sure the file is in that location.\n\nMethod 4: Unblock the file\nIn some cases the file may be blocked by Windows. Check the properties of the file, there may be a note saying This file came from another computer and might be blocked to help protect this computer To check for and unblock the file, follow these steps:\na.Right-click the blocked file and then select Properties.\nb.In the General tab, select Unblock if the option is available.\n\nMethod 5: Check to see if your antivirus software is blocking the file\nYou can check to see if your antivirus software is blocking a file by temporarily disabling it, and then trying to open the file. If you have to temporarily disable your antivirus software, you should re-enable it as soon as you are done. If you’re connected to the Internet while your antivirus software is disabled, your PC is vulnerable to attacks.\nImportant: Disabling your antivirus software or changing the settings may make your PC vulnerable to viral, fraudulent, or malicious attacks. Microsoft does not recommend that you disable your antivirus software or change the settings.  If you have to temporarily disable your antivirus software, you should re-enable it as soon as you are done. Use this workaround at your own risk. To temporarily disable your antivirus software, see http://windows.microsoft.com/windows7/disable-antivirus-software."


def get_chat_history(history):
    """
    Function to extract previous user prompt and gpt response for context in next response
    """
    prompt_history = []

    for chat in history:
        if chat['is_user']:
            temp = {'role': 'user', 'content': chat['message']}
        else:
            temp = {'role': 'assistant', 'content': chat['message']}

        prompt_history.append(temp)

    return prompt_history


def get_gpt_response(prompt, history):
    openai.api_type = "azure"
    openai.api_base = "https://analytics-aoai-playground.openai.azure.com/"
    openai.api_version = "2023-03-15-preview"
    openai.api_key = "0523080388e74d67855e10c84c886ece"

    # Prepare the "messages" parameter as a combination of system role + historical context + current prompt
    custom_messages = [{"role": "system",    "content": context_3}] + \
                      get_chat_history(history) + \
                      [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(
        engine="analytics-aoai-gpt-35",
        messages=custom_messages,
        temperature=0,
        max_tokens=400,
        top_p=0.99,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None)
    
    response = response["choices"][0]["message"]["content"]

    print("RESPONSE:", response)
    return response
