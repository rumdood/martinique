using Martinique.Common.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Martinique.ResourceAccess.Contracts
{
    public interface IDeviceRepository
    {
        void StartColorSequence(string deviceId, ColorSequence sequence);
        void StopCurrentSequence(string deviceId);
        void ShutdownDevice(string deviceId);
        IEnumerable<string> GetDeviceList();
        bool IsValidDevice(string deviceId);
    }
}
