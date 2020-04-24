import os

settings = {
    'host': os.environ.get('ACCOUNT_HOST', 'https://sredevops.documents.azure.com:443/'),
    'master_key': os.environ.get('ACCOUNT_KEY', 'jEdyU4qvtudIAoK9mxWkJ3IqUT3IUzbc195UE7YG0limMdelJYmYa79WsfwSeaaZjcC5xV5SbpkUQmrOHbYL6A=='),
    'database_id': os.environ.get('COSMOS_DATABASE', 'airlines'),
    'container_id': os.environ.get('COSMOS_CONTAINER', 'openflights'),
}