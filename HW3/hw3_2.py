text = "Python динамически типизируется и собирает мусор.\
        Он поддерживает множество парадигм программирования, включая структурированное (в частности, процедурное), объектно-ориентированное и функциональное программирование.\
        Его часто описывают как язык с включенными батарейками из-за его обширной стандартной библиотеки".split()


for i in range(len(text)):
    if text[i].istitle():
        text[i] = text[i].lower()
    if "." in text[i]:
        text[i] = text[i].replace(".", "")
    if "," in text[i]:
        text[i] = text[i].replace(".", "")

temp_dict = dict()
for item in text:
    key = temp_dict.setdefault(item, text.count(item))

values = temp_dict.values()
sorted_values = list(sorted(values, reverse=True))

result = {}
top = 10

for value in sorted_values:
    for element in temp_dict.keys():
        if temp_dict[element] == value:
            if element not in result:
                result[element] = temp_dict[element]
                top -= 1
                break
    if top <= 0: break

print(result)