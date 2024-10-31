#include "Graphics.hpp"

#include <sstream>

#include <SFML/Graphics/Image.hpp>
#include <SFML/Graphics/Rect.hpp>

std::map<std::string,std::vector<sf::Texture*>> Graphics::_graphics;

void Graphics::loadTilemap(std::string const& fileName,
                           std::string const& name,
                           int tileSize)
{
    if(!tilesetIsLoaded(fileName))
    {
        sf::Image tileSet;

        tileSet.loadFromFile(fileName);

        int widthInTiles = tileSet.getSize().x / tileSize;
        int heightInTiles = tileSet.getSize().y / tileSize;

        sf::Texture* graphic;
        sf::Vector2i pixelPos;
        _graphics.insert(std::pair<std::string,std::vector<sf::Texture*>>
                             (name,std::vector<sf::Texture*>(widthInTiles*heightInTiles)));

        for(int i = 0; i < heightInTiles; ++i)
        {
            pixelPos.y = i * tileSize;
            for(int j = 0; j < widthInTiles; ++j)
            {
                pixelPos.x = j * tileSize;

                graphic = new sf::Texture();
                graphic->loadFromImage(tileSet,sf::IntRect(pixelPos,
                                                           sf::Vector2i(tileSize,
                                                                        tileSize)));

                _graphics[name][j + i*j] = graphic;
            }
        }
    }
}

sf::Texture const& Graphics::getTexture(std::string const& tileMapName, int i)
{ 
    for(auto tileMap : _graphics)
    {
        //Tilemap Name
        if(!tileMap.first.compare(tileMapName))
        {
            if(tileMap.second.size() > i)
            {
                return *(tileMap.second[i]);
            }
        }
    }

    return *(new sf::Texture());
}

bool Graphics::tilesetIsLoaded(std::string const& name)
{ 
    return _graphics.find(name) != _graphics.end();
}