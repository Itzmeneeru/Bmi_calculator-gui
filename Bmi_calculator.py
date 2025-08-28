import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get()) / 100  # cm → m
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)

        # Determine category and suggestion
        if bmi < 18.5:
            category = "Underweight"
            suggestion = "Eat more nutritious food and increase calorie intake."
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
            suggestion = "Great! Maintain your current lifestyle."
        elif 25 <= bmi < 29.9:
            category = "Overweight"
            suggestion = "Exercise regularly and monitor your diet."
        else:
            category = "Obese"
            suggestion = "Seek medical advice for a proper health plan."

        # Show result in label
        result_label.config(
            text=f"BMI: {bmi}\nCategory: {category}\nSuggestion: {suggestion}",
            fg="#2d3436"
        )

        # Save result in a file
        with open("bmi_records.txt", "a") as f:
            f.write(f"Weight: {weight}kg, Height: {height*100}cm, "
                    f"BMI: {bmi}, Category: {category}\n")

    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for weight and height.")

def reset_fields():
    entry_weight.delete(0, tk.END)
    entry_height.delete(0, tk.END)
    result_label.config(text="")

# ---------------- GUI ----------------
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("380x300")
root.config(bg="#dfe6e9")

# Title
label_title = tk.Label(
    root, text="BMI Calculator",
    font=("Verdana", 18, "bold"),
    bg="#0984e3", fg="white", padx=10, pady=10
)
label_title.pack(fill="x")

# Frame for inputs
frame_inputs = tk.Frame(root, bg="#dfe6e9")
frame_inputs.pack(pady=15)

# Weight input
label_weight = tk.Label(frame_inputs, text="Enter weight (kg):", bg="#dfe6e9", font=("Arial", 12))
label_weight.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_weight = tk.Entry(frame_inputs, font=("Arial", 12))
entry_weight.grid(row=0, column=1, padx=5, pady=5)

# Height input
label_height = tk.Label(frame_inputs, text="Enter height (cm):", bg="#dfe6e9", font=("Arial", 12))
label_height.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_height = tk.Entry(frame_inputs, font=("Arial", 12))
entry_height.grid(row=1, column=1, padx=5, pady=5)

# Buttons
frame_buttons = tk.Frame(root, bg="#dfe6e9")
frame_buttons.pack(pady=10)

btn_calculate = tk.Button(
    frame_buttons, text="Calculate BMI",
    command=calculate_bmi,
    bg="#00b894", fg="white", font=("Arial", 12, "bold"), width=14
)
btn_calculate.grid(row=0, column=0, padx=10)

btn_reset = tk.Button(
    frame_buttons, text="Reset",
    command=reset_fields,
    bg="#d63031", fg="white", font=("Arial", 12, "bold"), width=10
)
btn_reset.grid(row=0, column=1, padx=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#dfe6e9", justify="center")
result_label.pack(pady=20)

# Run
root.mainloop()
