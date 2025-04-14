def get_staff_info():
    date = input("Enter date (e.g., 03/04/2024): ")
    staff_id = input("Enter Staff ID (e.g., FN19): ") 
    staff_name = input("Enter Staff Name (e.g., John Paul): ")
    return date, staff_id, staff_name

def get_requisition_total():
    total = 0
    while True:
        item = input("Enter item name (Press Enter to finish): ")
        if not item:
            break
        try:
            total += float(input(f"Enter price for {item}: $"))
        except ValueError:
            print("Invalid price! Please enter a number.")
    return total

def process_requisition(total, staff_id):
    if total < 500:
        return "Approved", f"{staff_id}{str(int(total))[-3:]}"
    return "Pending", "No Approval" 

def display_requisition():
    date, staff_id, staff_name = get_staff_info()
    total = get_requisition_total()
    status, approval_ref = process_requisition(total, staff_id)

    print("\n--- Requisition Details ---")
    print(f"Date: {date}")
    print(f"Requisition ID: 10001")
    print(f"Staff ID: {staff_id}")
    print(f"Staff Name: {staff_name}")
    print(f"Total: ${total:.2f}")
    print(f"Status: {status}")
    if approval_ref:
        print(f"Approval Reference: {approval_ref}")

display_requisition()
