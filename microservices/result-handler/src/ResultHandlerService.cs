using Microsoft.Azure.Cosmos;
using Microsoft.Extensions.Logging;
using System.Threading.Tasks;

public class ResultHandlerService
{
    private readonly CosmosClient _cosmosClient;
    private readonly ILogger<ResultHandlerService> _logger;
    private readonly Container _container;

    public ResultHandlerService(CosmosClient cosmosClient, ILogger<ResultHandlerService> logger)
    {
        _cosmosClient = cosmosClient;
        _logger = logger;
        _container = _cosmosClient.GetContainer("DatabaseName", "ContainerName");
    }

    public async Task HandleProcessedDataAsync(string processedData)
    {
        _logger.LogInformation($"Handling processed data: {processedData}");

        // Store processed data in Cosmos DB
        var item = new { id = Guid.NewGuid().ToString(), data = processedData };
        await _container.CreateItemAsync(item, new PartitionKey(item.id));

        _logger.LogInformation($"Processed data stored: {processedData}");
    }
}
