import tkinter as tk
from ttkbootstrap import Style
from ttkbootstrap.widgets import DateEntry
from datetime import datetime, timedelta

class DateRangePicker(tk.Tk):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.title("Date Range Picker")
        self.geometry("400x200")

        # Create a style
        style = Style(theme='litera')

        # Start Date
        self.start_date_label = tk.Label(self, text="Start Date:")
        self.start_date_label.pack(pady=(20, 5))
        self.start_date = DateEntry(self, bootstyle='primary')
        self.start_date.pack()

        # End Date
        self.end_date_label = tk.Label(self, text="End Date:")
        self.end_date_label.pack(pady=(20, 5))
        self.end_date = DateEntry(self, bootstyle='primary')
        self.end_date.pack()

        # Validate Dates Button
        self.validate_button = tk.Button(self, text="Validate Dates", command=self.validate_dates)
        self.validate_button.pack(pady=(20, 5))

        # Update the end date's minimum date when the start date changes
        self.start_date.bind("<<DateEntrySelected>>", self.update_end_date_min)

    def update_end_date_min(self, event):
        # Get the start date value
        start_date_value = self.start_date.entry.get()
        # Set the end date's minimum date to one day after the start date
        self.end_date.config(startdate=start_date_value + timedelta(days=1))

    def validate_dates(self):
        # Get the start and end date values
        start_date_value = self.start_date.entry.get()
        end_date_value = self.end_date.entry.get()

        # Check if the start date is less than the end date
        if start_date_value < end_date_value:
            print("Success: Start date is less than end date.")
        else:
            print("Failure: Start date is not less than end date.")

if __name__ == "__main__":
    app = DateRangePicker()
    app.mainloop()
