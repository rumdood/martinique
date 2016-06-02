using System.Collections.Generic;

namespace Martinique.Common.Models
{
    public class ColorSequence
    {
        private List<RgbColor> _colors = new List<RgbColor>();
        private int _fadeDelay = 0;
        private int _cycleDelay = 0;

        public string Name { get; set; }

        public List<RgbColor> Colors
        {
            get { return _colors; }
            set { _colors = value; }
        }

        public int FadeDelay
        {
            get { return _fadeDelay; }
            set { _fadeDelay = value; }
        }

        public int CycleDelay
        {
            get { return _cycleDelay; }
            set { _cycleDelay = value; }
        }
    }
}
