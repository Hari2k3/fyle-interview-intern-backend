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
