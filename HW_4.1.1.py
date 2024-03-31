from pathlib import Path

def  total_salary(file_path: Path):
    try:
        employee = []
        t_salary, qty = 0, 0
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                try:
                    line = line.strip()
                    employee = line.split(",")
                    t_salary += float(employee[1])
                    qty += 1
                except Exception as ex:
                    print(f"mistake in data structure: {ex}, line: {line}")
                av_salary = t_salary/qty
    except FileNotFoundError as ex:
        print(f"{ex}")
    
    return (t_salary, av_salary)

def main():
    file_path = Path("salary.txt")
    (t_salrary, av_salary) = total_salary(file_path)
    print(f"Total salary is {t_salrary}, avarage salary is {av_salary}")

if __name__ == "__main__":
    main()