"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template
import hackbright

app = Flask(__name__)


@app.route('/student')
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    grades = hackbright.get_grades_by_github(github)


    return render_template("student_info.html", github_user=github,
                           first_name=first, last_name=last, grades=grades)


@app.route("/search")
def search_student():
    """search user names"""

    return render_template("student_search.html")


@app.route("/new_student")
def new_student():
    """" Displaying new student input form"""
    return render_template("add_student.html")


@app.route("/add_student", methods=['POST'])
def add_student():
    """Adding a student to database"""

    last_name = request.form.get('last_name')
    first_name = request.form.get('first_name')
    github = request.form.get('github')

    output = hackbright.make_new_student(first_name, last_name, github)

    return f"{output}"


@app.route("student/<project>")
def display_project():
    """Display information about given project."""

    return render_template("project_info.html")



if __name__ == '__main__':
    hackbright.connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')
