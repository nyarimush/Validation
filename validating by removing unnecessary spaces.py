

text = "  Hello world  "
print(text.strip())  # "Hello world"

text = "  hello"
print(text.lstrip()) # "hello"

text = "hello  "
print(text.rstrip()) # "hello"

text = "##hello##"
print(text.strip("#")) # "hello"

filename = ">>>report.pdf<<<"
print(filename.strip("<>"))  # "report.pdf"
