"""
Your module description
"""

from searchtweets import load_credentials
from searchtweets import ResultStream, gen_rule_payload, load_credentials

premium_search_args = load_credentials(filename="./search_tweets_creds_example.yaml",
                 yaml_key="search_tweets_api",
                 env_overwrite=False)

# Internet a été coupé du 17 janvier au 20 avril 2017 https://frama.link/cAcmQvd3
query = "#bringbackourinternet"
rule = gen_rule_payload(query, results_per_call=100, from_date="2017-01-17", to_date="2017-04-20")
rs = ResultStream(rule_payload=rule, max_results=3000, **premium_search_args)

import json
with open('tweets-bringbackourinternet.json', 'a', encoding='utf-8') as f:
    for tweet in rs.stream():
        json.dump(tweet, f)
        f.write('\n')
print('done')

