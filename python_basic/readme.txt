python -m pyftpdlib
ftp://127.0.0.1:2121/

课程内容
1 pycharm安装
2 anaconda/python安装
3 python基础语法
4 python常用包requests的使用
5 正则表达式
6 python爬虫
7 自动化操作接口
8 python识别图片

拓展内容
pycharm的使用技巧

1  安装pycharm
http://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC

2 安装anaconda
https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/
环境变量：
C:\Users\yourname\Miniconda3
C:\Users\yourname\Miniconda3\Scripts
C:\Users\yourname\Miniconda3\Library\bin

修改源
conda config --get
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/

conda env list 查看系统中有哪些python环境
conda create -n python1v3 python=3.5 创建python环境
activate python1v3  切换python环境（linux中，前面要加source,即：source activate python1v3）
conda list 当前环境安装的有哪些包
conda search xxx 搜索xxx有哪些版本
conda install xxx  安装xxx
conda uninstall xxx  卸载xxx
conda install  flask==1.0.2 安装指定版本的包，不指定版本的话，会通过依赖关系，安装合适的最高版本
deactivate  退出python环境

pip的用法
pip search xxx    搜索xxx有哪些版本
pip install  xxx   安装xxx
pip uninstall xxx    卸载xxx
pip install  flask==1.0.2  安装指定版本的包，不指定版本的话


conda 源配置


3 python 基础用法
a 基本数据结构int,float,str,list,tuple,dict,set
b 循环控制语句if for while
c 常用内置函数len,type,sort,abs,int,float,str,range,enumerate,input
d 文件的读写

4 python常用包requests的使用
    pip install requests
    创建一个django的server,观测流量

5 正则表达式
   a) re.match(pattern, string, flags=0)
   ^ 匹配字符串的开头
   $ 匹配字符串的末尾
   . 匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
   [...]  用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
   re*   匹配0个或多个的表达式。
   re+   匹配1个或多个的表达式。
   re?    匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
   re{ n}  精确匹配 n 个前面表达式。例如， o{2} 不能匹配 "Bob" 中的 "o"，但是能匹配 "food" 中的两个 o。
   a| b  匹配a或b
   \w	匹配字母数字及下划线
   \W	匹配非字母数字及下划线
   \s	匹配任意空白字符，等价于 [\t\n\r\f].
   \S	匹配任意非空字符
   \d	匹配任意数字，等价于 [0-9].
   \D	匹配任意非数字
   b) findall(string[, pos[, endpos]])  在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
   string : 待匹配的字符串。
   pos : 可选参数，指定字符串的起始位置，默认为 0。
   endpos : 可选参数，指定字符串的结束位置，默认为字符串的长度
   c) re.split(pattern, string[, maxsplit=0, flags=0])
        split 方法按照能够匹配的子串将字符串分割后返回列表





6 python爬虫


7 自动化操作接口


8 python识别图片
