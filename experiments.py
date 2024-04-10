import mlflow

def calculator(a,b,operation):
    if operation  == "add":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "mul":
        return a * b
    elif operation == "div":
        return a / b
    else:
        return "Invalid operation"
    

if __name__ == "__main__":
    with mlflow.start_run():
        a = 5
        b = 10
        opt = "add"
        result = calculator(a,b,"sub")  
        mlflow.log_param("a", a)
        mlflow.log_param("b", b)
        mlflow.log_param("operation", opt)
        print(f"The result is:{result}")
        mlflow.log_metric("result", result)
                                