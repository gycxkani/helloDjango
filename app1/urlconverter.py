class FourDigitYearConverter:
    # 4位非负整数的正则表达式
    regex = r'[0-9]{4}'

    # 转换为python对象
    def to_python(self, value):
        return int(value)

    # 转换为url
    def to_url(self, value):
        return '%04d' % value