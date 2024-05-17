
from flask import Blueprint
from flask import make_response,jsonify
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment
from core.models.assignments import AssignmentStateEnum
from core.models.assignments import GradeEnum

from .schema import AssignmentSchema, AssignmentGradeSchema

principal_assignments_resources = Blueprint('principal_assignments_resources', __name__)


@principal_assignments_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_assignments(p):
    """Returns list of submitted and graded assignments"""
    assignments = Assignment.get_submitted_and_graded_assignments()
    assignments_dump = AssignmentSchema().dump(assignments, many=True)
    return APIResponse.respond(data=assignments_dump)


@principal_assignments_resources.route('/assignments/grade', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
@decorators.authenticate_principal
def grade_assignment(p, incoming_payload):
    """Grade or re-grade an assignment"""
    grade_assignment_payload = AssignmentGradeSchema().load(incoming_payload)

    # Retrieve the assignment
    assignment = Assignment.query.get(grade_assignment_payload.id)

    # Check if the assignment exists    
    if assignment is None:
        print("Here")
        response = jsonify({'message': 'None'})
        response.status_code=400
        return response
    # print("Assignment state:", type(str(assignment.state)))
    # print(type(str(AssignmentStateEnum.DRAFT)))
    # Check if the assignment is in the "Draft" state
    if str(assignment.state) == str(AssignmentStateEnum.DRAFT):
        print("Here")
        response = jsonify({'message': 'Your message here'})
        response.status_code=400
        return response

    # Proceed with grading the assignment
    graded_assignment = Assignment.mark_grade(
        _id=grade_assignment_payload.id,
        grade=grade_assignment_payload.grade,
        auth_principal=p
    )
    db.session.commit()
    graded_assignment_dump = AssignmentSchema().dump(graded_assignment)
    return APIResponse.respond(data=graded_assignment_dump)

from flask import Blueprint
from core.models.teachers import Teacher
from core.models.users import User
from core.apis.responses import APIResponse
from core.apis.decorators import authenticate_principal

principal_resources = Blueprint('principal_resources', __name__)

@principal_resources.route('/teachers', methods=['GET'])
@authenticate_principal
def list_teachers(principal):
    """List all teachers."""
    teachers = Teacher.query.all()
    teacher_data = [{
        'id': teacher.id,
        'created_at': teacher.created_at,
        'updated_at': teacher.updated_at,
        'user_id': teacher.user_id
    } for teacher in teachers]
    return APIResponse.respond(data=teacher_data)
