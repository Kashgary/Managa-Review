# Full Stack Final Project

## Manga Review API

This API is about reviewing mangas and take an idea about the manga before you read it
https://manga-reviews.herokuapp.com/manga_list

## Auth
you can make a user at this url but with no roles, you can only view reviews and manga_list
https://kashgary1.auth0.com/authorize?audience=mangareview&response_type=token&client_id=uphmj7bMT1NIkIMgLkBXvb3ztxmkmLJ6&redirect_uri=https://manga-reviews.herokuapp.com/manga_list

in this app there are two roles Admin and Reviewer 
- Admin: have full access
- Reviewer: can only add, edit and delete reviews and the other endpoints that doesn't requier an auth

These are the permissions 	
- add:review (Admin,Reviewer)		
- edit:review (Admin,Reviewer)
- delete:review (Admin,Reviewer)
- add:manga (Admin)

## Endpoints

- GET '/manga_list'
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

- POST '/add_manga'
    - Request Arguments: String:title, String:author, Array:genre, Float:rating
    - Returns: A success when created 
```
{
    "created": "Tower Of God",
    "success": true
}
```

- GET '/manga/<int:manga_id>/reviews'
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

- GET '/review/<int:id>' 
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

- DELETE '/review/<int:id>'
    - Delete an object containing the review
    - Request Arguments: None
    - Returns: success on delete
```
{
    "deleted": 1,
    "success": true
}
```

- PATCH '/review/<id>' 
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