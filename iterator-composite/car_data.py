from os import path

ford_list = [
    {"model_name":"Aerostar","model_make_id":"ford"},
    {"model_name":"Anglia","model_make_id":"ford"},
    {"model_name":"Artic","model_make_id":"ford"},
    {"model_name":"Aspire","model_make_id":"ford"},
    {"model_name":"Bantam","model_make_id":"ford"},
    {"model_name":"Bronco","model_make_id":"ford"},
    {"model_name":"Bronco II","model_make_id":"ford"}
]

gmc_dict = {
    "Acadia": {"model_make_id":"gmc"},
    "Autonomy": {"model_make_id":"gmc"},
    "Canyon": {"model_make_id":"gmc"},
    "Envoy": {"model_make_id":"gmc"},
    "EV1": {"model_make_id":"gmc"},
    "Firebird": {"model_make_id":"gmc"},
    "Jimmy": {"model_make_id":"gmc"},
    "Safari": {"model_make_id":"gmc"},
    "Savana": {"model_make_id":"gmc"},
    "Sierra": {"model_make_id":"gmc"}
}

cadillac_tuple = (
    {"model_name":"60","model_make_id":"cadillac"},
    {"model_name":"61","model_make_id":"cadillac"},
    {"model_name":"62","model_make_id":"cadillac"},
    {"model_name":"6239D","model_make_id":"cadillac"},
    {"model_name":"Allante","model_make_id":"cadillac"},
    {"model_name":"ATS","model_make_id":"cadillac"},
    {"model_name":"ATS Coupe","model_make_id":"Cadillac"},
    {"model_name":"Aurora","model_make_id":"cadillac"}
)

def acura_generator():
    with open(path.join(path.dirname(path.realpath(__file__)),'acura.csv')) as f:
        for line in f:
            line = line.rstrip("\n").split(",", 1)
            yield {"model_name":line[0],"model_make_id": line[1]}