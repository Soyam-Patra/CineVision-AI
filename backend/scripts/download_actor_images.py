import asyncio
import aiohttp
import aiofiles
import pandas as pd
import json
from itertools import count
from pathlib import Path

# ---------------- CONFIG ---------------- #

API_KEY = "67b561e775bf974e7893e5f76d5dd81a"

ROOT = Path(__file__).resolve().parents[2]

ACTORS_CSV = ROOT / "backend" / "actor_database" / "actors.csv"

IMAGE_DIR = ROOT / "backend" / "actor_database" / "actor_images"

IMAGE_DIR.mkdir(parents=True, exist_ok=True)

IMAGE_BASE = "https://image.tmdb.org/t/p/original"

# -------- Progress Counter -------- #

progress = count(1)

# -------- Number of images per tier -------- #

def images_for_tier(tier):

    if tier == 1:
        return 8

    if tier == 2:
        return 5

    if tier == 3:
        return 3

    return 2


# -------- Download one image -------- #

async def download_image(session, url, path):

    async with session.get(url) as response:

        #print("Downloading:", url)
        #print("Status:", response.status)

        if response.status == 200:

            async with aiofiles.open(path, "wb") as f:

                await f.write(await response.read())

        else:
            print("FAILED:", url)


# -------- Download one actor -------- #

async def process_actor(session, actor,total):

    actor_id = actor.actor_id
    actor_name = actor.actor_name
    current = next(progress)
    tier = actor.tier

    actor_folder = IMAGE_DIR / str(actor_id)

    actor_folder.mkdir(exist_ok=True)

    metadata_file = actor_folder / "metadata.json"

    # Resume support
    if metadata_file.exists():
        print(
            f"[{current}/{total}] "
            f"{actor_name} ✓ Already downloaded"
        )
        return

    # Search actor
    search_url = "https://api.themoviedb.org/3/search/person"

    params = {

        "api_key": API_KEY,

        "query": actor_name

    }

    async with session.get(search_url, params=params) as response:

        #print(actor_name, response.status)
        #text = await response.text()
        #print(text[:500])
        data = await response.json()


        if response.status != 200:
            print(actor_name, "Search Failed")
            return

        data = await response.json()

    if len(data["results"]) == 0:
        print(actor_name, "Not Found")
        return

    person = data["results"][0]

    person_id = person["id"]

    # Fetch all profile images

    images_url = f"https://api.themoviedb.org/3/person/{person_id}/images"

    async with session.get(
        images_url,
        params={"api_key": API_KEY}
    ) as response:

        if response.status != 200:
            return

        images = await response.json()

    profiles = images.get("profiles", [])
    profiles.sort(
        key=lambda p: (
            p.get("vote_average", 0),
            p.get("vote_count", 0),
            p.get("height", 0) * p.get("width", 0)
        ),
        reverse=True
    )
    print(actor_name, "Profiles:", len(profiles))

    max_images = images_for_tier(tier)

    downloaded = 0

    for profile in profiles[:max_images]:

        file_path = profile["file_path"]

        url = IMAGE_BASE + file_path

        save_path = actor_folder / f"{downloaded}.jpg"

        await download_image(session, url, save_path)

        downloaded += 1

    metadata = {

        "actor_id": int(actor_id),

        "actor_name": actor_name,

        "tmdb_id": person_id,

        "downloaded_images": downloaded

    }

    async with aiofiles.open(metadata_file, "w") as f:

        await f.write(json.dumps(metadata, indent=4))

    print(
        f"[{current}/{total}] "
        f"{actor_name} ✓ "
        f"{downloaded} images"
        )    


# -------- Main -------- #

async def main():

    actors = pd.read_csv(ACTORS_CSV)
    total = len(actors)
    print(f"Downloading images for {len(actors)} actors...")

    # ---------- TEST MODE ----------

    #actors = actors.head(10)

    connector = aiohttp.TCPConnector(limit=10)

    async with aiohttp.ClientSession(connector=connector) as session:

        tasks = []

        for actor in actors.itertuples():

            tasks.append(
                process_actor(
                    session,
                    actor,
                    total
                )
            )

        results = await asyncio.gather(
            *tasks,
            return_exceptions=True
        )

        for result in results:

            if isinstance(result, Exception):

                print(result)


if __name__ == "__main__":

    asyncio.run(main())