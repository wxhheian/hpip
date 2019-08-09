import requests
import pygal

from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

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

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    plot_dict = {
        'value':repo_dict['stargazers_count'],
        'label':str(repo_dict['description']),                    #注意要加str 不然报错
        'xlink':repo_dict['html_url']             #添加具体的链接
        }
    plot_dicts.append(plot_dict)

 #可视化
my_style = LS('#333366',base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.force_uri_protocol = 'http'
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names


chart.add('',plot_dicts)
chart.render_to_file('python_repos.svg')
