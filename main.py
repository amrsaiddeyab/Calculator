#My Third Python Project (Calculator) - (2026-3-13 / Friday)

import tkinter
import math

#game setup
button_values = [
    ["AC", "+/-", "%", "÷", "log", "ln"], 
    ["7", "8", "9", "×", "x²", "sin"], 
    ["4", "5", "6", "-", "xⁿ", "cos"],
    ["1", "2", "3", "+", "π", "tan"],
    ["0", ".", "√", "=", "DEL", "round"]
]

operator_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]
function_symbols = ["log", "x²", "xⁿ", "π", "DEL"]
extra_symbols = ["ln", "sin", "cos", "tan", "round"]

row_count = len(button_values)
column_count = len(button_values[0])

#window setup
window = tkinter.Tk()
window.title('Calculator')
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text='0', anchor='w', background="#000000", font=('Arial', 45), 
                foreground="white", width=3, height=2)

frame.pack()
label.grid(row=0, column=0, columnspan=column_count, sticky='we')

#button setup
for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, width=4, height=2, font=("Arial", 30), 
                    command=lambda value=value : button_clicked(value),)
        
        if value in operator_symbols:
            if value == "=":
                button.config(foreground="#000000", background="#F59038")
        
            else:
                button.config(foreground="#000000", background="#F6AA67")

        elif value in top_symbols:
            if value == "AC":
                button.config(foreground="#000000", background="#FFFF82")

            else:
                button.config(foreground="#000000", background="#F1F1B7")

        elif value in function_symbols:
            if value == "DEL":
                button.config(foreground="#000000", background="#866BF2")
   
            else:
                button.config(foreground="#000000", background="#B09CFF")

        elif value in extra_symbols:
            if value == "round" :
                button.config(foreground="#000000", background="#12CFE4")
            else :

                button.config(foreground="#000000", background="#30EBFF")

        else:
            if value == "." or value == "√" or value == "0":
                button.config(foreground="#000000", background="#F2988F")
            
            else:
                button.config(foreground="#000000", background="#A9A9A9")

        button.grid(row=row+1, column=column)

A = '0'
operator = None
B = '0'
sqr_num = '0'
log_num = '0'
ln_num = '0'
sin_num = '0'
cos_num = '0'
tan_num = '0'
detection = None

def clear_all():
    global A, B, operator, sqr_num, log_num, ln_num, sin_num, cos_num, tan_num, label, detection

    A = '0'
    operator = None
    B = '0'
    sqr_num = '0'
    log_num = '0'
    ln_num = '0'
    sin_num = '0'
    cos_num = '0'
    tan_num = '0'
    detection = None

def remove_zero_decimal(num):
    if num % 1 == 0 :
        num = int(num)
    
    return str(num)

def square_root():
    global A, B, sqr_num, label, operator

    if "√" in A :
        A = (math.sqrt(float(A[1:])))

    if "√" in B :
        B = math.sqrt(float(B[1:]))

    if "√" in sqr_num:
        sqr_num = str(math.sqrt(float(sqr_num[1:])))

    return A, B

def log():
    global A, B, log_num, label, operator

    if "log" in A :
        A = math.log10(float(A[3:]))

    if "log" in B :
        B = math.log10(float(B[3:]))

    if "log" in log_num:
        log_num = str(math.log10(float(log_num[3:])))

    return A, B

def pi():
    global A, B, operator, label

    pi_value = math.pi

    if "π" in A :
        a, b = A.split("π")
        pi_index = A.find("π")
        A = A.replace("π", "")
        
        if len(A) == 0:
            A = pi_value
        
        elif pi_index == len(A):            
            A = float(A) * pi_value

        else:
            if a == "" :
                A = float(A) * pi_value
                
            else:
                A = float(a) * float(b) * pi_value

    if "π" in B :
        c, d = B.split("π")
        pi_index = B.find("π")
        B = B.replace("π", "")

        if len(B) == 0:
            B = pi_value
        
        elif pi_index == len(B):            
            B = float(B) * pi_value

        else:
            if c == "" :
                B = float(B) * pi_value
                
            else:
                B = float(c) * float(d) * pi_value

    return A, B

def power_2():
    global A, B, operator, label

    if "^2" in A: 
        a, b = A.split("^")
        A = float(a) ** float(b)

    if "^2" in B:
        c, d = B.split("^")
        B = float(c) ** float(d)

    return A, B

def power_num():
    global A, B, operator, label

    if "^" in A:
        a, b = A.split("^")
        A = float(a) ** float(b)

    if "^" in B:
        c, d = B.split("^")
        B = float(c) ** float(d)

    return A, B

def ln():
    global A, B, ln_num, label, operator

    if "ln" in A :
        A = math.log(float(A[2:]))

    if "ln" in B :
        B = math.log(float(B[2:]))

    if "ln" in ln_num:
        ln_num = str(math.log(float(ln_num[2:])))

    return A, B

def sin():
    global A, B, sin_num, label, operator

    if "sin" in A :
        A = math.sin(math.radians(float(A[3:])))

    if "sin" in B :
        B = math.sin(math.radians(float(B[3:])))

    if "sin" in sin_num:
        sin_num = str(math.sin(math.radians(float(sin_num[3:]))))

    return A, B

