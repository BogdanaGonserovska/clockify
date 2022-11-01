from requests import get
from json import loads, dumps

api_key = 'N2FkN2M3YzItOTg4Zi00ODI4LTk0NmUtNDQxMTY5NzdmZjE4'
data = get('https://api.clockify.me/api/v1/workspaces/63615c163560570dc23ca6f1/projects/63615c58eb805462b0b1b146/tasks', headers={'x-api-key': api_key})
json_obj = loads(data.content)
print(dumps(json_obj, indent = 2, ensure_ascii=False))


data_for_tasks = get('https://api.clockify.me/api/v1/workspaces/63615c163560570dc23ca6f1/user/63615c163560570dc23ca6f0/time-entries', headers={'x-api-key': api_key})
json_for_tasks = loads(data_for_tasks.content)

for i in range(len(json_obj)):
    task_id = json_obj[i]['id']
    date = None
    for j in range(len(json_for_tasks)):
        if task_id == json_for_tasks[j]['taskId']:
            date = json_for_tasks[j]['timeInterval']['start']
            break
    print(f"Task:\t\t{json_obj[i]['name']}")
    if json_obj[i]['duration'] is not None:
        print(f"Duration:\t{json_obj[i]['duration'][2::]}")
    else:
        print(f"Duration:\t{json_obj[i]['duration']}")
    print(f"Date:\t\t{date}\n")