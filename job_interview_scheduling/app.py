from flask import Flask, request, jsonify

app = Flask(__name__)


def count_max_interviews(list_interviews):
    end_time = list_interviews[0][1]

    # sort the interviews by end time
    sorted_interviews = sorted(list_interviews, key=lambda x: x[1])

    # counting first interview as a person can attend minimun one interview
    num_interviews = 1  

    for interview in sorted_interviews:
        if interview[0] >= end_time:
            # if the start time of the current interview is equal to the end time of last interview or after the end time,
            # then a person can attend this interview
            num_interviews += 1
            # update the end time to the end time of current interview
            end_time = interview[1]

    return num_interviews


@app.route('/schedule', methods=['POST'])
def schedule_interviews():
    try:
        data = request.get_json()

        # check if start_times n end_times exist in data recieved
        if not data or 'start_times' not in data or 'end_times' not in data:
            return jsonify({"error": "JSON key is missing"}), 400

        start_times = data['start_times']
        end_times = data['end_times']

        # if start and end time not equal return an error
        if len(start_times) != len(end_times):
            return jsonify({"error": "Numbers of start times and end times are not equal"}), 400

        # combine start and end times into tuples within a list and sort
        list_interviews = sorted(zip(start_times, end_times))

        # check if start time of each interview is lower than end time
        for start, end in list_interviews:
            if start >= end:
                return jsonify({"error": f"Start time {start} is not lower than end time {end} in tuple ({start}, {end})."}), 400

        num_interviews = count_max_interviews(list_interviews)

        return jsonify({"max_interviews": num_interviews}), 200

    # handling errors that might appear
    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 400


if __name__ == '__main__':
    app.run(debug=True)
