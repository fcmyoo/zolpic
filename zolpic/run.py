import os


def download_pic(first_name, title):
    first_name = first_name[-15:]
    path = os.getcwd()
    name = path + '\\pic' + '\\' + title + '\\' + first_name.replace('/', '.')
    print('pathname:', name)

    if not os.path.exists('pic\\'+title):
        os.makedirs('pic\\'+title)
        if not os.path.exists(name):
            # data = rq.get(url)
            with open(name, 'wb') as f:
                f.write()
            f.close()
        else:
            pass
    else:
        if not os.path.exists(name):
            # data = rq.get(url)
            with open(name, 'wb') as f:
                f.write()
            f.close()
        else:
            pass

download_pic('http://desk.fd.zol-img.com.cn/t_s1920x1080c5/g5/M00/09/07/ChMkJlcdy4uIA-o5AARU99Yz4qMAAQkXgHYXzkABFUP812.jpg', 'test1')
