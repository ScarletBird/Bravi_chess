# CHESSKNIGHT

Chessknight is a project for a challenge given by Bravi

### Challenge Description

You must develop an application that allows the registration of chess pieces (type/name and color). In addition, given a location on a coordinate chosen by the user and the piece id, if it is a knight, find out all possible locations where the knight can move in 2 turns.

### API

The api should: 
<li>receive the piece type/name and the color and return the piece id;</li>
<li>receive cell coordinate (in Algebraic notation) and the piece id and return an array
with all possible locations where the knight can move within 2 turns.</li>

***
## How to use

### Setup

<ol>
<li>Use the requirements.txt where all libraries are already in place</li>
<li>Run the migrations to get all databases in place</li>
<li>Populate the chessboard database using the csv files</li>
</ol>

```bash
# Creating a new Virtual Environment and opening it:
python -m virtualenv env
source env\Scripts\activate

# Installing all dependencies:
python -m pip install -r requirements.txt

# Run migrations in /chessknight folder
python manage.py migrate

# Execute the script to populate the chessboard from /chessknight folder
python manage.py load_chessboard --path ../csv_chessboard.csv
```
***
## API Routes

The API can be accessed by running the django server

```bash
python manage.py runserver
```

And using the common route of `api/v1/`, followed by one of the two main routes: **pieces** or **moves**.



### Pieces

Pieces allow the user to see and register new pieces.

The Chesspieces database is not populated so the user can populate as they please, by using a `POST` method.

By using the `GET` method the user will list all chess pieces ID. To get a specific piece, query_params with **type** and **colour**.



### Moves

Users will be able to check all possible movements for a knight after 2 turns by using `GET` method with query_params with **piece_id** (of a knight) and **coordinate** with the starting position.

## Final notes

Feel free to contact me in case of any questions or suggestions.