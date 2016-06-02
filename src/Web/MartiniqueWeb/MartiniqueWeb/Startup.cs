using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(MartiniqueWeb.Startup))]
namespace MartiniqueWeb
{
    public partial class Startup
    {
        public void Configuration(IAppBuilder app)
        {
            ConfigureAuth(app);
        }
    }
}
