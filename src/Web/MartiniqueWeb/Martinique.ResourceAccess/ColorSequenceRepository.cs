using System;
using System.Collections.Generic;
using Martinique.Common.Models;
using Martinique.ResourceAccess.Contracts;

namespace Martinique.ResourceAccess
{
    public class ColorSequenceRepository : IColorSequenceRepository
    {
        public void DeleteColorSequence(string name)
        {
            throw new NotImplementedException();
        }

        public IEnumerable<ColorSequence> FindColorSequence(string name)
        {
            throw new NotImplementedException();
        }

        public void UpdateColorSequence(ColorSequence sequence)
        {
            throw new NotImplementedException();
        }
    }
}
