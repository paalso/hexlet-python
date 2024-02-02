#!/usr/bin/env python3

from flask_app.data import generate_companies, generate_companies_old
companies_old = generate_companies_old(100)
companies = generate_companies(100)


def main():
    print(companies_old[:5])
    print()
    print(companies[:5])


if __name__ == '__main__':
    main()
