from flask import Flask, request
import logging, json


app = Flask(__name__)


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500


@app.route('/', methods=['POST'])
def process_json():
    customer_data = request.json

   # temp_utf8comment = customer_data['event_data']['comment'].encode('utf-8')
   # customer_data['event_data']['comment'] = temp_utf8comment
   # print customer_data['event_data']['comment']

    # Data from BQ
    #st = u'\u5b98\u7f51\u8ba2\u7968\u5927\u96be\uff0c\u6362\u597d\u51e0\u4e2a\u6d4f\u89c8\u5668\u5747\u65e0\u6cd5\u5b8c\u6210\u8ba2\u7968\uff0c\u624b\u673aAPP\u5df2\u7ecf\u6709\u8fd1\u4e00\u4e2a\u6708\u65e0\u6cd5\u4f7f\u7528\uff0c\uff0c\u8bf7\u63d0\u5347\u7f51\u7ad9\u7684\u6280\u672f\u652f\u6301\uff0c\u4e0d\u8981\u8bbe\u7f6e\u8fc7\u4e8e\u590d\u6742\u7684\u8ba2\u7968\u9a8c\u8bc1\u73af\u8282\uff0c\u6781\u5927\u5f71\u54cd\u8ba2\u8d2d\u8d35\u822a\u7684\u70ed\u60c5\u3002'
    #print st.encode('utf-8')

    # initialize the log settings
    logging.basicConfig(filename='data/app.log', level=logging.INFO)
    logging.info(customer_data)
    return 'OK'


if __name__ == '__main__':
    app.run(debug=True)


