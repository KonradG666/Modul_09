from flask import Flask, request, render_template, redirect, url_for, make_response, json
from forms import MusicVideoLibraryDraft
from data import videos

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"


@app.route("/library/", methods=["GET", "POST"])
def videos_list():
    form = MusicVideoLibraryDraft()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            videos.create(form.data)
            videos.save_all()
        return redirect(url_for("videos_list"))

    return render_template("music.html", form=form, videos=videos.all(), error=error)

@app.route("/library/<int:video_id>/", methods=["GET", "POST"])
def video_update(video_id):
    video = videos.get(video_id - 1)
    form = MusicVideoLibraryDraft(data=video)

    if request.method == "POST":
        if form.validate_on_submit():
           videos.update(video_id - 1, form.data)
        return redirect(url_for("videos_list"))
    return render_template("music_upd.html", form=form, video_id=video_id)


@app.route("/library/delete/", methods=["GET", "POST"])
def video_delete():
    form = MusicVideoLibraryDraft()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            videos.delete(form.data)
            videos.save_all()
        return redirect(url_for("videos_list"))
    return render_template("music_del.html", form=form, videos=videos.all(), error=error)


@app.errorhandler(400)
def bad_request(error):
    return make_response(({'error': 'Bad request', 'status_code': 400}), 400)


if __name__ == "__main__":
    app.run(debug=True)
