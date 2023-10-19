import os




def get_filenames_in_directory(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

if __name__ == '__main__':
    filename = 'E:/py/ChatIE/prompts/FL/反分裂国家法.json'
    a = os.path.exists(filename)
    print(a)

    # 使用方法
    directory = 'E:/py/ChatIE/prompts/FL/' # 将这里替换为你的目录路径
    filenames = get_filenames_in_directory(directory)
    for fname in filenames:
        fname = fname.replace('.json','')
        print("'"+fname+"',")
    #print(filenames)