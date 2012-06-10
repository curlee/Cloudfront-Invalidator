Cloudfront-Invalidator
======================

Cloudfront Invalidation script for the boto library. Eventually this will integrate with Django.

Usage
=====

Create a settings.py file which matches the contents of settings_default.py
Set up the AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY and AWS_CF_DISTRIBUTION_ID variables with values that match your AWS Cloudfront distribution.

Run from command line:
python invalidate.py [file 1] [file 2] [file 3] [...]

Note:
Files must start with a forward slash ( ie: python invalidate.py /example.css ).