import requests as pyreq
import dbconnect 

# get nyt games login cookie (grab from cache? fetch auth token using username and pw?)

# get crossword data from nyt website
## uses the form https://www.nytimes.com/svc/crosswords/v3//puzzles.json?publish_type=daily&sort_order=asc&sort_by=print_date&date_start=2024-04-01&date_end=2024-04-30
## response object has members with the keys "author", "editor", "print_date", "puzzle_id", and "solved" (true/false)  


# fetch individual crossword stats from nyt
## send GET request to 'https://www.nytimes.com/svc/crosswords/v6/game/{id}.json' with nyt cookie
## respose object has member 'calc' with keys "solved" (true/false) and "secondsSpentSolving" (int)


# fetch data from database

# write to database