# Delaboard
### An imageboard made entirely using Flask and Bootstrap 4

## How to setup
Clone the repository 
```bash
git clone https://github.com/dossier-hash/delaboard.git 
```

## How to use
Setup the database in the src folder from the python cmd and then run
```python3 
from app import db
db.create_all()
exit()
```
Then,
```bash
python3 app.py 
```

## To-do 
* Board styling
* Add comments
* Captcha

### **DO NOT** USE WITH A PRODUCTION SERVER