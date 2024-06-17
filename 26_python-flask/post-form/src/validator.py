# BEGIN (write your solution here)
def validate(course):
    errors = {}
    if not course['title']:
        errors['title'] = "Can't be blank"
    if course['paid'] == '':
        errors['paid'] = "Can't be blank"
    return errors
# END
