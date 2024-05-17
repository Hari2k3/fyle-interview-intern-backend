from .exceptions import FyleError


def base_assert(error_code, msg):
    # print(error_code)
    raise FyleError(error_code, msg)


def assert_auth(cond, msg='UNAUTHORIZED'):
    if cond is False:
        base_assert(404, msg)


def assert_true(cond, msg='FORBIDDEN'):
    if cond is False:
        base_assert(404, msg)


def assert_valid(cond, msg='BAD_REQUEST'):
    # print("Valid:",cond)
    if cond is False:
        base_assert(400, msg)


def assert_found(_obj, msg='FOUND'):
    # print(_obj)
    
    if _obj is None:
        # print("HERE")
        base_assert(404, msg)

