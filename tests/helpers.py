import logging


def log_2_console(response, params=None):
    method = response.request.method
    logging.info(f'Method: "{method}", URL: "{response.url}", Status Code: "{response.status_code}"')
    if params:
        logging.info(f"Params: {params}")
