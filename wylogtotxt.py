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
        c = eval(open(args[1]).read())#�б�����ת��
        a = b + c #�б�ϲ�
        one = list(set(a))#�б�ȥ��
        for i in one:
            open(n,'a+').writelines(i+'\n')
    print "-----------------���ڽ�������ת��-----------------"
    print "-----------------���ڽ���ȥ��-----------------"
    print "-----------------���ڽ��кϲ�-----------------"
print "-------->Ҥ�Ӹ�����ϣ��ϲ��ɹ�<--------"
        




