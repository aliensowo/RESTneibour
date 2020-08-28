from flask import url_for

# def make_public_dot(dot):
#     new_dot = {}
#     for field in dot:
#         if field == 'id':
#             new_dot['uri'] = url_for('get_dot', dot_id=dot['id'], _external=True)
#         else:
#             new_dot[field] = dot[field]
#     return new_task
