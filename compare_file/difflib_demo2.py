# coding=UTF-8
# 作者:herui
# 时间:2021/6/27 16:02
# 功能:

import difflib,sys

def readFile(filename):    #文件读取分隔函数
    try:
        with open(filename,'rb') as filehandle:
            text = filehandle.read().splitlines()   #读取后以行的形式进行分隔
            print(text)
            return text
    except IOError as error:
        print('Read file Error:' + str(error))
        sys.exit()

file_path1 = r'D:/study/pythonScript/compare_file/test_file/A.txt' #sys.argv[1]
file_path2 = r'D:/study/pythonScript/compare_file/test_file/B.txt' #sys.argv[2]

file1 = readFile(file_path1)
file2 = readFile(file_path2)

file1_lines  = file1.splitlines()

d = difflib.Differ()
diff = d.compare(file1, file2)
# print('\n'.join(diff))
print(diff)