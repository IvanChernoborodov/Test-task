# Test task

Restful API application. This application parses Hacker News(https://news.ycombinator.com/) website and saves 30 posts (title, url, created)   each 8 hour.  
Availiable methods: GET
Urls:

 - Show all posts - `/posts/` 
 - Detail post - `/posts/id`
 - Offset - `/posts/?offset=5`
 - Limit - `/posts/?limit=2`- Limit must be  `0<limit<100` else will be exception
- Combine - `/posts/offset=10&limit=10` 
- Order - `/posts/?ordering=-title` , `/posts/?ordering=title` - Only title ordering else will be exception
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### []()Prerequisites

You need to install docker and docker-compose on your local machine if you didn't  - 
https://docs.docker.com/compose/install/ and https://docs.docker.com/install/


### []()Installing

Clone the repository on your local machine

```
git clone https://github.com/IvanChernoborodov/Test-task.git

```
Create a docker containers

    docker-compose up -d    
      
Check that all containers are running. State flag must be 'Up' 

 ```
docker-compose ps
```
That's all
Now project is availiable at localhost:8000

## []()Running the tests

Go inside the container with web-application. Make sure that container is running.

    docker-compose exec web bash

And just run tests
	
    ./manage.py test






## []()Built With
-   [Docker](https://docs.docker.com/)  - Сontainerization
-   [Docker-compose](https://docs.docker.com/compose/)  - Сontainerization
-   [Django rest framework](https://www.django-rest-framework.org/)  - The web framework used
-   [Celery](http://docs.celeryproject.org/en/latest/)  - Distributed task queue
-   [Redis](https://redis.io/)  - As a broker for celery
-   [PostgresSQL](https://www.postgresql.org/)  - Database
-  [PyTest](https://docs.pytest.org/en/latest/contents.html)  - Testing
-   Request, Bs4  - Libraries for parsing 


## []()Authors

-   **Ivan Chernoborodov**  -  _Initial work_  -  [Test task](https://github.com/IvanChernoborodov/Test-task)



