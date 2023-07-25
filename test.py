import codecs

def ReadFile(filePath,encoding="utf-8"):
    with codecs.open(filePath,"r",encoding) as f:
        return f.read()
def WriteFile(filePath,u,encoding="gbk"):
    with codecs.open(filePath,"w",encoding) as f:
        f.write(u)
def UTF8_2_GBK(src,dst):
    content = ReadFile(src,encoding="utf-8")
    WriteFile(dst,content,encoding="gbk")

UTF8_2_GBK(r'C:/Users/Kehl Zeyu Li/Desktop/school_info.csv', r'C:/Users/Kehl Zeyu Li/Desktop/school_info_updated.csv')
