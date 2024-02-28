from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

notes = []  # Initialize an empty list to store notes

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if request.form.get("action") == "add":
            title = request.form.get("title")
            note = request.form.get("note")
            if title and note:
                notes.append({"title": title, "content": note})
        return redirect(url_for('index'))
    return render_template("home.html", notes=notes) 

@app.route('/edit', methods=["POST"])
def edit_note():
    note_index = int(request.form.get("note_index"))
    new_note = request.form.get("new_note")
    if new_note:
        notes[note_index]["content"] = new_note
    return redirect(url_for('index'))

@app.route('/delete', methods=["POST"])
def delete_note():
    note_index = int(request.form.get("note_index"))
    del notes[note_index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
