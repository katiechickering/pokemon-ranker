# ⚡ Pokemon Ranker


## 🌟 Highlights

- Rank Pokemon from 1 to 10
- Your custom ranking will post to the homepage
- Randomize the ranks with the randomize button!


## ℹ️ Overview

Hello, my name is Katie. This Pokemon ranking app is my final project for Harvard's Introduction to Computer Science course, also known as CS50. This course started my software engineering journey and I am thrilled to share what I learned. I have encorporated Flask, Python, Jinja, jQuery, SQL, HTML, and Bootstrap. into my project to hightlight some of the languages I have learned. My files are organized in an MVC format. I hope you have some fun while ranking your favorite Pokemon!


### ✍️ Authors

Katie Chickering - https://github.com/katiechickering


## 🚀 Usage

```bash
python server.py
 * Serving Flask app 'flask_app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
 * Running on http://localhost:5001
```
Run 'python server.py' in your terminal. Then, copy and paste http://localhost:5001 into your browser to view the application!


## ⬇️ Installation

```bash
python pipenv install
```
First, install all the required packages with the code above. Then, run pokemon_ranker.sql in your local MySQL database software to save the database. Finally, change the user and password in lines 8 and 9 of flask_app/config/mysqlconnection.py to match your database credentials. Please see below for a reference.

```py
connection = pymysql.connect(host = 'localhost',
                            user = 'root', # Line 8
                            password = 'rootroot', # Line 9
                            db = db,
                            charset = 'utf8mb4',
                            cursorclass = pymysql.cursors.DictCursor,
                            autocommit = False)
```


## 💭 Feedback and Contributing

If you found this insightful or if you have suggestions, please start a [discussion](https://github.com/katiechickering/pokemon-ranker/discussions/1)!

**Reference**: [Hide rank option once it has been selected using jQuery](https://stackoverflow.com/questions/26137309/remove-selected-option-from-another-select-box)

**Reference**: [Project inspiration](https://cajunavenger.github.io/)