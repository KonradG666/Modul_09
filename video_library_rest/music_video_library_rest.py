from flask import Flask, jsonify, abort, make_response, request
from data_rest import videos

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"


@app.route("/api/v1/library/", methods=["GET"])
def videos_list_api_v1():
    return jsonify(videos.all())

@app.route("/api/v1/library/<int:video_id>", methods=["GET"])
def get_video(video_id):
    video = videos.get(video_id)
    if not video:
        abort(404)
    return jsonify(video)


@app.route("/api/v1/library/", methods=["POST"])
def create_video():
    if not request.json or not 'title' in request.json:
        abort(400)
    video = {
        'id': videos.all()[-1]['id'] + 1,
        'title': request.json['title'],
        'band': request.json.get('band', ''),
        'genre': request.json.get('genre', '')
    }
    videos.create(video)
    return jsonify(video), 201

@app.route("/api/v1/library/<int:video_id>", methods=['DELETE'])
def delete_video(video_id):
    result = videos.delete(video_id)
    if not result:
        abort(404)
    return jsonify({'result': result})


@app.route("/api/v1/library/<int:video_id>", methods=["PUT"])
def update_video(video_id):
    video = videos.get(video_id)
    if not video:
        abort(404)
    if not request.json:
        abort(400)
    data = request.json
    if any([
        'title' in data and not isinstance(data.get('title'), str),
        'band' in data and not isinstance(data.get('band'), str),
        'genre' in data and not isinstance(data.get('genre'), str)
    ]):
        abort(400)
    video = {
        'id': data.get('id', video['id']),
        'title': data.get('title', video['title']),
        'band': data.get('band', video['band']),
        'genre': data.get('genre', video['genre'])
    }
    videos.update(video_id, video)
    return jsonify(video)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status_code': 404}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(({'error': 'Bad request', 'status_code': 400}), 400)


if __name__ == "__main__":
    app.run(debug=True)
