README - Requisition System
============================

Description:
------------
This Python program simulates a simple Requisition System for managing staff item requests. 
The system collects staff information and item details, calculates the total cost, and determines 
the approval status based on the cost.

Features:
---------
- Generates a unique Requisition ID for each submission.
- Collects:
  - Date
  - Staff ID and Name
  - Three items and their respective costs
- Calculates the total cost of the items.
- Determines the requisition status and generates an approval reference if applicable.
- Displays the details of each requisition.

Approval Rules:
---------------
- If the total cost is **less than $500**:
  - Status: Approved
  - Approval Reference Number: [StaffID][RequisitionID]
- If the total cost is **$500 or more**:
  - Status: Pending
  - Approval Reference Number: Not available

How to Run:
-----------
1. Make sure you have Python installed.
2. Save the script in a file (e.g., `redeem.py`).
3. Open your terminal or command prompt.
4. Run the script using:
   python redeem.py
5. Follow the prompts to enter requisition details for 4 staff members.

Program Output:
---------------
- After input, the program prints all requisition entries, including:
  - Date
  - Staff ID and Name
  - Total Cost
  - Requisition ID
  - Approval Status
  - Approval Reference Number
