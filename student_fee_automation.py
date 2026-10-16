import csv

def parse_fee(value):
    value = value.strip()

    if value == "":
        return None, "Missing Fee Due"

    try:
        fee = int(value)
    except ValueError:
        return None, "Invalid Fee Due"

    if fee < 0:
        return None, "Negative Fee Due"

    return fee, "OK"


def validate_status(value):
    value = value.strip().title()

    if value not in ["Pending", "Clear"]:
        return "Invalid Status"

    return "OK"


students = []


required_columns = [
    "student_id",
    "name",
    "fee_due",
    "fee_paid",
    "status"
]

students = []

with open("students.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    if reader.fieldnames is None:
        raise ValueError("CSV file is empty or missing its header.")

    missing_columns = [
        column for column in required_columns
        if column not in reader.fieldnames
    ]

    if missing_columns:
        raise ValueError(
            f"CSV is missing required columns: {', '.join(missing_columns)}"
        )

    for row in reader:
        students.append(row)


total_students = len(students)

pending_students = sum(
    1 for s in students
    if s["status"].strip().title() == "Pending"
)

clear_students = sum(
    1 for s in students
    if s["status"].strip().title() == "Clear"
)


known_fee_due = 0
records_to_review = []
invalid_status_records = []

for student in students:
    fee, status = parse_fee(student["fee_due"])

    
    if student["name"].strip() == "":
        records_to_review.append({
            "name": "[Blank Name]",
            "issue": "Missing Student Name"
        })
    status_result = validate_status(student["status"])

    if status_result != "OK":
        invalid_status_records.append({
            "name": student["name"],
            "status": student["status"]
        })


    if status == "OK":
        known_fee_due += fee
    else:
        records_to_review.append({
            "name": student["name"],
            "issue": status
        })

print("STUDENT FEE MANAGEMENT AUTOMATION")
print("---------------------------------")
print("Total Students:", total_students)
print("Pending Students:", pending_students)
print("Clear Students:", clear_students)
print("Total Known Fee Due: ₹", known_fee_due)
print("Records to Review:", len(records_to_review))

print("\nRECORDS TO REVIEW")
for record in records_to_review:
    print(record["name"], "-", record["issue"])


name_counts = {}

for student in students:
    name = student["name"].strip().lower()
    name_counts[name] = name_counts.get(name, 0) + 1


print("\nINVALID STATUS RECORDS")

if len(invalid_status_records) == 0:
    print("No invalid statuses found.")
else:
    for record in invalid_status_records:
        print(record["name"], "-", record["status"], "- Invalid Status")

# Save summary report to a text file

with open("fee_report.txt", "w", encoding="utf-8") as report:
    report.write("STUDENT FEE MANAGEMENT REPORT\n")
    report.write("-----------------------------\n")
    report.write(f"Total Students: {total_students}\n")
    report.write(f"Pending Students: {pending_students}\n")
    report.write(f"Clear Students: {clear_students}\n")
    report.write(f"Total Known Fee Due: Rs. {known_fee_due}\n")
    report.write(f"Records to Review: {len(records_to_review)}\n")

    report.write("\nRECORDS TO REVIEW\n")
    for record in records_to_review:
        report.write(f"{record['name']} - {record['issue']}\n")

        
    report.write("\nDUPLICATE NAMES\n")

    for name, count in name_counts.items():
        if count > 1:
            report.write(f"{name.title()} - {count} records\n")

            
    report.write("\nINVALID STATUS RECORDS\n")

    if len(invalid_status_records) == 0:
        report.write("No invalid statuses found.\n")
    else:
        for record in invalid_status_records:
            report.write(
                f"{record['name']} - {record['status']} - Invalid Status\n"
            )


        

print("\nReport saved successfully: fee_report.txt")



# Detect duplicate student names

print("\nDUPLICATE NAMES")
for name, count in name_counts.items():
    if count > 1:
        print(name.title(), "-", count, "records")
