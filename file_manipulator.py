import sys

def main():
    if sys.argv[1] == "reverse":
        do_reverse()
    elif sys.argv[1] == "copy":
        do_copy()
    elif sys.argv[1] == "duplicate-contents":
        do_duplicate_contents()
    elif sys.argv[1] == "replace-string":
        do_replace_string()
    else:
        print("不正なコマンドです")
        
# reverse操作をする関数
def do_reverse():
    input_path = sys.argv[2]
    output_path = sys.argv[3]
    content = ""
    
    with open(input_path, "r") as f:
        content = f.read()[::-1]
        
    with open(output_path, "w") as f:
        f.write(content)

# copy操作をする関数
def do_copy():
    input_path = sys.argv[2]
    output_path = sys.argv[3]
    content = ""
    
    with open(input_path, "r") as f:
        content = f.read()
        
    with open(output_path, "w") as f:
        f.write(content)
        

# duplicate-contents操作をする関数
def do_duplicate_contents():
    input_path = sys.argv[2]
    n = int(sys.argv[3])  # 整数じゃなかったとき用のバリデーションは後でやる
    content = ""
    
    with open(input_path, "r") as f:
        content = f.read()
        
    with open(input_path, "w") as f:
        for i in range(n):
            f.write(content)
    
# replace-string操作をする関数
def do_replace_string():
    input_path = sys.argv[2]
    needle = sys.argv[3]
    new_string = sys.argv[4]
    content = ""
    
    with open(input_path, "r") as f:
        content = f.read().replace(needle, new_string)
        
    with open(input_path, "w") as f:
        f.write(content)

# 実行
main()