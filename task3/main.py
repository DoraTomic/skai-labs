from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)


arg_parser = reqparse.RequestParser()
arg_parser.add_argument("start_times", type=int, action="append", required=True)
arg_parser.add_argument("end_times", type=int, action="append", required=True)


class InterviewScheduler(Resource):
    def post(self):
        args = arg_parser.parse_args()

        start_times = args["start_times"]
        end_times = args["end_times"]
        if len(start_times) != len(end_times):
            return {"message": "Number of start times and end times do not match"}, 400
        
        max_interviews = self.calculate_max_interviews(start_times, end_times)

        return {"max_interviews": max_interviews}, 200
    

    def calculate_max_interviews(self, start_times, end_times):

        intervals = list(zip(start_times, end_times))
        max_interviews = 1
        current_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= current_end:
                max_interviews += 1
                current_end = end

        return max_interviews


api.add_resource(InterviewScheduler, "/interviewscheduler")

if __name__ == "__main__":
    app.run(debug=True)