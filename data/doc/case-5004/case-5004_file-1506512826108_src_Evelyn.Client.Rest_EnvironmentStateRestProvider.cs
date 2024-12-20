﻿namespace Evelyn.Client.Rest
{
    using System;
    using System.Collections.Generic;
    using Domain;
    using Generated;
    using Microsoft.Extensions.Logging;
    using Microsoft.Extensions.Options;
    using Provider;

    public class EnvironmentStateRestProvider : IEnvironmentStateProvider
    {
        private readonly EvelynRestClient _client;
        private readonly ILogger<EnvironmentStateRestProvider> _logger;

        public EnvironmentStateRestProvider(IOptions<EnvironmentStateRestProviderOptions> options, ILogger<EnvironmentStateRestProvider> logger)
        {
            _client = new EvelynRestClient(options.Value.BaseUrl);
            _logger = logger;
        }

        public Domain.EnvironmentState Invoke(Guid projectId, string environmentKey)
        {
            try
            {
                var dto = _client
                    .GetAsync(projectId, environmentKey)
                    .GetAwaiter().GetResult();

                var toggleStates = new List<Domain.ToggleState>();

                foreach (var toggleState in dto.EnvironmentState.ToggleStates)
                {
                    if (bool.TryParse(toggleState.Value, out var value))
                    {
                        toggleStates.Add(new Domain.ToggleState(toggleState.Key, value));
                    }
                }

                return new Domain.EnvironmentState(dto.Audit.StreamPosition.Value, toggleStates);
            }
            catch (SwaggerException ex)
            {
                _logger.LogWarning(ex, "Failed to get state of {@projectdId} {@environmentKey} from {@serverBaseUrl}", projectId, environmentKey, _client.BaseUrl);
                throw new SynchronizationException("FailedToGetEnvironmentState", ex);
            }
        }
    }
}