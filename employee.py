_monthly = 'monthly'
_hourly = 'hourly'
_no_bonus = 'no bonus'
_bonus_commission = 'bonus_commission'
_contract_commission = 'contract_commission'


class Salary:
    """
    Salary class which handles the type of contract and pay
    """
    def __init__(self, is_monthly_contract, monthly_salary=None, rate=None, hours=None):
        self.is_monthly_contract = is_monthly_contract
        self.monthly_salary = monthly_salary
        self.rate = rate
        self.hours = hours

    def get_pay(self):
        if self.is_monthly_contract:
            return self.monthly_salary
        else:
            return self.rate * self.hours

    def get_type(self):
        if self.is_monthly_contract:
            return _monthly
        else:
            return _hourly

    def get_rate(self):
        if not self.is_monthly_contract:
            return self.rate

    def get_hours(self):
        if not self.is_monthly_contract:
            return self.hours

class Commission:
    """
    Commission class to handle commissions paid for the different employees 
    """
    def __init__(self, commission_type, number_of_contracts=None, commission_per_contract=None, bonus=None):
        self.commission_type = commission_type
        self.number_of_contracts = number_of_contracts
        self.commission_per_contract = commission_per_contract
        self.bonus = bonus

    def get_pay(self):  
        if self.commission_type == _no_bonus:
            return 0
        elif self.commission_type == _bonus_commission:
            return self.bonus
        elif self.commission_type == _contract_commission:
            return self.number_of_contracts * self.commission_per_contract

    def get_type(self):
        return self.commission_type
        
    def get_number_of_contracts(self):
        return self.number_of_contracts

    def get_commission_per_contract(self):
        return self.commission_per_contract

    def get_bonus(self):
        if self.commission_type == _bonus_commission:
            return self.bonus

class Employee:
    """
    Employee class to create employes.
    It takes a name for the employee, a salary object and a commission object.
    """

    def __init__(self, name, salary, commission):
        self.name = name
        self.salary = salary
        self.commission = commission

    def __str__(self):
        message = f'{self.name} works on a '
        if self.salary.get_type() == _monthly:
            message = message + f'monthly salary of {self.salary.get_pay()}'
        else:
            message = message + f'contract of {self.salary.get_hours()} hours at {self.salary.get_rate()}/hour'


        if self.commission.get_type() == _bonus_commission:
            message = message + f' and receives a bonus commission of {self.commission.get_bonus()}'
        elif self.commission.get_type() == _contract_commission:
            message = message + f' and receives a commission for {self.commission.get_number_of_contracts()} contract(s) at {self.commission.get_commission_per_contract()}/contract'

        message = message + f'. Their total pay is {self.salary.get_pay() + self.commission.get_pay()}.'
        return message

    def get_pay(self):
        return self.salary.get_pay() + self.commission.get_pay()


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie_salary = Salary(True, 4000)
billie_commission = Commission(_no_bonus)
billie = Employee('Billie', billie_salary, billie_commission)



# {Charlie} works on a {contract} of {100} hours at 25/hour}.  
# Their total pay is {2500}.
charlie_salary = Salary(False, None, 25, 100)
charlie_commission = Commission(_no_bonus)
charlie = Employee('Charlie', charlie_salary, charlie_commission)



# {Renee} works on a {monthly salary} of {3000} 
# and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee_salary = Salary(True, 3000)
renee_commission = Commission(_contract_commission, 4, 200)
renee = Employee('Renee', renee_salary, renee_commission)



# Jan works on a contract of 150 hours at 25/hour and receives a 
# commission for 3 contract(s) at 220/contract.  Their total pay is {4410}.
jan_salary = Salary(False, None, 25, 150)
jan_commission = Commission(_contract_commission, 3, 220)
jan = Employee('Jan', jan_salary, jan_commission)



# Robbie works on a monthly salary of 2000 and receives a bonus 
# commission of 1500.  Their total pay is 3500.
robbie_salary = Salary(True, 2000)
robbie_commission = Commission(_bonus_commission, None, None, 1500)
robbie = Employee('Robbie', robbie_salary, robbie_commission)


# # Ariel works on a contract of 120 hours at 30/hour and receives a bonus 
# commission of 600.  Their total pay is 4200.
ariel_salary = Salary(False, None, 30, 120)
ariel_commission = Commission(_bonus_commission, None, None, 600)
ariel = Employee('Ariel', ariel_salary, ariel_commission)
