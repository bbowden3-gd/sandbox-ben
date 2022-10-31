from googleads import ad_manager
import pprint as pp
import json
def main(client):
  # Initialize appropriate service.
  custom_targeting_service = client.GetService(
      'CustomTargetingService', version='v202208')

  # Create statement to get all targeting keys.
  targeting_key_statement = ad_manager.StatementBuilder(version='v202208')

  all_keys = []

  # Get custom targeting keys by statement.
  while True:
    response = custom_targeting_service.getCustomTargetingKeysByStatement(
        targeting_key_statement.ToStatement())
    if 'results' in response and len(response['results']):
      all_keys.extend(response['results'])
      targeting_key_statement.offset += targeting_key_statement.limit
    else:
      break

  if all_keys:
    # Create a statement to select custom targeting values.
    statement = (ad_manager.StatementBuilder(version='v202208')
                 .Where('customTargetingKeyId IN (%s)' %
                        ', '.join([str(key['id']) for key in all_keys])))

    # Retrieve a small amount of custom targeting values at a time, paging
    # through until all custom targeting values have been retrieved.
    #while True:
    response = custom_targeting_service.getCustomTargetingValuesByStatement(
        statement.ToStatement())

      #print(response)  
    for custom_targeting_value in response['results']:
        # Print out some information for each custom targeting value.
        print('Custom targeting value with ID "%d", name "%s", display name '
              '"%s", and custom targeting key ID "%d" was found. \n' %
              (custom_targeting_value['id'], custom_targeting_value['name'],
                custom_targeting_value['displayName'],
                custom_targeting_value['customTargetingKeyId']
            ))
      statement.offset += statement.limit


    print('\nNumber of results found: %s' % response['totalResultSetSize'])


if __name__ == '__main__':
  # Initialize client object.
  ad_manager_client = ad_manager.AdManagerClient.LoadFromStorage()
  main(ad_manager_client)