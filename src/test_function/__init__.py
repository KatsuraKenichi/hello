try:
    import azure.functions as func
except Exception:
    func = None

import json
from .operations import parse_int, compute


def handle_request(params):
    a_s = params.get('A')
    b_s = params.get('B')
    op = params.get('op', 'mul')
    if a_s is None or b_s is None:
        return {"error": "Parameters A and B are required"}, 400
    try:
        a = parse_int(a_s)
        b = parse_int(b_s)
    except ValueError:
        return {"error": "A and B must be integers"}, 400
    try:
        result = compute(op, a, b)
    except ZeroDivisionError:
        return {"error": "Division by zero"}, 400
    except ValueError:
        return {"error": "Invalid operation"}, 400
    return {"operation": op, "inputs": {"A": a, "B": b}, "result": result}, 200


def main(req):
    params = {}
    try:
        params = req.params
    except Exception:
        pass
    try:
        body = req.get_json()
        if isinstance(body, dict):
            params = {**params, **body}
    except Exception:
        pass
    body, status = handle_request(params)
    if func is not None:
        return func.HttpResponse(json.dumps(body), status_code=status, mimetype="application/json")
    else:
        # Fallback for local execution
        print(json.dumps(body, ensure_ascii=False))
        import sys
        sys.exit(0)


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python -m src.test_function A B [op]")
    else:
        params = {'A': sys.argv[1], 'B': sys.argv[2]}
        if len(sys.argv) >= 4:
            params['op'] = sys.argv[3]
        body, status = handle_request(params)
        import pprint
        pprint.pprint(body)
        print('status', status)
