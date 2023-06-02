import re
from io import StringIO

# reg_url = re.compile(
#     r"(https?://(?:www\.)?[-a-zA-Z\d@:%._+~#=]{1,256}\.[a-zA-Z\d()]{1,6}\b[-a-zA-Z\d()@:%_+.~#?&/=]*)")
reg_url = re.compile(r"((?=.*[a-z])[-A-Za-z\d]+\.)+((?=.*[a-z])[-A-Za-z\d]+)")


def escape_url(url: str, replace_dot_by: str = '🤔') -> str:
    seg = url.split('.')
    return replace_dot_by.join(seg)


def escape_text(text: str, replace_dot_by: str = '🤔') -> str:
    text = text.replace("http://", '')
    text = text.replace("https://", '')
    with StringIO() as sio:
        prev = 0
        for mat in reg_url.finditer(text):
            sio.write(text[prev:mat.start()])
            sio.write(escape_url(mat.group(), replace_dot_by))
            prev = mat.end()

        sio.write(text[prev:])

        return sio.getvalue()


if __name__ == "__main__":
    msg = "HEADER https://docs.python.org/zh-cn/3/library/re.html?highlight=re#match-objects AND THIS IS OTHER http://pypi.org/project/regex/ END"
    msg = escape_text(msg)
    print(msg)
