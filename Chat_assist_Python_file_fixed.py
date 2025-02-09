{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ef212939-afce-44c3-96f6-1d55080cce38",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "\n",
    "# Check if the database file 'chat_assistant.db' exists in the current directory\n",
    "print(os.path.exists(\"chat_assistant.db\"))\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "759adffd-3f34-4563-8d9e-b4362f625682",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Tables in database: [('departments',), ('sqlite_sequence',), ('employees',)]\n"
     ]
    }
   ],
   "source": [
    "import sqlite3\n",
    "\n",
    "# Connect to the SQLite database\n",
    "conn = sqlite3.connect('chat_assistant.db')\n",
    "cursor = conn.cursor()\n",
    "\n",
    "# Retrieve and display all table names in the database\n",
    "cursor.execute(\"SELECT name FROM sqlite_master WHERE type='table';\")\n",
    "tables = cursor.fetchall()\n",
    "\n",
    "print(\"Tables in database:\", tables)\n",
    "\n",
    "# Close the database connection\n",
    "conn.close()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "815a0f6c-9772-475c-9e20-b97099760cfd",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package punkt to\n",
      "[nltk_data]     C:\\Users\\krish\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package punkt is already up-to-date!\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello! I'm your chat assistant. How can I assist you?\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "You:  \"Who is the manager of the Sales department?\"\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Assistant:\n",
      " Alice\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "You:  byee\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Assistant:\n",
      " Sorry, I didn't understand that query.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "You:  bye\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Goodbye! Have a nice day!\n"
     ]
    }
   ],
   "source": [
    "import sqlite3\n",
    "import re\n",
    "import nltk\n",
    "import pandas as pd\n",
    "from datetime import datetime\n",
    "\n",
    "# Download punkt tokenizer for NLP\n",
    "nltk.download('punkt')\n",
    "\n",
    "# Database connection\n",
    "def connect_db():\n",
    "    conn = sqlite3.connect('chat_assistant.db')\n",
    "    return conn\n",
    "\n",
    "# Load CSV data into SQLite\n",
    "def load_csv_to_db(csv_path):\n",
    "    df = pd.read_csv(csv_path)\n",
    "    conn = connect_db()\n",
    "    df.to_sql('employees', conn, if_exists='replace', index=False)\n",
    "    conn.close()\n",
    "\n",
    "# Queries\n",
    "\n",
    "def get_employees_in_department(department):\n",
    "    conn = connect_db()\n",
    "    cursor = conn.cursor()\n",
    "    cursor.execute(\"\"\"\n",
    "        SELECT name FROM employees \n",
    "        WHERE department_id = (SELECT id FROM departments WHERE name = ?)\n",
    "    \"\"\", (department,))\n",
    "    employees = cursor.fetchall()\n",
    "    conn.close()\n",
    "    \n",
    "    if not employees:\n",
    "        return \"No employees found.\"\n",
    "    \n",
    "    return \"\\n\".join([f\"{i+1}. {employee[0]}\" for i, employee in enumerate(employees)])\n",
    "\n",
    "\n",
    "def get_manager_of_department(department):\n",
    "    conn = connect_db()\n",
    "    cursor = conn.cursor()\n",
    "    cursor.execute(\"SELECT manager FROM departments WHERE name = ?\", (department,))\n",
    "    manager = cursor.fetchone()\n",
    "    conn.close()\n",
    "    return manager[0] if manager else \"No manager found.\"\n",
    "\n",
    "\n",
    "def get_employees_hired_after(date):\n",
    "    try:\n",
    "        hire_date = datetime.strptime(date, '%Y-%m-%d').date()\n",
    "    except ValueError:\n",
    "        return \"Invalid date format. Use YYYY-MM-DD.\"\n",
    "    \n",
    "    conn = connect_db()\n",
    "    cursor = conn.cursor()\n",
    "    cursor.execute(\"SELECT name FROM employees WHERE hire_date > ?\", (hire_date,))\n",
    "    employees = cursor.fetchall()\n",
    "    conn.close()\n",
    "    \n",
    "    if not employees:\n",
    "        return \"No employees found.\"\n",
    "    \n",
    "    return \"\\n\".join([f\"{i+1}. {employee[0]}\" for i, employee in enumerate(employees)])\n",
    "\n",
    "\n",
    "def get_total_salary_expense(department):\n",
    "    conn = connect_db()\n",
    "    cursor = conn.cursor()\n",
    "    cursor.execute(\"\"\"\n",
    "        SELECT SUM(salary) FROM employees \n",
    "        WHERE department_id = (SELECT id FROM departments WHERE name = ?)\n",
    "    \"\"\", (department,))\n",
    "    total_salary = cursor.fetchone()\n",
    "    conn.close()\n",
    "    return total_salary[0] if total_salary and total_salary[0] else \"No salary data found.\"\n",
    "\n",
    "# Query Processor\n",
    "def process_query(query):\n",
    "    query = query.lower()\n",
    "\n",
    "    if \"employees in the\" in query and \"department\" in query:\n",
    "        match = re.search(r\"employees in the (.*?) department\", query)\n",
    "        if match:\n",
    "            return get_employees_in_department(match.group(1).capitalize())\n",
    "    \n",
    "    elif \"manager of the\" in query and \"department\" in query:\n",
    "        match = re.search(r\"manager of the (.*?) department\", query)\n",
    "        if match:\n",
    "            return get_manager_of_department(match.group(1).capitalize())\n",
    "    \n",
    "    elif \"employees hired after\" in query:\n",
    "        match = re.search(r\"employees hired after (\\d{4}-\\d{2}-\\d{2})\", query)\n",
    "        if match:\n",
    "            return get_employees_hired_after(match.group(1))\n",
    "    \n",
    "    elif \"total salary expense for the\" in query:\n",
    "        match = re.search(r\"total salary expense for the (.*?) department\", query)\n",
    "        if match:\n",
    "            return get_total_salary_expense(match.group(1).capitalize())\n",
    "    \n",
    "    return \"Sorry, I didn't understand that query.\"\n",
    "\n",
    "# Start Chat Assistant\n",
    "def start_chat():\n",
    "    print(\"Hello! I'm your chat assistant. How can I assist you?\")\n",
    "    while True:\n",
    "        user_input = input(\"You: \")\n",
    "        if user_input.lower() in [\"exit\", \"quit\", \"bye\"]:\n",
    "            print(\"Goodbye! Have a nice day!\")\n",
    "            break\n",
    "        response = process_query(user_input)\n",
    "        print(\"Assistant:\\n\", response)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    #load_csv_to_db('employees.csv')  # Load data\n",
    "    load_csv_to_db(r\"C:\\Users\\krish\\Downloads\\employees.csv\") \n",
    "    start_chat()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "59d7e176-b6b4-4b6c-a0b9-dd9912cb7b14",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
