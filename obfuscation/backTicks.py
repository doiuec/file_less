import re


simbol = ["$", "&", "'", '"', "'" ]

def backticks(content_data):
    result = []
    content_data = list(content_data)

    for i in range(len(content_data)):
        if content_data[i] == "`":
            if content_data[i+1] == "n":
                del content_data[i+1]
                content_data.append(" ")
                i += 1

            elif content_data[i+1] == "\\" and content_data[i+2] == "n":
                result.append(content_data[i])
                
            else:
                pass
        else:
            result.append(content_data[i])

    after_replace = str(result)
    return (after_replace)