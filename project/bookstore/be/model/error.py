error_code = {
    401: "authorization fail.",
    511: "non exist user id {}",
    512: "exist user id {}",
    513: "non exist store id {}",
    514: "exist store id {}",
    515: "non exist book id {}",
    516: "exist book id {}",
    517: "stock level low, book id {}",
    518: "invalid order id {}",
    519: "not sufficient funds, order id {}",
    520: "illegal searching method, illegal method {}",
    521: "not exist book contains keywords, keywords {}",
    522: "not exist orders, user_id {}",
    523: "not pay the order, order_id {}",
    524: "not reach the order , order_id {}",
    525: "can not cancel the order, order_id {}",
    526: "",
    527: "",
    528: "",
}


def error_non_exist_user_id(user_id):
    return 511, error_code[511].format(user_id)


def error_exist_user_id(user_id):
    return 512, error_code[512].format(user_id)


def error_non_exist_store_id(store_id):
    return 513, error_code[513].format(store_id)


def error_exist_store_id(store_id):
    return 514, error_code[514].format(store_id)


def error_non_exist_book_id(book_id):
    return 515, error_code[515].format(book_id)


def error_exist_book_id(book_id):
    return 516, error_code[516].format(book_id)


def error_stock_level_low(book_id):
    return 517, error_code[517].format(book_id)


def error_invalid_order_id(order_id):
    return 518, error_code[518].format(order_id)


def error_not_sufficient_funds(order_id):
    return 519, error_code[519].format(order_id)


def error_authorization_fail():
    return 401, error_code[401]


def error_and_message(code, message):
    return code, message

def error_searching_method(illegal_method):
    return 520, error_code[520].format(illegal_method)

def error_contains_keywords(keywords):
    return 521, error_code[521].format(keywords)

def error_not_exist_order(user_id):
    return 522, error_code[522].format(user_id)


def error_not_pay_order(order_id):
    return 523, error_code[523].format(order_id)


def error_not_reach_order(order_id):
    return 524, error_code[524].format(order_id)

def error_can_not_cancel(order_id):
    return 525, error_code[525].format(order_id)