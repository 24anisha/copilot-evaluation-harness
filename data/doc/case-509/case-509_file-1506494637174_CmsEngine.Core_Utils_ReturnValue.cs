using Newtonsoft.Json;

namespace CmsEngine.Core
{
    public class ReturnValue
    {
        public ReturnValue(string message, bool isError = false)
        {
            Message = message;
            IsError = IsError;
        }

        [JsonProperty(PropertyName = "message")]
        public string Message { get; private set; }

        [JsonProperty(PropertyName = "isError")]
        public bool IsError { get; private set; }

        [JsonProperty(PropertyName = "exception")]
        public string Exception { get; private set; }

        [JsonProperty(PropertyName = "value")]
        public object Value { get; set; }

        public void SetErrorMessage(string message, string exception = "")
        {
            Message = message;
            Exception = exception;
            IsError = true;
        }
    }
}