import requests

with open('./main.py', 'r+' ,encoding='utf-8') as f:
    filestr = f.read()

    GET = requests.get('https://raw.githubusercontent.com/lovelyxmj/misaka/master/main.py')
    if GET.text == filestr:
        print('更新检查完毕！并没有更新')
        f.close()
    else:
        print('发现新的更新，准备更新')
        f.seek(0)
        f.truncate()
        f.write(filestr.replace(filestr, GET.text))
        print('更新完毕!')
        