
## 打字练习格式化工具

**描述：**  

🔗 at top-right corner
  
![Demo](imgs/output.gif)


**File Structure; Read the following guide if you plan to use this as a collection repository; if not, directly click the web app link at the top right**
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

**How to use:**  

1. Place your raw English text files into the `raw_txt` folder。
2. Run the formatting script as per the following instruction：

- To format a specific file:

```shell
  python pte_formatter.py --file yourfile.txt
```

- To process the entire `raw_txt` directory:

```shell
  python pte_formatter.py --directory
  ```

- To generate a 10fastfingers practice link for a specific file and open it in a browser:

```shell
  python pte_formatter.py --open your_raw_file.txt
  ```

After running the above commands, the link will be printed to the console and will open in your default web browser for immediate typing practice.

3. requirements 

```shell 
pip install -r requirements.txt
```
## **例子:**
For example, when I have the following text in `raw_txt/sports_star.txt`
![](/imgs/example_1.png)

Run the command:
```shell
python formatter.py --open sports_star.txt
```

And then you can start practicing.

![](/imgs/example_2.png)

**Note:**
This tool preserves the order of words and punctuation in the generated link. It also treats hyphenated words as single entities to ensure the accuracy of the practice.

