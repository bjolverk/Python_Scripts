import requests, bs4, sys
#s = requests.get("https://www.yandex.ru/")
#b = bs4.BeautifulSoup(s.text, "html.parser")

#course_USD = b.select(".inline-stocks__value_inner ")

#print(type(course_USD))
#print(course_USD[0].getText())
my_argument = 0
if len(sys.argv) > 1:
    my_argument = float(sys.argv[1])
else:
    my_argument=float(input("Введите нужную сумму: "))

def courseFinder():
    s = requests.get("https://www.yandex.ru/")
    b = bs4.BeautifulSoup(s.text, "html.parser")
    course_USD = b.select(".inline-stocks__value_inner ")
    result = (course_USD[0].getText())
    result = float(result[:2] +"."+ result[3:])
    return(result)


usd_now = courseFinder()
print("Ваша сумма в рублях будет составлять", round(usd_now * my_argument, 2))
