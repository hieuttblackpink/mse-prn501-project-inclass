# DAY 3 - 051024 - PPR501 - MSE - FSB - Inclass exercise

import json

languages = {
    "language": "Python",
    "author": "Rossum"
}

json_string = json.dumps(languages)
print(type(json_string))
print(json_string)