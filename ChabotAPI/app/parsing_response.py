def parse_response(response):
    """
    response: QueryResult object from dialogflow
    return a dictionary with relevant information about de response from Dialogflow
    
    """

    text   = response.fulfillment_text
    intent = response.intent.display_name

    if hasattr(response, "all_required_params_present"):
        all_parameters = True

    elif not hasattr(response, "all_required_params_present"):
        all_parameters  = False
    
    if all_parameters == True and intent == "UserNeeds":
        search_products = True
    else:
        search_products = False
    
    response = {

        "text": text,
        "intent": intent,
        "all_parameters": all_parameters,
        "search": search_products,
        "query": _get_query(response)
    }
    return response

def _get_query(response):

    n_product = len(response.parameters.fields["Products"].list_value)
    n_number  = len(response.parameters.fields["number"].list_value)

    products = []
    cant = []

    for index in range(n_product):
        products.append(response.parameters.fields["Products"].list_value[index])

    for index in range(n_number):
        cant.append(response.parameters.fields["number"].list_value[index])

    if len(cant) > len(products):

        cant = cant[:len(products)]

    
    
    elif len(products) > len(cant) and len(cant) > 0:

        dif = len(products) - len(cant)
        temp = [cant[-1]] * dif
        cant.extend(temp)
    
    query = {

        "products":products,
        "cants": cant
    }
    
    return query

    



