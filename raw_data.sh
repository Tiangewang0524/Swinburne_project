curl "http://45.113.232.90/couchdbro/instagram/_design/instagram/_view/summary" \
-G \
--data-urlencode 'start_key=["melbourne",2017,1,1]' \
--data-urlencode 'end_key=["melbourne",2018,3,12]' \
--data-urlencode 'reduce=false' \
--data-urlencode 'include_docs=true' \
--user "readonly:ween7ighai9gahR6" \
-o /tmp/raw_instagram_data.json

curl "http://45.113.232.90/couchdbro/twitter/_design/twitter/_view/summary" \
-G \
--data-urlencode 'start_key=["melbourne",2017,6,15]' \
--data-urlencode 'end_key=["melbourne",2018,5,4]' \
--data-urlencode 'reduce=false' \
--data-urlencode 'include_docs=true' \
--user "readonly:ween7ighai9gahR6" \
-o /tmp/raw_twitter_data.json