import json


def validate(stops):
    errors = {
        "num": 0,
        "bus_id": 0,
        "stop_id": 0,
        "stop_name": 0,
        "next_stop": 0,
        "stop_type": 0,
        "a_time": 0
    }
    for stop in stops:
        if not isinstance(stop['bus_id'], int):
            errors['num'] += 1
            errors['bus_id'] += 1
        if not isinstance(stop['stop_id'], int):
            errors['num'] += 1
            errors['stop_id'] += 1
        if not isinstance(stop['stop_name'], str) or not stop['stop_name']:
            errors['num'] += 1
            errors['stop_name'] += 1
        if not isinstance(stop['next_stop'], int):
            errors['num'] += 1
            errors['next_stop'] += 1
        if not isinstance(stop['stop_type'], str) or len(stop['stop_type']) > 1:
            errors['num'] += 1
            errors['stop_type'] += 1
        if not isinstance(stop['a_time'], str) or not stop['a_time']:
            errors['num'] += 1
            errors['a_time'] += 1
    return errors


def load_data():
    return json.loads(input())


def print_errors(errors):
    print("Type and required field validation:", errors['num'], "errors")
    for key in errors:
        if key != "num":
            print(key, ":", errors[key])


def main():
    stops = load_data()
    errors = validate(stops)
    print_errors(errors)


if __name__ == '__main__':
    main()
