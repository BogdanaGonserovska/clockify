from requests import get
from json import loads, dumps

api_key = 'N2FkN2M3YzItOTg4Zi00ODI4LTk0NmUtNDQxMTY5NzdmZjE4'
data = get('https://api.clockify.me/api/v1/workspaces/63615c163560570dc23ca6f1/projects/63615c58eb805462b0b1b146/tasks', headers={'x-api-key': api_key})
json_obj = loads(data.content)
print(dumps(json_obj, indent = 2, ensure_ascii=False))