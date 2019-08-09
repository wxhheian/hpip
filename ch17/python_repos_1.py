import requests

#执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:",r.status_code)           #200表示请求成功

#将API响应储存在一个变量里
response_dict = r.json()

#处理结果
#print(response_dict.keys())

print("Totol repositories:",response_dict['total_count'])

#搜索有关仓库的信息
repo_dicts = response_dict['items']
print("Repositories returned:",len(repo_dicts))


print("\nSelected information about first repository:")
for repo_dict in repo_dicts:
    print("Name:",repo_dict['name'])
    print("Owner:",repo_dict['owner']['login'])
    print("Stars:",repo_dict['stargazers_count'])
    print('Repository:',repo_dict['html_url'])
    print('Description:',repo_dict['description'])
