function ActorCard({ result }) {

    return (

        <div className="actor-card">

            <h2>

                🎭 {result.actor}

            </h2>

            <p>

                ⭐ Match Confidence

                <br/>

                <strong>

                    {result.confidence.toFixed(2)}%

                </strong>

            </p>

            <p>

                🎬 Showing recommended movies

            </p>

        </div>

    );

}

export default ActorCard;