## PTE Typing Practice Formatter

**Description:**  
This Python script is designed for PTE (Pearson Test of English) test takers who want to practice their typing skills using real test material. The tool converts given English text files to a format suitable for the website 10fastfingers and generates a link for practice, making it easy to practice typing with customized content.

**Folder Structure:**
```shell
.
├── formatter.py
├── raw_txt/
└── fast_txt/
```

- `formatter.py`: This is the main script that does the formatting and link generation.
- `raw_txt/`: Place all your raw text files in this directory that you want to format.
- `fast_txt/`: The formatted files will be saved in this directory.

**Usage:**  

1. Place your raw English text files inside the `raw_txt` folder.
2. Run the formatter script as described below:

- To format a specific file:

```shell
  python formatter.py --file yourfile.txt
```

- To process the entire `raw_txt` directory:

```shell
  python formatter.py --directory
```

- To generate a 10fastfingers practice link for a specific file and open it in your browser:

```shell
  python formatter.py --open your_raw_file.txt
```

After running the above command, the link will be printed to the console, and it will also be opened in your default web browser for immediate typing practice.

**Notes:**  
This tool retains the order of words and punctuation from the input file in the generated link. It also treats hyphenated words as single entities to ensure accuracy in practice.

**Benefits:**  
Practicing with real PTE material can provide a more realistic experience and better preparation for the actual test.
