import os
import hashlib

filter_file = ["xml", "iml", "log", "jar", "lst", "properties", "class", "cache", "meta", "zip"]
check_file = ["java","pom", "txt"]

# 遍历文件夹
def walkFile(file):
    file_name_maps = {}
    file_name_lst = []

    for root, dirs, files in os.walk(file): #os.walk
        print(root, dirs, files)

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
                # print(file_name,":",data)
            file_md5 = hashlib.md5(data).hexdigest()
            file_name_lst.append(f)
            file_name_maps[f] = {"md5": file_md5, "file_name": file_name}
    return file_name_maps, file_name_lst


def compare_dirs(dir1, dir2):
    file_name_maps1, file_name_lst1 = walkFile(dir1)
    file_name_maps2, file_name_lst2 = walkFile(dir2)
    print("开始校验文件数量")
    gap_1 = list(set(file_name_lst1).difference(set(file_name_lst2)))  # b中有而a中没有的
    if gap_1:
        print("路径：" + dir2 + "缺少文件")
        for g in gap_1:
            print(g)
        # return False

    gap_2 = list(set(file_name_lst2).difference(set(file_name_lst1)))  # b中有而a中没有的
    if gap_2:
        print("路径：" + dir1 + "缺少文件")
        for g in gap_2:
            print(g)
        # return False
    print("文件数量校验一致")

    print("开始文件内容校验")
    flag = True
    for key in file_name_maps1:
        if file_name_maps1[key]["md5"] != file_name_maps2[key]["md5"]:
            print("\033[1;31;42m " + file_name_maps1[key]["file_name"] + "文件内容不一致" + "\033[0m")
            flag = False
    print("文件内容校验结束，文件内容" +"一致" if flag else "不一致")
    return flag


def main():
    print("文件校验开始")
    flag = compare_dirs(r"D:\study\test_A",
                        r"D:\study\test_B")

    print("校验结束," + "文件比对" + "成功" if flag else "失败")


if __name__ == '__main__':
    main()