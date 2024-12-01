# Steps for the Cinemato Project

1. Clone the Git Repository
2. Create a new Virtual Enviroment and install the dependencies given in requirements.txt file
3. Open the directory ("Cinemato/manage.py") containing manage.py file in the terminal
4. Run the command "python manage.py runserver" in the terminal
5. Access the API endpoints with the help of respective URLs given in the ("Cinemato/Movies/urls.py")
   - "/movies" is the enpoint to show all the movies.
   - "/movies/?actor_id=3" is the endpoint to show all the movies of actor having id no. 3
   - "/movies/?actor_id=3&director_id=2" is the endpoint to apply multiple filters
   - "/movie/2" is the endpoint to show the details of a particular movie with id no. 2, also to create a new movie object in the database and to update the movie object with id no. 2
   - "/actor/6" is the endpoint to delete the actor who is not associated to any movie
