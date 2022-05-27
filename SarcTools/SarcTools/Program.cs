// Commands: batch_unbuild, batch_build, build <file>, unbuild <folder>

using SarcTools;

async Task BatchUnbuild()
{
    throw new NotImplementedException();
}

async Task BatchBuild()
{
    throw new NotImplementedException();
}

if (args.Length > 1)
{
    switch (args[0])
    {
        case "unbuild":
            await Utils.UnbuildSarc(args[1]);
            break;
        case "build":
            await Utils.BuildSarc(args[1]);
            break;
    }
}
if (args.Length > 0)
{
    switch (args[0])
    {
        case "batch_unbuild":
            await BatchUnbuild();
            break;
        case "batch_build":
            await BatchBuild();
            break;
    }
}
else
{
    Console.WriteLine("No command was specified");
}
