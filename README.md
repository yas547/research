README.txt

=========================
Requisition System Script
=========================

Description:
------------
This Python script implements a simple Requisition System for staff to request office or departmental items. 
Each request includes staff details and item information, then calculates the total cost and determines if 
the requisition is approved based on a cost threshold of $500.

Features:
---------
- Automatically generates a unique requisition ID starting from 10000.
- Collects staff information (Date, Staff ID, Name).
- Accepts 3 items with individual prices.
- Approves requisitions with a total cost under $500.
- Displays a formatted summary of all requisitions.

How to Use:
-----------
1. Run the script in a Python 3 environment.
2. For each of the 4 requisitions:
   - Input the date (format: DD/MM/YYYY)
   - Enter Staff ID
   - Enter Staff Name
   - Input the name and price of 3 items
3. The program will calculate the total cost.
4. Requisitions below $500 are approved automatically.
5. After all entries, the script displays a detailed summary for each request.

Sample Input:
-------------
Enter the date (DD/MM/YYYY): 12/04/2025  
Enter the Staff ID: ST123  
Enter the Staff Name: John Doe  
Enter the name of item: Pen  
Enter a price for Pen: 5  
Enter the name of item: Notebook  
Enter a price for Notebook: 10  
Enter the name of item: USB  
Enter a price for USB: 15  

Sample Output:
--------------
Printing Requisition:

Date: 12/04/2025  
Staff ID: ST123  
Staff Name: John Doe  
Total: $30.0  
Requisition ID: 10000  
Status: approved  
Approval Reference Number: ST12310000  

Code Structure:
---------------
- RequisitionSystem Class:
  * __init__() : Initializes requisition with unique ID and staff info.
  * staff_info(): Prompts for and returns staff details.
  * requisitions_details(): Collects and stores item names and prices.
  * requisition_approval(): Determines approval based on total cost.
  * display_requisitions(): Prints out requisition summary.

- Main Loop:
  * Runs 4 times to collect and process 4 requisitions.
  * Stores each requisition in a list.
  * Displays all summaries at the end.

Notes:
------
- The script is command-line based and requires user input.
- Maximum of 3 items per requisition in current version.
- No external files or database used—data is stored temporarily in memory.

Suggestions for Future Enhancements:
------------------------------------
- Allow dynamic number of items.
- Add option to save requisitions to a file or database.
- Include staff authentication/login.
- Add GUI or web interface for better user interaction.

Author:
-------
(Your Name)
April 2025
