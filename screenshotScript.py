# Library
from selenium import webdriver
import time
import urllib.request

def getHtml(url):
    html = urllib.request.urlopen(url).read()
    return html
 
def saveHtml(file_name, file_content):
    with open(file_name, "wb") as f:
        f.write(file_content)

f1 = open("./v1.csv")
line = f1.readline()
count = 0
# print(type(line))
while line:
    if count > 210:
        break
    if count <= 200:
        line = f1.readline()
        count += 1
        continue
    cor = []
    tmp = line.split(",")
    cor.append(tmp[2])
    cor.append(tmp[3].strip())
    print(cor)
    data = ''
    with open('/Users/hanyuchen/Documents/index.html', 'r+') as f:
        for line2 in f.readlines():
            # print(line2)
            # print(1)
            if(line2.find('LatLng') >= 0):
                line2 = '                const c = new google.maps.LatLng(' + cor[0] + ',' + cor[1] + ');\n'
                # print(line2)
            data += line2
    with open('/Users/hanyuchen/Documents/index.html', 'r+') as f:
        f.writelines(data)

    driver = webdriver.Chrome()
    driver.get("file:///Users/hanyuchen/Documents/index.html")
    driver.maximize_window()
    time.sleep(2)
    print(count)
    try:
        picture_url = driver.get_screenshot_as_file("/Users/hanyuchen/Desktop/img2/" + str(count) + ".png")
        print("Success", picture_url)
    except BaseException as msg:
        print(msg)

    driver.quit()
    count += 1
    line = f1.readline()
f1.close()


