# Los Pollos Hermanos — Drive-Thru System

A Python-based drive-thru restaurant management system developed as a group course project. The system simulates real-world drive-thru operations using a **PyQt5 graphical user interface**, **role-based architecture**, and a **Microsoft Azure–hosted database** for persistent storage.

The project emphasizes clean separation of responsibilities, object-oriented design, and a realistic workflow for order handling.

---

## Key Features

- **PyQt5 GUI** for interactive order management  
- **Role-based system design**
  - **Cashier**: takes customer orders and manages order flow
  - **Cook**: prepares orders and updates order status
  - **Manager**: oversees system operations and data
- **Persistent cloud storage** using **Microsoft Azure**
- Modular, object-oriented Python architecture
- UML diagrams and a final project report included

---

## Tech Stack

- **Language:** Python 3.x  
- **Frontend:** PyQt5  
- **Database:** Microsoft Azure (cloud-hosted)  
- **Architecture:** Object-oriented, role-based modules  

---

## Getting Started

### 1) Clone the repository

```bash
git clone https://github.com/CS-3560-02-5/Los-Pollos-Hermanos-Drive-Thru-System.git
cd Los-Pollos-Hermanos-Drive-Thru-System
```

### 2) Set up a virtual environment (recommended)

```bash
python -m venv .venv
```

Activate the environment:

**macOS / Linux**
```bash
source .venv/bin/activate
```

**Windows (PowerShell)**
```powershell
.venv\Scripts\Activate.ps1
```

### 3) Install dependencies

```bash
pip install pyqt5
```

---

## Running the Application

```bash
python main.py
```

If your system uses `python3`:

```bash
python3 main.py
```

---

## Project Structure (High Level)

```text
Cashier/
Cook/
Manager/
Diagrams/
Group Assignments/
images/
main.py
data_bridge.py
MenuItem.py
Order.py
OrderItem.py
5_FinalReport.pdf
```

---

## Database

- The application connects to a **Microsoft Azure–hosted database**.
- Database credentials and connection configuration are handled in the data access layer (e.g., `data_bridge.py`).
- Ensure Azure resources/connection details are configured before running the application.

---

## Documentation

For detailed design decisions, UML diagrams, requirements, and analysis, see:

- **5_FinalReport.pdf**

---

## Notes for Developers

- PyQt5 handles UI logic and is separated from business logic.
- Core domain models include `Order`, `OrderItem`, and `MenuItem`.
- Database access is centralized to simplify maintenance and future changes.
- Role-based modules help maintain clear responsibility boundaries.

---

No license is specified in this repository.  
Assume all rights reserved unless a license file is added.
