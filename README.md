## Set up Project Locally

## Step: 1 Create virtual environment in your machine.

# command to create virtual env and activate it

    python3 -m venv venv
    source venv/bin/activate

## Step: 2 Install the requirement

    pip install -r requirements.txt

## Step: 3 Run server in local machine

### Run this command in terminal

    ./start.sh

## Step 5 : Running Alembic in our Project 

     - alembic upgrade head
## Step 6 : Api endpoint curl 

 curl --location 'http://localhost:5000/identify' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "mcfl@hilvle.edu",
    "phoneNumber": "123457"
}

'


