# Proxy pattern is used when we have to implement some access restrictions , pre and post processing , caching.


from abc import ABC, abstractmethod
class EmployeeDao(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def create_employee(self, employee_name):
        pass

    @abstractmethod
    def update_employee(self, employee_name):
        pass

    @abstractmethod
    def delete_employee(self, employee_name):
        pass


class EmployeeImpl(EmployeeDao):
    def __init__(self):
        pass
    def create_employee(self, employee_name):
        print(f"new employee created with name {employee_name}.")

    def delete_employee(self, employee_name):
        print(f"employee deleted with name {employee_name}.")

    def update_employee(self, employee_name):
        print(f"employee updated with name {employee_name}.")


class EmployeeProxy(EmployeeDao):
    def __init__(self):
        self.employee = EmployeeImpl()

    def create_employee(self, employee_name,user_level):
        if not user_level == 'ADMIN':
            print("not authorised to create employee.")
        else:
            self.employee.create_employee(employee_name)

    def delete_employee(self, employee_name,user_level):
        if not user_level == 'ADMIN':
            print("not authorised to delete employee.")
        else:
            self.employee.delete_employee(employee_name)

    def update_employee(self, employee_name,user_level):
        self.employee.update_employee(employee_name)



if __name__ == '__main__':
    proxy_obj = EmployeeProxy()
    proxy_obj.create_employee('Sharad', 'ADMIN')