
## 打字练习格式化工具

**描述：**  

点右上角链接🔗
  

**文件结构：如果你需要当成一个收集仓库使用 or 直接点击右上角链接webapp**
```shell
.
├── pte_formatter.py
├── typingweb.py
├── raw_txt/
└── fast_txt/
```

- `pte_formatter.py:` The main script responsible for formatting and generating links.
- `typingweb.py:` The Streamlit web application script for interactive usage.
- `raw_txt/:` The folder where your raw English text files should be placed for formatting.
- `fast_txt/:` Folder containing formatted text files.

**使用方法:**  

1. 将您的原始英文文本文件放入 `raw_txt` 文件夹中。
2. 按照以下说明运行格式化脚本：

- 要格式化特定的文件：

```shell
  python pte_formatter.py --file yourfile.txt
```

- 要处理整个 `raw_txt` 目录

```shell
  python pte_formatter.py --directory
  ```

- 要为特定文件生成 10fastfingers 练习链接并在浏览器中打开:

```shell
  python pte_formatter.py --open your_raw_file.txt
  ```

运行上述命令后，链接将打印到控制台，并将在您的默认网页浏览器中打开，以便立即进行打字练习。

3. requirements 

```shell 
pip install -r requirements.txt
```
## **例子:**
比如当我有一下文本在 `raw_txt/sports_star.txt`
![](/imgs/example_1.png)

执行操作
```shell
python formatter.py --open sports_star.txt
```

然后就可以开打了

![](/imgs/example_2.png)


**注意事项:**  
此工具在生成的链接中保留了输入文件的单词和标点的顺序。它还将连字符连接的单词视为单个实体，以确保练习的准确性。

