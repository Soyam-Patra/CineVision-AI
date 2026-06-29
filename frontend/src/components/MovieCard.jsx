function MovieCard({ movie }) {

    return (

        <div className="movie-card">

            <img

                src={
                    movie.poster ??
                    "https://via.placeholder.com/300x450?text=No+Poster"
                }

                alt={movie.title}

                className="movie-poster"

            />

            <div className="movie-info">

                <h3>

                    {movie.title}

                </h3>

                <div className="rating">

                    ⭐ IMDb {movie.imdb_rating}

                </div>

                <div className="meta">

                    {movie.year} • {movie.runtime} min

                </div>

                <div className="genres">

                    {

                        movie.genres.map((genre)=>(

                            <span

                                key={genre}

                                className="genre"

                            >

                                {genre}

                            </span>

                        ))

                    }

                </div>

                {

                    movie.trailer &&

                    <a

                        href={movie.trailer}

                        target="_blank"

                        rel="noreferrer"

                        className="trailer-btn"

                    >

                        ▶ Watch Trailer

                    </a>

                }

            </div>

        </div>

    );

}

export default MovieCard;