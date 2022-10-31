# Import the library.
from googleads import ad_manager

# Initialize a client object, by default uses the credentials in ~/googleads.yaml.
client = ad_manager.AdManagerClient.LoadFromStorage()

# Initialize a service.
network_service = client.GetService('NetworkService', version='v202208')

# Make a request.
current_network = network_service.getCurrentNetwork()

print("Current network has network code '%s' and display name '%s'." %
        (current_network['networkCode'], current_network['displayName']))
