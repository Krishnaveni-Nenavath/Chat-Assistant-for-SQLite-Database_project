# Chat Assistant for Employee and Department Queries

## Overview
This chat assistant is designed to help users retrieve employee and department-related information from an SQLite database using natural language queries. The assistant translates user queries into SQL commands and fetches relevant data.

## Features
- Retrieve a list of employees in a specific department.
- Find the manager of a given department.
- List employees hired after a certain date.
- Calculate the total salary expense for a department.
- Handles errors gracefully and provides meaningful feedback.

## How It Works
1. The assistant receives a user query in natural language.
2. It processes the query using regex to determine intent.
3. The corresponding SQL query is executed on the SQLite database.
4. The results are formatted and displayed to the user.

## Requirements
- Python 3.x
- SQLite3
- Required Python libraries: `sqlite3`, `pandas`, `nltk`, `re`, `datetime`

## Setup Instructions
1. **Ensure Python is installed on your system.**
2. **Install dependencies:**
   ```bash
   pip install pandas nltk
   ```
3. **Prepare the database:**
   - Ensure `employees.csv` is in the project directory.
   - Run the script to load the data:
     ```bash
     python chat_assistant.py
     ```
4. **Start the chat assistant:**
   ```bash
   python chat_assistant.py
   ```

## Usage
Once the assistant is running, you can ask questions like:
- Show me all employees in the Sales department.
- Who is the manager of the HR department?
- List all employees hired after 2023-01-01.
- What is the total salary expense for the IT department?

### Example Interaction

You: Show me all employees in the Sales department.
Assistant:
 1. Teresa Barber
 2. Michael Andersen
 3. Stephanie Knight
 4. Cassidy Spears
 ...

You: Who is the manager of the Engineering department?
Assistant:
 Bob

You: List all employees hired after 2023-01-01.
Assistant:
 1. Teresa Barber
 2. Marilyn Hill
 3. Katrina Lopez
 ...

You:  "Who is the manager of the Sales department?"
Assistant:
 Alice

You: Total salary expense for the Marketing department.
Assistant:
 4479625
 
You:  byee
Assistant:
 Sorry, I didn't understand that query.
 
You:  bye
Goodbye! Have a nice day!

You: quit
Goodbye! Have a nice day!

To exit, simply type `exit`, `quit`, or `bye`.

## Limitations
- The assistant relies on regex patterns, which limits query flexibility.
- Only predefined question formats are currently supported.
- The SQLite database must be preloaded with employee data.

## Future Enhancements
- Implement Natural Language Processing (NLP) for better query understanding.
- Expand query support with more flexible and varied sentence structures.
- Develop a user-friendly interface.
- Improve error handling and logging mechanisms.

## License
This project is open-source and can be modified and distributed freely.

## Contribution Guidelines
Contributions are welcome! To contribute:
1. Fork this repository.
2. Create a new branch (`feature-new-functionality`).
3. Commit your changes and push to your branch.
4. Submit a pull request for review.

## Troubleshooting
- If you encounter issues loading data, ensure `employees.csv` is in the correct directory.
- If dependencies are missing, run `pip install -r requirements.txt`.
- If the chat assistant does not recognize a query, try rephrasing it in a supported format.

For additional help, feel free to open an issue in the repository.

