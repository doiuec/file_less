#TODO:クラスに書き換える

import re

data = 'This is an ("{1}{0}{2}" -f"AMP","EX", "LE")'

def formatReplace(contentData):

    if(re.search(r"-(f|F)", contentData)):
        exchange_index = re.findall(r"\"(\{.*\})\"", contentData)
        # print("hey")
        # print(exchange_index)
        exchange_index = (re.findall(r"\{\d\}", exchange_index[0]))
        brackets = "\{\}"
        for i in range(len(exchange_index)):
            for x in range(len(brackets)):
                exchange_index[i] = exchange_index[i].replace(brackets[x],'')
        print(exchange_index)
        # ['1', '0', '2']

        exchange_sentence = re.findall(r"-f\".*\)", contentData)
        exchange_components = re.findall(r"\".*?\"", exchange_sentence[0])
        print(exchange_components)
        # ['"AMP","EX", "LE"']

        exchanged = list()

        for entry in exchange_index:
            exchanged.append(exchange_components[int(entry)])
        print(exchanged)
        # ['"EX"', '"AMP"', '"LE"']

        exchanged = ''.join(exchanged).replace('\"','')
        print(exchanged)
        # EXAMPLE

        raw_content = re.findall(r".*\(\"\{", data)
        raw_content = raw_content[0].strip("\(\"\{")
        print(raw_content)

        



formatReplace(data)
