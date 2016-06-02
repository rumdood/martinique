using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Martinique.Common.Models;
using Martinique.ResourceAccess.Contracts;

namespace Martinique.ResourceAccess
{
    public class DeviceRepository : IDeviceRepository
    {
        public IEnumerable<string> GetDeviceList()
        {
            throw new NotImplementedException();
        }

        public bool IsValidDevice(string deviceId)
        {
            throw new NotImplementedException();
        }

        public void ShutdownDevice(string deviceId)
        {
            throw new NotImplementedException();
        }

        public void StartColorSequence(string deviceId, ColorSequence sequence)
        {
            throw new NotImplementedException();
        }

        public void StopCurrentSequence(string deviceId)
        {
            throw new NotImplementedException();
        }
    }
}
