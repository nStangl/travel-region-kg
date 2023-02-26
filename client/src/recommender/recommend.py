from recommender.user_input import DashboardData
import pandas as pd
import re
import sys
sys.path.append('../graphdb-client/')


def buildQuery(data: DashboardData):
    allowed_regions = " ".join(
        ['(travelregion:{})'.format(reg)
         for reg, allowed in data.regions.items() if allowed]
    )

    query = f"""PREFIX dbo:<http://dbpedia.org/ontology/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX travelkg: <http://cit.tum.de/ontology/travelkg/>
    PREFIX travelregion: <http://cit.tum.de/ressource/travelkg/region/>
    SELECT ?region (FLOOR(7*(?budget/?cost)) AS ?numberOfDays) ?monthRating
    ?nature ?hiking ?beach ?waterSports ?winterSports ?entertainment ?culture
    ?culinary ?citiesArchitecture ?shopping
    WHERE {{
        BIND ({data.budget} AS ?budget)
        VALUES (?allowed_region) {{
            {allowed_regions}
        }}
        ?regionIRI dbo:subregion* ?allowed_region ;
            travelkg:avgCostPerWeek ?cost ;
            travelkg:{data.month}Rating/rdfs:label ?monthRating ;
            rdfs:label ?region .
        FILTER(?cost*2 < ?budget)
        ?regionIRI travelkg:natureRating/rdfs:label ?nature ;
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
    data = []

    for row in values:
        d_row = [row.get(col).get('value') for col in cols]
        data.append(d_row)

    df = pd.DataFrame(data, columns=cols)
    return (df, cols)


def rankRegions(userData: DashboardData, dataFrame: pd.DataFrame, df_cols):
    """Assign each region a rating on a scale from [0;100].

    Rating depends on user inputs.
    Activity prefernces are weighted (*2)
    The longer the duration of the stay, the higher the rating.
    """
    minScore, maxScore = getMinMaxScore(userData.preferences)
    def normalize(x): return round(
        100 * ((x - minScore) / (maxScore - minScore)))

    scores = []
    for i in dataFrame.index:
        df_row = dataFrame.iloc[i]
        score = 0
        for preference, selected in userData.preferences.items():
            x = int(df_row[preference]) - 3
            score += (x * 2 if selected else x)

        score += calculateDaysScore(int(df_row['numberOfDays']))
        score += int(df_row['monthRating']) - 3

        scores.append(normalize(score))

    dataFrame.insert(1, "score", scores)


def getMinMaxScore(preferences: dict()):
    """Calculate highest and lowest possible score for normalization."""
    n = len(preferences)
    x = list(preferences.values()).count(True)

    # preferences are weighted in the score (* 2), min-max scores depend
    # on number of selected preferences
    minScore = -2 + 1 + x * -4 + (n-x) * (-2)
    maxScore = 2 + 5 + x * 4 + (n-x) * 2
    return (minScore, maxScore)


def calculateDaysScore(n):
    if n < 3:
        return 1
    elif n < 7:
        return 2
    elif n < 14:
        return 3
    elif n < 21:
        return 4
    else:
        return 5


def displayRegion(rank, region, score, staytime, avgCostPerWeek):
    region = f"""-----
**Destination {rank}: {region}**
| Score | Maximum Staytime | Average Cost Per Week |
|:------|:------------------|:----------------------|
|{score} % |{staytime} days | {avgCostPerWeek}    |
"""
    return region


def prettyPrintRegion(region: str):
    """Convert regions `USA_southwest` to `USA southwest`"""
    regex = r"[_]+"
    return re.sub(regex, ' ', region)


def displayRecommendations(df: pd.DataFrame):
    rank = 1
    output = """*Recommended Travel Trips:*
---
"""
    for index, row in df.iterrows():
        output += displayRegion(rank, prettyPrintRegion(row['region']).strip(),
                                row['score'], row['numberOfDays'], 400)
        output += "\n"
        rank += 1

    return output
