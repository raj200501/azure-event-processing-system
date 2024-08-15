using Microsoft.Azure.ServiceBus;
using Microsoft.Extensions.Logging;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

public class EventIngestionService
{
    private readonly IQueueClient _queueClient;
    private readonly ILogger<EventIngestionService> _logger;

    public EventIngestionService(IQueueClient queueClient, ILogger<EventIngestionService> logger)
    {
        _queueClient = queueClient;
        _logger = logger;
    }

    public async Task IngestEventAsync(string eventData)
    {
        var message = new Message(Encoding.UTF8.GetBytes(eventData));
        await _queueClient.SendAsync(message);
        _logger.LogInformation($"Event ingested: {eventData}");
    }

    public async Task ReceiveMessagesAsync()
    {
        var messageHandlerOptions = new MessageHandlerOptions(ExceptionReceivedHandler)
        {
            MaxConcurrentCalls = 1,
            AutoComplete = false
        };

        _queueClient.RegisterMessageHandler(ProcessMessagesAsync, messageHandlerOptions);
    }

    private async Task ProcessMessagesAsync(Message message, CancellationToken token)
    {
        var eventData = Encoding.UTF8.GetString(message.Body);
        _logger.LogInformation($"Processing event: {eventData}");

        // Process the event here...

        await _queueClient.CompleteAsync(message.SystemProperties.LockToken);
    }

    private Task ExceptionReceivedHandler(ExceptionReceivedEventArgs exceptionReceivedEventArgs)
    {
        _logger.LogError($"Message handler encountered an exception {exceptionReceivedEventArgs.Exception}.");
        return Task.CompletedTask;
    }
}
