using System;
using RawRabbit.Compatibility.Legacy.Configuration.Exchange;
using RawRabbit.Compatibility.Legacy.Configuration.Queue;

namespace RawRabbit.Compatibility.Legacy.Configuration.Request
{
	public class RequestConfigurationBuilder : IRequestConfigurationBuilder
	{
		private readonly QueueConfigurationBuilder _replyQueue;
		private readonly ExchangeConfigurationBuilder _exchange;
		public RequestConfiguration Configuration { get; }

		public RequestConfigurationBuilder(RequestConfiguration defaultConfig)
		{
			_replyQueue = new QueueConfigurationBuilder(defaultConfig.ReplyQueue);
			_exchange = new ExchangeConfigurationBuilder(defaultConfig.Exchange);
			Configuration = defaultConfig ?? new RequestConfiguration();
		}

		public IRequestConfigurationBuilder WithExchange(Action<IExchangeConfigurationBuilder> exchange)
		{
			exchange(_exchange);
			Configuration.Exchange = _exchange.Configuration;
			return this;
		}

		public IRequestConfigurationBuilder WithRoutingKey(string routingKey)
		{
			Configuration.RoutingKey = routingKey;
			return this;
		}

		public IRequestConfigurationBuilder WithReplyQueue(Action<IQueueConfigurationBuilder> replyTo)
		{
			replyTo(_replyQueue);
			Configuration.ReplyQueue = _replyQueue.Configuration;
			return this;
		}

		public IRequestConfigurationBuilder WithNoAck(bool noAck)
		{
			return WithAutoAck(noAck);
		}

		public IRequestConfigurationBuilder WithAutoAck(bool autoAck)
		{
			Configuration.AutoAck = autoAck;
			return this;
		}
	}
}