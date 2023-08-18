
## PTE 打字练习格式化工具

**描述：**  
此 Python 脚本是为 PTE（Pearson 英语测试）考生设计的，帮助他们使用真实的测试材料练习打字技巧。此工具可以将给定的作文文本转换为适合 10fastfingers 网站的格式，并生成一个供练习的链接，用作于pte机考的打字spelling随便背一下作文模版:

- 增加了单词纠错功能, 可以在`formatter.py`里面设置`False`关闭纠正功能

**文件结构：**
```shell
.
├── formatter.py
├── raw_txt/
└── fast_txt/
```



- `formatter.py`: 这是执行格式化和链接生成的主脚本
- `raw_txt/`: 这是执行格式化和链接生成的主脚本
- `fast_txt/`: 这是执行格式化和链接生成的主脚本

**使用方法:**  

1. 将您的原始英文文本文件放入 `raw_txt` 文件夹中。
2. 按照以下说明运行格式化脚本：

- 要格式化特定的文件：

```shell
  python formatter.py --file yourfile.txt
```

- 要处理整个 `raw_txt` 目录

```shell
  python formatter.py --directory
  ```

- 要为特定文件生成 10fastfingers 练习链接并在浏览器中打开:

```shell
  python formatter.py --open your_raw_file.txt
  ```

运行上述命令后，链接将打印到控制台，并将在您的默认网页浏览器中打开，以便立即进行打字练习。

3. requirements 

```shell 
pip install -r requirements.txt
```
## **例子:**
例子当我有一下文本在 `raw_txt/sports_star.txt`
![](/imgs/example_1.png)

执行操作
```shell
python formatter.py --open sports_star.txt
```

然后就可以开打了

![](/imgs/example_2.png)


**注意事项:**  
此工具在生成的链接中保留了输入文件的单词和标点的顺序。它还将连字符连接的单词视为单个实体，以确保练习的准确性。



**好处:**  
使用真实的 PTE 材料进行练习可以提供更真实的体验，并更好地为实际测试做准备。
