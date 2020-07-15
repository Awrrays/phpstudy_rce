### phpstudy_rce

**requirements** : `pip install -r requirements.txt`

**env** : python3

**vul** : phpstudy_rce

**args** :

```
usage:
       _               _             _
 _ __ | |__  _ __  ___| |_ _   _  __| |_   _
| '_ \| '_ \| '_ \/ __| __| | | |/ _` | | | |
| |_) | | | | |_) \__ \ |_| |_| | (_| | |_| |
| .__/|_| |_| .__/|___/\__|\__,_|\__,_|\__, |
|_|         |_|                        |___/

Phpstudy Backdoor detect tool.

optional arguments:
  -h, --help         show this help message and exit
  -u URL, --url URL  Target to detect.
  -c, --command      Whether to enter the interactive shell.
```

**e.g.** : 

```python
python3 phpstudy_rce.py -u http://example.com -c
    -u 	http://example.com			# 指定目标
    -c 								# 加上-c 写shell，不加只检测是否存在漏洞。
```

**Test screenshot** ：

<img src="./detect.png" alt="image-20200715135801214" style="zoom:80%;" />

<img src="./getshell.png" alt="image-20200715140013848" style="zoom: 67%;" />