import tkinter as tk
from tkinter import ttk
import pandas as pd
from collections import Counter

class MigraineDiaryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Migraine Diary")

        # Create a DataFrame to store migraine data
        self.migraine_data = pd.DataFrame(columns=["Date", "Cause"])

        # Calendar
        self.calendar = ttk.Treeview(self.root, columns=("Date"))
        self.calendar.heading("#1", text="Date")
        self.calendar.grid(row=0, column=0, padx=10, pady=10)

        # Entry fields
        self.date_entry = ttk.Entry(self.root, width=15)
        self.cause_entry = ttk.Entry(self.root, width=30)
        self.date_label = ttk.Label(self.root, text="Date (YYYY-MM-DD):")
        self.cause_label = ttk.Label(self.root, text="Possible Cause:")
        self.date_label.grid(row=1, column=0, padx=10, pady=10)
        self.cause_label.grid(row=1, column=1, padx=10, pady=10)
        self.date_entry.grid(row=2, column=0, padx=10, pady=10)
        self.cause_entry.grid(row=2, column=1, padx=10, pady=10)

        # Add Entry button
        self.add_button = ttk.Button(self.root, text="Add Entry", command=self.add_entry)
        self.add_button.grid(row=2, column=2, padx=10, pady=10)

        # Most Frequent Cause
        self.most_frequent_cause_label = ttk.Label(self.root, text="Most Frequent Cause:")
        self.most_frequent_cause = ttk.Label(self.root, text="")
        self.most_frequent_cause_label.grid(row=3, column=0, padx=10, pady=10)
        self.most_frequent_cause.grid(row=3, column=1, padx=10, pady=10)

    def add_entry(self):
        date = self.date_entry.get()
        cause = self.cause_entry.get()

        if date and cause:
            self.migraine_data = self.migraine_data.append({"Date": date, "Cause": cause}, ignore_index=True)
            self.update_calendar()
            self.update_most_frequent_cause()

    def update_calendar(self):
        self.calendar.insert("", "end", values=self.date_entry.get())
        self.date_entry.delete(0, "end")
        self.cause_entry.delete(0, "end")

    def update_most_frequent_cause(self):
        if not self.migraine_data.empty:
            most_frequent = Counter(self.migraine_data["Cause"]).most_common(1)
            self.most_frequent_cause.config(text=most_frequent[0][0])
        else:
            self.most_frequent_cause.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = MigraineDiaryApp(root)
    root.mainloop()
