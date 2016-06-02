using Martinique.Common.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Martinique.Managers.Contracts
{
    public interface IColorSequenceManager
    {
        void StartSequenceOnDevice(string deviceId, ColorSequence sequence);
        void StopSequenceOnDevice(string deviceId);
        void ShutdownDevice(string deviceId);
        ColorSequence GetColorSequence(string name);
        IEnumerable<ColorSequence> FindColorSequences(string name);
        void UpdateColorSequence(ColorSequence sequence);
        IEnumerable<string> GetDeviceList();
    }
}
