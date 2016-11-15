# -*- coding: cp936 -*-
import sys
import getopt
def usage():
    print "this in for wydomain.log merge"
    print "example: python wylogtotxt.py 1.log 2.log -o 3.log"

opts,args = getopt.getopt(sys.argv[1:],"ho:",["help","output="])
#opts, args = getopt.getopt(sys.argv[1:], "ho:", ["help", "output="])
for m,n in opts:

    if m in ("-h","--help"):
        usage()
        sys.exit()
    if m in ("-o","--output"):

        b = eval(open(args[0]).read())
        c = eval(open(args[1]).read())#列表类型转换
        a = b + c #列表合并
        one = list(set(a))#列表去重
        for i in one:
            open(n,'a+').writelines(i+'\n')
    print "-----------------正在进行类型转换-----------------"
    print "-----------------正在进行去重-----------------"
    print "-----------------正在进行合并-----------------"
print "-------->窑子哥哥在上，合并成功<--------"
        




