import requests
import json
import re

#changable

space_id = "44505211"

api_token = 'pk_44428424_G1QVCPF98EA8BYPE6UIIYS8YOQL2WQSF'

headers_values = {
  "Content-Type": "application/json",
  "Authorization": f"{api_token}"
}

url_get_folders = "https://api.clickup.com/api/v2/space/" + space_id + "/folder"

query_folders = {
  "archived": "false"
}

response_space = requests.get(url_get_folders, headers=headers_values, params=query_folders)

for folder in response_space.json()["folders"]:

    url_get_lists = f"https://api.clickup.com/api/v2/folder/{folder['id']}/list"

    query = {
      "archived": "false"
    }

    response_ls = requests.get(url_get_lists, headers=headers_values, params=query)

    print(response_ls.json())

    for list in response_ls.json()["lists"]:

        print(list["id"]+' '+list['name'])
        url_get_tasks = f"https://api.clickup.com/api/v2/list/{list['id']}/task"

        page = 0
        check_tasks = 0


        while check_tasks != []:
            query_tasks = {
            "page": page,
            "archived": "false",
            "include_closed": "true",
            "subtasks": "true"}
            response_tasks = requests.get(url_get_tasks, headers=headers_values, params=query_tasks)
            check_tasks = response_tasks.json()['tasks']
            page = page + 1
            for task in response_tasks.json()["tasks"]:
                payload2 = {
                    "value": 9
                }
                url_cf = f"https://api.clickup.com/api/v2/task/{task['id']}/field/5db20fa1-82c7-476c-84a5-31ab7bb24382"
                response = requests.post(url_cf, json = payload2, headers = headers_values)
                print(task['name']+' '+'done')
