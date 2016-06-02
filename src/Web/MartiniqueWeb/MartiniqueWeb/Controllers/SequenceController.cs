using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Http;
using Martinique.Common.Models;

namespace MartiniqueWeb.Controllers
{
    public class SequenceController : ApiController
    {
        [HttpGet]
        public IHttpActionResult GetSequenceByName(string name)
        {
            ColorSequence s = new ColorSequence();
            s.Name = name;

            return Ok(s);
        }

        [HttpPost]
        public IHttpActionResult Create([FromBody] ColorSequence sequence)
        {
            if (sequence == null)
            {
                return BadRequest();
            }

            // TODO: Add it to the repository

            return CreatedAtRoute("GetSequenceByName", new { controller = "SequenceController", name = sequence.Name }, sequence);
        }

        [HttpPut]
        public IHttpActionResult Update(string name, [FromBody] ColorSequence sequence)
        {
            if (sequence == null || sequence.Name.Length == 0)
            {
                return BadRequest();
            }

            return Ok();
        }

        [HttpDelete]
        public IHttpActionResult Delete(string name)
        {
            return Ok();
        }

        public IHttpActionResult StartSequenceByName(string name)
        {
            // TODO: Code to send message to queue to request sequence start
            return Ok();
        }
    }
}