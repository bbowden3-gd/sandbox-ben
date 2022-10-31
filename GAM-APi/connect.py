
# from googleads import ad_manager
# from googleads import oauth2


# # Initialize the GoogleRefreshTokenClient using the credentials you received
# # in the earlier steps.
# key_file = 'app_key.json'
# application_name = "test'" 
# oauth2_client = oauth2.GoogleServiceAccountClient(
#     key_file, oauth2.GetAPIScope('ad_manager'))

# # Initialize the Ad Manager client.
# ad_manager_client = ad_manager.AdManagerClient(oauth2_client, application_name)
import json
from googleads import ad_manager
from googleads import oauth2

# OAuth2 credential information. In a real application, you'd probably be
# pulling these values from a credential storage.
KEY_FILE = 'app_key.json'

# Ad Manager API information.
APPLICATION_NAME = 'TEST'
networkCode= ''

def main(KEY_FILE, APPLICATION_NAME):
  oauth2_client = oauth2.GoogleServiceAccountClient(
      KEY_FILE, oauth2.GetAPIScope('ad_manager'))

  client = ad_manager.AdManagerClient(
      oauth2_client, APPLICATION_NAME)

  networks = client.GetService('NetworkService').getAllNetworks()
#   for network in networks:
#     print('Network with network code "%s" and display name "%s" was found.'
#           % (network['networkCode'], network['displayName']))
  
  print(networks)



  custom_field_service = client.GetService(
      'CustomFieldService', version='v202208')
  print('stage2')
  # Create a statement to select custom fields.
  statement = ad_manager.StatementBuilder(version='v202208', network_code=networkCode)

  # Retrieve a small amount of custom fields at a time, paging
  # through until all custom fields have been retrieved.
  while True:
    response = custom_field_service.getCustomFieldsByStatement(
        statement.ToStatement())
    if 'results' in response and len(response['results']):
      for custom_field in response['results']:
        # Print out some information for each custom field.
        print('Custom field with ID "%d" and name "%s" was found.\n' %
              (custom_field['id'], custom_field['name']))
      statement.offset += statement.limit
    else:
      break

  print('\nNumber of results found: %s' % response['totalResultSetSize'])







if __name__ == '__main__':
  main(KEY_FILE, APPLICATION_NAME)