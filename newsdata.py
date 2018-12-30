#!/usr/bin/env python3

import psycopg2

NEWS_DB = "news"

divider = "----------------------------------------------------------"


def most_popular_articles():
    query = '''
    SELECT articles.id, title, count(*) as num
    FROM articles, log
    WHERE log.path = concat('/article/', articles.slug)
    GROUP BY articles.id
    ORDER BY num DESC
    LIMIT 3;
    '''
    articles = execute_query(query)
    res = "Most Popular Articles\n{}".format(divider)
    for row in articles:
        res += "\n\"{0}\" - {1} views".format(row[1], row[2])
    return res


def most_popular_authors():
    query = '''
        SELECT authors.id, authors.name, count(*) as num
        FROM authors, articles, log
        WHERE authors.id = articles.author
        AND log.path = concat('/article/', articles.slug)
        GROUP BY authors.id
        ORDER BY num DESC
        LIMIT 3;
    '''
    authors = execute_query(query)
    res = "Most Popular Authors\n{}".format(divider)
    for author in authors:
        res += "\n{0} - {1} views".format(author[1], author[2])
    return res


def days_with_errors_over_1_percent():
    query = '''
        SELECT day, rate
        FROM(
            SELECT to_char(time, 'FMMonth DD, yyyy') AS day,
            avg(CASE WHEN status like '40%' THEN 1 ELSE 0 END) as rate
            FROM log
            GROUP BY day
        ) as subq
        WHERE rate > 0.01
        ORDER BY rate DESC
    '''

    rates = execute_query(query)
    res = "Days Where More Than 1% of Requests Lead to Errors\n{}" \
        .format(divider)
    for rate in rates:
        pct = "{:.1%}".format(rate[1])
        res += "\n{0} - {1} errors".format(rate[0], pct)
    return res


def execute_query(query):
    db = psycopg2.connect(database=NEWS_DB)
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result


def print_result():
    articles = most_popular_articles()
    authors = most_popular_authors()
    days = days_with_errors_over_1_percent()
    print("\n{0}\n\n{1}\n\n{2}\n".format(articles, authors, days))


print_result()
