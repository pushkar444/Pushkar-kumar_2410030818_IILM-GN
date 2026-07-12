import json
import os
import csv
import sys

# Constants for default settings
DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
TIME_SLOTS = [
    "09:00 - 10:00",
    "10:00 - 11:00",
    "11:00 - 12:00",
    "12:00 - 13:00",
    "13:00 - 14:00",  # Lunch / Break
    "14:00 - 15:00",
    "15:00 - 16:00",
]

DATA_FILE = "timetable_data.json"

class Timetable:
    def __init__(self):
        self.schedule = {}
        self.load_from_file()

    def load_from_file(self):
        """Loads the timetable data from a JSON file, or initializes an empty one."""
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, 'r') as f:
                    self.schedule = json.load(f)
            except Exception as e:
                print(f"Error loading timetable data: {e}")
                self.schedule = {}
        else:
            self.schedule = {}
            
        # Ensure all day-slot combinations are initialized if they don't exist
        for day in DAYS_OF_WEEK:
            if day not in self.schedule:
                self.schedule[day] = {}
            for slot in TIME_SLOTS:
                if slot not in self.schedule[day]:
                    self.schedule[day][slot] = None

    def save_to_file(self):
        """Saves the current timetable data to a JSON file."""
        try:
            with open(DATA_FILE, 'w') as f:
                json.dump(self.schedule, f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving timetable data: {e}")
            return False

    def add_class(self, day, slot, subject, teacher, room):
        """Adds or updates a class in the timetable."""
        if day not in DAYS_OF_WEEK:
            return False, f"Invalid day. Choose from: {', '.join(DAYS_OF_WEEK)}"
        if slot not in TIME_SLOTS:
            return False, f"Invalid time slot. Choose from: {', '.join(TIME_SLOTS)}"
        
        self.schedule[day][slot] = {
            "subject": subject,
            "teacher": teacher,
            "room": room
        }
        self.save_to_file()
        return True, "Class added/updated successfully!"

    def delete_class(self, day, slot):
        """Removes a class from a specific day and time slot."""
        if day not in DAYS_OF_WEEK or slot not in TIME_SLOTS:
            return False, "Invalid day or time slot."
        
        if self.schedule[day][slot] is None:
            return False, "No class scheduled in this slot."
        
        self.schedule[day][slot] = None
        self.save_to_file()
        return True, "Class removed successfully!"

    def clear_timetable(self):
        """Resets the entire timetable."""
        for day in DAYS_OF_WEEK:
            self.schedule[day] = {slot: None for slot in TIME_SLOTS}
        self.save_to_file()

    def get_display_text(self, day, slot):
        """Helper to format the slot content for table display."""
        info = self.schedule[day][slot]
        if info is None:
            return ""
        # Format as "Subject (Room)" or just "Subject"
        subject = info.get("subject", "")
        room = info.get("room", "")
        if room:
            return f"{subject} ({room})"
        return subject

    def display_timetable(self):
        """Prints the timetable in a beautiful formatted table structure."""
        print("\n" + "=" * 110)
        print(" " * 45 + "WEEKLY TIMETABLE")
        print("=" * 110)
        
        # Calculate widths: time slot col is ~15, day columns are ~18 each
        col_width = 18
        slot_width = 15
        
        # Header row
        header = f"| {'Time Slot':<{slot_width}} |"
        for day in DAYS_OF_WEEK:
            header += f" {day:^{col_width}} |"
        
        separator = "+" + "-" * (slot_width + 2) + "+" + ("-" * (col_width + 2) + "+") * len(DAYS_OF_WEEK)
        
        print(separator)
        print(header)
        print(separator)
        
        for slot in TIME_SLOTS:
            row_str = f"| {slot:<{slot_width}} |"
            for day in DAYS_OF_WEEK:
                class_text = self.get_display_text(day, slot)
                # Handle cell text truncation if it's too long for the column
                if len(class_text) > col_width:
                    class_text = class_text[:col_width - 3] + "..."
                row_str += f" {class_text:^{col_width}} |"
            print(row_str)
            print(separator)
        print()

    def export_to_csv(self, filename="timetable.csv"):
        """Exports the timetable to a CSV file."""
        try:
            with open(filename, mode='w', newline='') as f:
                writer = csv.writer(f)
                # Write header
                writer.writerow(["Time Slot"] + DAYS_OF_WEEK)
                
                for slot in TIME_SLOTS:
                    row = [slot]
                    for day in DAYS_OF_WEEK:
                        info = self.schedule[day][slot]
                        if info:
                            detail = f"{info['subject']} by {info['teacher']} in {info['room']}"
                            row.append(detail)
                        else:
                            row.append("Free")
                    writer.writerow(row)
            return True, f"Successfully exported to {filename}"
        except Exception as e:
            return False, f"Failed to export: {e}"


def get_choice(prompt, options):
    """Utility to prompt user for a choice with simple numeric input validation."""
    while True:
        try:
            print(prompt)
            for idx, opt in enumerate(options, 1):
                print(f"{idx}. {opt}")
            val = input("Enter choice (number): ").strip()
            if not val:
                continue
            choice_idx = int(val) - 1
            if 0 <= choice_idx < len(options):
                return options[choice_idx]
            else:
                print(f"Please enter a number between 1 and {len(options)}.\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")


def main():
    timetable = Timetable()
    
    while True:
        print("=== TIMETABLE MANAGER MENU ===")
        print("1. Display Weekly Timetable")
        print("2. Add/Edit a Class Slot")
        print("3. Remove a Class Slot")
        print("4. Clear Timetable")
        print("5. Export Timetable to CSV")
        print("6. Exit")
        
        choice = input("Select an option (1-6): ").strip()
        
        if choice == "1":
            timetable.display_timetable()
            
        elif choice == "2":
            print("\n--- Add/Edit Class ---")
            day = get_choice("Select Day:", DAYS_OF_WEEK)
            slot = get_choice("Select Time Slot:", TIME_SLOTS)
            
            # Show current slot info if any
            current = timetable.schedule[day][slot]
            if current:
                print(f"Current class: {current['subject']} taught by {current['teacher']} in room {current['room']}")
                overwrite = input("Do you want to overwrite this slot? (y/n): ").strip().lower()
                if overwrite != 'y':
                    print("Cancelled.")
                    continue
            
            subject = input("Enter Subject Name: ").strip()
            if not subject:
                print("Subject name cannot be empty. Cancelled.")
                continue
                
            teacher = input("Enter Teacher Name (optional): ").strip()
            room = input("Enter Room Number/Lab (optional): ").strip()
            
            success, msg = timetable.add_class(day, slot, subject, teacher, room)
            print(f"\n{msg}\n")
            
        elif choice == "3":
            print("\n--- Remove Class ---")
            day = get_choice("Select Day:", DAYS_OF_WEEK)
            slot = get_choice("Select Time Slot:", TIME_SLOTS)
            
            success, msg = timetable.delete_class(day, slot)
            print(f"\n{msg}\n")
            
        elif choice == "4":
            confirm = input("Are you sure you want to clear the entire timetable? (yes/no): ").strip().lower()
            if confirm == "yes":
                timetable.clear_timetable()
                print("\nTimetable cleared successfully!\n")
            else:
                print("\nCancelled.\n")
                
        elif choice == "5":
            filename = input("Enter output filename [timetable.csv]: ").strip()
            if not filename:
                filename = "timetable.csv"
            success, msg = timetable.export_to_csv(filename)
            print(f"\n{msg}\n")
            
        elif choice == "6":
            print("\nThank you for using Timetable Manager! Goodbye.")
            sys.exit(0)
            
        else:
            print("\nInvalid choice. Please choose a valid option (1-6).\n")


if __name__ == "__main__":
    main()
