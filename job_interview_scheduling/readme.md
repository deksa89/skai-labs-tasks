# Interview Scheduler Application

This Flask-based web application is designed to help calculate the maximum number of non-overlapping interviews a person can attend based on the provided start and end times.
It exposes an endpoint `/schedule` that accepts JSON data containing interview start and end times.

## Endpoint
- URL: /schedule
- Method: POST
- Content-Type: application/json


## Running the app
Clone the repository:
``` git clone https://github.com/deksa89/skai-labs-tasks.git ```

Navigate to the cloned directory:
``` cd skai_labs_tasks/job_interview_scheduling ```

Make sure that you have installed Flask. I recommend to create new environment where you will install Flask.

``` python3 -m venv <name_of_virtualenv> ```

Once you have created an envionment activate it and install Flask:
``` pip install Flask ```

Activate the environment:
on Linux: ``` source /path/to/your/environment/bin/activate ```

Run the app in your terminal:
``` python app.py ```


## Sending POST request to test the app
### using curl
- open a new terminal
- paste:
```
curl -X POST http://127.0.0.1:5000/schedule -H 'Content-Type: application/json' -d '{"start_times": [10, 20, 30, 40, 40, 63], "end_times": [40, 25, 35, 45, 62, 70]}' 
```
- change `start_times` or `end_times` to see different responses


### using Postman:
- download the Postman app
- open the app, click `New`, then `HTTP` Request and choose `POST` on dropdown arrow
- next to POST paste URL ``` http://127.0.0.1:5000/schedule ```
- in `Headers` under `Key` write `Content-Type` and under `Value` write `application/json`
- go to `Body` next to `Headers`
- choose `raw` radio button and `JSON` from dropdown arrow
- paste:
    ``` 
    {
        "start_times": [10, 20, 30, 40, 40, 63], 
        "end_times": [30, 25, 35, 63, 72, 70]
    }
- click on `Send` and whatch for messages in the lower section of the app and in terminal where you run app.py
- change `start_times` or `end_times` to see different responses
