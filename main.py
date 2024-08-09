import openai
import argparse
import time
import os
import pickle
import json

# parser = argparse.ArgumentParser(
#                     prog='VoiceToAction',
#                     description='Converts voicetotext notes to actions and organises them',
#                     epilog='Contact DK for any further info')

# parser.add_argument('-k', '--OAIkeyfile', required=True)      # option that takes a value
# # parser.add_argument('-v', '--verbose', action='store_true') 
# args = parser.parse_args()

class Config:
    def __init__(self, OAIapikey, OAIurl):
        self.OAIkey = OAIapikey
        # self.OAIurl = OAIurl

def set_up_args():
    """
    Simple function to take in arg parameters and make a config object out of them 
    """
    OpenAIAPIURL = ""
    args.OAIkeyfile
    conf = Config()
    return conf

def get_completion(client, prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=0.2,
    )

    return response

if __name__ == "__main__":
    loadfromfile = True
    # conf = set_up_args()
    f = open("C:\\Users\\Dhruv\\OAIVTAKey.key", "r")
    lines = f.readlines()
    f.close()
    client = openai.OpenAI(
    # This is the default and can be omitted
    api_key=lines[0])
    if not loadfromfile:
        prompt = "I am going to feed you a block of text. From this, identify all actionable steps and list them. Then find all notable information and list those separately. \
                In a separate section, identify my overall mood from this text and write it in a short sentence. \
                Output all of these in a json format. This is the following text to analyse:\n\n"
        stt_file = open(os.path.join(os.getcwd(), "testdata\\test_voice_HV60Beau.txt"), "r")
        lines = stt_file.readlines()
        stt_file.close()
        prompt += lines[0]
        print(prompt)
        # exit(0)
        response = get_completion(client, prompt)
        print(response)
        with open("response.pickle", "wb") as f:
            pickle.dump(response, f)
    elif loadfromfile:
        with open("testresponse.pickle", "rb") as f:
            loadedobject = pickle.load(f)
            print(loadedobject.choices[0].message.content)
            json_output = json.loads(loadedobject.choices[0].message.content)
            print(json_output)