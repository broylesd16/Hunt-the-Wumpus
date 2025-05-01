# Use official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the game file
COPY wumpus.py .

# Run the game
CMD ["python", "wumpus.py"]
