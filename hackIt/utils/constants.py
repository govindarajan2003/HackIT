status_options = {
    1: "SCHEDULED",
    2: "IN PROGRESS",
    3: "COMPLETED",
    4: "TEST ERROR",
}

def generate_status_choices():
    return list(status_options.items())
