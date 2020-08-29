#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 12:19:23 2020

@author: Ritesh Tiwary
"""

from flask import Flask
from flask_cors import CORS
from flask_restplus import Api, Resource, reqparse
from werkzeug.datastructures import FileStorage

app = Flask(__name__)
CORS(app)
api = Api(app,
          version='1.0',
          title='Resume Parser',
          description='Resume Parser Api(s) is designed for extracting information from resume(s).',
          default='Resume Parser Api',
          default_label='Api(s) for Resume Parser'
          )

upload_parser = reqparse.RequestParser(bundle_errors=True)
upload_parser.add_argument('resume', location='files', type=FileStorage, required=True)


@api.route('/upload')
class Upload(Resource):
    @api.expect(upload_parser)
    @api.doc(responses={201: 'Created'})
    def post(self):
        args = upload_parser.parse_args()
        uploaded_file = args['resume']
        print(uploaded_file)
        uploaded_file.save('../data/abc.pdf')
        return {'Message': 'File Created.'}, 201


if __name__ == '__main__':
    app.run()
