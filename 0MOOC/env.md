# 环境搭建

在GitBook里面加入Disqus插件

##关键步骤: 

在GitBook的根目录下时, 新建一个文件book.json, 输入以下语句

{
    "plugins": ["disqus"],
    "pluginsConfig": {
        "disqus": {
            "shortName": "XXXXXXX"
        }
    }
}

参考内容:

###注册disqus

打开:https://disqus.com/
点击"Sign Up",输入邮箱,用户名,密码,创建账号
新建站点
登录后,点击右上角的齿轮,选择"Add Disqus To Site",填写"Site name",这是book.json里面要填的"shortName","Finish registration".
备注：
"shortName"和注册时填写的用户名作用不同: 用户名是账号的名称,而"shortName"是这个新建站点唯一的名称.一个账号可以有多个站点,也就有多个"shortName".

在网页上使用这个"shortName"以后,这个网页下面的所有评论都会发送到disqus上对应"shortName"的站点. 打开网页时,"shortName"告诉disqus需要加载并显示哪个站点的评论.

###插件安装

Gitbook中，在要编辑的书里， 点击右上角的下拉三角形，选择Edit Book Configuration.
系统会自动生成book.jason
添加下面的内容。
{
"plugins": ["disqus"],
“pluginsConfig”: {
"disqus": {
 “shortName":” “NAME-FROM-DISQUS”
  }
}
}
将NAME-FROM-DISQUS 改为上面提到注册时写的shortname。

参考链接:

https://zoejane.gitbooks.io/omooc2py/content/0MOOC/disqus.html

https://github.com/GitbookIO/plugin-disqus