# Simple Calculator (Python)

A command-line calculator written in Python — my first Python project.
I had previously built several projects in C#.

## Features

- Four basic operations: `+`  `-`  `*`  `/`
- Extra operations: power `**` and modulo `%` and Square root `sqrt`
- **Chaining** — the previous result is reused as the next first operand
- **Numbered history** with the commands `h`, `c` and `delete`
- Error handling: division by zero, invalid input, invalid operator
- Every result is automatically appended to `file.txt`

## Special Commands

These work at **any** input step:

| Command | Action |
| --- | --- |
| `h` / `H` | Show the calculation history |
| `c` / `C` | Clear the whole history |
| `delete` / `DELETE` | Delete a single entry by its number |
| `q` / `Q` | Quit the program |

## ▶️ How to Run
```bash```
git clone https://github.com/raha-software/calculator.git
cd calculator
python calculator.py

## Example Session

text
Please enter a number! 12
What operator do you want? *
Please enter another number! 3
36
What operator do you want? +
Please enter another number! 4
40
What operator do you want? h
 1. 12 * 3 = 36
 2. 36 + 4 = 40
What operator do you want? q
Goodbye

The same results are also stored in `file.txt`:

text
36
40

## Technologies

- Python 3.x
- Git & GitHub

## What I Learned

- Python functions, loops, conditionals and lists
- Error handling with `try` / `except` (`ValueError`, `ZeroDivisionError`, `OSError`)
- Flow control: `break`, `continue`, exit flags and state variables
- File I/O (appending results to a text file)
- Git workflow: `init`, `add`, `commit`, `push`
- Writing a proper project README

## Roadmap

- [ ] **Refactor to object-oriented code** — separate responsibilities into dedicated classes (history, formatting, file writing, calculation core, user interface)
- [ ] Add unit tests with `pytest`
- [ ] Add a GUI with Tkinter

## Known Limitations

Honest notes about the current single-file version — all of them are on the list for the next version:

- `file.txt` is written to the current working directory.
- Inside the `delete` dialog there is no way to cancel; the program keeps asking until a valid number is entered.
- `Ctrl+C` / `Ctrl+D` are not handled, so the program exits without a message.

## Author

**Raha** — software engineering student and developer
GitHub: https://github.com/raha-software

---

<div dir="rtl">

## دربارهٔ این پروژه

این پروژه یک ماشینحساب خط فرمان با پایتون است؛ اولین پروژهٔ پایتونی من.
پیش از این چند پروژه با سیشارپ نوشته بودم و این کار برای یادگیری مفاهیم پایهٔ پایتون و آشنایی با گیت و گیتهاب انجام شد.

### امکانات

- چهار عمل اصلی: جمع (`+`)، تفریق (`-`)، ضرب (`*`)، تقسیم (`/`)
- عملیات دیگر: توان (`**`) ، باقیمانده (`%`) ، جذر (`sqrt`)
- زنجیرهسازی محاسبات؛ نتیجهٔ قبلی بهعنوان عملوند اولِ محاسبهٔ بعدی استفاده میشود
- تاریخچهٔ شمارهگذاریشده همراه با دستورهای `h`، `c` و `delete`
- مدیریت خطاها: تقسیم بر صفر، ورودی نامعتبر و عملگر ناشناس
- ذخیرهٔ خودکار هر نتیجه در فایل متنی `file.txt`

### دستورهای ویژه

این دستورها در هر مرحله از برنامه کار میکنند:

| دستور | کار |
| --- | --- |
| `h` / `H` | نمایش تاریخچهٔ محاسبات |
| `c` / `C` | پاک کردن کل تاریخچه |
| `delete` / `DELETE` | حذف یک عضو مشخص از تاریخچه با شمارهٔ آن |
| `q` / `Q` | خروج از برنامه |

### اجرا

bash
git clone https://github.com/raha-software/calculator.git
cd calculator
python calculator.py

### نقشهٔ راه

- [ ] بازنویسی کد با ساختار شیءگرا و تفکیک مسئولیتها در کلاسهای جداگانه
- [ ] نوشتن تستهای واحد با `pytest`
- [ ] افزودن رابط گرافیکی با Tkinter

### محدودیتهای نسخهٔ فعلی

- فایل `file.txt` در پوشهٔ جاری ساخته میشود.
- در دیالوگ `delete` راهی برای لغو وجود ندارد و برنامه تا وارد کردن یک شمارهٔ معتبر ادامه میدهد.
- ترکیب کلیدهای `Ctrl+C` و `Ctrl+D` مدیریت نشده است.

این موارد در نسخهٔ بعدی (نسخهٔ شیءگرا) برطرف میشوند.

</div>
