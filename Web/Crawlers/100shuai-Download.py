#!/usr/bin/env python3

# $ ./Download.py

import subprocess, sys, os, codecs

Error_List = []

Error_List.append("http://v.youku.com/v_show/id_XMTY3ODM5MzM0MA==.html")
Error_List.append("http://v.youku.com/v_show/id_XMTY3ODQwNDAwMA==.html")
Error_List.append("http://v.youku.com/v_show/id_XMTY3ODQxODY0NA==.html")
Error_List.append("http://v.youku.com/v_show/id_XMTY3ODQzMDEyOA==.html")
Error_List.append("http://v.youku.com/v_show/id_XMTY3ODQ3MzY4MA==.html")
Error_List.append("http://v.youku.com/v_show/id_XMTY3ODQ4Nzk1Mg==.html")
Error_List.append("http://v.youku.com/v_show/id_XMTY3ODQ4MjAwNA==.html")

# Retry
while len(Error_List) != 0:
    NewError_List = []
    for url in Error_List:
        if os.system("you-get -y proxy.uku.im:443 " + url) != 0:
            print("Download Error: " + url)
            NewError_List.append(url)
    Error_List = []
    Error_List = NewError_List[:]
