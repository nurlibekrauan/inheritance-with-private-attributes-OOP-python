class Employee:
    def __init__(self, name, age, salary) -> None:
        self.set_name(name)
        self.set_age(age)
        self.set_salary(salary)

    # Сеттеры с проверками
    def set_name(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Имя должно быть непустой строкой.")
        self.name = name

    def set_age(self, age):
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Возраст должен быть положительным целым числом.")
        self.age = age

    def set_salary(self, new_salary):
        if not isinstance(new_salary, (int, float)) or new_salary <= 0:
            raise ValueError("Зарплата должна быть положительным числом.")
        self._salary = new_salary

    def get_salary(self):
        return self._salary


class Manager(Employee):
    def __init__(self, name, age, salary, bonus):
        super().__init__(name, age, salary)
        self.set_bonus(bonus)

    def set_bonus(self, new_bonus):
        if not isinstance(new_bonus, (int, float)) or new_bonus < 0:
            raise ValueError("Бонус должен быть неотрицательным числом.")
        self.__bonus = new_bonus

    def get_bonus(self):
        return self.__bonus


class Executive(Manager):
    def __init__(self, name, age, salary, bonus, strategy_plan=None):
        super().__init__(name, age, salary, bonus)
        self.set_strategy_plan(strategy_plan)

    def set_strategy_plan(self, new_strategy_plan):
        if not isinstance(new_strategy_plan, str) or not new_strategy_plan.strip():
            self.__strategy_plan = "No strategy plan"
        else:
            self.__strategy_plan = new_strategy_plan

    def get_strategy_plan(self):
        return self.__strategy_plan


# Пример использования с проверками:
try:
    employee = Employee(name="John Doe", age=30, salary=50000)
    manager = Manager(name="Alice Smith", age=35, salary=70000, bonus=5000)
    executive = Executive(
        name="Bob Johnson",
        age=50,
        salary=100000,
        bonus=20000,
        strategy_plan="Expand to Asia",
    )

    # Попытка изменения данных через сеттеры
    manager.set_bonus(7000)  # Изменение бонуса
    executive.set_strategy_plan("Expand to Europe")  # Изменение стратегического плана

    # Получение значений
    print(employee.get_salary())  # 50000
    print(manager.get_bonus())  # 7000
    print(executive.get_strategy_plan())  # Expand to Europe

except ValueError as e:
    print(f"Ошибка: {e}")
