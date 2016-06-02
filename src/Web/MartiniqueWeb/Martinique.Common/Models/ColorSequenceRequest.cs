namespace Martinique.Common.Models
{
    public enum SequenceRequestMessage
    {
        START,
        STOP
    }

    public class ColorSequenceRequest
    {
        private string _message = string.Empty;
        private ColorSequence _targetSequence = null;

        public string Message
        {
            get { return _message; }
            set { _message = value; }
        }

        public ColorSequence TargetSequence
        {
            get { return _targetSequence; }
            set { _targetSequence = value; }
        }
    }
}
