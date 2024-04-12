from flask import Blueprint, jsonify, request
from users.model.courses_model import Courses
from users.repository.courses_repository import CoursesRepository, LocalCoursesRepository

blueprint = Blueprint('courses_controller', __name__)
repository = LocalCoursesRepository()


# Endpoint to insert users
# Endpoint to insert users
@blueprint.route("/courses", methods=["POST"])
def insert_courses():
    # Get the course data from the request
    courses_data = request.get_json()

    # Check if the course already exists based on its name
    existing_course = repository.encontrar (courses_data["name"])
    if existing_course:
        return jsonify({"message": "CURSO EXISTENTE"}), 409  # Conflict error code

    # Create a new course and add it to the repository
    new_course = repository.add(courses_data["name"], courses_data["DESCRIPTION"])

    # Return the newly inserted course
    return jsonify(new_course)



# Endpoint to retrieve users based on user_id
@blueprint.route("/courses/<courses_id>", methods=["GET"])
def get_courses(courses_id):
    # Find the user with the given user_id
    #user = next((user for user in users if user.id == int(user_id)), None)
    id= int(courses_id)
    courses_found = repository.get(id)
    # If the user is not found, return a 404 error
    if courses_found is None:
        return jsonify({"message": "User not found"}), 404

    # Return the retrieved user
    return jsonify(courses_found)