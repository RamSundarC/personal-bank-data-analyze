Personal Bank Data Analyze:


This code is designed to provide some basic analysis of banking transactions for a particular account. The code requires a data file in Excel format, with the following columns:

Date (in date format)
Description (string)
Amount (numeric)
Channel (string)
Nature (string)
The code includes the following functions:

mini_statement(): displays the last 5 transactions in either a dataframe or a line graph.
debit_summary(): provides a summary of debit transactions by month, including the maximum, minimum, or average amount.
custom_exporter(): exports a custom range of transactions to either a CSV, TXT or XLS file, or displays the data.
for_four(): provides a summary of debit transactions for a custom range of dates, including subtotals for UPI, card, net banking, and ATM transactions.
Libraries used
The following Python libraries are used in this code:

pandas
matplotlib
numpy
How to use the code
Make sure that the Excel data file is saved in the correct directory.
Run the code.
Select one of the functions from the menu to perform the desired analysis.
