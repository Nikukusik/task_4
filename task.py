from pathlib import Path
import re
#path = Path("salary.txt")
def total_salary(path):
    try:
        with open(path) as file:
            lines = file.readlines()
            pattern = r"\d+"
            str_num_list = []
            count = 0
            for line in lines:
                str_num_list += re.findall(pattern, line)
                num_list = []
                count += 1
            for i in str_num_list:
                num_list.append(int(i))
            total = 0
            for i in num_list:
                total += i
            average = total/count
            return (f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {int(average)}")
    except FileNotFoundError:
        print("File not found")
    except Exception:
        print("Unknown problem")

#print(total_salary(path))
        
path = Path("cats_info.txt")
def get_cats_info(path):
    with open(path, "r") as file:
        lines = file.readlines()
        pattern = r"[^\n]"
        cats_info = []
        for line in lines:
            line = re.findall(pattern, line)
            string = ""
            for i in line:
                string += i
            line = string.split(",")
            cat_info = {}
            cat_info.update({"id":line[0]})
            cat_info.update({"name":line[1]})
            cat_info.update({"age":line[2]})
            cats_info.append(cat_info)
        return cats_info

#print(get_cats_info(path))
