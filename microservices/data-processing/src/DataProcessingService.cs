using Microsoft.Azure.EventGrid;
using Microsoft.Azure.EventGrid.Models;
using Microsoft.Extensions.Logging;
using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;

public class DataProcessingService
{
    private readonly EventGridClient _eventGridClient;
    private readonly ILogger<DataProcessingService> _logger;

    public DataProcessingService(EventGridClient eventGridClient, ILogger<DataProcessingService> logger)
    {
        _eventGridClient = eventGridClient;
        _logger = logger;
    }

    public async Task ProcessDataAsync(string eventData)
    {
        _logger.LogInformation($"Processing data: {eventData}");

        // Perform real-time data processing here...

        var eventDataProcessed = $"{eventData} - processed at {DateTime.UtcNow}";
        await PublishEventAsync(eventDataProcessed);
    }

    private async Task PublishEventAsync(string processedData)
    {
        var eventGridEvent = new EventGridEvent(
            Guid.NewGuid().ToString(),
            "DataProcessed",
            processedData,
            "DataProcessingService",
            DateTime.UtcNow,
            "1.0");

        var events = new List<EventGridEvent> { eventGridEvent };

        await _eventGridClient.PublishEventsAsync("https://your-event-grid-endpoint.com", events);
        _logger.LogInformation($"Processed event published: {processedData}");
    }
}
