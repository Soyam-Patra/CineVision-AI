import MovieCard from "./MovieCard";

function MovieGrid({ movies }) {

    return (

        <>

            <h2 className="section-title">

                🎬 Recommended Movies

            </h2>

            <div
                id="movies"
                className="movies-grid"
            >

                {

                    movies.map((movie,index)=>(

                        <MovieCard

                            key={index}

                            movie={movie}

                        />

                    ))

                }

            </div>

        </>

    );

}

export default MovieGrid;