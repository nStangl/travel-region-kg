import pandas as pd
import re
import math
import sys
sys.path.append('../graphdb-client/')
import swagger_client


def buildQuery(user_input):
    allowed_regions = " ".join(
        ['(travelregion:{})'.format(reg)
         for reg, allowed in user_input.regions.items() if allowed]
    )

    query = f"""PREFIX dbo:<http://dbpedia.org/ontology/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX travelkg: <http://cit.tum.de/ontology/travelkg/>
    PREFIX travelregion: <http://cit.tum.de/ressource/travelkg/region/>
    SELECT ?region ?cost (FLOOR(7*(?budget/?cost)) AS ?numberOfDays) ?monthRating
    ?nature ?hiking ?beach ?waterSports ?winterSports ?entertainment ?culture
    ?culinary ?citiesArchitecture ?shopping
    WHERE {{
        BIND ({user_input.budget} AS ?budget)
        VALUES (?allowed_region) {{
            {allowed_regions}
        }}
        ?regionIRI dbo:subregion* ?allowed_region ;
            travelkg:avgCostPerWeek ?cost .
        FILTER NOT EXISTS {{ ?any dbo:subregion ?regionIRI }}
        FILTER(?cost*2 < ?budget)
        ?regionIRI rdfs:label ?region ;
            travelkg:{user_input.month}Rating/rdfs:label ?monthRating ;
            travelkg:natureRating/rdfs:label ?nature ;
            travelkg:hikingRating/rdfs:label ?hiking ;
            travelkg:beachRating/rdfs:label ?beach ;
            travelkg:waterSportsRating/rdfs:label ?waterSports ;
            travelkg:winterSportsRating/rdfs:label ?winterSports ;
            travelkg:entertainmentRating/rdfs:label ?entertainment ;
            travelkg:cultureRating/rdfs:label ?culture ;
            travelkg:culinaryRating/rdfs:label ?culinary ;
            travelkg:citiesArchitectureRating/rdfs:label ?citiesArchitecture ;
            travelkg:shoppingRating/rdfs:label ?shopping .
    }}
    """
    return query


def readAPIResponse(response):
    cols = response.get('head').get('vars')
    values = response.get('results').get('bindings')
    user_input = []

    for row in values:
        d_row = [row.get(col).get('value') for col in cols]
        user_input.append(d_row)

    df = pd.DataFrame(user_input, columns=cols)
    return df


def rankRegions(user_input, dataFrame: pd.DataFrame):
    """Assign each region a rating on a scale from [0;100].

    Rating depends on user inputs.
    Activity prefernces are weighted (*2)
    The longer the duration of the stay, the higher the rating.
    """
    minScore, maxScore = getMinMaxScore(user_input.preferences)
    def normalize(x): return round(
        100 * ((x - minScore) / (maxScore - minScore)))

    scores = []
    for i in dataFrame.index:
        df_row = dataFrame.iloc[i]
        score = 0
        for preference, selected in user_input.preferences.items():
            x = int(df_row[preference]) - 3
            score += (x * 2 if selected else x)

        score += 1 if int(df_row['numberOfDays']) > user_input.maxDays else 0
        score += int(df_row['monthRating']) - 3

        scores.append(normalize(score))

    dataFrame.insert(1, "score", scores)


def getMinMaxScore(user_preferences):
    """Calculate highest and lowest possible score for normalization."""
    n = len(user_preferences)
    x = list(user_preferences.values()).count(True)

    # preferences are weighted in the score (* 2), min-max scores depend
    # on number of selected preferences
    minScore = -2 + 1 + x * -4 + (n-x) * (-2)
    maxScore = 2 + 5 + x * 4 + (n-x) * 2
    return (minScore, maxScore)
    

def displayRecommendations(df: pd.DataFrame, user_input):
    rank = 1
    def pretty(reg): return re.sub(r"[_]+", " ", reg).strip()
    output = "*Recommended Travel Trips:*\n---\n"

    for _, row in df.iterrows():
        cost = int(row['cost'])
        max_stay = min(user_input.maxDays, int(row['numberOfDays']))
        cost_of_stay = math.ceil(max_stay * cost / 7)
        output += displayRegion(rank, pretty(row['region']),
                                row['score'], max_stay, cost_of_stay)
        output += "\n"
        rank += 1

    return output


def displayRegion(rank, region, score, staytime, avgCostPerWeek):
    region = f"""-----
**Destination {rank}: {region}**
| Score | Staytime | Cost of stay |
|:------|:------------------|:----------------------|
|{score} % |{staytime} days | {avgCostPerWeek}    |
"""
    return region


_sparql_client = swagger_client.SparqlApi()

_repository_id = 'TravelRegion'


def execute(user_input):
    query = buildQuery(user_input)
    response = _sparql_client.execute_get_select_query(
        _repository_id, query, query_ln='sparql', infer=True,
        timeout=30, distinct=True, limit=0, offset=0)

    df = readAPIResponse(response)

    rankRegions(user_input, df)
    md_result = displayRecommendations(df.nlargest(10, 'score'), user_input)
    return md_result
