# set env
set -e

# run mysql
docker run -d -p 3307:3306 --name mysql -v $(pwd)/backup/database/:/var/lib/mysql/ -e MYSQL_ROOT_PASSWORD=123456 mysql