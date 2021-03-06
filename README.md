<h1 align="center">
 Gallery 🎨
</h1> 

<h1 align="center">
⚠️ WIP ⚠️
</h1>

<h2 align="center">
Gallery is a place where you can explore throught wikidata-registered paintings (and that's a lot of paintings)
</h2>

## Technical stack
- Django
- Vuejs
- PostgreSQL
- RabbitMQ + Celery + Flower (asynchronous job and admin panel for them)
- Docker

## Get Started
To launch the project you need to use Docker
- run : git clone https://github.com/lvnav/art_gallery.git
- run : cd art_gallery
- run : make
- run : gunzip < ./backend/seeds/initial_dump.gz | docker exec -i db psql -U postgres -d postgres
- wait until end of feeding (this may take a while)
- go to http://localhost:3000/#/painting/all

## How it work
Gallery is ship with data seed but it contain tools to fetch data from Wikidata wih SPARQL query (./backend/worker/repositories)

Backend: 
- an API for Paintings, Creators, Depicts, Movements of paintings. All are hyperlinked between them throught Paintings.
- some worker with tasks for fetching Wikidata with SPARQL queries (./backend/worker/sparql_repository.py)

Frontend:
- A frontend developed with Vite and Tailwind CSS
- A minimal responsivness actually

## Roadmap
- Improve search (actually "van gog" isn't find by example)
- Improve UI on details view
- Implementing UI for Movements and Location
- Do some fun stats on Creators
- Implementing user session to keep liked paintings
- and much more...

## Useful commands
```Backup Database```
  docker exec -t db pg_dumpall -c -U postgres | gzip > ./dump_$(date +"%Y-%m-%d_%H_%M_%S").gz

```Restore Database```
  gunzip < ./backend/seeds/initial_dump.gz | docker exec -i db psql -U postgres -d postgres
