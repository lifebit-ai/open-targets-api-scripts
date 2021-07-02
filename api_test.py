from opentargets import OpenTargetsClient
from opentargets.statistics import HarmonicSumScorer


def function_query_disease(str_disease_type, str_output_filename):
    """
    Args:
        str_disease_type: String
        str_output_filename: String
    """

    print('Querying for disease: ', str_disease_type)


    ot = OpenTargetsClient()

    # or with API key

    #from opentargets import OpenTargetsClient
    #ot = OpenTargetsClient(auth_app_name=<APIKEY_APPNAME>, auth_secret=<APIKEY_SECRET>)


    # search for a target


    search_result = ot.search(str_disease_type)
    print (search_result[0])

    # search associations for a target
    
    a_for_target = ot.get_associations_for_target(str_disease_type)
    for a in a_for_target:
        print(a['id'], a['association_score']['overall'])
        print(a['target'], a['association_score']['overall'])



    # search associations for a disease


    a_for_disease = ot.get_associations_for_disease(str_disease_type)

    a_for_disease[1]

    #get an association by id:

    # get evidence for a target

    e_for_target = ot.get_evidence_for_target(str_disease_type)
    for evidence_json in e_for_target.to_json():
        print(evidence_json)

    # get evidence for a disease:

    e_for_disease = ot.get_evidence_for_disease(str_disease_type)

    client = OpenTargetsClient()
    response = client.filter_associations()
    response
    print(response)
    response.filter(direct=True)
    print(response)
    response.filter(scorevalue_min=0.2)
    print("Filtering by scorevalue_min",response)
    print(response[0])
    response = client.get_associations_for_target(str_disease_type,
                                                  fields=['association_score.overall',
                                                          'target.gene_info.symbol']
                                                  )

    response.to_excel(str_output_filename)


if __name__ == '__main__':

    function_query_disease(str_disease_type='schizophrenia',
                           str_output_filename='schizophrenia_associated_diseases_by_datasource.xls')
