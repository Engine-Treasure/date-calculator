#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

import click


WEEKDAY = ("Monday",
           "Tuesday",
           "Wednesday",
           "Thursday",
           "Friday",
           "Saturday",
           "Sunday")


class DateCalculator(object):
    """"""

    def __init__(self, date_1, date_2, num_of_days):
        self.today = datetime.datetime.today()
        self.date_1 = date_1
        self.date_2 = date_2
        self.nod = num_of_days

    def cal(self):

        def today(dt):
            print "It is {0}, {1}.\nHave a nice day~".format(
                dt,
                WEEKDAY[dt.weekday()]
            )

        def next_date(dt, num):
            dt_ = dt + datetime.timedelta(num)
            ab = "after" if num >= 0 else "before"
            print "{0} days {1} {2} is {3}".format(
                num,
                ab,
                dt,
                dt_
            )

        def in_days(dt_1, dt_2):
            delta = dt_2 - dt_1
            print "There are {0} days between {1} and {2}.".format(
                delta,
                dt_1,
                dt_2
            )

        if not self.date_2 and not self.nod:
            today(self.date_1) if self.date_1 != self.today \
                else today(self.today)
        elif not self.date_2 and self.nod:
            next_date(self.date_1, self.nod)
        elif not self.nod and self.date_2:
            in_days(self.date_1, self.date_2)
        else:
            in_days(self.date_1, self.date_2)
            next_date(self.date_1, self.nod)


def date_format(ctx, param, value):
    """"""
    if isinstance(value, (unicode, str)):
        value = value.replace("/", "").replace(".", "").replace("-", "")
        try:
            value = datetime.datetime.strptime(value, "%Y%m%d")
        except ValueError:
            raise ValueError("Incorrect data format")

    return value


@click.command()
@click.argument("date_p",
                default=datetime.datetime.today(),  # `required == False`
                callback=date_format,
                type=click.STRING)
@click.option("-d", "days",
              type=click.INT,
              help="Date difference")
@click.option("-n", "date_n",
              callback=date_format,
              type=click.STRING)
@click.pass_context
def cli(ctx, **kwargs):
    date_p = kwargs.pop("date_p")
    date_n = kwargs.pop("date_n")
    days = kwargs.pop("days")
    dc = DateCalculator(date_p, date_n, days)
    dc.cal()

if __name__ == "__main__":
    cli()
