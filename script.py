from pysentimiento import create_analyzer
import json

params = {
    "display_name": "Text To Emotion"
}

emotion_analyzer = create_analyzer(task="emotion", lang="en")

def output_modifier(ori_string):
    lines = ori_string.splitlines()
    emo_string = ""
    for txt in lines:
        line = txt.strip()
        if line != "":
            emo_line = emotion_analyzer.predict(line)
            the_emo = json.dumps(emo_line.probas)
            emo_string = emo_string + line + "--emostart--" + the_emo + "--emoend--\n"

    print(emo_string)
    return emo_string

    #emo_string = emotion_analyzer.predict(ori_string)
    #res = json.dumps(emo_string.probas)
    #return ori_string + "--emostart--" + res + "--emoend--"
