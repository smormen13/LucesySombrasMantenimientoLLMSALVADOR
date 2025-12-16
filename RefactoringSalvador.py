"""
Payroll System (Refactored)

This module provides a clean, typed, and documented implementation of a simple
CLI-based payroll system. It replaces the procedural approach with clearer
abstractions, descriptive names, and reusable functions while keeping behavior
compatible with the original app.py.

Usage:
    python RefactoringSalvador.py

The program allows you to:
- Add employees for departments: Sales (Ventas), IT, and HR (RRHH)
- Compute net salary applying department-specific tax and a cafeteria discount
- Print a report of all recorded employees
- Exit the application
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import List


class Department(Enum):
    """Enumeration of supported departments with user-facing labels."""

    SALES = "Ventas"
    IT = "IT"
    HR = "RRHH"


@dataclass
class Employee:
    """Represents an employee payroll entry.

    Attributes:
        name: The employee's full name.
        department: The department to which the employee belongs.
        gross_salary: The gross salary amount provided by the user.
        net_salary: The computed net salary after tax and cafeteria discount.
    """

    name: str
    department: Department
    gross_salary: float
    net_salary: float


class PayrollCalculator:
    """Encapsulates payroll calculation rules.

    This calculator applies a department-specific tax rate and a fixed
    cafeteria discount. Rules mirror the original program:
    - Sales (Ventas): 15% tax
    - IT: 15% tax
    - HR (RRHH): 16% tax
    - Cafeteria discount: 50 (flat)
    Net salary has a floor at 0.
    """

    CAFETERIA_DISCOUNT: float = 50.0

    def tax_rate_for(self, department: Department) -> float:
        """Return the tax rate for a given department.

        Args:
            department: Department enum value.
        Returns:
            A tax rate as a decimal (e.g., 0.15 for 15%).
        """
        if department in (Department.SALES, Department.IT):
            return 0.15
        if department is Department.HR:
            return 0.16
        # Default safeguard if new departments are added without rules
        return 0.15

    def compute_net_salary(self, gross_salary: float, department: Department) -> float:
        """Compute the net salary for a given gross salary and department.

        Formula: net = gross - (gross * tax_rate) - CAFETERIA_DISCOUNT
        The result is floored at 0.

        Args:
            gross_salary: Gross salary amount.
            department: Department to determine the tax rate.
        Returns:
            The computed net salary (never negative).
        """
        tax = gross_salary * self.tax_rate_for(department)
        net = gross_salary - tax - self.CAFETERIA_DISCOUNT
        return max(net, 0.0)


class PayrollSystem:
    """Manages employees and interactions for the CLI-based payroll system."""

    def __init__(self, calculator: PayrollCalculator | None = None) -> None:
        self.calculator: PayrollCalculator = calculator or PayrollCalculator()
        self.employees: List[Employee] = []

    def add_employee(self, name: str, department: Department, gross_salary: float) -> Employee:
        """Create and store a new Employee after calculating their net salary.

        Args:
            name: Employee name.
            department: Department of the employee.
            gross_salary: Gross salary provided by the user.
        Returns:
            The created Employee instance.
        """
        net_salary = self.calculator.compute_net_salary(gross_salary, department)
        employee = Employee(name=name, department=department, gross_salary=gross_salary, net_salary=net_salary)
        self.employees.append(employee)
        return employee

    def generate_report_lines(self) -> List[str]:
        """Generate the report lines representing all current employees.

        Returns:
            A list of strings to be printed to stdout as the report.
        """
        if not self.employees:
            return ["No hay nadie"]

        lines: List[str] = []
        for emp in self.employees:
            lines.append(f"Emp: {emp.name}")
            lines.append(f"Depto: {emp.department.value}")
            lines.append(f"Pago Final: {emp.net_salary}")
            lines.append("----------------")
        return lines


def print_menu() -> None:
    """Print the main menu to stdout."""
    print("")
    print("1. Agregar empleado Ventas")
    print("2. Agregar empleado IT")
    print("3. Agregar empleado RRHH")
    print("4. Ver reporte")
    print("5. Salir")
    print("")


def run_cli() -> None:
    """Run the interactive CLI for the payroll system."""
    system = PayrollSystem()

    print("********************************")
    print("SISTEMA DE NOMINAS V2.3 FINAL_REAL_AHORA_SI")
    print("********************************")

    running = True
    while running:
        print_menu()
        option = input("Seleccione opcion: ")

        if option == "1":
            name = input("Nombre: ")
            gross_str = input("Sueldo Bruto: ")
            try:
                gross = float(gross_str)
            except ValueError:
                print("Entrada inválida, ingrese un número para el sueldo.")
                continue
            system.add_employee(name=name, department=Department.SALES, gross_salary=gross)
            print("Guardado Ventas.")

        elif option == "2":
            name = input("Nombre: ")
            gross_str = input("Sueldo Bruto: ")
            try:
                gross = float(gross_str)
            except ValueError:
                print("Entrada inválida, ingrese un número para el sueldo.")
                continue
            system.add_employee(name=name, department=Department.IT, gross_salary=gross)
            print("Guardado IT.")

        elif option == "3":
            name = input("Nombre: ")
            gross_str = input("Sueldo Bruto: ")
            try:
                gross = float(gross_str)
            except ValueError:
                print("Entrada inválida, ingrese un número para el sueldo.")
                continue
            system.add_employee(name=name, department=Department.HR, gross_salary=gross)
            print("Guardado RRHH.")

        elif option == "4":
            for line in system.generate_report_lines():
                print(line)

        elif option == "5":
            running = False

        else:
            print("Error")


if __name__ == "__main__":
    run_cli()
