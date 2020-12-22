# Simple Booking System
This is a simple booking system, that we were tasked to make as a schoolproject. We chose Aarhus Golfclub as our case. We are not affiliated with Aarhus Golfclub in any way.



## Install
Firstly you have to active the virtual enviroment:
```source .env/bin/activate```

Then install the program:
```pip install -e .```


## Start the program
Go to the booking folder, then to layout:
```cd booking/layout```
start the program by writing: 
```python gui.py```

## Work Schedule
![alt text](https://media.discordapp.net/attachments/781211340316475452/790901817880870923/unknown.png)

## File structure:
```
.
├── booking
│   ├── data
│   │   ├── Database.db
│   │   ├── database.py
│   │   ├── __init__.py
│   │   ├── reservation_data.py
│   │   ├── test
│   │   │   ├── __init__.py
│   │   │   └── test.py
│   │   └── user_data.py
│   ├── __init__.py
│   ├── layout
│   │   ├── booking_page.py
│   │   ├── components
│   │   │   ├── header.py
│   │   │   ├── __init__.py
│   │   │   └── table.py
│   │   ├── gui.py
│   │   ├── __init__.py
│   │   ├── login_page.py
│   │   ├── registration_page.py
│   │   ├── reservation_page.py
│   │   └── test
│   │       ├── __init__.py
│   │       └── testing.py
│   └── logic
│       ├── __init__.py
│       ├── reservation_logic.py
│       ├── test
│       │   ├── __init__.py
│       │   ├── test.py
│       │   └── test_user_logic.py
│       └── user_logic.py
├── LICENSE
├── README.md
└── setup.py
```
