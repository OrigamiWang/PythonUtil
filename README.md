# PythonUtil

## MySqlDemo
- mysql 连接执行工具

## PyWebviewFlaskDemo
- flask项目整合pywebview利用pyinstaller打包成exe可执行程序
- cmd
    - `{python_path}\\Scripts\pyinstaller --add-data "templates;templates" -F -w app.py`
    - `--add-data`为添加静态文件
    - `-F`打包成单独一个exe，否则打包成一个文件夹
    - `-w`关闭terminal

## ModulePathDemo
- sys.path.append()函数的使用
> 由于打包成pywebview以后，或者部署前后端到云端，会出现相对路径的错误，因此使用此函数
> 顺便了解以下pprint(Data Pretty Print)