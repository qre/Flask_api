from flask import Flask #, request
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

#names = {"Gleb": {"age": 31, "gender": "male"},
        #"bill": {"age": 70, "gender": "male"}}

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Send name of the video", required=True)
video_put_args.add_argument("views", type=int, help="Send views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="Send likes of the video", required=True)

videos = {}

def abort_incorrect_id(video_id):
    if video_id not in videos:
        abort(404, message="Video id is incorrect")

def abort_vid_exists(video_id):
    if video_id in videos:
        abort(409, message="A video with this id already exists")

class Video(Resource):
    def get(self, video_id):
        abort_incorrect_id(video_id)
        return videos[video_id]

    def put(self, video_id):
        abort_vid_exists(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id]

    def delete(self, video_id):
        abort_incorrect_id(video_id)
        del videos[video_id]
        return '', 204
# class HelloWorld(Resource):
#     def get(self, name):
#         return names[name]

    # def post(self):
    #     return {"data": "Posted"}

#api.add_resource(HelloWorld, "/helloworld/<string:name>")

api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)

