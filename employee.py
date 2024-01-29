#Employee ID Name Age Salary (PM)
employees = [["161E90", "Ramu", 35, 59000],
["171E22", "Tejas", 30, 82100],
["171G55", "Abhi", 25, 100000],
["152K46", "Jaya", 32, 85000]]

#write a program to sort the data and print the sorted data, giving options to sort by name, age and salary

#sort by name
def sort_by_name():
    print("Sorted by name")
    sorted_list = sorted(employees, key=lambda x: x[1])
    for i in sorted_list:
        print(i)
    
#sort by age
def sort_by_age():
    print("Sorted by age")
    sorted_list = sorted(employees, key=lambda x: x[2])
    for i in sorted_list:
        print(i)

#sort by salary
def sort_by_salary():
    print("Sorted by salary")
    sorted_list = sorted(employees, key=lambda x: x[3])
    for i in sorted_list:
        print(i)

#main
print("1. Sort by name")
print("2. Sort by age")
print("3. Sort by salary")
choice = int(input("Enter your choice: "))
if choice == 1:
    sort_by_name()
elif choice == 2:
    sort_by_age()
elif choice == 3:
    sort_by_salary()
else:
    print("Invalid choice")




