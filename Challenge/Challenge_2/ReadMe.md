# Challenge 2 


In this code, we first retrieve the metadata of the instance using the requests library and the Azure Instance Metadata Service URL. The metadata is then parsed as a JSON object.

We then check if a data_key parameter is passed in the request. If it is, we return the value of the specific data key in the metadata. If not, we return the full metadata.

This Azure Function could be triggered by an HTTP request and return the JSON response to the client.

# Deployment

1.Create an Azure Function App: Go to the Azure portal and create a new Azure Function App. You can either use the Azure CLI, Azure Powershell, or the Azure portal to create the Function App.

2.Add a new function: Once you have created the Function App, add a new function to it. You can do this through the Azure portal or by using the Azure Functions Core Tools. Choose the HTTP Trigger template and provide a name for your function.

3.Deploy the code: Deploy your code to the Azure Function. You can do this by copying and pasting the code into the Azure portal, or by using Git to push the code to the Function App.

4.Configure the function: Configure the function to run in a specific version of Python. You can do this by specifying the runtime version in the function.json file or by using the Azure portal.

5.Test the function: Test the function by sending an HTTP request to the function endpoint. You can use tools such as curl or Postman to send the request.

# Links used and 2 sample codes
1. Challenge2a is retrieving metadata from azure VM instance and written in python language.
2. Challenge2b is written in powershell format for the same.
3. https://learn.microsoft.com/en-us/azure/virtual-machines/linux/instance-metadata-service?tabs=windows
