export PYTHONPATH="."
luigi --module top_artists AggregateArtists --local-scheduler --date-interval 2016-06
