def cross_join(employees, departments):
    """
    Реализует декартово произведение списков employees и departments

    :param employees: Список LastName сотрудников таблицы Employee
    :param departments: Список DepartmentName таблицы Department
    :return: Генератор пар (LastName, DepartmentName)
    """
    return ((col, row) for col in employees for row in departments)
