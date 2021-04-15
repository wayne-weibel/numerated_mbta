# Numerated Coding Challenge

## Challenge
Find the next departing train for a particular stop on the MBTA T network.

## Story Form
As an MBTA rider, I would like to know when the next train is going to depart from a specific
stop so that I know when I should plan to get to the boarding area.
Instructions

Write a program in a language of your choice (we prefer Python or Angular) that interacts with
the MBTA public API (https://api-v3.mbta.com) to achieve the following acceptance criteria:

1. Your program should prompt users to select from a list of routes that service only Light
and Heavy Rail trains.
2. Your program should display a listing of stops related to the selected route and prompt
the user to select a stop
3. Your program should display a list of route directions and prompt the user to select a
direction
4. Your program should display the next predicted departure time for a train based on the
previously selected inputs

## Evaluation
Your code submission will be evaluated on function, code structure, performance, readability,
testability and supplied automated tests. If there are any package dependencies or special
install instructions, please make sure to include those with your submission.

__*to be complete within 48 hours*__

---

#### Django

This was my first time using Django.  Apologies that it is not fully utilized and
some of the things are likely out of place.  I am sure there are also ways to incorporate NPM
to acquire and manage frontend libraries that would greatly improve the UI; went with standard
CSS (minimally would want a Sass or Less compiler) and jQuery.  The initial setup of Django and
working with the obfuscatation of `manage.py` and setting up the repo for presentation was
more of an issue than the actual exercise. Not to mention that the MBTA API has a few issues:
when requesting stops you are able to include the related route, however, this is only when
filtering with a single route (not a list). So, that required a significant refactor and addition
of paths, functions, and additional ajax call from the frontend.

Anyway ... to use:

```
cd [path-to-repo]/django
make
make run

* In your favorite browser go to `http://localhost:8000/mbta`
```

Running tests:

```
cd [path-to-repo]/django
make
make test

* Coverage report generated to [path-to-repo]/django/htmlcov
```

---

This was an interesting exercise touching on many aspects of software development.
I certainly learned things. I hope to extend this same exercise to other frameworks.
