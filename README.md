### Running

    git clone https://github.com/cscanlin/simplyinsured_lite.git
    cd simplyinsured_lite
    python manage.py migrate  # create db
    python manage.py runserver  # runs server
    python manage.py shell  # opens django shell

And inside of the shell run the following

    from plan_finder.models import *
    Region.load_from_csv('raw_california_plans/regions.csv')
    Plan.load_from_csv('raw_california_plans/plan.csv')
    Price.load_from_csv('raw_california_plans/prices.csv')

**Warning:** I didn't have time to optimize the data loading, so it takes about 5 mins to run.

Then go to: `http://127.0.0.1:8000/plan_finder/` to see it live!

TODO:

1. Put loading scripts in a command and optimize query for loading. Alternatively: fixtures

2. Better relationships between the models. I ran out of time on this part, but defining the relationships on the models (instead of fetching by common attributes) would make this much better. Also, django has some nice tricks like `prefetch_related` to optimize queries on stuff like this.

3. Fix fields on Plan model
