
from pathlib import Path

def  get_cats_info(file_path: Path):
    try:
        cat_dict= {}
        cats_list=[]
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                try:
                    line = line.strip()
                    cat_str = line.split(",")
                    cat_dict = {
                        'id': cat_str[0],
                        'name': cat_str[1],
                        'age': str(int(cat_str[2]))
                        }
                    cats_list.append(cat_dict)
                except Exception as ex:
                    print(f"mistake in data structure: {ex}, line: {line}")
      
    except FileNotFoundError as ex:
        print(f"{ex}")
    
    return cats_list

def main():
    file_path = Path("cats.txt")
    cats_info = get_cats_info(file_path)
    print(cats_info)

if __name__ == "__main__":
    main()