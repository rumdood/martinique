using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Martinique.Common.Models;

namespace Martinique.ResourceAccess.Contracts
{
    public interface IColorSequenceRepository
    {
        IEnumerable<ColorSequence> FindColorSequence(string name);
        void UpdateColorSequence(ColorSequence sequence);
        void DeleteColorSequence(string name);
    }
}
