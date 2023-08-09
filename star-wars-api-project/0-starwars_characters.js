#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const movieEndpoint = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Function to fetch character names
function fetchCharacterNames(characterUrls) {
  const fetchPromises = characterUrls.map(url => {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          const character = JSON.parse(body);
          resolve(character.name);
        }
      });
    });
  });

  return Promise.all(fetchPromises);
}

request(movieEndpoint, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const filmData = JSON.parse(body);
    const characterUrls = filmData.characters;

    fetchCharacterNames(characterUrls)
      .then(characterNames => {
        characterNames.forEach(name => console.log(name));
      })
      .catch(error => {
        console.error(error);
      });
  }
});

