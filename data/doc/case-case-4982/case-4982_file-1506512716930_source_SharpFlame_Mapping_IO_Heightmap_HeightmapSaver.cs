using System;
using System.Drawing;
using Ninject.Extensions.Logging;
using SharpFlame.Bitmaps;
using SharpFlame.Colors;
using SharpFlame.Core;

namespace SharpFlame.Mapping.IO.Heightmap
{
    public class HeightmapSaver : IIOSaver
    {
        private readonly ILogger logger;

        public HeightmapSaver(ILoggerFactory logFactory)
        {
            logger = logFactory.GetCurrentClassLogger();
        }

        public Result Save(string path, Map map, bool overwrite, bool compress = false) // compress is ignored.
        {
            var returnResult = new Result(string.Format("Saving heightmap to \"{0}\".", path), false);
            logger.Info ("Saving heightmap to \"{0}\"", path);

            var heightmapBitmap = new Bitmap(map.Terrain.TileSize.X + 1, map.Terrain.TileSize.Y + 1);
            for ( var Y = 0; Y <= map.Terrain.TileSize.Y; Y++ )
            {
                for ( var X = 0; X <= map.Terrain.TileSize.X; X++ )
                {
                    heightmapBitmap.SetPixel(X, Y,
                                             ColorTranslator.FromOle(ColorUtil.OsRgb(Convert.ToInt32(map.Terrain.Vertices[X, Y].Height), map.Terrain.Vertices[X, Y].Height,
                                                            map.Terrain.Vertices[X, Y].Height)));
                }
            }

            var subResult = BitmapUtil.SaveBitmap(path, overwrite, heightmapBitmap);
            if (!subResult.Success) {
                returnResult.ProblemAdd (subResult.Problem);
            }

            return returnResult;
        }

    }
}
