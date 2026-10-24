# Python Programming Lab Projects

A collection of practical exercises (Travaux Pratiques) completed during my university studies, implemented in Python. The projects cover file handling, object-oriented programming, scientific computing with NumPy, and graphical user interfaces using Tkinter, Flet, and PyQt5.

## Projects

### Data Management and Logic

| File | Description |
|------|-------------|
| `Les_Fichiers.py` | Student management with file-based storage: read, add, display and compute statistics, through an interactive menu |
| `Etudiants.txt` | Data file used by `Les_Fichiers.py` (one student per line: `name, age, group, average`) |
| `Bibliotheque.py` | Library management system for books |
| `Epicerie.py` | Computes statistics and data for the different products of a shop |
| `Club-Sportif.py` | Football club management system |
| `File D´attente.py` | Queue simulation of clients, computing the average waiting time per client |

### Libraries and GUI Applications

| File | Description | Technology |
|------|-------------|------------|
| `Numpy.py` | Experiments with common NumPy functions | NumPy |
| `Tkinter.py` | Demonstration of Tkinter message boxes | Tkinter |
| `To-do List.py` | Simple task list application | Flet |
| `Primaires.py` | Finds all prime numbers between two user-supplied numbers | PyQt5 |
| `PgmeCHAR.py` | Game show application: the user enters a phone number and, based on a set of rules, may win a prize | PyQt5 |

## Student Management (`Les_Fichiers.py`)

The script stores students in `Etudiants.txt`, one per line:

```
Ahmed Ben Ali, 20, GLSI1, 14.5
```

Functions:

| Function | Purpose |
|----------|---------|
| `lire_fichier` | Prints the raw content of the file |
| `ajouter_etudiant` | Appends a new student to the file |
| `afficher_etudiants_propre` | Displays each student with labelled fields (name, age, group, average) |
| `statistiques_etudiants` | Total students, overall average, count per group (GLSI1 / GLSI2) and best student |

When launched, the script shows an interactive menu:

| Command | Action |
|---------|--------|
| `1` | Display all students |
| `2` | Add a student |
| `3` | Display statistics |
| `4` | Read the raw file content |
| `0` | Quit |

> **Note:** at startup the script rewrites `Etudiants.txt` with the initial students, then adds two more, so the file is reset on every run.

## Concepts Covered

- File input/output
- Classes and object-oriented programming
- Lists, dictionaries, and data processing
- Queue simulation and basic statistics
- Numerical computing with NumPy
- Event-driven GUI development (Tkinter, Flet, PyQt5)

## Getting Started

### Prerequisites

- Python 3.8 or higher
- The following packages, depending on the project:

| Package | Required by |
|---------|-------------|
| `numpy` | `Numpy.py` |
| `flet` | `To-do List.py` |
| `PyQt5` | `Primaires.py`, `PgmeCHAR.py` |

`Tkinter` is included with most standard Python installations. `Les_Fichiers.py` uses only the standard library.

### Installation

```bash
git clone <your-repository-url>
cd <your-repository-folder>
pip install numpy flet PyQt5
```

### Running a Project

```bash
python <filename>.py
```

Examples:

```bash
python Les_Fichiers.py
python Primaires.py
```

Run `Les_Fichiers.py` from the folder that contains `Etudiants.txt`, since the file is opened with a relative path.

## Repository Structure

```
.
├── Les_Fichiers.py
├── Etudiants.txt
├── Bibliotheque.py
├── Epicerie.py
├── Club-Sportif.py
├── File D´attente.py
├── Numpy.py
├── Tkinter.py
├── To-do List.py
├── Primaires.py
├── PgmeCHAR.py
└── README.md
```

## License

This project is intended for educational purposes.
