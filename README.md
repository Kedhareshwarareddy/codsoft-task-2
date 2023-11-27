# codsoft-task-2

# README: CALCULATOR (task 2)

## Author: KEDHARESHWARA SUBBA REDDY S

## Batch:(NOVEMBER A13)

## Domain: PYTHON Programming

## Aim

The aim of this project is to create a user friendly simple calculator

## Description

A simple calculator with basic arithmetic operations which prompts the user to input two numbers and an operation choice it performs the calculation and displays the result.

## Libraries Used

The following important libraries were used for this project:

- tkinter

 ##Working of the code



1. **Entry Field (`entry`):**
   - An Entry widget is used to display and input numeric values and mathematical operations.

2. **Numeric and Operation Buttons:**
   - Buttons for digits 0-9, decimal point '.', and basic arithmetic operations (+, -, *, /) are arranged in a grid layout using `tk.Button`.
   - Each button press is linked to the `button_click` method through the `command` parameter, passing the corresponding button value.

3. **Button Click Handling (`button_click` method):**
   - When a numeric button is clicked, the corresponding digit is appended to the current entry in the Entry field.
   - When an arithmetic operation button is clicked, the operation is appended to the current entry.
   - If the '=' button is clicked, the expression in the entry is evaluated using `eval`. The result is then displayed in the Entry field.
   - Error handling is implemented to catch any exceptions that may occur during evaluation, displaying an "Error" message in the Entry field.

4. **Grid Layout:**
   - Buttons are organized in a 4x4 grid layout to resemble a standard calculator layout.

5. **Font and Styling:**
   - The Entry field uses the Arial font with a font size of 14 for a clean and readable appearance.

6. **Initialization and Main Loop:**
   - The `__init__` method initializes the GUI components.
   - The `button_click` method handles button clicks and updates the Entry field accordingly.
   - The `main` function creates the main Tkinter window, instantiates the `SimpleCalculator` class, and starts the Tkinter main loop.


