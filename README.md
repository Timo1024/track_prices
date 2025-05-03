# track_prices

Amazon price tracker application that monitors product prices.

## Running with Docker

Build the containers:
```
docker-compose build
```

Start the services in detached mode:
```
docker-compose up -d
```

Stop and remove the containers:
```
docker-compose down
```

## Testing the Application

Once the containers are running:

1. Open http://localhost:8000/ in your browser to verify the API is working
2. Visit http://localhost:8000/health/db to check database connectivity
3. Access API documentation at http://localhost:8000/docs

## Database Access

The MySQL database is accessible:
- Port: 3307 (on host) -> 3306 (in container)
- Username: price_tracker
- Password: password
- Database name: price_tracker_db

## Debugging

If you encounter issues:

1. View container logs:
   ```
   docker-compose logs backend
   docker-compose logs db
   ```

2. Enter the backend container:
   ```
   docker-compose exec backend bash
   ```
   
3. Inside the container, check file structure:
   ```
   ls -la
   ```
   
4. Verify the app.py file exists and is in the correct location:
   ```
   cat app.py
   ```