def cos():
    global A, B, cos_num, label, operator

    if "cos" in A :
        A = math.cos(math.radians(float(A[3:])))

    if "cos" in B :
        B = math.cos(math.radians(float(B[3:])))

    if "cos" in cos_num:
        cos_num = str(math.cos(math.radians(float(cos_num[3:]))))

    return A, B

def tan():
    global A, B, tan_num, label, operator

    if "tan" in A :
        A = math.tan(math.radians(float(A[3:])))

    if "tan" in B :
        B = math.tan(math.radians(float(B[3:])))

    if "tan" in tan_num:
        tan_num = str(math.tan(math.radians(float(tan_num[3:]))))

    return A, B

def button_clicked(value):
    global A, B, operator, sqr_num, log_num, ln_num, sin_num, cos_num, tan_num, label, detection

    if value in top_symbols:
        if value == "AC":
            label["text"] = '0'

            clear_all()
            
        elif value == "+/-":
            A = label["text"]
            label["text"] = remove_zero_decimal(float(A) * -1)

        else :
            A = label["text"]
            label["text"] = remove_zero_decimal(float(A) / 100)

    elif value in operator_symbols:
            if value == "=":
                B = label["text"]

                if "√" in A or "√" in B or "√" in sqr_num:
                    
                    A, B = square_root()

                    if sqr_num != '0' and operator is None :
                        label["text"] = remove_zero_decimal(float(sqr_num) * float(B))

                        detection = True
                
                elif "log" in A or "log" in B :
                    A, B = log()

                    if log_num != '0' and operator is None :
                        label["text"] = remove_zero_decimal(float(log_num) * float(B))

                        detection = True

                elif "π" in A or "π" in B:
                    A, B = pi()

                elif "^2" in A or "^2" in B:
                    A, B = power_2()

                elif "^" in A or "^" in B:
                    A, B = power_num()

                elif "ln" in A or "ln" in B or "ln" in ln_num:
                    A, B = ln()

                    if ln_num != '0' and operator is None :
                        label["text"] = remove_zero_decimal(float(ln_num) * float(B))

                        detection = True
                        
                elif "sin" in A or "sin" in B or "sin" in sin_num:
                    A, B = sin()

                    if sin_num != '0' and operator is None :
                        label["text"] = remove_zero_decimal(float(sin_num) * float(B))

                        detection = True

                elif "cos" in A or "cos" in B or "cos" in cos_num:
                    A, B = cos()

                    if cos_num != '0' and operator is None :
                        label["text"] = remove_zero_decimal(float(cos_num) * float(B))

                        detection = True

                elif "tan" in A or "tan" in B or "tan" in tan_num:
                    A, B = tan()

                    if tan_num != '0' and operator is None :
                        label["text"] = remove_zero_decimal(float(tan_num) * float(B))

                        detection = True

                if operator is not None:
                    numA = float(A) 
                    numB = float(B)

                    if operator == '÷':
                        if B != '0' :
                            label["text"] = remove_zero_decimal(numA / numB)

                    elif operator == '×':
                        label["text"] = remove_zero_decimal(numA * numB)
                                
                    elif operator == '-':
                        label["text"] = remove_zero_decimal(numA - numB)

                    else:
                        label["text"] = remove_zero_decimal(numA + numB)
                    
                elif detection == None:
                    label["text"] = remove_zero_decimal(float(B))

                clear_all()
            
            else:
                if operator is None:
                    if value == "÷":
                        A = label["text"]
                        label["text"] = '0'

                        operator = value
                        
                    elif value == "×":
                        A = label["text"]
                        label["text"] = '0'

                        operator = value

                    elif value == "-":
                        A = label["text"]
                        label["text"] = '0'

                        operator = value

                    else:
                        A = label["text"]
                        label["text"] = '0'

                        operator = value

    elif value in function_symbols:
        if value == 'DEL':
            if label["text"] != '0':
                if label["text"].endswith("log") or label["text"].endswith("sin") or label["text"].endswith("cos") or label["text"].endswith("tan"):
                    label["text"] = label["text"][:-3]

                elif label["text"].endswith("ln"):
                    label["text"] = label["text"][:-2]

                else :
                    label["text"] = label["text"][:-1]

                if len(label["text"]) == 0:
                    label["text"] = '0'

        elif value == "log" :
            log_num = label["text"]
            label["text"] = 'log'

        elif value == "π" :
            if label["text"] == '0':
                label["text"] = "π"

            else :
                label["text"] += "π"

        elif value == "x²":
            if label["text"] != '0':
                label["text"] += "^2"

        else:
            if label["text"] != '0':
                label["text"] += "^" 
            
    elif value in extra_symbols:
        if value == "ln":
            ln_num = label["text"]
            label["text"] = "ln"

        elif value == "sin":
            sin_num = label["text"]
            label["text"] = "sin"

        elif value == "cos":
            cos_num = label["text"]
            label["text"] = "cos"

        elif value == "tan":
            tan_num = label["text"]
            label["text"] = "tan"

        else:
            if label["text"] != '0':
                label["text"] = str(remove_zero_decimal(round(float(label["text"]), 2)))

    else:
        if value == ".":
            if value not in label["text"]:
                label["text"] += value

        elif value in "0123456789":
            if label["text"] == '0':
                label["text"] = value

            else :
                label["text"] += value

        else:
            sqr_num = label["text"]
            label["text"] = "√"
            
#center the window
window.update()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = window.winfo_width()
window_height = window.winfo_height()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()