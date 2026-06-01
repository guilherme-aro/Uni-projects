# Contact Management System

A simple and efficient command-line contact management system built in Python. Register, search, edit, and delete contacts with ease.

## 📋 Description

This project is a contact management application that allows users to:
- **Register** new contacts with name, phone, and email
- **List** all saved contacts in alphabetical order
- **Search** for specific contacts by name
- **Edit** contact information (phone or email)
- **Delete** one or more contacts
- **Persist** data to a local file (`contatos.txt`)

## 🚀 Features

✅ Simple and intuitive command-line interface  
✅ Input validation (names, emails)  
✅ Alphabetical sorting of contacts  
✅ Multiple contact deletion (by name)  
✅ Contact data persistence  
✅ Error handling and user feedback  
✅ No external dependencies required  

## 📦 Requirements

- Python 3.6 or higher
- No external libraries needed

## 💻 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/contact-management-system.git
cd contact-management-system
```

2. Run the program:
```bash
python agenda.py
```

## 🎮 How to Use

When you run the program, you'll see a menu with these options:

```
==================================
   CONTACT MANAGEMENT SYSTEM
==================================
  1. Register contact
  2. List contacts
  3. Search contact
  4. Edit contact
  5. Delete contact
  0. Exit
==================================
```

### Register a Contact (Option 1)
```
Choose an option: 1
--- REGISTER CONTACT ---
Name: John Smith
Phone: (11) 99999-8888
Email: john@email.com
Contact 'John Smith' registered successfully!
```

### List Contacts (Option 2)
```
Choose an option: 2
--- CONTACT LIST ---
[01] John Smith              | (11) 99999-8888 | john@email.com
[02] Mary Johnson            | (21) 98888-7777 | mary@email.com

Total: 2 contact(s).
```

### Search for a Contact (Option 3)
```
Choose an option: 3
--- SEARCH CONTACT ---
Enter the name to search: john
Name: John Smith | Phone: (11) 99999-8888 | Email: john@email.com

1 result(s) found.
```

### Edit a Contact (Option 4)
```
Choose an option: 4
--- EDIT CONTACT ---
Contact name to edit: john
Contact found: John Smith | Phone: (11) 99999-8888

What do you want to edit?
(1) Phone
(2) Email
Choose: 1
New phone: (11) 98888-7777
Contact updated successfully!
```

### Delete a Contact (Option 5)
```
Choose an option: 5
--- DELETE CONTACT ---
Contact name to delete: john
   • John Smith

Total of 1 contact(s) to delete.
Continue? (yes/no): yes
1 contact(s) deleted.
```

## 📁 File Structure

```
contact-management-system/
├── agenda.py          # Main program
├── contatos.txt       # Contact data (created at runtime)
├── README.md          # This file
├── .gitignore         # Git ignore rules
└── requirements.txt   # Python dependencies
```

## 💾 Data Storage

Contacts are stored in a `contatos.txt` file with the following format:

```
Name;Phone;Email
John Smith;(11) 99999-8888;john@email.com
Mary Johnson;(21) 98888-7777;mary@email.com
```

The file is automatically created when you first run the program.

## ✨ Validation Rules

- **Name**: Only letters and spaces allowed
- **Phone**: Cannot be empty
- **Email**: Must contain "@" and "." if provided

## 🔒 Security Considerations

- This is a simple educational project
- Data is stored in plain text (not encrypted)
- For sensitive data, consider implementing encryption
- Suitable for learning purposes only

## 📚 Learning Objectives

This project demonstrates:
- File handling in Python
- Input validation
- Exception handling
- Function organization
- String manipulation
- Data persistence

## 🚦 Future Improvements

- [ ] Search by phone or email
- [ ] Contact categories or groups
- [ ] Backup functionality
- [ ] CSV import/export
- [ ] Contact photo/picture support
- [ ] Graphical user interface (GUI)
- [ ] Database integration (SQLite)

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

**Created by:** Guilherme Aro  
**Date:** June 1, 2026

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements.

---

**Made with ❤️ for learning Python**
