#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

def log(msg):
  print(msg)

def exec(cmd):
  result_code = os.system(cmd)
  if result_code != 0:
    log("命令执行失败 ===> " + cmd)
    exit(1)

'''
从命令行读取数据
'''
def popen(cmd):
  stream = os.popen(cmd)
  result = stream.read().rstrip()
  stream.close()
  return result

'''
将固定格式的git提交信息格化
返回二维数组
[' 810c6b1', 'Initial commit', 'liulinru13', '2020-07-01 16:41:30']]
'''
def splitgitmsg(cmd_param):
  git_msg = popen('git %s' % cmd_param)
  # log(git_msg)
  msg_list = list(filter(lambda x: len(x) > 0, git_msg.split('*')))
  # log(str(msg_list))
  note_content_list = []
  for msg in msg_list:
    content_arr = msg.split('|^|')
    note_content_list.append(content_arr)
  # log(str(note_content_list))
  return note_content_list

'''
将提交记录按天分组
顺序为时间倒序
'''
def msggrouping(content_list):
  msg_dict = {}
  for msg_arr in content_list:
    # 2020-07-01 17:38:16\n 取年月日
    date = msg_arr[-1].split(' ')[0]
    if date not in msg_dict:
      msg_dict[date] = []
      
    msg_dict[date].append({'author': msg_arr[-2], 'content': msg_arr[1]})
  
  # log(str(msg_dict))
  return msg_dict


def build_day_content(date, day_note_content):
  temp_str = ''
  template_title = '### %s \n\n' % date
  template_content = '%d. %s\n'
  day_note_content.reverse()
  index = 1
  temp_str += template_title
  for content in day_note_content:
    temp_str += template_content % (index, content['content'])
    index += 1
  return temp_str

'''
根据字典内容生成markdown格式的文件
'''
def generate_markdown_file(msg_dict):
  body = ''
  dates = sorted(msg_dict.keys())
  
  for date in dates:
    body += build_day_content(date, msg_dict[date])
    body += '\n\n'
  log(body)
  
  title = ''
  # log(msg_dict.keys())
  dates.reverse()
  if len(dates) > 1:
    title = '%s TO %s' % (dates[-1] , dates[0])
  else:
    title = '%s' % dates[0]

  file_path = './note/%s.md' % title

  with open(file_path, 'w+') as f:
    f.write('## %s\n\n' % title)
    f.write(body)

  return

generate_markdown_file(msggrouping(splitgitmsg(sys.argv[1])))