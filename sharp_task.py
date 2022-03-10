if __name__ == "__main__": 
    path = input("Enter a path to file: ") 
    with open(path, "r", encoding="utf-8") as f: 
 
    a = f.readlines() 
    for i in a: 
        if i.startswith("#"): 
        a.remove(i) 

    with open("file.py", "w", encoding="utf-8") as f: 
    for i in a: 
        f.write(i)
