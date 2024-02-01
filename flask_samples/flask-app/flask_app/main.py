#!/usr/bin/env python3

from flask_app.data import generate_companies
companies = generate_companies(100)


def main():
    print(companies)


if __name__ == '__main__':
    main()
