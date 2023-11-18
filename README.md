# Prerequisites
## GeoDjango Dependencies (GEOS, GDAL, and PROJ.4): 
```
sudo apt install gdal-bin libgdal-dev python3-gdal binutils libproj-dev geos libgeos-dev
```
## Setting up a Spatial Database With PostgreSQL and PostGIS
use Docker to quickly create a database using the kartoza postgis image, which provides a container with PostgreSQL and PostGIS already installed
```
docker run --name=postgis -d -e POSTGRES_USER=user001 -e POSTGRES_PASS=123456789 -e POSTGRES_DBNAME=gis -p 5432:5432 kartoza/postgis:13.0
```
After running the command, you’ll have a PostgreSQL server listening on the 5432 port with a database called gis. Database credentials; username:user001 password:123456789
# Getting Started
1. Clone this repository to your local machine.
   ```
   git clone https://github.com/Mvg4m61/GeoDjango-tutorial.git
   ```
2. In the project directory, activate the virtual environment
   ```
   source env/bin/activate
   ```
3. Install packages for your project
   ```
   pip install django psycopg2-binary
   ```
4. Run server. Superuser credentials; email:admin@gmail.com pass:admin123
   ```
   python manage.py runserver
   ```
5. data.json contains locations of shops around Nairobi. The project aims to give the 6 nearest shops to the user’s location, which is hardcoded (coordinates of Nairobi, Kenya), but this ideally should be specified by the user or retrieved automatically from the user’s browser with their permission using JavaScript and the HTML5 GeoLocation API.
