import os
import hashlib

filter_file = ["xml", "iml", "log", "jar", "lst", "properties", "class", "cache", "meta", "zip"]
check_file = ["java","pom", "txt"]

# 遍历文件夹
def walkFile(file):
    file_name_maps = {}
    file_name_lst = []

    for root, dirs, files in os.walk(file): #os.walk
        # print(root, dirs, files)

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list

        # 遍历文件
        for f in files:
            file_name = os.path.join(root, f)
            file_type = file_name.split(".")[-1]
            # print(file_type)
            if file_type in filter_file:
                continue
            if file_type not in check_file:
                continue
            with open(file_name, 'rb') as fp:
                data = fp.read()
            file_md5 = hashlib.md5(data).hexdigest()
            file_name_lst.append(f)
            file_name_maps[f] = {"md5": file_md5, "file_name": file_name}
    print(file_name_lst)
    return file_name_maps, file_name_lst


def compare_dirs(dir1, dir2):
    file_name_maps1, file_name_lst1 = walkFile(dir1)
    file_name_maps2, file_name_lst2 = walkFile(dir2)
    print("开始校验文件数量")
    flag1 = True
    gap_1 = list(set(file_name_lst1).difference(set(file_name_lst2)))  # 1中有而2中没有的
    if gap_1:
        flag1 = False
        for g in gap_1:
            print("路径：" + dir2 + "缺少文件:" + g)

    flag2 = True
    gap_2 = list(set(file_name_lst2).difference(set(file_name_lst1)))  # 2中有而1中没有的
    if gap_2:
        flag2 = False
        print("路径：" + dir1 + "缺少文件:",end="")
        for g in gap_2:
             print(g,end=" ")
        print()

    file_name_lst1_num = str(len(file_name_lst1))
    print(dir1 + " 文件数量为：" + file_name_lst1_num)
    file_name_lst2_num = str(len(file_name_lst2))
    print(dir2 + " 文件数量为：" + file_name_lst2_num)

    if len(gap_1) == len(gap_2):
        print("结果：文件数量一致")
    else:
        print("结果：文件数量不一致")

    if flag1 and flag2:
        flag = True
    else:
        flag = False
    return flag


def main():
    print("文件校验开始")
    flag = compare_dirs(r"D:\study\test_A",
                        r"D:\study\test_A")

    # print("校验结束," + "文件比对" + "成功" if flag else "失败")


if __name__ == '__main__':
    main()