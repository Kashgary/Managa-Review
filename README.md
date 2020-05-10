# Full Stack Final Project

## Getting Started

### About this Project 

This project is part of fullstak develper nano degree and it is the last project in the course.
The idea of the this project is to give the readers a source to have an idea about a manga if they like to read it
and a platform for manga enthusiastic to share thier opinions of the manga.

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/Manga-Review` directory and running:

```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.

## Database Setup

### Database init

you need to setup the database in the "modle.py" you need to put your DATABSE_URI in this variable database_path

### Migration

you need to run this command to migrate the database 
```
flask run db upgrade
```
now your database should be done

## Running the server

From within the `Manga-Review` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `app.py` directs flask to use the `app.py` directory and the `__init__.py` file to find the application. 

## Manga Review API 

This API is about reviewing mangas and take an idea about the manga before you read it
https://manga-reviews.herokuapp.com/

## Auth
you can make a user at this url but with no roles, you can only view reviews and mangas
https://kashgary1.auth0.com/authorize?audience=mangareview&response_type=token&client_id=uphmj7bMT1NIkIMgLkBXvb3ztxmkmLJ6&redirect_uri=https://manga-reviews.herokuapp.com/

in this app there are two roles Admin and Reviewer 
- Admin: have full access
- Reviewer: can only add, edit and delete reviews and the other endpoints that doesn't requier an auth

These are the permissions 	
- add:review (Admin,Reviewer)		
- edit:review (Admin,Reviewer)
- delete:review (Admin,Reviewer)
- add:manga (Admin)

This app runs on python so please install leatest version of python via pip
```

```
## Endpoints

- GET '/mangas'
    - Fetches list of all mangas 10 per page
    - Request Arguments: None
    - Returns: An object with mangas details
```
{
    "mangas": [
        {
            "author": "SUI",
            "genre": [
                "Action",
                "Fantasy"
            ],
            "id": 1,
            "rating": 9.78,
            "title": "Tower Of God"
        }
    ],
    "success": true,
    "total_mangas": 1
}
```

- POST '/mangas'
    - Request Arguments: String:title, String:author, Array:genre, Float:rating
    - Returns: A success when created 
```
{
    "created": "Tower Of God",
    "success": true
}
```

- GET '/mangas/manga_id/reviews'
    - Fetches list of all reviews of a spicfic manga
    - Request Arguments: None
    - Returns: An object with reviews details
```
{
    "manga": [
        [
            "Tower Of God"
        ]
    ],
    "reviews": [
        {
            "id": 2,
            "manga_id": 1,
            "name": "Kashgay",
            "title": "Do you even need a review?"
        }
    ],
    "success": true,
    "total_reviews": 2
}
```

- GET '/reviews/id' 
    - Fetches an object containing the review
    - Request Arguments: None
    - Returns: An object with review details
```
{
    "review": [
        {
            "id": 2,
            "manga_id": 1,
            "name": "Kashgay",
            "rating": 10,
            "review": "This is the best manga of all time you don't need a review to read it just DO IT",
            "title": "Do you even need a review?"
        }
    ],
    "success": true
}
```

- POST '/mangas/manga_id/reviews'
    - Creat review for the manga you choosed
    - Request Arguments: String:name, Float:rating, String:review, String:title
    - Returns: success on creation and the title
```
{
    "created": "TEST",
    "success": true
}
```

- DELETE '/reviews/id'
    - Delete an object containing the review
    - Request Arguments: None
    - Returns: success on delete
```
{
    "deleted": 1,
    "success": true
}
```

- PATCH '/reviews/id' 
    - Edit an object containing the review
    - Request Arguments: String:name, String:title, String:review, Float:rating
    - Returns: success on Edit with the new updated object
```
{
    "id": 3,
    "manga_id": 1,
    "name": "Kashgay",
    "rating": 10,
    "review": "The story is about a boy named Bam and Bam the 25th, and Bam in Korean mean night. thus his name is the 25th night cuz he was born at that night",
    "success": true,
    "title": "What Bam mean"
}
```