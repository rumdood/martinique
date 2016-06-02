using System;
using System.Collections.Generic;
using System.Linq;
using Martinique.Common.Models;
using Martinique.Managers.Contracts;
using Martinique.ResourceAccess.Contracts;

namespace Martinique.Managers
{
    public class ColorSequenceManager : IColorSequenceManager
    {
        private readonly IColorSequenceRepository _sequences;
        private readonly IDeviceRepository _devices;

        public IEnumerable<ColorSequence> FindColorSequences(string name)
        {
            IEnumerable<ColorSequence> sequences = _sequences.FindColorSequence(name);
            return sequences;
        }

        public ColorSequence GetColorSequence(string name)
        {
            ColorSequence sequence = FindColorSequences(name).Where(x => x.Name.Equals(name)).FirstOrDefault();
            return sequence;
        }

        public IEnumerable<string> GetDeviceList()
        {
            IEnumerable<string> devices = _devices.GetDeviceList();
            return devices;
        }

        public void StartSequenceOnDevice(string deviceId, ColorSequence sequence)
        {
            if (deviceId.Length == 0)
            {
                throw new InvalidOperationException("Device ID Cannot Be Empty");
            }

            if (sequence == null || sequence.Colors.Count == 0)
            {
                throw new InvalidOperationException("Sequence Cannot Be Null or Have No Colors");
            }

            if (!_devices.IsValidDevice(deviceId))
            {
                throw new InvalidOperationException(string.Format("No Such Device Exists [{0}]", deviceId));
            }

            _devices.StartColorSequence(deviceId, sequence);
        }

        public void StopSequenceOnDevice(string deviceId)
        {
            if (deviceId.Length == 0)
            {
                throw new InvalidOperationException("Device ID Cannot Be Empty");
            }

            if (!_devices.IsValidDevice(deviceId))
            {
                throw new InvalidOperationException(string.Format("No Such Device Exists [{0}]", deviceId));
            }

            _devices.StopCurrentSequence(deviceId);
        }

        public void UpdateColorSequence(ColorSequence sequence)
        {
            _sequences.UpdateColorSequence(sequence);
        }

        public void ShutdownDevice(string deviceId)
        {
            if (deviceId.Length == 0)
            {
                throw new InvalidOperationException("Device ID Cannot Be Empty");
            }

            if (!_devices.IsValidDevice(deviceId))
            {
                throw new InvalidOperationException(string.Format("No Such Device Exists [{0}]", deviceId));
            }

            _devices.ShutdownDevice(deviceId);
        }
    }
}
