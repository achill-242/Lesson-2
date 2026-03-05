address = ("8", "hilsingson", "Amsterdam", "South east holland", "Japan", "12345678")
for i in address:

    print(i)
houseno, apartName, city, state, country , pin = address
print(city)
#packing a report card
report = ("john", 56, 87, 65) #name,math,science,english score
#unpack the tuple
name, math, science, english = report
print("Student name: ", name)
print("math grade: ", math)
print("science grade: ", science)
print("english grade: ", english)

total = math + science + english // 3
print("average: ", total)

# travel planner

city = (("Paris", "France", 1200 ), ("Berlin ", " Germany", 1600))
print("Available cities: ")
for i in range(len(city)):
    print(i+1, "-", city[i][0])