#include <Book/Aircraft.hpp>
#include <Book/ResourceHolder.hpp>
#include <Book/Utility.hpp>

#include <SFML/Graphics/RenderTarget.hpp>
#include <SFML/Graphics/RenderStates.hpp>


Textures::ID toTextureID(Aircraft::Type type)
{
	switch (type)
	{
		case Aircraft::Eagle:
			return Textures::Eagle;

		case Aircraft::Raptor:
			return Textures::Raptor;
	}
}

Aircraft::Aircraft(Type type, const TextureHolder& textures)
: mType(type)
, mSprite(textures.get(toTextureID(type)))
{
	centerOrigin(mSprite);
}

void Aircraft::drawCurrent(sf::RenderTarget& target, sf::RenderStates states) const
{
	target.draw(mSprite, states);
}

unsigned int Aircraft::getCategory() const
{
	switch (mType)
	{
		case Eagle:
			return Category::PlayerAircraft;

		default:
			return Category::EnemyAircraft;
	}
}