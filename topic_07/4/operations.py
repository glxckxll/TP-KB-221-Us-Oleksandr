class Operations:
    def sum(self, x, y):
        # Повертає суму 
        return x + y

    def min(self, x, y):
        # Повертає різницю 
        return x - y

    def mult(self, x, y):
        # Повертає добуток 
        return x * y

    def div(self, x, y):
        # Перевірка на ділення на нуль та повернення результату ділення
        if y == 0:
            raise ZeroDivisionError("На нуль не можна ділити")
        return x / y

    def get_operation_name(self, operation):
        # Визначення назви операції для логування
        operation_names = {
            "+": "Додавання",
            "-": "Віднімання",
            "*": "Множення",
            "/": "Ділення"
        }
        return operation_names.get(operation, "Невідома операція")
