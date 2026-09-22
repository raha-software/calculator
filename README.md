# Simple Calculator (Python)

A simple command-line calculator written in Python — my first Python project. I previously built several projects in C#.

## Features

- Basic operations: addition (+), subtraction (-), multiplication (*), division (/)
- Extra operations: power (**) and modulo (%)
- Continuous calculation (chaining): the previous result is reused as the next first operand
- Numbered calculation history
- Special commands available at any step: h, c, delete, q
- Error handling: division by zero, invalid input, invalid operator
- Saves each result to a text file

## Special Commands
| Command | Action |
|---------|--------|
| `h` / `H` | Show calculation history |
| `c` / `C` | Clear all history |
| `delete` / `DELETE` | Delete a specific item from history |
| `q` / `Q` | Quit the program |

## How to Run

    git clone https://github.com/raha-software/calculator.git
    cd calculator
    python calculator.py

## Example Output


What operator do you want?*

Please enter another number!3

36

What operator do you want?+

Please enter another number!4

40

What operator do you want?h

12 * 3 = 36
36 + 4 = 40
What operator do you want?q

Goodbye
## Technologies

- Python 3.x
- Git & GitHub

## What I Learned

- Python functions, loops, conditionals, and lists
- Error handling with try/except (ValueError, ZeroDivisionError, OSError)
- Flow control: break/continue, exit flags, and state variables
- File I/O (saving results)
- Git workflow: init, add, commit, push
- Creating a professional GitHub repository


## Future Plans

- Add a GUI using Tkinter
- Write unit tests with pytest
- Add advanced operations (power, square root, percentage)

## Author

Raha — software engineering student and developer.
GitHub: https://github.com/raha-software

## دربارهٔ این پروژه

این پروژه یک ماشین‌حساب ساده با پایتونه؛ اولین پروژهٔ پایتونیِ من.
پیش از این چند پروژه با سی‌شارپ ساختم و این کار برای یادگیری مفاهیم پایهٔ پایتون و آشنایی با گیت و گیت‌هاب انجام شد.

امکانات

- چهار عمل اصلی: جمع، تفریق، ضرب، تقسیم
- توان (**) و باقیمانده (%)
- زنجیره‌سازی محاسبات (نتیجهٔ قبلی به‌عنوان عملوند بعدی)
- تاریخچهٔ شماره‌گذاری‌شده با دستورهای h، c و delete
- مدیریت خطاها: تقسیم بر صفر، ورودی نامعتبر و عملگر نامعتبر
- ذخیره‌سازی خودکار نتایج در فایل متنی
