from ortools.sat.python import cp_model
from pydantic import BaseModel
from app.domain.api.dtos.models import Activity
    
class Optimizer:
    
    def __init__(self) -> None:
        self.model = cp_model.CpModel()
        self.activities: list[Activity] = []
        self.activities_var: dict = {}
        self.target_calories: int = 0
        self.no_hours: int = 0
        self._status = None
        
    def initialize_variables(self, activities: list[Activity], target_calories: int, no_hours: int):
        """Initialize variables for the optimizer

        Args:
            activities (list[Activity]): given activities
            target_calories (int): given target calories
            no_hours (int): given number of hours
        """
        self.target_calories = target_calories
        self.no_hours = no_hours
        self.activities = activities
        for activity in activities:
            self.activities_var[activity.name] = self.model.NewIntVar(0, 1, activity.name)
            
    def add_object_function(self):
        """ Add the objective function to the model
            function grows with the number of activities (dynamic)
        """
        self.model.Maximize(sum(self.activities_var[activity.name] * activity.calories for activity in self.activities))    
        
    def add_constraints(self):
        """Add constraints to the model

            explaination:
                - sum of activities should be less than or equal to the number of hours
                - sum of activities should be less than or equal to the target calories
                - activities should be in descending order
        """
        self.model.Add(sum(self.activities_var[activity.name] for activity in self.activities) <= self.no_hours)
        self.model.Add(sum(self.activities_var[activity.name] * activity.calories for activity in self.activities) <= self.target_calories)
        for i in range(len(self.activities) - 1):
            self.model.Add(self.activities_var[self.activities[i].name] >= self.activities_var[self.activities[i + 1].name])
            
    def solve_function(self):
        """Solve the model and return the result

        Returns:
            list[Activity]: list of activities that are selected
        """
        outcome = True
        solver = cp_model.CpSolver()
        self._status = solver.Solve(self.model)
        if self._status == cp_model.OPTIMAL:
            outcome = True
        else:
            outcome = False
            
        return outcome
    
    def return_result(self):
        """Return the result of the model

        Returns:
            list[Activity]: list of activities that are selected
        """
        result = []
        if self._status == cp_model.OPTIMAL:
            for activity in self.activities:
                if self.activities_var[activity.name].solution_value() == 1:
                    result.append(activity)
        return result
        
            
              
        