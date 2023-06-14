import os

for filename in os.listdir("./"):
    print(filename)
    if '.py' in filename:
        continue
    text = []
    with open(filename, 'r') as f:
        text = f.readlines()
        for i in range(0, len(text)):
            if 'https://cdn.6-d.cc' in text[i]:
                text[i] = text[i].replace('https://cdn.6-d.cc/img', 'https://img.r2.6-d.cc/oldcdn')
                print(text[i])
    with open(filename, 'w+') as f:
        f.writelines(text)
