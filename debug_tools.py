

def print_request_dir(request, ignore_meta=True):
    request_dir = dir(request)
    filt_req_dir = [y for y in request_dir if not y.startswith('_')] if ignore_meta else [y for y in request_dir]
    for x in filt_req_dir:
        print(x)