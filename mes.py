month = str(input())

month_dict = {
    "1" : "January",
    "2" : "February",
    "3" : "March",
    "4" : "April",
    "5" : "May",
    "6" : "June",
    "7" : "July",
    "8" : "August",
    "9" : "September",
    "10" : "Octuber",
    "11" : "November",
    "12" : "December",

}
for (key, value) in month_dict.items():
    if key == month:
        print(value)