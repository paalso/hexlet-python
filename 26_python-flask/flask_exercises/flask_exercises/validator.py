def validate(course):
    errors = {}
    if not course['title']:
        errors['title'] = "Can't be blank"
    if course['paid'] is None:
        errors['paid'] = "Can't be blank"
    return errors
